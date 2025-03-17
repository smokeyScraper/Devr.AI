import React, { useEffect, useState } from 'react';
import { motion } from 'framer-motion';
import { toast } from 'react-hot-toast';
import { Users, GitPullRequest, MessageSquare, Activity } from 'lucide-react';
import axios from 'axios';
import StatCard from './StatCard';
import BotIntegration from '../integration/BotIntegration';
import { Github, Slack } from 'lucide-react';

export default function Dashboard() {
  const [repoStats, setRepoStats] = useState<any>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  // Fetch repository stats on mount
  useEffect(() => {
    const fetchRepoStats = async () => {
      setLoading(true);
      try {
        const response = await axios.post('http://localhost:8000/api/repo-stats', {
          repo_url: 'https://github.com/AOSSIE-Org/Devr.AI/',
        });
        setRepoStats(response.data);
        console.log(response.data);
      } catch (err) {
        setError('Failed to fetch repository stats. Please check the backend server.');
      } finally {
        setLoading(false);
      }
    };

    fetchRepoStats();
  }, []);

  const handleNewIntegration = () => {
    toast.success('Creating new integration...');
  };

  if (loading) {
    return <div>Loading...</div>;
  }

  if (error) {
    return <div className="text-red-500">{error}</div>;
  }

  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      exit={{ opacity: 0, y: -20 }}
    >
      <div className="flex items-center justify-between mb-8">
        <h1 className="text-3xl font-bold">Dashboard Overview</h1>
        <motion.button 
          whileHover={{ scale: 1.05 }}
          whileTap={{ scale: 0.95 }}
          onClick={handleNewIntegration}
          className="px-4 py-2 bg-green-500 hover:bg-green-600 rounded-lg transition-colors"
        >
          New Integration
        </motion.button>
      </div>

      {/* Stats Section */}
      {repoStats && (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
          <StatCard 
            icon={<Users size={24} />}
            title="Active Contributors"
            value={repoStats.contributors.length}
            trend={12} // Example trend value
          />
          <StatCard 
            icon={<GitPullRequest size={24} />}
            title="Open PRs"
            value={repoStats.pull_requests.open} 
            trend={repoStats.pull_requests.open} // Example trend value
          />
          <StatCard 
            icon={<MessageSquare size={24} />}
            title="Community Posts"
            value="892" // Replace with actual backend data if available
            trend={8} // Example trend value
          />
          <StatCard 
            icon={<Activity size={24} />}
            title="Response Rate"
            value="94%" // Replace with actual backend data if available
            trend={5} // Example trend value
          />
        </div>
      )}

      {/* Quick Actions */}
      <h2 className="text-2xl font-bold mb-6">Quick Actions</h2>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <BotIntegration 
          platform="GitHub"
          icon={<Github size={24} />}
          connected={true}
          description="Automate your GitHub workflow"
          features={['Issue triage', 'PR reviews', 'Welcome messages']}
        />
        <BotIntegration 
          platform="Discord"
          icon={<MessageSquare size={24} />}
          connected={false}
          description="Engage with your community"
          features={['Support channels', 'Role management', 'Event notifications']}
        />
        <BotIntegration 
          platform="Slack"
          icon={<Slack size={24} />}
          connected={true}
          description="Team collaboration hub"
          features={['Channel monitoring', 'Instant notifications', 'Command center']}
        />
      </div>
    </motion.div>
  );
};
