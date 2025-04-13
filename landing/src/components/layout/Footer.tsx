import React from 'react';
import { Github, Twitter, Linkedin } from 'lucide-react';

const Footer: React.FC = () => {
    const currentYear = new Date().getFullYear();

    return (
        <footer className="bg-dark-lighter py-12">
            <div className="container mx-auto px-6">
                <div className="flex flex-col md:flex-row justify-between items-center mb-8">
                    <div className="mb-6 md:mb-0">
                        <h3 className="text-2xl font-bold gradient-text mb-2">Devr.AI</h3>
                        <p className="text-gray-400 text-sm max-w-xs">
                            Revolutionizing developer relations with AI-powered community management.
                        </p>
                    </div>
                    <div className="flex flex-col gap-6 sm:flex-row sm:gap-12">
                        <div>
                            <h4 className="font-medium mb-3 text-white">Links</h4>
                            <ul className="space-y-2">
                                <li><a href="#features" className="text-gray-400 hover:text-primary text-sm">Features</a></li>
                                <li><a href="#how-it-works" className="text-gray-400 hover:text-primary text-sm">How It Works</a></li>
                                <li><a href="#integrations" className="text-gray-400 hover:text-primary text-sm">Integrations</a></li>
                                <li><a href="#waitlist" className="text-gray-400 hover:text-primary text-sm">Join Waitlist</a></li>
                            </ul>
                        </div>
                        <div>
                            <h4 className="font-medium mb-3 text-white">Legal</h4>
                            <ul className="space-y-2">
                                <li><a href="#" className="text-gray-400 hover:text-primary text-sm">Privacy Policy</a></li>
                                <li><a href="#" className="text-gray-400 hover:text-primary text-sm">Terms of Service</a></li>
                                <li><a href="#" className="text-gray-400 hover:text-primary text-sm">Cookie Policy</a></li>
                            </ul>
                        </div>
                    </div>
                </div>

                <div className="border-t border-gray-800 pt-8 flex flex-col md:flex-row justify-between items-center">
                    <p className="text-gray-500 text-sm mb-4 md:mb-0">
                        &copy; {currentYear} Devr.AI. All rights reserved.
                    </p>
                    <div className="flex space-x-6">
                        <a href="https://github.com/AOSSIE-Org/Devr.AI/" className="text-gray-400 hover:text-primary" target='_blank'>
                            <Github size={20} />
                        </a>
                        <a href="#" className="text-gray-400 hover:text-primary">
                            <Twitter size={20} />
                        </a>
                        <a href="#" className="text-gray-400 hover:text-primary">
                            <Linkedin size={20} />
                        </a>
                    </div>
                </div>
            </div>
        </footer>
    );
};

export default Footer;