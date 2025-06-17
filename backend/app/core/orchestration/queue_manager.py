import asyncio
import logging
from typing import Dict, Any, Callable, Optional
from datetime import datetime
from enum import Enum
import pika
import time
import json

logger = logging.getLogger(__name__)

class QueuePriority(str, Enum):
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"

class AsyncQueueManager:
    """Queue manager for agent orchestration"""

    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        self.channel = self.connection.channel()
        self.queues = {
            QueuePriority.HIGH: 'high_task_queue',
            QueuePriority.MEDIUM: 'medium_task_queue',
            QueuePriority.LOW: 'low_task_queue'
        }
        self.handlers: Dict[str, Callable] = {}
        self.running = False
        self.worker_tasks = []

    def callback(ch, method, properties, body):
        print(f" [x] Received {body.decode()}")
        time.sleep(body.count(b'.'))
        print(" [x] Done")
        ch.basic_ack(delivery_tag=method.delivery_tag)

    async def start(self, num_workers: int = 3):
        """Start the queue processing workers"""
        self.running = True

        # for i in range(num_workers):
        #     task = asyncio.create_task(self._worker(f"worker-{i}"))
        #     self.worker_tasks.append(task)

        logger.info("Setting QOS")
        self.channel.basic_qos(prefetch_count=1)
        logger.info("QOS set")
        logger.info("Starting Queues")
        for i in self.queues.values():
            self.channel.queue_declare(queue=i, durable=True)
            logger.info(f"Queue {i} started")
        logger.info("Starting Channel")
        self.channel.start_consuming()
        logger.info(f"Started channel {self.channel.channel_number}")

    async def stop(self):
        """Stop the queue processing"""
        self.running = False

        # Cancel all worker tasks
        for task in self.worker_tasks:
            task.cancel()

        await asyncio.gather(*self.worker_tasks, return_exceptions=True)
        logger.info("Stopped all queue workers")
        self.channel.stop_consuming()
        self.connection.close()
        logger.info('Stopped Queue')

    async def enqueue(self,
                      message: Dict[str, Any],
                      priority: QueuePriority = QueuePriority.MEDIUM,
                      delay: float = 0):
        """Add a message to the queue"""

        if delay > 0:
            await asyncio.sleep(delay)

        queue_item = {
            "id": message.get("id", f"msg_{datetime.now().timestamp()}"),
            "timestamp": datetime.now().isoformat(),
            "priority": priority,
            "data": message
        }
        json_message = json.dumps(queue_item)
        # await self.queues[priority].put(queue_item)
        self.channel.basic_publish(exchange='', routing_key=f'{self.queues[priority]}', body=json_message)
        logger.info(f"Enqueued message {queue_item['id']} with priority {priority}")

    def register_handler(self, message_type: str, handler: Callable):
        """Register a handler for a specific message type"""
        self.handlers[message_type] = handler
        logger.info(f"Registered handler for message type: {message_type}")

    async def _worker(self, worker_name: str):
        """Worker coroutine to process queue items"""
        logger.info(f"Started queue worker: {worker_name}")

        while self.running:
            try:
                # Process queues by priority
                item = await self._get_next_item()

                if item:
                    await self._process_item(item, worker_name)
                else:
                    # No items available, wait a bit
                    await asyncio.sleep(0.1)

            except asyncio.CancelledError:
                logger.info(f"Worker {worker_name} cancelled")
                break
            except (ConnectionError, TimeoutError) as e:
                logger.error(f"Connection error in worker {worker_name}: {str(e)}")
                await asyncio.sleep(5)  # Longer pause for connection issues
            except Exception as e:
                logger.error(f"Unexpected error in worker {worker_name}: {str(e)}")
                await asyncio.sleep(1)  # Brief pause on error

    async def _get_next_item(self) -> Optional[Dict[str, Any]]:
        """Get the next item from queues (priority-based)"""

        # Try high priority first
        try:
            return self.queues[QueuePriority.HIGH].get_nowait()
        except asyncio.QueueEmpty:
            pass

        # Then medium priority
        try:
            return self.queues[QueuePriority.MEDIUM].get_nowait()
        except asyncio.QueueEmpty:
            pass

        # Finally low priority
        try:
            return self.queues[QueuePriority.LOW].get_nowait()
        except asyncio.QueueEmpty:
            pass

        return None

    async def _process_item(self, item: Dict[str, Any], worker_name: str):
        """Process a queue item"""
        try:
            message_data = item["data"]
            message_type = message_data.get("type", "unknown")

            handler = self.handlers.get(message_type)

            if handler:
                logger.debug(f"Worker {worker_name} processing {item['id']} (type: {message_type})")
                await handler(message_data)
            else:
                logger.warning(f"No handler found for message type: {message_type}")

        except Exception as e:
            logger.error(f"Error processing item {item['id']}: {str(e)}")
