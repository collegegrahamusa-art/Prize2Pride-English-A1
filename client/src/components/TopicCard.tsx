import { Link } from "wouter";
import { GrammarTopic } from "../types/curriculum";
import { CheckCircle2, Circle, ArrowRight } from "lucide-react";
import { cn } from "@/lib/utils";

interface TopicCardProps {
  topic: GrammarTopic;
  isCompleted?: boolean;
}

export default function TopicCard({ topic, isCompleted = false }: TopicCardProps) {
  return (
    <Link href={`/topic/${topic.id}`}>
      <a className="group relative block h-full overflow-hidden rounded-lg border border-[#4A5568] bg-[#2D3748]/30 hover:bg-[#2D3748]/50 transition-all hover:border-[#FF6B00]">
        {/* Status Indicator Strip */}
        <div className={cn(
          "absolute left-0 top-0 bottom-0 w-1 transition-colors",
          isCompleted ? "bg-[#00E676]" : "bg-[#FF6B00] group-hover:bg-[#FF8F00]"
        )} />

        <div className="p-6 pl-8">
          <div className="flex items-start justify-between mb-4">
            <span className="font-mono text-xs text-[#FF6B00] uppercase tracking-wider border border-[#FF6B00]/30 px-2 py-1 rounded bg-[#FF6B00]/10">
              JOB #{topic.id.toString().padStart(2, '0')}
            </span>
            {isCompleted ? (
              <CheckCircle2 className="h-5 w-5 text-[#00E676]" />
            ) : (
              <Circle className="h-5 w-5 text-gray-600 group-hover:text-[#FF6B00] transition-colors" />
            )}
          </div>

          <h3 className="text-xl font-bold text-white mb-2 group-hover:text-[#FF6B00] transition-colors font-display">
            {topic.title}
          </h3>
          
          <p className="text-sm text-gray-400 mb-6 line-clamp-2">
            {topic.subtitle}
          </p>

          <div className="flex items-center text-sm font-medium text-gray-500 group-hover:text-white transition-colors mt-auto">
            <span>Start Job</span>
            <ArrowRight className="ml-2 h-4 w-4 transform group-hover:translate-x-1 transition-transform" />
          </div>
        </div>
        
        {/* Background Texture Overlay */}
        <div className="absolute inset-0 bg-[url('/images/card-texture.png')] opacity-10 pointer-events-none mix-blend-overlay" />
      </a>
    </Link>
  );
}
