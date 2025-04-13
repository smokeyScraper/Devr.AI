import React from 'react';
import { motion } from 'framer-motion';
import { Bot, Github, MessageSquare, Users } from 'lucide-react';

const Hero: React.FC = () => {
    const container = {
        hidden: { opacity: 0 },
        show: {
            opacity: 1,
            transition: {
                staggerChildren: 0.2,
            },
        },
    };

    const item = {
        hidden: { opacity: 0, y: 20 },
        show: { opacity: 1, y: 0 },
    };

    return (
        <section className="relative min-h-screen flex items-center justify-center pt-24 pb-16">
            {/* Background decorations */}
            <div className="absolute inset-0 overflow-hidden pointer-events-none">
                <div className="absolute top-1/3 left-1/4 w-96 h-96 radial-gradient-bg"></div>
                <div className="absolute bottom-1/4 right-1/3 w-96 h-96 radial-gradient-bg"></div>

                {/* Floating icons */}
                <motion.div
                    animate={{
                        y: [10, -10, 10],
                        rotate: [0, 5, -5, 0],
                    }}
                    transition={{
                        duration: 6,
                        repeat: Infinity,
                        repeatType: 'reverse',
                    }}
                    className="absolute top-1/4 left-1/5 text-green-500/20"
                >
                    <Bot size={120} />
                </motion.div>
                <motion.div
                    animate={{
                        y: [-10, 10, -10],
                        rotate: [0, -5, 5, 0],
                    }}
                    transition={{
                        duration: 7,
                        repeat: Infinity,
                        repeatType: 'reverse',
                    }}
                    className="absolute bottom-1/3 right-1/6 text-blue-500/20"
                >
                    <Github size={80} />
                </motion.div>
                <motion.div
                    animate={{
                        y: [5, -15, 5],
                    }}
                    transition={{
                        duration: 8,
                        repeat: Infinity,
                        repeatType: 'reverse',
                    }}
                    className="absolute top-2/3 left-1/6 text-purple-500/20"
                >
                    <MessageSquare size={100} />
                </motion.div>
            </div>

            <div className="container mx-auto px-6 z-10">
                <motion.div
                    variants={container}
                    initial="hidden"
                    animate="show"
                    className="max-w-4xl mx-auto text-center"
                >
                    <motion.div variants={item} className="mb-6">
                        <span className="px-4 py-2 rounded-full bg-green-500/10 text-green-500 text-sm font-medium">
                            Developer Experience Reimagined
                        </span>
                    </motion.div>
                    <motion.h1
                        variants={item}
                        className="text-4xl md:text-6xl font-bold mb-6"
                    >
                        AI-Powered <span className="gradient-text">Developer Relations</span> Assistant
                    </motion.h1>
                    <motion.p
                        variants={item}
                        className="text-lg md:text-xl text-gray-400 mb-8 max-w-3xl mx-auto"
                    >
                        Devr.AI revolutionizes open-source community management by automating engagement,
                        streamlining onboarding, and delivering real-time project updates across Discord,
                        Slack, GitHub, and more.
                    </motion.p>
                    <motion.div
                        variants={item}
                        className="flex flex-col sm:flex-row gap-4 justify-center mb-12"
                    >
                        <a href="#waitlist" className="btn-primary flex items-center justify-center gap-2">
                            <Users size={18} />
                            Join the Waitlist
                        </a>
                        <a href="#features" className="btn-secondary">
                            Explore Features
                        </a>
                    </motion.div>

                    <motion.div variants={item}>
                        <div className="relative rounded-xl overflow-hidden border border-gray-800">
                            <div className="absolute inset-0 bg-gradient-to-b from-transparent via-transparent to-dark z-10"></div>
                            <img
                                src="https://placehold.co/1200x675/27272a/e5e5e5/png?text=Devr.AI+Dashboard+Preview"
                                alt="Devr.AI Dashboard"
                                className="w-full h-auto"
                            />
                        </div>
                    </motion.div>
                </motion.div>
            </div>
        </section>
    );
};

export default Hero;