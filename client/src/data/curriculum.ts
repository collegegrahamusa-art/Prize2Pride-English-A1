import { Curriculum, GrammarTopic } from "../types/curriculum";

export const curriculum: Curriculum = {
  topics: [
    {
      id: 1,
      title: "Simple Present",
      subtitle: "Daily Routines and Facts",
      grammarRule: {
        tunisian: "Hādha nistā3mlouh kī nḥabbou nḥkiw 3ala ḥājāt tṣīr dīman, kī l-khidma mta3 Oussama, wālla ḥājāt ṣaḥīḥa. M3a 'he', 'she', w 'it', nzidou 's' l-l-fē3l. Kīma 'He works' wālla 'It starts'.",
        english: "(We use this when we want to talk about things that happen always, like Oussama's work, or things that are true. With 'he', 'she', and 'it', we add 's' to the verb. Like 'He works' or 'It starts'.)"
      },
      dialogue: {
        title: "Oussama's Morning Routine",
        lines: [
          { speaker: "Customer", text: "Hello, Oussama. What time **do** you **open** the garage?" },
          { speaker: "Oussama", text: "I always **open** at 8:00 AM. My assistant, Karim, **cleans** the tools first." },
          { speaker: "Customer", text: "My car **needs** a new battery. **Does** the shop **close** for lunch?" },
          { speaker: "Oussama", text: "No, we **work** all day. Karim **takes** a break at 1:00 PM." }
        ],
        questions: [
          { id: 1, question: "Oussama always _______ (check) the oil level.", answer: "checks" },
          { id: 2, question: "The customer's car _______ (not start) in the morning.", answer: "doesn't start" },
          { id: 3, question: "_______ (Do/Does) the engine _______ (make) a strange noise?", answer: "Does / make" }
        ]
      },
      mcqs: [
        {
          id: 1,
          question: "Karim _______ the tools every morning.",
          options: ["clean", "cleans", "cleaning", "cleaned"],
          correctAnswer: 1,
          explanation: "With 'Karim' (he), we must add 's' to the verb in Simple Present. So 'cleans' is correct."
        },
        {
          id: 2,
          question: "_______ you fix BMW cars?",
          options: ["Does", "Is", "Do", "Are"],
          correctAnswer: 2,
          explanation: "With 'you', we use 'Do' to ask questions in Simple Present. 'Does' is for he/she/it."
        },
        {
          id: 3,
          question: "The garage _______ on Sundays.",
          options: ["not open", "don't open", "doesn't open", "no open"],
          correctAnswer: 2,
          explanation: "The garage is 'it'. For negatives with he/she/it, we use 'doesn't' + verb."
        }
      ],
      vocabulary: [
        { word: "Engine", tunisian: "Moteur", example: "The **engine** is the heart of the car." },
        { word: "Tool", tunisian: "Adāt / Mātériel", example: "Hand me that **tool**, please." },
        { word: "Check", tunisian: "Ythabbet", example: "I **check** the tires every day." },
        { word: "Fix", tunisian: "Yṣallaḥ", example: "We **fix** all types of cars here." }
      ],
      summary: "Use Simple Present for things you do every day (routines) and facts that are always true."
    },
    {
      id: 2,
      title: "Simple Past",
      subtitle: "Completed Actions",
      grammarRule: {
        tunisian: "Nistā3mlouh kī nḥkiw 3ala ḥāja ṣāret w wfāt fī l-māḍī. Zid 'ed' l-l-fē3l l-3ādī (kīma 'worked'). Fammā af3āl ttbaddel kīma 'go' twalli 'went'.",
        english: "(We use it when we talk about something that happened and finished in the past. Add 'ed' to regular verbs (like 'worked'). Some verbs change, like 'go' becomes 'went'.)"
      },
      dialogue: {
        title: "Discussing Yesterday's Repair",
        lines: [
          { speaker: "Karim", text: "Oussama, **did** you **finish** the Toyota yesterday?" },
          { speaker: "Oussama", text: "Yes, I **changed** the oil and **checked** the brakes." },
          { speaker: "Karim", text: "What about the flat tire? **Did** the customer **wait**?" },
          { speaker: "Oussama", text: "No, he **left** the car and **came** back later. We **fixed** it quickly." }
        ],
        questions: [
          { id: 1, question: "I _______ (repair) the engine last night.", answer: "repaired" },
          { id: 2, question: "He _______ (buy) a new wrench yesterday.", answer: "bought" },
          { id: 3, question: "_______ (Did) you _______ (see) the scratch on the door?", answer: "Did / see" }
        ]
      },
      mcqs: [
        {
          id: 1,
          question: "Yesterday, I _______ a new battery.",
          options: ["buy", "buyed", "bought", "buying"],
          correctAnswer: 2,
          explanation: "'Buy' is an irregular verb. The past form is 'bought', not 'buyed'."
        },
        {
          id: 2,
          question: "She _______ come to the garage last week.",
          options: ["didn't", "don't", "doesn't", "wasn't"],
          correctAnswer: 0,
          explanation: "For negatives in the past, we use 'didn't' for all persons (I, you, he, she, etc.)."
        },
        {
          id: 3,
          question: "When _______ you start working as a mechanic?",
          options: ["do", "did", "were", "have"],
          correctAnswer: 1,
          explanation: "We use 'did' to ask questions about the past."
        }
      ],
      vocabulary: [
        { word: "Yesterday", tunisian: "El-bāraḥ", example: "I worked late **yesterday**." },
        { word: "Last week", tunisian: "El-jem3a lī fātet", example: "We were very busy **last week**." },
        { word: "Bought", tunisian: "Chrā", example: "He **bought** new tires." },
        { word: "Sold", tunisian: "Bā3", example: "I **sold** my old car." }
      ],
      summary: "Use Simple Past for actions that started and finished in the past. Watch out for irregular verbs!"
    },
    {
      id: 3,
      title: "Present Perfect",
      subtitle: "Recent Past with Present Relevance",
      grammarRule: {
        tunisian: "Hādha nistā3mlouh kī ḥāja ṣāret fī l-māḍī āmā māzāl 3andhā 2ahamiyya tawa, wālla kī mā nqūlūch waqtāsh ṣāret biḍḍabṭ. Nistā3mlou 'have' wālla 'has' + l-fē3l fī taṣrīf thāleth (Past Participle).",
        english: "(We use this when something happened in the past but still has importance now, or when we don't say exactly when it happened. We use 'have' or 'has' + the verb in the third form (Past Participle).)"
      },
      dialogue: {
        title: "Checking Status of Repairs",
        lines: [
          { speaker: "Customer", text: "Hi Oussama, **have** you **checked** my car yet?" },
          { speaker: "Oussama", text: "Yes, I **have found** the problem. The radiator is broken." },
          { speaker: "Customer", text: "**Has** Karim **ordered** the new part?" },
          { speaker: "Oussama", text: "He **has** just **called** the supplier. It will arrive soon." }
        ],
        questions: [
          { id: 1, question: "We _______ (have/has) finished the work.", answer: "have" },
          { id: 2, question: "She _______ (have/has) lost her car keys.", answer: "has" },
          { id: 3, question: "I _______ (never/be) to Germany.", answer: "have never been" }
        ]
      },
      mcqs: [
        {
          id: 1,
          question: "I _______ fixed three cars today.",
          options: ["have", "has", "had", "did"],
          correctAnswer: 0,
          explanation: "With 'I', we use 'have'. The time period 'today' is not finished, so Present Perfect is good."
        },
        {
          id: 2,
          question: "_______ Oussama seen the new tools?",
          options: ["Have", "Has", "Did", "Is"],
          correctAnswer: 1,
          explanation: "Oussama is 'he', so we use 'Has'."
        },
        {
          id: 3,
          question: "We have _______ the engine oil.",
          options: ["change", "changed", "changing", "changes"],
          correctAnswer: 1,
          explanation: "After 'have', we need the Past Participle. For regular verbs like 'change', it ends in 'ed'."
        }
      ],
      vocabulary: [
        { word: "Already", tunisian: "Sāyē / Dījā", example: "I have **already** done it." },
        { word: "Yet", tunisian: "L-tawa", example: "Have you finished **yet**?" },
        { word: "Just", tunisian: "Tawa kī", example: "He has **just** left." },
        { word: "Since", tunisian: "Melli", example: "I have worked here **since** 2010." }
      ],
      summary: "Use Present Perfect for past actions that are important now, or when the time isn't specific."
    },
    {
      id: 4,
      title: "Past Continuous",
      subtitle: "Ongoing Actions in the Past",
      grammarRule: {
        tunisian: "Nistā3mlouh kī nḥkiw 3ala ḥāja kānet qā3da tṣīr fī waqt m3ayyen fī l-māḍī. Dīma 'was' wālla 'were' + fē3l + 'ing'. Kīma 'I was working'.",
        english: "(We use it to talk about something that was happening at a specific time in the past. Always 'was' or 'were' + verb + 'ing'. Like 'I was working'.)"
      },
      dialogue: {
        title: "The Interrupted Job",
        lines: [
          { speaker: "Karim", text: "What **were** you **doing** when the lights went out?" },
          { speaker: "Oussama", text: "I **was welding** the exhaust pipe. It was dangerous!" },
          { speaker: "Karim", text: "I **was looking** for the flashlight. The customer **was waiting** outside." },
          { speaker: "Oussama", text: "Luckily, the power came back quickly while we **were talking**." }
        ],
        questions: [
          { id: 1, question: "At 9 AM, I _______ (drive) to the garage.", answer: "was driving" },
          { id: 2, question: "They _______ (not / work) when I arrived.", answer: "weren't working" },
          { id: 3, question: "What _______ (you / do) when I called?", answer: "were you doing" }
        ]
      },
      mcqs: [
        {
          id: 1,
          question: "I _______ working on the Audi when you called.",
          options: ["am", "was", "were", "been"],
          correctAnswer: 1,
          explanation: "With 'I', we use 'was' for the past."
        },
        {
          id: 2,
          question: "The mechanics _______ repairing the truck all night.",
          options: ["was", "were", "is", "are"],
          correctAnswer: 1,
          explanation: "'Mechanics' is plural (they), so we use 'were'."
        },
        {
          id: 3,
          question: "He was _______ the tire when it exploded.",
          options: ["inflate", "inflated", "inflating", "inflates"],
          correctAnswer: 2,
          explanation: "Past Continuous always uses verb + ing."
        }
      ],
      vocabulary: [
        { word: "While", tunisian: "Fī waqt mā / Mādām", example: "He called **while** I was working." },
        { word: "When", tunisian: "Waqt elli", example: "I was sleeping **when** you arrived." },
        { word: "Welding", tunisian: "Soudure", example: "He is good at **welding**." },
        { word: "Waiting", tunisian: "Yistannā", example: "The customer is **waiting**." }
      ],
      summary: "Use Past Continuous for actions that were in progress at a specific moment in the past."
    },
    {
      id: 5,
      title: "Simple Future (Will)",
      subtitle: "Spontaneous Decisions and Predictions",
      grammarRule: {
        tunisian: "Nistā3mlou 'will' kī nākhdhou qarār tawa tawa, wālla kī ntwaq3ou ḥāja bāsh tṣīr. Sāhel barchā: 'will' + l-fē3l kīma hūwa. 'I will help you'.",
        english: "(We use 'will' when we make a decision right now, or predict something will happen. Very simple: 'will' + the verb as it is. 'I will help you'.)"
      },
      dialogue: {
        title: "A Sudden Problem",
        lines: [
          { speaker: "Customer", text: "Oh no, I have a flat tire! I'm late for work." },
          { speaker: "Oussama", text: "Don't worry. I **will change** it for you right now." },
          { speaker: "Customer", text: "Thank you! How much **will** it **cost**?" },
          { speaker: "Oussama", text: "It **will be** 20 Dinars. I **will bring** the jack." }
        ],
        questions: [
          { id: 1, question: "I think it _______ (rain) tomorrow.", answer: "will rain" },
          { id: 2, question: "Wait, I _______ (help) you with that heavy box.", answer: "will help" },
          { id: 3, question: "_______ (Will) you _______ (call) me later?", answer: "Will / call" }
        ]
      },
      mcqs: [
        {
          id: 1,
          question: "The phone is ringing. I _______ answer it.",
          options: ["will", "am going to", "am", "will be"],
          correctAnswer: 0,
          explanation: "This is a spontaneous decision (decided right now), so we use 'will'."
        },
        {
          id: 2,
          question: "In 2050, cars _______ fly.",
          options: ["will", "did", "have", "are"],
          correctAnswer: 0,
          explanation: "This is a prediction about the future, so we use 'will'."
        },
        {
          id: 3,
          question: "I promise I _______ finish the car today.",
          options: ["will", "am", "do", "have"],
          correctAnswer: 0,
          explanation: "We use 'will' for promises."
        }
      ],
      vocabulary: [
        { word: "Tomorrow", tunisian: "Ghodwa", example: "See you **tomorrow**." },
        { word: "Next year", tunisian: "El-3ām el-jāy", example: "I will buy a new shop **next year**." },
        { word: "Hope", tunisian: "Yitmānnā", example: "I **hope** it works." },
        { word: "Promise", tunisian: "Yū3ed", example: "I **promise** to fix it." }
      ],
      summary: "Use 'will' for decisions made at the moment of speaking, predictions, and promises."
    },
    {
      id: 6,
      title: "Future with 'Going To'",
      subtitle: "Planned Future Actions",
      grammarRule: {
        tunisian: "Hādha nistā3mlouh kī ybda 3andnā khṭṭa wālla niyya bāsh na3mlou ḥāja. 'Am/Is/Are' + 'going to' + l-fē3l. 'I am going to buy a new tool'.",
        english: "(We use this when we have a plan or intention to do something. 'Am/Is/Are' + 'going to' + the verb. 'I am going to buy a new tool'.)"
      },
      dialogue: {
        title: "Planning the Week",
        lines: [
          { speaker: "Karim", text: "What **are** you **going to do** this weekend, Oussama?" },
          { speaker: "Oussama", text: "I **am going to paint** the garage walls. They look old." },
          { speaker: "Karim", text: "**Is** the supplier **going to deliver** the paint today?" },
          { speaker: "Oussama", text: "Yes, he **is going to come** at 5 PM. We **are going to start** Saturday morning." }
        ],
        questions: [
          { id: 1, question: "She _______ (buy) a new car next month.", answer: "is going to buy" },
          { id: 2, question: "We _______ (not / work) on Friday.", answer: "are not going to work" },
          { id: 3, question: "_______ (Are) you _______ (visit) your family?", answer: "Are / going to visit" }
        ]
      },
      mcqs: [
        {
          id: 1,
          question: "Look at those dark clouds! It _______ rain.",
          options: ["is going to", "will", "is", "goes to"],
          correctAnswer: 0,
          explanation: "When we see evidence (clouds) that something is about to happen, we use 'going to'."
        },
        {
          id: 2,
          question: "I _______ visit my brother in France next summer. I have the ticket.",
          options: ["will", "am going to", "go to", "am"],
          correctAnswer: 1,
          explanation: "It is a plan (I have the ticket), so 'am going to' is better than 'will'."
        },
        {
          id: 3,
          question: "What _______ you going to do?",
          options: ["are", "do", "will", "have"],
          correctAnswer: 0,
          explanation: "The structure is 'Are you going to...'."
        }
      ],
      vocabulary: [
        { word: "Plan", tunisian: "Khṭṭa / Ykhaṭṭet", example: "That is a good **plan**." },
        { word: "Intend", tunisian: "Ynwi", example: "I **intend** to finish early." },
        { word: "Soon", tunisian: "Qarīban", example: "He is coming **soon**." },
        { word: "Prepare", tunisian: "Yḥaḍḍer", example: "Please **prepare** the invoice." }
      ],
      summary: "Use 'going to' for plans you already made and predictions based on what you see."
    }
  ],
  commonMistakes: []
};

