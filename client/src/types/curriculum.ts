export interface DialogueLine {
  speaker: string;
  text: string;
}

export interface DialogueQuestion {
  id: number;
  question: string;
  answer: string;
}

export interface Dialogue {
  title: string;
  lines: DialogueLine[];
  questions: DialogueQuestion[];
}

export interface MCQ {
  id: number;
  question: string;
  options: string[];
  correctAnswer: number; // 0-3 index
  explanation: string;
}

export interface VocabularyItem {
  word: string;
  tunisian: string;
  example: string;
}

export interface GrammarTopic {
  id: number;
  title: string;
  subtitle: string;
  grammarRule: {
    tunisian: string;
    english: string;
  };
  dialogue: Dialogue;
  mcqs: MCQ[];
  vocabulary: VocabularyItem[];
  summary: string;
}

export interface Curriculum {
  topics: GrammarTopic[];
  commonMistakes: {
    mistake: string;
    correction: string;
    explanation: string;
  }[];
}
