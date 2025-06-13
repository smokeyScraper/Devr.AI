from discord.ext import commands
import discord
from app.core.orchestration.queue_manager import AsyncQueueManager, QueuePriority
from bots.discord.discord_bot import DiscordBot

class DevRelCommands(commands.Cog):
    def __init__(self, bot: DiscordBot, queue_manager: AsyncQueueManager):
        self.bot = bot
        self.queue = queue_manager

    @commands.command(name="reset")
    async def reset_thread(self, ctx: commands.Context):
        """Reset your DevRel thread and memory."""
        user_id = str(ctx.author.id)
        cleanup = {
            "type": "clear_thread_memory",
            "memory_thread_id": user_id,
            "user_id": user_id,
            "cleanup_reason": "manual_reset"
        }
        await self.queue.enqueue(cleanup, QueuePriority.HIGH)
        self.bot.active_threads.pop(user_id, None)
        await ctx.send("Your DevRel thread & memory have been reset! Send another message to start fresh.")

    @commands.command(name="help_devrel")
    async def help_devrel(self, ctx: commands.Context):
        """Show DevRel assistant help."""
        embed = discord.Embed(
            title="DevRel Assistant Help",
            description="I can help you with Devr.AI related questions!"
        )
        embed.add_field(
            name="Commands",
            value=(
                "• `!reset` – Reset your DevRel thread and memory\n"
                "• `!help_devrel` – Show this help message"
            ),
            inline=False
        )
        await ctx.send(embed=embed)
