import React, { useEffect } from 'react';
import { Toaster } from 'react-hot-toast';
import Lenis from '@studio-freight/lenis';
import Hero from './components/sections/Hero';
import Features from './components/sections/Features';
import HowItWorks from './components/sections/HowItWorks';
import Integrations from './components/sections/Integrations';
import Waitlist from './components/sections/Waitlist';
import Footer from './components/layout/Footer';
import Navbar from './components/layout/Navbar';

function App() {
  useEffect(() => {
    // Initialize smooth scroll
    const lenis = new Lenis({
      duration: 1.2,
      easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
      smoothWheel: true,
    });

    function raf(time: number) {
      lenis.raf(time);
      requestAnimationFrame(raf);
    }

    requestAnimationFrame(raf);
  }, []);

  return (
    <div className="min-h-screen bg-dark">
      <Navbar />
      <main>
        <Hero />
        <Features />
        <HowItWorks />
        <Integrations />
        <Waitlist />
      </main>
      <Footer />
      <Toaster position="top-right" />
    </div>
  );
}

export default App;