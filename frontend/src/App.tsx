import React, { useEffect, useState } from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate, Outlet } from 'react-router-dom';
import { Toaster } from 'react-hot-toast';
import Sidebar from './components/layout/Sidebar';
import Dashboard from './components/dashboard/Dashboard';
import BotIntegrationPage from './components/integration/BotIntegrationPage';
import ContributorsPage from './components/contributors/ContributorsPage';
import PullRequestsPage from './components/pages/PullRequestsPage';
import SettingsPage from './components/pages/SettingsPage';
import AnalyticsPage from './components/pages/AnalyticsPage';
import SupportPage from './components/pages/SupportPage';
import LandingPage from './components/landing/LandingPage';
import LoginPage from './components/pages/LoginPage';
import ProfilePage from './components/pages/ProfilePage';
import { AnimatePresence } from 'framer-motion';

function App() {
  const [isSidebarOpen, setIsSidebarOpen] = useState(true);
  const [repoData, setRepoData] = useState<any>(null); // Store fetched repo stats
  const [isAuthenticated, setIsAuthenticated] = useState(false);

  // Check for existing authentication on app load
  useEffect(() => {
    const savedAuth = localStorage.getItem('isAuthenticated');
    if (savedAuth === 'true') {
      setIsAuthenticated(true);
    }
  }, []);

  const handleLogin = () => {
    setIsAuthenticated(true);
    localStorage.setItem('isAuthenticated', 'true');
  };

  const handleLogout = () => {
    setIsAuthenticated(false);
    localStorage.removeItem('isAuthenticated');
    setRepoData(null);
  };

  const ProtectedLayout = () => (
    <div className="flex">
      <Sidebar
        isOpen={isSidebarOpen}
        setIsOpen={setIsSidebarOpen}
        onLogout={handleLogout}
      />
      <main
        className={`transition-all duration-300 flex-1 ${
          isSidebarOpen ? 'ml-64' : 'ml-20'
        }`}
      >
        <div className="p-8">
          <AnimatePresence mode="wait">
            <Outlet />
          </AnimatePresence>
        </div>
      </main>
    </div>
  );

  return (
    <Router>
      <div className="min-h-screen bg-gray-950 text-white">
        <Toaster position="top-right" />
        <Routes>
          <Route
            path="/login"
            element={
              isAuthenticated ? (
                <Navigate to="/" replace />
              ) : (
                <LoginPage onLogin={handleLogin} />
              )
            }
          />
          <Route
            path="/"
            element={
              isAuthenticated ? <ProtectedLayout /> : <Navigate to="/login" replace />
            }
          >
            <Route index element={<LandingPage setRepoData={setRepoData} />} />
            <Route path="dashboard" element={<Dashboard repoData={repoData} />} />
            <Route path="integration" element={<BotIntegrationPage />} />
            <Route path="contributors" element={<ContributorsPage repoData={repoData} />} />
            <Route path="analytics" element={<AnalyticsPage repoData={repoData} />} />
            <Route path="prs" element={<PullRequestsPage repoData={repoData} />} />
            <Route path="support" element={<SupportPage />} />
            <Route path="settings" element={<SettingsPage />} />
            <Route path="profile" element={<ProfilePage />} />
          </Route>
        </Routes>
      </div>
    </Router>
  );
}

export default App;

