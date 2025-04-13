import React from 'react';
import { motion } from 'framer-motion';
import {
    BrainCircuit,
    Workflow,
    Database,
    GitMerge,
    ArrowRight,
    Github,
    Slack,
    MessageSquare,
    Users,
    Shield,
    Layers,
    Server,
    Code,
    FileCode
} from 'lucide-react';

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
        {
            icon: <Users size={32} />,
            title: 'Contributor Management',
            description: 'Automate onboarding for new contributors, provide personalized guidance, and track contribution milestones to boost engagement.',
            color: 'from-orange-500 to-amber-500',
        },
        {
            icon: <Shield size={32} />,
            title: 'Maintainer Support',
            description: 'Reduce workload for maintainers through automated issue triage, PR reviews, and community health monitoring tools.',
            color: 'from-green-500 to-emerald-500',
        }
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

                <div className="grid grid-cols-1 md:grid-cols-2 gap-6 lg:gap-10 max-w-5xl mx-auto">
                    {steps.map((step, index) => (
                        <motion.div
                            key={index}
                            initial={{ opacity: 0, x: index % 2 === 0 ? -30 : 30 }}
                            whileInView={{ opacity: 1, x: 0 }}
                            viewport={{ once: true }}
                            transition={{ duration: 0.6, delay: index * 0.1 }}
                            className="relative"
                        >
                            <div className="flex gap-4 items-start">
                                <div className={`p-3 rounded-lg bg-gradient-to-br ${step.color} text-white shadow-lg`}>
                                    {step.icon}
                                </div>
                                <div>
                                    <h3 className="text-lg font-semibold mb-1">{step.title}</h3>
                                    <p className="text-sm text-gray-400">{step.description}</p>
                                </div>
                            </div>

                            {index < steps.length - 2 && index % 2 === 0 && (
                                <motion.div
                                    initial={{ opacity: 0, height: 0 }}
                                    whileInView={{ opacity: 1, height: '100%' }}
                                    viewport={{ once: true }}
                                    transition={{ duration: 0.8, delay: 0.4 + index * 0.1 }}
                                    className={`absolute top-14 left-6 h-full w-px bg-gradient-to-b ${step.color} opacity-70`}
                                >
                                </motion.div>
                            )}

                            {index < steps.length - 2 && index % 2 === 1 && (
                                <motion.div
                                    initial={{ opacity: 0, height: 0 }}
                                    whileInView={{ opacity: 1, height: '100%' }}
                                    viewport={{ once: true }}
                                    transition={{ duration: 0.8, delay: 0.4 + index * 0.1 }}
                                    className={`absolute top-14 left-6 h-full w-px bg-gradient-to-b ${step.color} opacity-70`}
                                >
                                </motion.div>
                            )}
                        </motion.div>
                    ))}
                </div>

                <motion.div
                    initial={{ opacity: 0, y: 30 }}
                    whileInView={{ opacity: 1, y: 0 }}
                    viewport={{ once: true }}
                    transition={{ duration: 0.8, delay: 0.5 }}
                    className="mt-16 max-w-4xl mx-auto"
                >
                    <h3 className="text-xl font-semibold text-center mb-6">System Architecture</h3>

                    <div className="bg-dark-card border border-gray-700 rounded-xl p-6 md:p-8 shadow-lg">
                        <div className="flex flex-col space-y-6">
                            <div className="grid grid-cols-3 gap-3">
                                <div className="bg-blue-900/40 border border-blue-500/60 rounded-lg p-4 flex flex-col items-center justify-center text-center hover:border-blue-400 transition-colors shadow-md">
                                    <Github className="mb-2 text-blue-400" size={28} />
                                    <span className="text-sm font-medium text-blue-300">GitHub</span>
                                </div>
                                <div className="bg-blue-900/40 border border-blue-500/60 rounded-lg p-4 flex flex-col items-center justify-center text-center hover:border-blue-400 transition-colors shadow-md">
                                    <MessageSquare className="mb-2 text-blue-400" size={28} />
                                    <span className="text-sm font-medium text-blue-300">Discord</span>
                                </div>
                                <div className="bg-blue-900/40 border border-blue-500/60 rounded-lg p-4 flex flex-col items-center justify-center text-center hover:border-blue-400 transition-colors shadow-md">
                                    <Slack className="mb-2 text-blue-400" size={28} />
                                    <span className="text-sm font-medium text-blue-300">Slack</span>
                                </div>
                            </div>

                            <div className="flex justify-center">
                                <ArrowRight className="rotate-90 text-blue-400/70" size={24} />
                            </div>

                            <div className="bg-green-900/40 border border-green-500/60 rounded-lg p-4 text-center hover:border-green-400 transition-colors shadow-md">
                                <div className="flex justify-center mb-2">
                                    <Layers className="text-green-400" size={28} />
                                </div>
                                <h4 className="font-medium mb-1 text-green-300 text-base">API Gateway</h4>
                                <p className="text-sm text-gray-400">Handles authentication and request routing</p>
                            </div>

                            <div className="flex justify-center">
                                <ArrowRight className="rotate-90 text-green-400/70" size={24} />
                            </div>

                            <div className="grid grid-cols-2 gap-3">
                                <div className="bg-amber-900/40 border border-amber-500/60 rounded-lg p-4 text-center hover:border-amber-400 transition-colors shadow-md">
                                    <div className="flex justify-center mb-2">
                                        <Workflow className="text-amber-400" size={28} />
                                    </div>
                                    <h4 className="font-medium mb-1 text-amber-300 text-base">Workflow Orchestrator</h4>
                                    <p className="text-sm text-gray-400">Manages service interactions</p>
                                </div>
                                <div className="bg-amber-900/40 border border-amber-500/60 rounded-lg p-4 text-center hover:border-amber-400 transition-colors shadow-md">
                                    <div className="flex justify-center mb-2">
                                        <Server className="text-amber-400" size={28} />
                                    </div>
                                    <h4 className="font-medium mb-1 text-amber-300 text-base">Task Queue</h4>
                                    <p className="text-sm text-gray-400">Processes async operations</p>
                                </div>
                            </div>

                            <div className="flex justify-center">
                                <ArrowRight className="rotate-90 text-amber-400/70" size={24} />
                            </div>

                            <div className="grid grid-cols-3 gap-3">
                                <div className="bg-purple-900/40 border border-purple-500/60 rounded-lg p-4 text-center hover:border-purple-400 transition-colors shadow-md">
                                    <div className="flex justify-center mb-2">
                                        <BrainCircuit className="text-purple-400" size={28} />
                                    </div>
                                    <h4 className="font-medium mb-1 text-purple-300 text-base">LLM Service</h4>
                                    <p className="text-sm text-gray-400">Natural language processing</p>
                                </div>
                                <div className="bg-purple-900/40 border border-purple-500/60 rounded-lg p-4 text-center hover:border-purple-400 transition-colors shadow-md">
                                    <div className="flex justify-center mb-2">
                                        <FileCode className="text-purple-400" size={28} />
                                    </div>
                                    <h4 className="font-medium mb-1 text-purple-300 text-base">Knowledge Retrieval</h4>
                                    <p className="text-sm text-gray-400">Data querying & retrieval</p>
                                </div>
                                <div className="bg-purple-900/40 border border-purple-500/60 rounded-lg p-4 text-center hover:border-purple-400 transition-colors shadow-md">
                                    <div className="flex justify-center mb-2">
                                        <Code className="text-purple-400" size={28} />
                                    </div>
                                    <h4 className="font-medium mb-1 text-purple-300 text-base">Code Understanding</h4>
                                    <p className="text-sm text-gray-400">Code analysis & processing</p>
                                </div>
                            </div>

                            <div className="flex justify-center">
                                <ArrowRight className="rotate-90 text-purple-400/70" size={24} />
                            </div>

                            <div className="bg-rose-900/40 border border-rose-500/60 rounded-lg p-4 text-center hover:border-rose-400 transition-colors shadow-md">
                                <div className="flex justify-center mb-2">
                                    <Database className="text-rose-400" size={28} />
                                </div>
                                <h4 className="font-medium mb-1 text-rose-300 text-base">Data Storage (Supabase)</h4>
                                <p className="text-sm text-gray-400">Vector DB and Relational DB</p>
                            </div>
                        </div>
                    </div>
                </motion.div>
            </div>
        </section>
    );
};

export default HowItWorks;