// Appending Topics 7-12
const additionalTopics: GrammarTopic[] = [
    {
      id: 7,
      title: "If Conditionals",
      subtitle: "Zero, First, and Second Conditionals",
      grammarRule: {
        tunisian: "Zero: Ḥaqā'iq (If you heat water, it boils). First: Ḥāja momken tṣīr (If it rains, I will stay home). Second: Ḥāja takhayyuliyya (If I had money, I would buy a Ferrari).",
        english: "(Zero: Facts (If you heat water, it boils). First: Possible future (If it rains, I will stay home). Second: Imaginary (If I had money, I would buy a Ferrari).)"
      },
      dialogue: {
        title: "Troubleshooting and Dreaming",
        lines: [
          { speaker: "Customer", text: "What happens **if** I **don't change** the oil?" },
          { speaker: "Oussama", text: "**If** you **don't change** it, the engine **breaks**." },
          { speaker: "Customer", text: "Okay. **If** I **leave** the car now, **will** you **finish** today?" },
          { speaker: "Oussama", text: "Yes. But **if** I **were** you, I **would wait** for the new tires too." }
        ],
        questions: [
          { id: 1, question: "If you _______ (mix) red and blue, you get purple.", answer: "mix" },
          { id: 2, question: "If he _______ (come) early, we will start.", answer: "comes" },
          { id: 3, question: "If I _______ (be) rich, I would travel.", answer: "were" }
        ]
      },
      mcqs: [
        {
          id: 1,
          question: "If you touch fire, you _______ burned.",
          options: ["get", "will get", "got", "getting"],
          correctAnswer: 0,
          explanation: "This is a general fact (Zero Conditional), so we use Present Simple in both parts."
        },
        {
          id: 2,
          question: "If I _______ time, I will help you.",
          options: ["have", "had", "has", "having"],
          correctAnswer: 0,
          explanation: "First Conditional (possible future): If + Present, Will + Verb."
        },
        {
          id: 3,
          question: "If I _______ a mechanic, I would fix my own car.",
          options: ["am", "was", "were", "been"],
          correctAnswer: 2,
          explanation: "Second Conditional (imaginary): We usually use 'were' for all persons (If I were, If he were)."
        }
      ],
      vocabulary: [
        { word: "If", tunisian: "Idhā / Kān", example: "**If** you go, I go." },
        { word: "Unless", tunisian: "Illā idhā", example: "Don't stop **unless** I tell you." },
        { word: "Result", tunisian: "Natīja", example: "The **result** was good." },
        { word: "Condition", tunisian: "Charṭ / Ḥāla", example: "The car is in good **condition**." }
      ],
      summary: "Use Zero for facts, First for likely future, and Second for imaginary situations."
    },
    {
      id: 8,
      title: "Adjectives and Adverbs",
      subtitle: "Describing Things and Actions",
      grammarRule: {
        tunisian: "Adjective yūṣef l-ism (A *fast* car). Adverb yūṣef l-fē3l (He drives *fast* / He works *slowly*). Aghlab l-adverbs yūfāw b-'ly', āmā fammā chwāya lā (fast, hard, good -> well).",
        english: "(Adjective describes the noun (A *fast* car). Adverb describes the verb (He drives *fast* / He works *slowly*). Most adverbs end in 'ly', but some don't (fast, hard, good -> well).)"
      },
      dialogue: {
        title: "A Careful Job",
        lines: [
          { speaker: "Oussama", text: "Karim, please work **carefully** on this engine. It is **expensive**." },
          { speaker: "Karim", text: "Don't worry, I always work **slowly** and **well**." },
          { speaker: "Oussama", text: "Good. The customer was **angry** yesterday because the other car was **dirty**." },
          { speaker: "Karim", text: "I will clean this one **perfectly**." }
        ],
        questions: [
          { id: 1, question: "He is a _______ (good/well) driver.", answer: "good" },
          { id: 2, question: "He drives _______ (good/well).", answer: "well" },
          { id: 3, question: "Please speak _______ (quiet/quietly).", answer: "quietly" }
        ]
      },
      mcqs: [
        {
          id: 1,
          question: "The mechanic works _______.",
          options: ["hard", "hardly", "harder", "hardest"],
          correctAnswer: 0,
          explanation: "'Hard' is an irregular adverb. 'Hardly' means 'almost not', which is different."
        },
        {
          id: 2,
          question: "This car is very _______.",
          options: ["fast", "fastly", "faster", "fastest"],
          correctAnswer: 0,
          explanation: "We need an adjective here to describe the car. 'Fast' is the adjective."
        },
        {
          id: 3,
          question: "She sings _______.",
          options: ["beautiful", "beautifully", "beauty", "beauties"],
          correctAnswer: 1,
          explanation: "We need an adverb to describe how she sings. 'Beautifully' is the adverb."
        }
      ],
      vocabulary: [
        { word: "Quickly", tunisian: "Fīsa3", example: "Come here **quickly**!" },
        { word: "Careful", tunisian: "Rādd bālek", example: "Be **careful** with that glass." },
        { word: "Loud", tunisian: "3āli (ṣawt)", example: "The engine is too **loud**." },
        { word: "Quietly", tunisian: "B-chwāya", example: "He works **quietly**." }
      ],
      summary: "Adjectives describe things (nouns). Adverbs describe actions (verbs). Many adverbs end in -ly."
    },
    {
      id: 9,
      title: "Comparatives and Superlatives",
      subtitle: "Comparing Things",
      grammarRule: {
        tunisian: "Comparative: Tqāren zūz ḥājāt (Bigger than, More expensive than). Superlative: Tqāren ḥāja b-l-majmū3a l-koll (The biggest, The most expensive). Irregular: Good -> Better -> Best.",
        english: "(Comparative: Compare two things (Bigger than, More expensive than). Superlative: Compare one thing to the group (The biggest, The most expensive). Irregular: Good -> Better -> Best.)"
      },
      dialogue: {
        title: "Choosing the Right Parts",
        lines: [
          { speaker: "Customer", text: "Which battery is **better**, the Bosch or the Varta?" },
          { speaker: "Oussama", text: "The Bosch is **more expensive**, but it is **stronger**." },
          { speaker: "Customer", text: "I want the **cheapest** one you have." },
          { speaker: "Oussama", text: "Okay, but the **best** quality is usually the **safest** choice." }
        ],
        questions: [
          { id: 1, question: "This car is _______ (fast) than that one.", answer: "faster" },
          { id: 2, question: "He is the _______ (old) mechanic in town.", answer: "oldest" },
          { id: 3, question: "This job is _______ (difficult) than I thought.", answer: "more difficult" }
        ]
      },
      mcqs: [
        {
          id: 1,
          question: "My car is _______ than yours.",
          options: ["bad", "worse", "worst", "badder"],
          correctAnswer: 1,
          explanation: "'Bad' is irregular. The comparative is 'worse'."
        },
        {
          id: 2,
          question: "This is the _______ day of my life.",
          options: ["happy", "happier", "happiest", "most happy"],
          correctAnswer: 2,
          explanation: "Superlative of 'happy' (ends in y) -> 'happiest'."
        },
        {
          id: 3,
          question: "Ferraris are _______ than Fiats.",
          options: ["expensive", "more expensive", "expensiver", "most expensive"],
          correctAnswer: 1,
          explanation: "Long adjectives (3+ syllables) use 'more' for comparative."
        }
      ],
      vocabulary: [
        { word: "Better", tunisian: "Khīr", example: "This oil is **better**." },
        { word: "Worse", tunisian: "Akhyeb", example: "The noise is **worse** now." },
        { word: "Cheaper", tunisian: "Arkhaṣ", example: "Is there a **cheaper** option?" },
        { word: "Most", tunisian: "Akther", example: "The **most** important thing." }
      ],
      summary: "Use -er/more for comparing two things. Use -est/most for the 'number one' in a group."
    },
    {
      id: 10,
      title: "Verbs 'To Be' and 'To Have'",
      subtitle: "Essential Verbs",
      grammarRule: {
        tunisian: "To Be (I am, You are, He is) nistā3mlouh l-l-waṣf (I am a mechanic). To Have (I have, You have, He has) nistā3mlouh l-l-milk (I have a car).",
        english: "(To Be (I am, You are, He is) used for description (I am a mechanic). To Have (I have, You have, He has) used for possession (I have a car).)"
      },
      dialogue: {
        title: "Introduction and Inventory",
        lines: [
          { speaker: "Customer", text: "**Are** you the owner of this garage?" },
          { speaker: "Oussama", text: "Yes, I **am**. I **have** ten years of experience." },
          { speaker: "Customer", text: "**Do** you **have** time to look at my brakes?" },
          { speaker: "Oussama", text: "Yes, I **am** free now. My assistant **has** the tools ready." }
        ],
        questions: [
          { id: 1, question: "She _______ (is/has) a new car.", answer: "has" },
          { id: 2, question: "They _______ (are/have) very tired.", answer: "are" },
          { id: 3, question: "_______ (Are/Do) you have a wrench?", answer: "Do" }
        ]
      },
      mcqs: [
        {
          id: 1,
          question: "He _______ a good mechanic.",
          options: ["is", "has", "have", "are"],
          correctAnswer: 0,
          explanation: "We are describing him, so we use 'is' (To Be)."
        },
        {
          id: 2,
          question: "We _______ three lifts in the garage.",
          options: ["is", "are", "have", "has"],
          correctAnswer: 2,
          explanation: "We are talking about possession (what we own), so we use 'have'."
        },
        {
          id: 3,
          question: "_______ you hungry?",
          options: ["Do", "Have", "Are", "Is"],
          correctAnswer: 2,
          explanation: "Hungry is an adjective (description), so we ask with 'Are'."
        }
      ],
      vocabulary: [
        { word: "Owner", tunisian: "Mūlā (l-maḥall)", example: "He is the **owner**." },
        { word: "Experience", tunisian: "Khibra", example: "She has a lot of **experience**." },
        { word: "Busy", tunisian: "Mashghūl", example: "I am very **busy**." },
        { word: "Free", tunisian: "Fāḍī / Lībr", example: "Are you **free** now?" }
      ],
      summary: "Use 'Be' to say what something IS. Use 'Have' to say what someone OWNS."
    },
    {
      id: 11,
      title: "Vocabulary",
      subtitle: "Garage Essentials",
      grammarRule: {
        tunisian: "Hādha mouch qā3da, hādha qāmūs ṣghīr l-l-kalimāt l-muhimma fī l-garāj. Aḥfaḍhom b-l-gdā!",
        english: "(This isn't a rule, it's a small dictionary for important garage words. Memorize them well!)"
      },
      dialogue: {
        title: "Naming the Parts",
        lines: [
          { speaker: "Oussama", text: "Karim, pass me the **wrench** and the **screwdriver**." },
          { speaker: "Karim", text: "Here they are. Do you need the **jack** too?" },
          { speaker: "Oussama", text: "No, just check the **spark plugs** and the **filter**." },
          { speaker: "Karim", text: "The **gearbox** looks fine, but the **clutch** is worn out." }
        ],
        questions: [
          { id: 1, question: "Use a _______ (hammer/wrench) to turn the bolt.", answer: "wrench" },
          { id: 2, question: "The car needs a new _______ (battery/tire) to start.", answer: "battery" },
          { id: 3, question: "Check the oil _______ (level/light).", answer: "level" }
        ]
      },
      mcqs: [
        {
          id: 1,
          question: "What do you use to lift a car?",
          options: ["Wrench", "Jack", "Hammer", "Filter"],
          correctAnswer: 1,
          explanation: "A 'Jack' (Cric) is used to lift the car."
        },
        {
          id: 2,
          question: "The _______ charges the battery while the engine runs.",
          options: ["Alternator", "Radiator", "Carburetor", "Brake"],
          correctAnswer: 0,
          explanation: "The Alternator generates electricity."
        },
        {
          id: 3,
          question: "You use a _______ to tighten a screw.",
          options: ["Hammer", "Screwdriver", "Saw", "Pump"],
          correctAnswer: 1,
          explanation: "Screwdriver (Tournevis) is for screws."
        }
      ],
      vocabulary: [
        { word: "Wrench", tunisian: "Miftāḥ", example: "I need a 10mm **wrench**." },
        { word: "Screwdriver", tunisian: "Tournevis", example: "Pass the **screwdriver**." },
        { word: "Jack", tunisian: "Cric", example: "Lift it with the **jack**." },
        { word: "Spare part", tunisian: "Pièce de rechange", example: "We need a **spare part**." }
      ],
      summary: "Focus on learning the names of tools and car parts."
    },
    {
      id: 12,
      title: "Common Confusions",
      subtitle: "Tricky Words",
      grammarRule: {
        tunisian: "Fammā kalimāt ychbbhou l-b3aḍhom. Too (barchā/zāda) vs To (ila). Their (mtā3hom) vs There (ghādī). Its (mtā3ou) vs It's (hūwa).",
        english: "(Some words look similar. Too (very/also) vs To (towards). Their (possession) vs There (place). Its (possession) vs It's (it is).)"
      },
      dialogue: {
        title: "Writing the Invoice",
        lines: [
          { speaker: "Customer", text: "Is **it's** (wrong) / **it's** (right) ready?" },
          { speaker: "Oussama", text: "Yes, **it's** ready. The price is not **too** high." },
          { speaker: "Customer", text: "Can I go **to** the office **to** pay?" },
          { speaker: "Oussama", text: "Yes, over **there**. Their machine is working now." }
        ],
        questions: [
          { id: 1, question: "I am tired _______ (to/too).", answer: "too" },
          { id: 2, question: "_______ (There/Their) car is red.", answer: "Their" },
          { id: 3, question: "_______ (It's/Its) a nice day.", answer: "It's" }
        ]
      },
      mcqs: [
        {
          id: 1,
          question: "I want _______ go home.",
          options: ["to", "too", "two", "toe"],
          correctAnswer: 0,
          explanation: "We use 'to' with verbs (to go, to eat)."
        },
        {
          id: 2,
          question: "This car is _______ expensive.",
          options: ["to", "too", "two", "toe"],
          correctAnswer: 1,
          explanation: "We use 'too' to mean 'very' or 'excessively'."
        },
        {
          id: 3,
          question: "The dog ate _______ food.",
          options: ["it's", "its", "is", "it"],
          correctAnswer: 1,
          explanation: "'Its' (no apostrophe) is for possession. 'It's' means 'It is'."
        }
      ],
      vocabulary: [
        { word: "Too", tunisian: "Barchā / Zāda", example: "It is **too** hot." },
        { word: "To", tunisian: "Ila / Bāsh", example: "I want **to** sleep." },
        { word: "There", tunisian: "Ghādī / Fammā", example: "**There** is a car." },
        { word: "Their", tunisian: "Mtā3hom", example: "It is **their** house." }
      ],
      summary: "Watch out for words that sound the same but have different spellings and meanings!"
    }
];

