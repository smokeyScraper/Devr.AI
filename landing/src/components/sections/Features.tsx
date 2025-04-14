import React from 'react';
import { motion } from 'framer-motion';
import {
    Users,
    GitPullRequest,
    BookOpen,
    BarChart3,
    MessageSquareQuote,
    Code2
} from 'lucide-react';

const Features: React.FC = () => {
    const features = [
        {
            icon: <Users size={24} />,
            title: 'Contributor Engagement',
            description: 'Automate onboarding for new contributors with personalized welcome messages and guidance through first contribution steps.'
        },
        {
            icon: <GitPullRequest size={24} />,
            title: 'Issue Triage & PR Assistance',
            description: 'Automatically categorize issues, identify duplicates, and provide initial code review comments for PRs.'
        },
        {
            icon: <BookOpen size={24} />,
            title: 'Knowledge Base Automation',
            description: 'Extract FAQs from conversations, maintain project wikis, and provide instant answers to common questions.'
        },
        {
            icon: <BarChart3 size={24} />,
            title: 'Community Analytics',
            description: 'Track engagement metrics, analyze contribution patterns, and monitor community health across platforms.'
        },
        {
            icon: <MessageSquareQuote size={24} />,
            title: 'Multi-Platform Support',
            description: 'Seamlessly integrate with Discord, Slack, GitHub, and Discourse to provide unified experiences.'
        },
        {
            icon: <Code2 size={24} />,
            title: 'Code Understanding',
            description: 'Leverage AI to understand code context, provide meaningful suggestions, and assist with documentation.'
        }
    ];

    const container = {
        hidden: { opacity: 0 },
        show: {
            opacity: 1,
            transition: {
                staggerChildren: 0.1,
                delayChildren: 0.3,
            },
        },
    };

    const item = {
        hidden: { opacity: 0, y: 20 },
        show: { opacity: 1, y: 0 },
    };

    return (
        <section id="features" className="section pt-0 pb-12 md:pb-20 relative">
            <div className="container mx-auto px-6">
                <motion.div
                    initial={{ opacity: 0, y: 20 }}
                    whileInView={{ opacity: 1, y: 0 }}
                    viewport={{ once: true }}
                    transition={{ duration: 0.5 }}
                    className="text-center mb-10 md:mb-16"
                >
                    <h2 className="text-3xl md:text-4xl font-bold mb-4">
                        Powerful <span className="gradient-text">Features</span>
                    </h2>
                    <p className="text-gray-400 max-w-2xl mx-auto">
                        Devr.AI comes packed with tools designed to reduce maintainer workload, improve contributor experience, and enhance project visibility.
                    </p>
                </motion.div>

                <motion.div
                    variants={container}
                    initial="hidden"
                    whileInView="show"
                    viewport={{ once: true }}
                    className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8"
                >
                    {features.map((feature, index) => (
                        <motion.div
                            key={index}
                            variants={item}
                            className="card hover-lift group"
                        >
                            <div className="mb-4 text-primary p-2 rounded-lg bg-primary/10 w-fit">
                                {feature.icon}
                            </div>
                            <h3 className="text-xl font-semibold mb-2 group-hover:text-primary transition-colors">
                                {feature.title}
                            </h3>
                            <p className="text-gray-400">
                                {feature.description}
                            </p>
                        </motion.div>
                    ))}
                </motion.div>
            </div>
        </section>
    );
};

export default Features;