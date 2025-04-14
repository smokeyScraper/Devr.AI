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
                                <div className={`relative z-10 p-3 rounded-lg bg-gradient-to-br ${step.color} text-white shadow-lg`}>
                                    {step.icon}
                                </div>
                                <div>
                                    <h3 className="text-lg font-semibold mb-1">{step.title}</h3>
                                    <p className="text-sm text-gray-400">{step.description}</p>
                                </div>
                            </div>

                            {index < steps.length - 1 && (
                                <>
                                    <div className="hidden md:block">
                                        {step.title !== "Contributor Management" && step.title !== "Maintainer Support" && (
                                            <motion.div
                                                initial={{ opacity: 0, height: 0 }}
                                                whileInView={{ opacity: 1, height: '100%' }}
                                                viewport={{ once: true }}
                                                transition={{ duration: 0.8, delay: 0.4 + index * 0.1 }}
                                                className={`absolute top-[46px] left-[24px] w-px bg-gradient-to-b ${step.color} opacity-70`}
                                                style={{ maxHeight: '120px', zIndex: 1 }}
                                            />
                                        )}

                                        {step.title === "Knowledge Retrieval" && (
                                            <motion.div
                                                initial={{ opacity: 0, height: 0 }}
                                                whileInView={{ opacity: 1, height: '100%' }}
                                                viewport={{ once: true }}
                                                transition={{ duration: 0.8, delay: 0.4 + index * 0.1 }}
                                                className={`absolute top-[46px] left-[24px] w-px bg-gradient-to-b ${step.color} opacity-70`}
                                                style={{ maxHeight: '120px', zIndex: 1 }}
                                            />
                                        )}
                                    </div>

                                    <div className="md:hidden absolute left-[24px] top-[46px] h-full">
                                        <div className={`h-full w-px bg-gradient-to-b ${step.color} opacity-70`} style={{ zIndex: 1 }}></div>
                                    </div>
                                </>
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

                    <div className="bg-dark-card border border-gray-700 rounded-xl p-4 md:p-8 shadow-lg overflow-hidden">
                        <div className="flex flex-col space-y-4 md:space-y-6">

                            <div className="grid grid-cols-3 gap-2 md:gap-3">
                                <div className="bg-blue-900/40 border border-blue-500/60 rounded-lg p-2 md:p-4 flex flex-col items-center justify-center text-center hover:border-blue-400 transition-colors shadow-md">
                                    <Github className="mb-1 md:mb-2 text-blue-400" size={24} />
                                    <span className="text-xs md:text-sm font-medium text-blue-300">GitHub</span>
                                </div>
                                <div className="bg-blue-900/40 border border-blue-500/60 rounded-lg p-2 md:p-4 flex flex-col items-center justify-center text-center hover:border-blue-400 transition-colors shadow-md">
                                    <MessageSquare className="mb-1 md:mb-2 text-blue-400" size={24} />
                                    <span className="text-xs md:text-sm font-medium text-blue-300">Discord</span>
                                </div>
                                <div className="bg-blue-900/40 border border-blue-500/60 rounded-lg p-2 md:p-4 flex flex-col items-center justify-center text-center hover:border-blue-400 transition-colors shadow-md">
                                    <Slack className="mb-1 md:mb-2 text-blue-400" size={24} />
                                    <span className="text-xs md:text-sm font-medium text-blue-300">Slack</span>
                                </div>
                            </div>

                            <div className="flex justify-center">
                                <ArrowRight className="rotate-90 text-blue-400/70" size={20} />
                            </div>

                            <div className="bg-green-900/40 border border-green-500/60 rounded-lg p-3 md:p-4 text-center hover:border-green-400 transition-colors shadow-md">
                                <div className="flex justify-center mb-1 md:mb-2">
                                    <Layers className="text-green-400" size={24} />
                                </div>
                                <h4 className="font-medium text-sm md:text-base text-green-300">API Gateway</h4>
                                <p className="text-xs md:text-sm text-gray-400">Handles authentication and routing</p>
                            </div>

                            <div className="flex justify-center">
                                <ArrowRight className="rotate-90 text-green-400/70" size={20} />
                            </div>

                            <div className="grid grid-cols-2 gap-2 md:gap-3">
                                <div className="bg-amber-900/40 border border-amber-500/60 rounded-lg p-2 md:p-4 text-center hover:border-amber-400 transition-colors shadow-md">
                                    <div className="flex justify-center mb-1 md:mb-2">
                                        <Workflow className="text-amber-400" size={24} />
                                    </div>
                                    <h4 className="font-medium text-xs md:text-base text-amber-300">Workflow Orchestrator</h4>
                                    <p className="text-xs text-gray-400">Manages services</p>
                                </div>
                                <div className="bg-amber-900/40 border border-amber-500/60 rounded-lg p-2 md:p-4 text-center hover:border-amber-400 transition-colors shadow-md">
                                    <div className="flex justify-center mb-1 md:mb-2">
                                        <Server className="text-amber-400" size={24} />
                                    </div>
                                    <h4 className="font-medium text-xs md:text-base text-amber-300">Task Queue</h4>
                                    <p className="text-xs text-gray-400">Async operations</p>
                                </div>
                            </div>

                            <div className="flex justify-center">
                                <ArrowRight className="rotate-90 text-amber-400/70" size={20} />
                            </div>

                            <div className="grid grid-cols-3 gap-2 md:gap-3">
                                <div className="bg-purple-900/40 border border-purple-500/60 rounded-lg p-2 md:p-4 text-center hover:border-purple-400 transition-colors shadow-md">
                                    <div className="flex justify-center mb-1 md:mb-2">
                                        <BrainCircuit className="text-purple-400" size={24} />
                                    </div>
                                    <h4 className="font-medium text-xs md:text-base text-purple-300">LLM Service</h4>
                                    <p className="text-xs text-gray-400">NLP</p>
                                </div>
                                <div className="bg-purple-900/40 border border-purple-500/60 rounded-lg p-2 md:p-4 text-center hover:border-purple-400 transition-colors shadow-md">
                                    <div className="flex justify-center mb-1 md:mb-2">
                                        <FileCode className="text-purple-400" size={24} />
                                    </div>
                                    <h4 className="font-medium text-xs md:text-base text-purple-300">Knowledge</h4>
                                    <p className="text-xs text-gray-400">Data retrieval</p>
                                </div>
                                <div className="bg-purple-900/40 border border-purple-500/60 rounded-lg p-2 md:p-4 text-center hover:border-purple-400 transition-colors shadow-md">
                                    <div className="flex justify-center mb-1 md:mb-2">
                                        <Code className="text-purple-400" size={24} />
                                    </div>
                                    <h4 className="font-medium text-xs md:text-base text-purple-300">Code</h4>
                                    <p className="text-xs text-gray-400">Analysis</p>
                                </div>
                            </div>

                            <div className="flex justify-center">
                                <ArrowRight className="rotate-90 text-purple-400/70" size={20} />
                            </div>

                            <div className="bg-rose-900/40 border border-rose-500/60 rounded-lg p-3 md:p-4 text-center hover:border-rose-400 transition-colors shadow-md">
                                <div className="flex justify-center mb-1 md:mb-2">
                                    <Database className="text-rose-400" size={24} />
                                </div>
                                <h4 className="font-medium text-sm md:text-base text-rose-300">Data Storage</h4>
                                <p className="text-xs md:text-sm text-gray-400">Vector & Relational DB</p>
                            </div>
                        </div>
                    </div>
                </motion.div>
            </div>
        </section>
    );
};

export default HowItWorks;