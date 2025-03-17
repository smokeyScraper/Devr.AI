import React, { useEffect, useState } from 'react';
import { motion } from 'framer-motion';
import axios from 'axios';

interface PullRequest {
  number: number;
  title: string;
  author: {
    login: string;
    avatar_url: string;
    profile_url: string;
  };
  state: string;
  url: string; // URL of the pull request
}

export default function PullRequestsPage() {
  const [prs, setPrs] = useState<PullRequest[]>([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  // Fetch pull request data on mount
  useEffect(() => {
    const fetchPullRequests = async () => {
      setLoading(true);
      try {
        const response = await axios.post('http://localhost:8000/api/repo-stats', {
          repo_url: 'https://github.com/AOSSIE-Org/Devr.AI',
        });

        // Extract pull request details from the response
        const pullRequests = response.data.pull_requests.details.map((pr: any) => ({
          number: pr.number,
          title: pr.title,
          author: pr.author,
          state: pr.state,
          url: pr.url, // Add the PR URL
        }));

        setPrs(pullRequests);
      } catch (err) {
        setError('Failed to fetch pull requests. Please check the backend server.');
      } finally {
        setLoading(false);
      }
    };

    fetchPullRequests();
  }, []);

  const getStatusColor = (state: string) => {
    switch (state) {
      case 'open':
        return 'text-yellow-500';
      case 'closed':
        return 'text-red-500';
      case 'merged':
        return 'text-green-500';
      default:
        return 'text-gray-500';
    }
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
        <h1 className="text-3xl font-bold">Pull Requests</h1>
      </div>

      <div className="bg-gray-900 rounded-xl overflow-hidden">
        <table className="w-full">
          <thead className="bg-gray-800">
            <tr>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-300 uppercase tracking-wider">
                Title
              </th>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-300 uppercase tracking-wider">
                Author
              </th>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-300 uppercase tracking-wider">
                Status
              </th>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-300 uppercase tracking-wider">
                PR Number
              </th>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-300 uppercase tracking-wider">
                Link
              </th>
            </tr>
          </thead>
          <tbody className="divide-y divide-gray-800">
            {prs.map((pr) => (
              <tr key={pr.number} className="hover:bg-gray-800">
                {/* Title */}
                <td className="px-6 py-4 whitespace-nowrap text-white">{pr.title}</td>

                {/* Author */}
                <td className="px-6 py-4 whitespace-nowrap flex items-center gap-2">
                  <img
                    src={pr.author.avatar_url}
                    alt={pr.author.login}
                    className="w-8 h-8 rounded-full"
                  />
                  <a
                    href={pr.author.profile_url}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="text-blue-400 hover:text-blue-300"
                  >
                    {pr.author.login}
                  </a>
                </td>

                {/* Status */}
                <td className="px-6 py-4 whitespace-nowrap">
                  <span className={`${getStatusColor(pr.state)} capitalize`}>{pr.state}</span>
                </td>

                {/* PR Number */}
                <td className="px-6 py-4 whitespace-nowrap text-gray-300">#{pr.number}</td>

                {/* PR Link */}
                <td className="px-6 py-4 whitespace-nowrap">
                  <a
                    href={pr.url}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="text-blue-400 hover:text-blue-300 underline"
                  >
                    View PR
                  </a>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </motion.div>
  );
}