curriculum.topics = [...curriculum.topics, ...additionalTopics];

curriculum.commonMistakes = [
  {
    mistake: "I have 25 years.",
    correction: "I am 25 years old.",
    explanation: "In English, we use 'to be' for age, not 'to have'."
  },
  {
    mistake: "I am mechanic.",
    correction: "I am a mechanic.",
    explanation: "We need the article 'a' before professions."
  },
  {
    mistake: "He work here.",
    correction: "He works here.",
    explanation: "Don't forget the 's' for he/she/it in Simple Present."
  },
  {
    mistake: "I didn't went.",
    correction: "I didn't go.",
    explanation: "After 'didn't', use the base form of the verb."
  },
  {
    mistake: "It is more good.",
    correction: "It is better.",
    explanation: "'Good' is irregular. Comparative is 'better', not 'more good'."
  },
  {
    mistake: "I am agree.",
    correction: "I agree.",
    explanation: "'Agree' is a verb, not an adjective. We don't use 'am'."
  },
  {
    mistake: "The people is...",
    correction: "The people are...",
    explanation: "'People' is plural."
  },
  {
    mistake: "I look forward to see you.",
    correction: "I look forward to seeing you.",
    explanation: "After 'look forward to', we use the -ing form."
  },
  {
    mistake: "I have been here since 2 years.",
    correction: "I have been here for 2 years.",
    explanation: "Use 'for' with a duration (2 years). Use 'since' with a starting point (2020)."
  },
  {
    mistake: "She is married with...",
    correction: "She is married to...",
    explanation: "We say 'married to', not 'married with'."
  }
];
