import Layout from "@/components/Layout";
import { curriculum } from "@/data/curriculum";
import { AlertTriangle, CheckCircle2, XCircle } from "lucide-react";

export default function Mistakes() {
  return (
    <Layout>
      <div className="max-w-4xl mx-auto">
        <div className="mb-8">
          <h1 className="text-3xl md:text-4xl font-bold text-white font-display mb-2 flex items-center gap-3">
            <AlertTriangle className="h-8 w-8 text-[#FF6B00]" />
            Common Mistakes
          </h1>
          <p className="text-gray-400">
            Watch out for these common errors. Learning from mistakes is the best way to improve.
          </p>
        </div>

        <div className="grid gap-6">
          {curriculum.commonMistakes.map((item, idx) => (
            <div key={idx} className="bg-[#1A1A1A] border border-[#4A5568] rounded-xl p-6 relative overflow-hidden group hover:border-[#FF6B00] transition-colors">
              <div className="absolute top-0 left-0 w-1 h-full bg-[#FF6B00]" />
              
              <div className="grid md:grid-cols-2 gap-6 mb-4">
                {/* Mistake */}
                <div className="bg-red-500/10 border border-red-500/20 rounded-lg p-4">
                  <div className="flex items-center gap-2 text-red-400 font-bold text-sm uppercase mb-2">
                    <XCircle className="h-4 w-4" /> Incorrect
                  </div>
                  <p className="text-lg text-white font-medium line-through decoration-red-500/50 decoration-2">
                    "{item.mistake}"
                  </p>
                </div>

                {/* Correction */}
                <div className="bg-[#00E676]/10 border border-[#00E676]/20 rounded-lg p-4">
                  <div className="flex items-center gap-2 text-[#00E676] font-bold text-sm uppercase mb-2">
                    <CheckCircle2 className="h-4 w-4" /> Correct
                  </div>
                  <p className="text-lg text-white font-medium">
                    "{item.correction}"
                  </p>
                </div>
              </div>

              <div className="bg-[#2D3748]/50 rounded p-4 text-gray-300 text-sm border-l-2 border-[#FF6B00]">
                <span className="text-[#FF6B00] font-bold mr-2">Why?</span>
                {item.explanation}
              </div>
            </div>
          ))}
        </div>
      </div>
    </Layout>
  );
}
