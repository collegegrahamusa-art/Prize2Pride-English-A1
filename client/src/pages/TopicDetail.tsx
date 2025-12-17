import { useParams, useLocation } from "wouter";
import Layout from "@/components/Layout";
import { curriculum } from "@/data/curriculum";
import { useState, useEffect } from "react";
import { ArrowLeft, ArrowRight, CheckCircle, HelpCircle, Book, MessageSquare, ListChecks, Award } from "lucide-react";
import { cn } from "@/lib/utils";
import { Button } from "@/components/ui/button";
import { toast } from "sonner";

export default function TopicDetail() {
  const { id } = useParams();
  const [, setLocation] = useLocation();
  const topicId = parseInt(id || "0");
  const topic = curriculum.topics.find((t) => t.id === topicId);

  const [activeTab, setActiveTab] = useState<"learn" | "dialogue" | "quiz">("learn");
  const [quizAnswers, setQuizAnswers] = useState<Record<number, number>>({});
  const [showResults, setShowResults] = useState(false);
  const [dialogueAnswers, setDialogueAnswers] = useState<Record<number, string>>({});
  const [dialogueResults, setDialogueResults] = useState<Record<number, boolean>>({});

  if (!topic) {
    return (
      <Layout>
        <div className="text-center py-20">
          <h2 className="text-2xl font-bold text-white">Topic not found</h2>
          <Button onClick={() => setLocation("/")} className="mt-4">
            Back to Dashboard
          </Button>
        </div>
      </Layout>
    );
  }

  const handleQuizSubmit = () => {
    setShowResults(true);
    const correctCount = topic.mcqs.filter(q => quizAnswers[q.id] === q.correctAnswer).length;
    
    if (correctCount === topic.mcqs.length) {
      toast.success("Perfect score! Job well done.");
      // Mark as completed
      const saved = JSON.parse(localStorage.getItem("completedTopics") || "[]");
      if (!saved.includes(topicId)) {
        localStorage.setItem("completedTopics", JSON.stringify([...saved, topicId]));
      }
    } else {
      toast("Review your answers and try again.");
    }
  };

  const checkDialogueAnswer = (id: number, correct: string) => {
    const userAns = dialogueAnswers[id]?.trim().toLowerCase();
    const isCorrect = userAns === correct.toLowerCase();
    setDialogueResults(prev => ({ ...prev, [id]: isCorrect }));
    if (isCorrect) toast.success("Correct!");
    else toast.error("Try again!");
  };

  return (
    <Layout>
      <div className="max-w-4xl mx-auto">
        {/* Header */}
        <div className="mb-8 flex items-center gap-4">
          <Button variant="ghost" size="icon" onClick={() => setLocation("/")} className="text-gray-400 hover:text-white">
            <ArrowLeft className="h-6 w-6" />
          </Button>
          <div>
            <div className="flex items-center gap-2 text-[#FF6B00] font-mono text-sm mb-1">
              <span>JOB #{topic.id.toString().padStart(2, '0')}</span>
              <span>•</span>
              <span>GRAMMAR SPECS</span>
            </div>
            <h1 className="text-3xl md:text-4xl font-bold text-white font-display">{topic.title}</h1>
            <p className="text-gray-400 mt-1">{topic.subtitle}</p>
          </div>
        </div>

        {/* Tabs */}
        <div className="grid grid-cols-3 gap-2 mb-8 bg-[#2D3748]/30 p-1 rounded-lg border border-[#4A5568]">
          {[
            { id: "learn", label: "1. Rule & Vocab", icon: Book },
            { id: "dialogue", label: "2. Dialogue", icon: MessageSquare },
            { id: "quiz", label: "3. Diagnostic Quiz", icon: ListChecks },
          ].map((tab) => (
            <button
              key={tab.id}
              onClick={() => setActiveTab(tab.id as any)}
              className={cn(
                "flex items-center justify-center gap-2 py-3 px-4 rounded-md text-sm font-bold transition-all",
                activeTab === tab.id
                  ? "bg-[#FF6B00] text-black shadow-lg"
                  : "text-gray-400 hover:text-white hover:bg-[#4A5568]/50"
              )}
            >
              <tab.icon className="h-4 w-4" />
              <span className="hidden md:inline">{tab.label}</span>
            </button>
          ))}
        </div>

        {/* Content Area */}
        <div className="bg-[#1A1A1A] border border-[#4A5568] rounded-xl p-6 md:p-8 shadow-2xl relative overflow-hidden">
          {/* Background Texture */}
          <div className="absolute inset-0 bg-[url('/images/card-texture.png')] opacity-5 pointer-events-none" />

          {activeTab === "learn" && (
            <div className="space-y-8 animate-in fade-in slide-in-from-bottom-4 duration-500">
              {/* Grammar Rule */}
              <section>
                <h2 className="text-xl font-bold text-[#FF6B00] mb-4 flex items-center gap-2">
                  <Book className="h-5 w-5" /> Grammar Rule
                </h2>
                <div className="bg-[#2D3748]/50 border-l-4 border-[#00E676] p-6 rounded-r-lg">
                  <p className="text-lg text-white mb-4 font-medium leading-relaxed" dir="rtl">
                    {topic.grammarRule.tunisian}
                  </p>
                  <p className="text-gray-400 italic border-t border-gray-700 pt-4">
                    {topic.grammarRule.english}
                  </p>
                </div>
              </section>

              {/* Vocabulary */}
              <section>
                <h2 className="text-xl font-bold text-[#FF6B00] mb-4 flex items-center gap-2">
                  <ListChecks className="h-5 w-5" /> Workshop Vocabulary
                </h2>
                <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                  {topic.vocabulary.map((word, idx) => (
                    <div key={idx} className="bg-[#2D3748]/30 border border-[#4A5568] p-4 rounded-lg hover:border-[#FF6B00] transition-colors">
                      <div className="flex justify-between items-start mb-2">
                        <span className="text-lg font-bold text-white">{word.word}</span>
                        <span className="text-[#00E676] font-mono text-sm">{word.tunisian}</span>
                      </div>
                      <p className="text-sm text-gray-400" dangerouslySetInnerHTML={{ __html: word.example.replace(/\*\*(.*?)\*\*/g, '<span class="text-[#FF6B00] font-bold">$1</span>') }} />
                    </div>
                  ))}
                </div>
              </section>

              <div className="flex justify-end">
                <Button onClick={() => setActiveTab("dialogue")} className="bg-[#FF6B00] hover:bg-[#FF8F00] text-black font-bold">
                  Next: Dialogue Practice <ArrowRight className="ml-2 h-4 w-4" />
                </Button>
              </div>
            </div>
          )}

          {activeTab === "dialogue" && (
            <div className="space-y-8 animate-in fade-in slide-in-from-bottom-4 duration-500">
              <section>
                <h2 className="text-xl font-bold text-[#FF6B00] mb-4 flex items-center gap-2">
                  <MessageSquare className="h-5 w-5" /> {topic.dialogue.title}
                </h2>
                
                {/* Dialogue Script */}
                <div className="space-y-4 mb-8">
                  {topic.dialogue.lines.map((line, idx) => (
                    <div key={idx} className={cn(
                      "flex gap-4 p-4 rounded-lg border",
                      line.speaker === "Oussama" 
                        ? "bg-[#2D3748]/50 border-[#FF6B00]/30 ml-8" 
                        : "bg-[#1A1A1A] border-[#4A5568] mr-8"
                    )}>
                      <div className="flex-shrink-0 w-20 font-bold text-gray-500 text-xs uppercase tracking-wider pt-1">
                        {line.speaker}
                      </div>
                      <div className="text-gray-200" dangerouslySetInnerHTML={{ __html: line.text.replace(/\*\*(.*?)\*\*/g, '<span class="text-[#FF6B00] font-bold">$1</span>') }} />
                    </div>
                  ))}
                </div>

                {/* Fill in the blanks */}
                <div className="bg-[#2D3748]/30 border border-[#4A5568] p-6 rounded-lg">
                  <h3 className="text-lg font-bold text-white mb-4">Practice: Fill in the blanks</h3>
                  <div className="space-y-4">
                    {topic.dialogue.questions.map((q) => (
                      <div key={q.id} className="flex flex-col md:flex-row md:items-center gap-4">
                        <span className="h-6 w-6 flex items-center justify-center rounded-full bg-[#4A5568] text-xs font-bold text-white">
                          {q.id}
                        </span>
                        <p className="text-gray-300 flex-grow">{q.question}</p>
                        <div className="flex gap-2">
                          <input 
                            type="text" 
                            className={cn(
                              "bg-[#1A1A1A] border rounded px-3 py-1 text-white focus:border-[#FF6B00] outline-none w-40",
                              dialogueResults[q.id] === true && "border-[#00E676] text-[#00E676]",
                              dialogueResults[q.id] === false && "border-red-500"
                            )}
                            placeholder="Type answer..."
                            value={dialogueAnswers[q.id] || ""}
                            onChange={(e) => setDialogueAnswers(prev => ({ ...prev, [q.id]: e.target.value }))}
                          />
                          <Button 
                            size="sm" 
                            variant="outline"
                            onClick={() => checkDialogueAnswer(q.id, q.answer)}
                            className="border-[#4A5568] hover:bg-[#4A5568] hover:text-white"
                          >
                            Check
                          </Button>
                        </div>
                      </div>
                    ))}
                  </div>
                </div>
              </section>

              <div className="flex justify-end">
                <Button onClick={() => setActiveTab("quiz")} className="bg-[#FF6B00] hover:bg-[#FF8F00] text-black font-bold">
                  Next: Diagnostic Quiz <ArrowRight className="ml-2 h-4 w-4" />
                </Button>
              </div>
            </div>
          )}

          {activeTab === "quiz" && (
            <div className="space-y-8 animate-in fade-in slide-in-from-bottom-4 duration-500">
              <section>
                <h2 className="text-xl font-bold text-[#FF6B00] mb-6 flex items-center gap-2">
                  <ListChecks className="h-5 w-5" /> Diagnostic Quiz
                </h2>
                
                <div className="space-y-8">
                  {topic.mcqs.map((mcq, idx) => (
                    <div key={mcq.id} className="border-b border-[#4A5568] pb-8 last:border-0">
                      <h3 className="text-lg text-white font-medium mb-4 flex gap-3">
                        <span className="text-[#FF6B00] font-mono">Q{idx + 1}.</span>
                        {mcq.question.replace("_______", "_______")}
                      </h3>
                      
                      <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
                        {mcq.options.map((option, optIdx) => {
                          const isSelected = quizAnswers[mcq.id] === optIdx;
                          const isCorrect = mcq.correctAnswer === optIdx;
                          const showCorrect = showResults && isCorrect;
                          const showWrong = showResults && isSelected && !isCorrect;

                          return (
                            <button
                              key={optIdx}
                              disabled={showResults}
                              onClick={() => setQuizAnswers(prev => ({ ...prev, [mcq.id]: optIdx }))}
                              className={cn(
                                "p-4 rounded-lg border text-left transition-all relative overflow-hidden",
                                isSelected ? "border-[#FF6B00] bg-[#FF6B00]/10" : "border-[#4A5568] bg-[#2D3748]/30 hover:bg-[#2D3748]/50",
                                showCorrect && "border-[#00E676] bg-[#00E676]/20",
                                showWrong && "border-red-500 bg-red-500/20"
                              )}
                            >
                              <span className={cn(
                                "font-medium",
                                isSelected ? "text-[#FF6B00]" : "text-gray-300",
                                showCorrect && "text-[#00E676]",
                                showWrong && "text-red-400"
                              )}>
                                {option}
                              </span>
                              
                              {showCorrect && <CheckCircle className="absolute right-4 top-4 h-5 w-5 text-[#00E676]" />}
                            </button>
                          );
                        })}
                      </div>

                      {showResults && (
                        <div className="mt-4 p-4 bg-[#2D3748] rounded border-l-4 border-[#FF6B00] text-gray-300 text-sm animate-in fade-in">
                          <span className="font-bold text-white block mb-1">Explanation:</span>
                          {mcq.explanation}
                        </div>
                      )}
                    </div>
                  ))}
                </div>
              </section>

              <div className="flex justify-end pt-4 border-t border-[#4A5568]">
                {!showResults ? (
                  <Button 
                    onClick={handleQuizSubmit} 
                    disabled={Object.keys(quizAnswers).length < topic.mcqs.length}
                    className="bg-[#FF6B00] hover:bg-[#FF8F00] text-black font-bold text-lg px-8 py-6"
                  >
                    Submit Diagnostics
                  </Button>
                ) : (
                  <Button 
                    onClick={() => setLocation("/")} 
                    className="bg-[#00E676] hover:bg-[#00C853] text-black font-bold text-lg px-8 py-6"
                  >
                    Complete Job <Award className="ml-2 h-5 w-5" />
                  </Button>
                )}
              </div>
            </div>
          )}
        </div>
      </div>
    </Layout>
  );
}
