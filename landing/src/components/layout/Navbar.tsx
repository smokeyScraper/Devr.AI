import React, { useState, useEffect } from 'react';
import { Menu, X } from 'lucide-react';
import { motion } from 'framer-motion';

const Navbar: React.FC = () => {
    const [isOpen, setIsOpen] = useState(false);
    const [scrolled, setScrolled] = useState(false);

    useEffect(() => {
        const handleScroll = () => {
            setScrolled(window.scrollY > 50);
        };

        window.addEventListener('scroll', handleScroll);
        return () => {
            window.removeEventListener('scroll', handleScroll);
        };
    }, []);

    const navLinks = [
        { name: 'Features', href: '#features' },
        { name: 'How It Works', href: '#how-it-works' },
        { name: 'Integrations', href: '#integrations' },
        { name: 'Join Waitlist', href: '#waitlist' },
    ];

    return (
        <header
            className={`fixed top-0 left-0 right-0 z-50 transition-all duration-300 ${scrolled ? 'bg-dark/90 backdrop-blur-sm py-3' : 'py-5'
                }`}
        >
            <div className="container mx-auto px-6">
                <div className="flex items-center justify-between">
                    <motion.div
                        initial={{ opacity: 0, x: -20 }}
                        animate={{ opacity: 1, x: 0 }}
                        className="flex items-center"
                    >
                        <a href="#" className="flex items-center">
                            <span className="text-2xl font-bold gradient-text">Devr.AI</span>
                        </a>
                    </motion.div>

                    {/* Desktop Nav */}
                    <motion.nav
                        initial={{ opacity: 0, y: -10 }}
                        animate={{ opacity: 1, y: 0 }}
                        className="hidden md:flex items-center space-x-8"
                    >
                        {navLinks.map((link) => (
                            <a
                                key={link.name}
                                href={link.href}
                                className={`text-sm font-medium transition-colors hover:text-primary ${link.name === 'Join Waitlist'
                                        ? 'px-4 py-2 rounded-lg bg-primary hover:bg-primary-hover text-white'
                                        : 'text-gray-300 hover:text-white'
                                    }`}
                            >
                                {link.name}
                            </a>
                        ))}
                    </motion.nav>

                    {/* Mobile Nav Toggle */}
                    <button
                        onClick={() => setIsOpen(!isOpen)}
                        className="md:hidden text-gray-300 hover:text-white"
                    >
                        {isOpen ? <X size={24} /> : <Menu size={24} />}
                    </button>
                </div>
            </div>

            {/* Mobile Nav */}
            <motion.div
                initial={{ opacity: 0, height: 0 }}
                animate={{
                    opacity: isOpen ? 1 : 0,
                    height: isOpen ? 'auto' : 0,
                }}
                className="md:hidden overflow-hidden"
            >
                <div className="container mx-auto px-6 py-4 bg-dark-lighter">
                    {navLinks.map((link) => (
                        <a
                            key={link.name}
                            href={link.href}
                            onClick={() => setIsOpen(false)}
                            className="block py-3 text-gray-300 hover:text-white"
                        >
                            {link.name}
                        </a>
                    ))}
                </div>
            </motion.div>
        </header>
    );
};

export default Navbar;