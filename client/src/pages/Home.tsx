import Layout from "@/components/Layout";
import TopicCard from "@/components/TopicCard";
import { curriculum } from "@/data/curriculum";
import { useLocation } from "wouter";
import { useEffect, useState } from "react";

export default function Home() {
  const [completedTopics, setCompletedTopics] = useState<number[]>([]);

  useEffect(() => {
    const saved = localStorage.getItem("completedTopics");
    if (saved) {
      setCompletedTopics(JSON.parse(saved));
    }
  }, []);

  const progress = Math.round((completedTopics.length / curriculum.topics.length) * 100);

  return (
    <Layout>
      {/* Hero Section */}
      <div className="relative mb-12 rounded-xl overflow-hidden border border-[#4A5568] bg-[#1A1A1A]">
        <div className="absolute inset-0 bg-[url('/images/hero-workshop.png')] bg-cover bg-center opacity-40" />
        <div className="absolute inset-0 bg-gradient-to-r from-[#1A1A1A] via-[#1A1A1A]/80 to-transparent" />
        
        <div className="relative p-8 md:p-12 max-w-2xl">
          <h1 className="text-4xl md:text-5xl font-bold text-white mb-4 font-display uppercase tracking-tight">
            Welcome back, <span className="text-[#FF6B00]">Oussama</span>
          </h1>
          <p className="text-lg text-gray-300 mb-8">
            Ready to upgrade your English skills? Select a job card below to start your training.
          </p>
          
          {/* Progress Bar */}
          <div className="bg-[#2D3748] rounded-full h-4 w-full max-w-md overflow-hidden border border-[#4A5568]">
            <div 
              className="h-full bg-[#00E676] transition-all duration-1000 ease-out relative"
              style={{ width: `${progress}%` }}
            >
              <div className="absolute inset-0 bg-white/20 animate-pulse" />
            </div>
          </div>
          <div className="flex justify-between max-w-md mt-2 text-sm font-mono text-gray-400">
            <span>PROGRESS</span>
            <span>{progress}% COMPLETED</span>
          </div>
        </div>
      </div>

      {/* Topics Grid */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {curriculum.topics.map((topic) => (
          <TopicCard 
            key={topic.id} 
            topic={topic} 
            isCompleted={completedTopics.includes(topic.id)}
          />
        ))}
      </div>
    </Layout>
  );
}
