import React from 'react';
import { motion } from 'framer-motion';
import { BrainCircuit, Workflow, Database, GitMerge } from 'lucide-react';

const HowItWorks: React.FC = () => {
    const steps = [
        {
            icon: <BrainCircuit size={32} />,
            title: 'AI-Powered Understanding',
            description: 'Our AI service layer understands natural language, code context, and project-specific information to provide intelligent responses.',
            color: 'from-green-500 to-blue-500',
        },
        {
            icon: <Workflow size={32} />,
            title: 'Workflow Orchestration',
            description: 'The core processing engine manages workflows between different services and handles the context for ongoing conversations.',
            color: 'from-blue-500 to-purple-500',
        },
        {
            icon: <Database size={32} />,
            title: 'Knowledge Retrieval',
            description: 'Our system stores and retrieves project-specific information from documentation, code, and past interactions.',
            color: 'from-purple-500 to-pink-500',
        },
        {
            icon: <GitMerge size={32} />,
            title: 'Platform Integration',
            description: 'Seamlessly connect with GitHub, Discord, Slack, and Discourse through dedicated integration services.',
            color: 'from-pink-500 to-orange-500',
        },
    ];

    return (
        <section id="how-it-works" className="section bg-dark-lighter">
            <div className="container mx-auto px-6">
                <motion.div
                    initial={{ opacity: 0, y: 20 }}
                    whileInView={{ opacity: 1, y: 0 }}
                    viewport={{ once: true }}
                    transition={{ duration: 0.5 }}
                    className="text-center mb-16"
                >
                    <h2 className="text-3xl md:text-4xl font-bold mb-4">
                        How <span className="gradient-text">It Works</span>
                    </h2>
                    <p className="text-gray-400 max-w-2xl mx-auto">
                        Devr.AI follows a microservices architecture designed for efficiency, scalability, and intelligent operations.
                    </p>
                </motion.div>

                <div className="grid grid-cols-1 md:grid-cols-2 gap-12 max-w-5xl mx-auto">
                    {steps.map((step, index) => (
                        <motion.div
                            key={index}
                            initial={{ opacity: 0, x: index % 2 === 0 ? -30 : 30 }}
                            whileInView={{ opacity: 1, x: 0 }}
                            viewport={{ once: true }}
                            transition={{ duration: 0.6, delay: index * 0.1 }}
                            className="relative"
                        >
                            <div className="flex gap-6 items-start">
                                <div className={`p-4 rounded-lg bg-gradient-to-br ${step.color} text-white`}>
                                    {step.icon}
                                </div>
                                <div>
                                    <h3 className="text-xl font-semibold mb-2">{step.title}</h3>
                                    <p className="text-gray-400">{step.description}</p>
                                </div>
                            </div>

                            {index < steps.length - 1 && (
                                <motion.div
                                    initial={{ opacity: 0, height: 0 }}
                                    whileInView={{ opacity: 1, height: '100%' }}
                                    viewport={{ once: true }}
                                    transition={{ duration: 0.8, delay: 0.4 + index * 0.1 }}
                                    className={`absolute top-16 left-8 w-px h-full bg-gradient-to-b ${step.color} opacity-50`}
                                >
                                </motion.div>
                            )}
                        </motion.div>
                    ))}
                </div>

                <motion.div
                    initial={{ opacity: 0 }}
                    whileInView={{ opacity: 1 }}
                    viewport={{ once: true }}
                    transition={{ duration: 1, delay: 0.6 }}
                    className="mt-16 bg-dark-card p-6 rounded-xl border border-gray-800 max-w-4xl mx-auto"
                >
                    <pre className="text-sm text-gray-300 overflow-auto">
                        <code className="language-mermaid">
                            {`
flowchart TB
  subgraph "External Platforms"
    GH["GitHub"] --- DS["Discord"] --- SL["Slack"]
  end
  
  subgraph "Core Processing"
    WF["Workflow Orchestrator"] --- LLM["LLM Service"]
    WF --- KR["Knowledge Retrieval"]
  end
  
  subgraph "Data Storage"
    VDB["Vector DB"] --- RDB["Relational DB"]
  end
  
  GH <--> API["API Gateway"] <--> WF
  DS <--> API
  SL <--> API
  
  LLM <--> VDB
  KR <--> VDB
  WF <--> RDB
              `}
                        </code>
                    </pre>
                </motion.div>
            </div>
        </section>
    );
};

export default HowItWorks;