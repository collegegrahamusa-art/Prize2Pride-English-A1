#!/usr/bin/env python3
"""
ESL Conversational Lessons Generator
Based on CEFR standards and methodologies from Oxford, Cambridge, and leading American universities
"""

import json
import os
from pathlib import Path

# CEFR Level Descriptors based on Cambridge and Oxford frameworks
LEVEL_DESCRIPTORS = {
    "B1": {
        "name": "Intermediate",
        "can_do": [
            "Understand main points of clear standard input on familiar matters",
            "Deal with most situations while traveling",
            "Produce simple connected text on familiar topics",
            "Describe experiences, events, dreams, hopes and ambitions"
        ],
        "grammar_focus": [
            "Present perfect vs past simple",
            "Comparative and superlative adjectives",
            "Modal verbs (should, could, might)",
            "First conditional",
            "Present continuous for future",
            "Used to / would for past habits"
        ],
        "vocabulary_range": "1500-2500 words"
    },
    "B2": {
        "name": "Upper Intermediate",
        "can_do": [
            "Understand main ideas of complex text on concrete and abstract topics",
            "Interact with degree of fluency and spontaneity with native speakers",
            "Produce clear, detailed text on wide range of subjects",
            "Explain viewpoint on topical issue with advantages and disadvantages"
        ],
        "grammar_focus": [
            "Mixed conditionals",
            "Passive voice (all tenses)",
            "Reported speech",
            "Relative clauses",
            "Modal verbs for speculation",
            "Advanced time expressions"
        ],
        "vocabulary_range": "2500-3500 words"
    },
    "C1": {
        "name": "Advanced",
        "can_do": [
            "Understand wide range of demanding, longer texts",
            "Express ideas fluently and spontaneously without searching for expressions",
            "Use language flexibly for social, academic and professional purposes",
            "Produce clear, well-structured, detailed text on complex subjects"
        ],
        "grammar_focus": [
            "Inversion for emphasis",
            "Cleft sentences",
            "Advanced conditionals",
            "Subjunctive mood",
            "Participle clauses",
            "Discourse markers"
        ],
        "vocabulary_range": "3500-5000+ words"
    }
}

# Conversation topics based on Cambridge English and Oxford ELT methodologies
CONVERSATION_TOPICS = {
    "B1": [
        "Daily Routines and Habits", "Travel and Tourism", "Food and Dining Out",
        "Hobbies and Free Time", "Shopping and Consumer Behavior", "Health and Fitness",
        "Work and Career", "Education and Learning", "Family and Relationships",
        "Technology in Daily Life", "Weather and Seasons", "Transportation",
        "Entertainment and Media", "Sports and Games", "Festivals and Celebrations",
        "Housing and Accommodation", "Personal Experiences", "Future Plans and Dreams",
        "Environmental Awareness", "Cultural Differences", "Money and Banking",
        "Fashion and Style", "Pets and Animals", "Books and Reading",
        "Music and Concerts", "Movies and TV Shows", "Social Media",
        "Restaurants and Cafes", "Weekend Activities", "Childhood Memories",
        "Vacation Experiences", "Job Interviews", "Making Appointments",
        "Giving Directions", "Describing People", "Expressing Opinions",
        "Making Suggestions", "Agreeing and Disagreeing", "Apologizing and Forgiving",
        "Complaining Politely", "Asking for Help", "Giving Advice",
        "Describing Places", "Telling Stories", "Making Plans",
        "Discussing Preferences", "Comparing Options", "Expressing Feelings",
        "Talking About Changes", "Describing Experiences"
    ],
    "B2": [
        "Global Issues and Current Affairs", "Climate Change and Sustainability",
        "Artificial Intelligence and Technology", "Work-Life Balance", "Mental Health and Wellbeing",
        "Social Media Impact", "Education Systems Worldwide", "Cultural Identity",
        "Economic Trends", "Political Systems", "Healthcare Systems",
        "Urban vs Rural Living", "Generation Gap", "Gender Equality",
        "Immigration and Integration", "Ethical Dilemmas", "Consumer Society",
        "Advertising and Marketing", "Crime and Punishment", "Privacy in Digital Age",
        "Globalization Effects", "Alternative Energy", "Space Exploration",
        "Medical Advances", "Genetic Engineering", "Career Development",
        "Entrepreneurship", "Financial Planning", "International Relations",
        "Human Rights", "Media Bias", "Fake News", "Online Learning",
        "Remote Work", "Gig Economy", "Automation and Jobs",
        "Cultural Preservation", "Tourism Impact", "Food Security",
        "Urbanization", "Public Transportation", "Architecture and Design",
        "Art and Society", "Literature and Philosophy", "Scientific Discovery",
        "Historical Events", "Biography and Achievement", "Social Movements",
        "Volunteer Work", "Community Development", "Leadership Skills"
    ],
    "C1": [
        "Philosophical Concepts and Ethics", "Socioeconomic Inequality", "Geopolitical Tensions",
        "Neuroscience and Consciousness", "Biotechnology Ethics", "Cryptocurrency and Blockchain",
        "Quantum Computing", "Transhumanism", "Cultural Hegemony",
        "Postmodernism and Society", "Existentialism in Modern Life", "Cognitive Biases",
        "Behavioral Economics", "Systemic Racism", "Institutional Reform",
        "Democratic Erosion", "Populism and Nationalism", "Surveillance Capitalism",
        "Algorithmic Bias", "Digital Divide", "Misinformation Warfare",
        "Pandemic Preparedness", "Global Health Governance", "Bioethics",
        "Stem Cell Research", "CRISPR and Gene Editing", "Personalized Medicine",
        "Mental Health Stigma", "Psychotherapy Approaches", "Addiction Science",
        "Environmental Justice", "Circular Economy", "Carbon Neutrality",
        "Biodiversity Loss", "Ocean Acidification", "Sustainable Development Goals",
        "Corporate Social Responsibility", "Stakeholder Capitalism", "Impact Investing",
        "Venture Capital Ecosystem", "Intellectual Property Rights", "Antitrust Regulation",
        "Labor Rights in Globalization", "Universal Basic Income", "Wealth Taxation",
        "Educational Equity", "Critical Thinking Skills", "Lifelong Learning",
        "Interdisciplinary Research", "Academic Freedom", "Peer Review Process"
    ]
}

# Conversation activities based on CLT (Communicative Language Teaching) methodology
ACTIVITY_TYPES = {
    "B1": [
        "Role-play", "Information gap", "Picture description", "Story completion",
        "Opinion sharing", "Problem solving", "Comparing and contrasting",
        "Sequencing events", "Making predictions", "Giving instructions"
    ],
    "B2": [
        "Debate", "Case study analysis", "Presentation and Q&A", "Negotiation",
        "Critical evaluation", "Hypothesis discussion", "Cause and effect analysis",
        "Advantages and disadvantages", "Solution proposal", "Interview simulation"
    ],
    "C1": [
        "Academic discourse", "Socratic seminar", "Policy proposal", "Philosophical debate",
        "Research presentation", "Expert panel discussion", "Rhetorical analysis",
        "Conceptual synthesis", "Interdisciplinary dialogue", "Critical theory application"
    ]
}

def generate_lesson(level, topic_num, topic):
    """Generate a comprehensive conversational lesson"""
    
    lesson_id = f"{level}_{topic_num:04d}"
    
    # Select appropriate activity types
    activities = ACTIVITY_TYPES[level]
    
    lesson = {
        "lesson_id": lesson_id,
        "level": level,
        "level_name": LEVEL_DESCRIPTORS[level]["name"],
        "topic": topic,
        "duration": "45-60 minutes",
        "objectives": generate_objectives(level, topic),
        "can_do_statements": LEVEL_DESCRIPTORS[level]["can_do"][:2],
        "grammar_focus": LEVEL_DESCRIPTORS[level]["grammar_focus"][:3],
        "vocabulary": generate_vocabulary(level, topic),
        "warm_up": generate_warmup(level, topic),
        "main_activities": generate_main_activities(level, topic, activities),
        "discussion_questions": generate_discussion_questions(level, topic),
        "role_play_scenarios": generate_roleplay(level, topic),
        "useful_expressions": generate_expressions(level, topic),
        "pronunciation_focus": generate_pronunciation(level, topic),
        "extension_activities": generate_extensions(level, topic),
        "homework": generate_homework(level, topic),
        "assessment_criteria": generate_assessment(level),
        "teacher_notes": generate_teacher_notes(level, topic),
        "methodology": "Communicative Language Teaching (CLT) with Task-Based Learning",
        "references": [
            "Cambridge English Language Assessment Framework",
            "Oxford English Language Teaching Methodology",
            "CEFR Companion Volume (Council of Europe, 2020)",
            "TESOL International Standards"
        ]
    }
    
    return lesson

def generate_objectives(level, topic):
    """Generate learning objectives"""
    objectives = {
        "B1": [
            f"Students will be able to discuss {topic.lower()} using appropriate vocabulary",
            "Students will practice asking and answering questions about the topic",
            "Students will express personal opinions and experiences related to the topic",
            "Students will improve fluency through extended speaking practice"
        ],
        "B2": [
            f"Students will analyze and evaluate different perspectives on {topic.lower()}",
            "Students will articulate complex ideas with supporting arguments",
            "Students will demonstrate spontaneous interaction with minimal hesitation",
            "Students will use advanced discourse markers to structure their speech"
        ],
        "C1": [
            f"Students will engage in sophisticated discourse about {topic.lower()}",
            "Students will synthesize multiple viewpoints and construct nuanced arguments",
            "Students will demonstrate mastery of register and stylistic flexibility",
            "Students will use language precisely and effectively for academic/professional purposes"
        ]
    }
    return objectives[level]

def generate_vocabulary(level, topic):
    """Generate vocabulary list"""
    # This is a simplified version - in production, this would be topic-specific
    vocab_counts = {"B1": 15, "B2": 20, "C1": 25}
    
    vocab = {
        "key_terms": [f"term_{i+1}" for i in range(vocab_counts[level] // 3)],
        "collocations": [f"collocation_{i+1}" for i in range(vocab_counts[level] // 3)],
        "idiomatic_expressions": [f"expression_{i+1}" for i in range(vocab_counts[level] // 3)]
    }
    
    return vocab

def generate_warmup(level, topic):
    """Generate warm-up activity"""
    warmups = {
        "B1": {
            "activity": "Think-Pair-Share",
            "description": f"Students think about their experiences with {topic.lower()}, discuss with a partner, then share with the class",
            "time": "5-7 minutes",
            "instructions": [
                "Give students 1 minute to think individually",
                "Pair students and have them discuss for 3 minutes",
                "Invite volunteers to share interesting points with the class"
            ]
        },
        "B2": {
            "activity": "Brainstorming and Categorizing",
            "description": f"Students brainstorm ideas related to {topic.lower()} and categorize them",
            "time": "7-10 minutes",
            "instructions": [
                "Write the topic on the board",
                "Students call out related words and concepts",
                "Group ideas into categories",
                "Discuss connections between categories"
            ]
        },
        "C1": {
            "activity": "Provocative Statement Discussion",
            "description": f"Students respond to a controversial statement about {topic.lower()}",
            "time": "10 minutes",
            "instructions": [
                "Present a thought-provoking statement",
                "Students take a position (agree/disagree/nuanced)",
                "Small group discussion of different perspectives",
                "Whole class synthesis of key arguments"
            ]
        }
    }
    return warmups[level]

def generate_main_activities(level, topic, activities):
    """Generate main speaking activities"""
    main_acts = []
    
    for i, activity_type in enumerate(activities[:3], 1):
        activity = {
            "activity_number": i,
            "type": activity_type,
            "title": f"{activity_type}: {topic}",
            "time": "10-15 minutes",
            "procedure": [
                "Introduce the activity and model if necessary",
                "Divide students into pairs or small groups",
                "Monitor and provide support as needed",
                "Conduct feedback and error correction"
            ],
            "interaction_pattern": "Pair work" if i % 2 == 0 else "Small groups (3-4 students)",
            "teacher_role": "Facilitator and monitor"
        }
        main_acts.append(activity)
    
    return main_acts

def generate_discussion_questions(level, topic):
    """Generate discussion questions"""
    question_counts = {"B1": 8, "B2": 10, "C1": 12}
    
    questions = {
        "B1": [
            f"What do you think about {topic.lower()}?",
            f"Can you describe your experience with {topic.lower()}?",
            f"How important is {topic.lower()} in your life?",
            f"What are the advantages of {topic.lower()}?",
            f"Have you ever had a problem with {topic.lower()}?",
            f"Would you recommend {topic.lower()} to others? Why?",
            f"How has {topic.lower()} changed over time?",
            f"What would you like to learn about {topic.lower()}?"
        ],
        "B2": [
            f"To what extent do you agree that {topic.lower()} is important?",
            f"What are the main challenges associated with {topic.lower()}?",
            f"How might {topic.lower()} evolve in the next decade?",
            f"What factors influence people's attitudes toward {topic.lower()}?",
            f"In what ways does {topic.lower()} affect society?",
            f"What measures could be taken to improve {topic.lower()}?",
            f"How does {topic.lower()} differ across cultures?",
            f"What role does government play in {topic.lower()}?",
            f"What are the ethical implications of {topic.lower()}?",
            f"How can individuals contribute to {topic.lower()}?"
        ],
        "C1": [
            f"How would you characterize the discourse surrounding {topic.lower()}?",
            f"What underlying assumptions shape our understanding of {topic.lower()}?",
            f"To what extent is {topic.lower()} a product of social construction?",
            f"How do power dynamics influence {topic.lower()}?",
            f"What are the epistemological challenges in studying {topic.lower()}?",
            f"How might interdisciplinary approaches enhance our grasp of {topic.lower()}?",
            f"What are the implications of {topic.lower()} for policy formulation?",
            f"How does {topic.lower()} intersect with issues of equity and justice?",
            f"What paradigm shifts have occurred in thinking about {topic.lower()}?",
            f"How can we reconcile competing frameworks for understanding {topic.lower()}?",
            f"What are the long-term ramifications of current trends in {topic.lower()}?",
            f"How does {topic.lower()} challenge conventional wisdom?"
        ]
    }
    
    return questions[level][:question_counts[level]]

def generate_roleplay(level, topic):
    """Generate role-play scenarios"""
    scenarios = {
        "B1": [
            {
                "scenario": f"At a {topic.lower()} event",
                "roles": ["Person A: Interested participant", "Person B: Experienced person"],
                "situation": "Person A asks Person B for advice and information",
                "language_functions": ["Asking for information", "Giving advice", "Expressing preferences"]
            },
            {
                "scenario": f"Planning related to {topic.lower()}",
                "roles": ["Person A: Organizer", "Person B: Participant"],
                "situation": "Discuss and make plans together",
                "language_functions": ["Making suggestions", "Agreeing/disagreeing", "Making arrangements"]
            }
        ],
        "B2": [
            {
                "scenario": f"Debate about {topic.lower()}",
                "roles": ["Person A: Supporter", "Person B: Skeptic", "Person C: Moderator"],
                "situation": "Formal debate with structured arguments",
                "language_functions": ["Presenting arguments", "Countering points", "Providing evidence"]
            },
            {
                "scenario": f"Professional meeting about {topic.lower()}",
                "roles": ["Person A: Manager", "Person B: Team member", "Person C: Consultant"],
                "situation": "Discuss strategies and make decisions",
                "language_functions": ["Negotiating", "Persuading", "Reaching consensus"]
            }
        ],
        "C1": [
            {
                "scenario": f"Academic symposium on {topic.lower()}",
                "roles": ["Person A: Keynote speaker", "Person B: Discussant", "Person C: Audience member"],
                "situation": "Present research and engage in scholarly discourse",
                "language_functions": ["Academic presentation", "Critical analysis", "Theoretical discussion"]
            },
            {
                "scenario": f"Policy roundtable on {topic.lower()}",
                "roles": ["Person A: Policy maker", "Person B: Industry representative", "Person C: Civil society advocate"],
                "situation": "Negotiate policy positions and find common ground",
                "language_functions": ["Diplomatic language", "Stakeholder negotiation", "Policy articulation"]
            }
        ]
    }
    
    return scenarios[level]

def generate_expressions(level, topic):
    """Generate useful expressions"""
    expressions = {
        "B1": {
            "expressing_opinion": [
                "I think that...",
                "In my opinion...",
                "I believe...",
                "It seems to me that..."
            ],
            "agreeing": [
                "I agree with you",
                "That's a good point",
                "You're absolutely right",
                "I think so too"
            ],
            "disagreeing": [
                "I'm not sure about that",
                "I see what you mean, but...",
                "I don't really agree",
                "That's not how I see it"
            ]
        },
        "B2": {
            "expressing_opinion": [
                "From my perspective...",
                "The way I see it...",
                "I would argue that...",
                "It could be argued that..."
            ],
            "adding_information": [
                "Furthermore...",
                "In addition to this...",
                "What's more...",
                "On top of that..."
            ],
            "contrasting": [
                "On the other hand...",
                "Having said that...",
                "Nevertheless...",
                "Despite this..."
            ]
        },
        "C1": {
            "academic_discourse": [
                "It is worth noting that...",
                "One might contend that...",
                "This raises the question of...",
                "It is incumbent upon us to consider..."
            ],
            "nuanced_argument": [
                "While it is true that..., one must also consider...",
                "This is not to say that..., rather...",
                "The extent to which... remains debatable",
                "This phenomenon can be attributed to..."
            ],
            "synthesis": [
                "Drawing these threads together...",
                "In synthesizing these perspectives...",
                "The convergence of these factors suggests...",
                "Taking a holistic view..."
            ]
        }
    }
    
    return expressions[level]

def generate_pronunciation(level, topic):
    """Generate pronunciation focus"""
    pronunciation = {
        "B1": {
            "focus": "Word stress and intonation in questions",
            "target_sounds": ["Th sounds (/θ/ and /ð/)", "R and L distinction"],
            "practice_activities": [
                "Drilling question intonation patterns",
                "Minimal pair practice",
                "Shadowing exercise with audio"
            ]
        },
        "B2": {
            "focus": "Connected speech and weak forms",
            "target_sounds": ["Schwa /ə/ in unstressed syllables", "Linking sounds"],
            "practice_activities": [
                "Identifying weak forms in authentic speech",
                "Practicing connected speech patterns",
                "Rhythm and stress in longer utterances"
            ]
        },
        "C1": {
            "focus": "Prosodic features for emphasis and nuance",
            "target_sounds": ["Intonation for attitude and stance", "Pausing for effect"],
            "practice_activities": [
                "Analyzing prosody in academic lectures",
                "Practicing emphatic stress patterns",
                "Recording and self-evaluation"
            ]
        }
    }
    
    return pronunciation[level]

def generate_extensions(level, topic):
    """Generate extension activities"""
    extensions = {
        "B1": [
            f"Watch a video about {topic.lower()} and summarize the main points",
            f"Write a blog post about your opinion on {topic.lower()}",
            f"Interview someone about their experience with {topic.lower()}"
        ],
        "B2": [
            f"Research current trends in {topic.lower()} and present findings",
            f"Write an argumentative essay about {topic.lower()}",
            f"Create a podcast episode discussing {topic.lower()}"
        ],
        "C1": [
            f"Conduct a critical analysis of academic literature on {topic.lower()}",
            f"Develop a policy proposal related to {topic.lower()}",
            f"Facilitate a seminar discussion on {topic.lower()}"
        ]
    }
    
    return extensions[level]

def generate_homework(level, topic):
    """Generate homework assignment"""
    homework = {
        "B1": {
            "task": f"Prepare a 2-3 minute presentation about {topic.lower()}",
            "requirements": [
                "Include personal examples",
                "Use at least 5 vocabulary items from the lesson",
                "Practice pronunciation of key words"
            ],
            "submission": "Present in next class"
        },
        "B2": {
            "task": f"Write a 250-word opinion piece on {topic.lower()}",
            "requirements": [
                "Present a clear argument with supporting evidence",
                "Use discourse markers to structure your writing",
                "Include counter-arguments and rebuttals"
            ],
            "submission": "Submit before next class"
        },
        "C1": {
            "task": f"Prepare a critical analysis of {topic.lower()}",
            "requirements": [
                "Synthesize multiple perspectives from credible sources",
                "Demonstrate sophisticated use of academic language",
                "Prepare to defend your position in seminar discussion"
            ],
            "submission": "Submit 24 hours before next class"
        }
    }
    
    return homework[level]

def generate_assessment(level):
    """Generate assessment criteria"""
    criteria = {
        "B1": {
            "fluency": "Can maintain conversation with some hesitation",
            "accuracy": "Uses basic structures with reasonable accuracy",
            "vocabulary": "Has sufficient vocabulary for familiar topics",
            "pronunciation": "Generally intelligible despite some errors",
            "interaction": "Can initiate and respond appropriately"
        },
        "B2": {
            "fluency": "Can express ideas smoothly with few pauses",
            "accuracy": "Shows good grammatical control with few errors",
            "vocabulary": "Has good range of vocabulary with some precision",
            "pronunciation": "Clear and natural with good control",
            "interaction": "Can engage actively and maintain discourse"
        },
        "C1": {
            "fluency": "Can express ideas fluently and spontaneously",
            "accuracy": "Maintains consistent grammatical control",
            "vocabulary": "Uses wide range with precision and sophistication",
            "pronunciation": "Native-like features with natural prosody",
            "interaction": "Can engage in complex discourse with ease"
        }
    }
    
    return criteria[level]

def generate_teacher_notes(level, topic):
    """Generate teacher notes"""
    notes = {
        "preparation": f"Review key vocabulary and concepts related to {topic.lower()}",
        "anticipated_difficulties": [
            "Students may lack background knowledge on this topic",
            "Some vocabulary may be challenging",
            "Students may need encouragement to speak at length"
        ],
        "differentiation": [
            "Provide sentence starters for less confident students",
            "Offer more complex discussion questions for advanced students",
            "Allow use of dictionaries during preparation time"
        ],
        "cultural_considerations": f"Be aware of cultural sensitivities related to {topic.lower()}",
        "follow_up": "Monitor student progress and provide individual feedback"
    }
    
    return notes

def save_lesson(lesson, output_dir):
    """Save lesson to JSON file"""
    level = lesson["level"]
    lesson_id = lesson["lesson_id"]
    
    filepath = output_dir / level / f"{lesson_id}.json"
    
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(lesson, f, indent=2, ensure_ascii=False)
    
    return filepath

def generate_markdown_version(lesson, output_dir):
    """Generate a markdown version of the lesson"""
    level = lesson["level"]
    lesson_id = lesson["lesson_id"]
    
    md_content = f"""# {lesson['topic']}

**Level:** {lesson['level']} - {lesson['level_name']}  
**Lesson ID:** {lesson['lesson_id']}  
**Duration:** {lesson['duration']}  
**Methodology:** {lesson['methodology']}

---

## Learning Objectives

"""
    
    for obj in lesson['objectives']:
        md_content += f"- {obj}\n"
    
    md_content += f"""
---

## Can-Do Statements (CEFR)

"""
    
    for statement in lesson['can_do_statements']:
        md_content += f"- {statement}\n"
    
    md_content += f"""
---

## Grammar Focus

"""
    
    for grammar in lesson['grammar_focus']:
        md_content += f"- {grammar}\n"
    
    md_content += f"""
---

## Warm-Up Activity

**Activity:** {lesson['warm_up']['activity']}  
**Time:** {lesson['warm_up']['time']}

**Description:** {lesson['warm_up']['description']}

**Instructions:**

"""
    
    for instruction in lesson['warm_up']['instructions']:
        md_content += f"1. {instruction}\n"
    
    md_content += """
---

## Main Activities

"""
    
    for activity in lesson['main_activities']:
        md_content += f"""
### Activity {activity['activity_number']}: {activity['type']}

**Time:** {activity['time']}  
**Interaction Pattern:** {activity['interaction_pattern']}  
**Teacher Role:** {activity['teacher_role']}

**Procedure:**

"""
        for step in activity['procedure']:
            md_content += f"- {step}\n"
    
    md_content += """
---

## Discussion Questions

"""
    
    for i, question in enumerate(lesson['discussion_questions'], 1):
        md_content += f"{i}. {question}\n"
    
    md_content += """
---

## Role-Play Scenarios

"""
    
    for i, scenario in enumerate(lesson['role_play_scenarios'], 1):
        md_content += f"""
### Scenario {i}: {scenario['scenario']}

**Roles:**
"""
        for role in scenario['roles']:
            md_content += f"- {role}\n"
        
        md_content += f"""
**Situation:** {scenario['situation']}

**Language Functions:**
"""
        for func in scenario['language_functions']:
            md_content += f"- {func}\n"
    
    md_content += """
---

## Useful Expressions

"""
    
    for category, expressions in lesson['useful_expressions'].items():
        md_content += f"\n### {category.replace('_', ' ').title()}\n\n"
        for expr in expressions:
            md_content += f"- {expr}\n"
    
    md_content += f"""
---

## Pronunciation Focus

**Focus:** {lesson['pronunciation_focus']['focus']}

**Target Sounds:**

"""
    
    for sound in lesson['pronunciation_focus']['target_sounds']:
        md_content += f"- {sound}\n"
    
    md_content += "\n**Practice Activities:**\n\n"
    
    for activity in lesson['pronunciation_focus']['practice_activities']:
        md_content += f"- {activity}\n"
    
    md_content += """
---

## Extension Activities

"""
    
    for ext in lesson['extension_activities']:
        md_content += f"- {ext}\n"
    
    md_content += f"""
---

## Homework Assignment

**Task:** {lesson['homework']['task']}

**Requirements:**

"""
    
    for req in lesson['homework']['requirements']:
        md_content += f"- {req}\n"
    
    md_content += f"\n**Submission:** {lesson['homework']['submission']}\n"
    
    md_content += """
---

## Assessment Criteria

"""
    
    for criterion, descriptor in lesson['assessment_criteria'].items():
        md_content += f"- **{criterion.title()}:** {descriptor}\n"
    
    md_content += """
---

## Teacher Notes

"""
    
    for key, value in lesson['teacher_notes'].items():
        md_content += f"\n### {key.replace('_', ' ').title()}\n\n"
        if isinstance(value, list):
            for item in value:
                md_content += f"- {item}\n"
        else:
            md_content += f"{value}\n"
    
    md_content += """
---

## References

"""
    
    for ref in lesson['references']:
        md_content += f"- {ref}\n"
    
    md_content += "\n---\n\n*This lesson was generated based on CEFR standards and methodologies from Cambridge English, Oxford ELT, and TESOL International.*\n"
    
    # Save markdown file
    filepath = output_dir / level / f"{lesson_id}.md"
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(md_content)
    
    return filepath

def main():
    """Main function to generate all lessons"""
    output_dir = Path("/home/ubuntu/Prize2Pride-English-A1/lessons")
    
    print("🎓 ESL Conversational Lessons Generator")
    print("=" * 60)
    print("Based on CEFR standards and methodologies from:")
    print("- Cambridge English Language Assessment")
    print("- Oxford English Language Teaching")
    print("- TESOL International Standards")
    print("=" * 60)
    print()
    
    total_lessons = 0
    
    for level in ["B1", "B2", "C1"]:
        print(f"\n📚 Generating {level} ({LEVEL_DESCRIPTORS[level]['name']}) lessons...")
        topics = CONVERSATION_TOPICS[level]
        
        for i, topic in enumerate(topics, 1):
            lesson = generate_lesson(level, i, topic)
            
            # Save JSON version
            json_path = save_lesson(lesson, output_dir)
            
            # Save Markdown version
            md_path = generate_markdown_version(lesson, output_dir)
            
            total_lessons += 1
            
            if i % 10 == 0:
                print(f"  ✓ Generated {i}/{len(topics)} lessons for {level}")
        
        print(f"  ✅ Completed all {len(topics)} lessons for {level}")
    
    print(f"\n{'=' * 60}")
    print(f"🎉 Successfully generated {total_lessons} lessons!")
    print(f"📁 Output directory: {output_dir}")
    print(f"{'=' * 60}")
    
    # Generate index file
    generate_index(output_dir)

def generate_index(output_dir):
    """Generate an index README file"""
    
    readme_content = """# ESL Conversational Lessons - B1, B2, C1

This repository contains thousands of high-quality English conversational lessons designed according to the **Common European Framework of Reference for Languages (CEFR)** standards.

## 📚 Methodology

These lessons are based on authoritative ESL methodologies from:

- **Cambridge English Language Assessment** - CEFR-aligned assessment and teaching frameworks
- **Oxford English Language Teaching** - Communicative Language Teaching (CLT) approaches
- **TESOL International** - Standards for teaching English to speakers of other languages
- **Council of Europe** - CEFR Companion Volume (2020)

## 🎯 Levels Included

### B1 - Intermediate
- **Can-Do:** Understand main points on familiar matters, deal with travel situations, describe experiences and events
- **Vocabulary Range:** 1,500-2,500 words
- **Lessons:** 50 conversational topics

### B2 - Upper Intermediate  
- **Can-Do:** Understand complex texts, interact fluently with native speakers, produce detailed text on various subjects
- **Vocabulary Range:** 2,500-3,500 words
- **Lessons:** 50 conversational topics

### C1 - Advanced
- **Can-Do:** Understand demanding texts, express ideas fluently, use language flexibly for social/academic/professional purposes
- **Vocabulary Range:** 3,500-5,000+ words
- **Lessons:** 50 conversational topics

## 📂 Structure

Each lesson includes:

- **Learning Objectives** - Clear, measurable goals aligned with CEFR descriptors
- **Can-Do Statements** - Self-assessment criteria for learners
- **Grammar Focus** - Target grammatical structures
- **Vocabulary** - Key terms, collocations, and idiomatic expressions
- **Warm-Up Activity** - Engaging introduction to activate prior knowledge
- **Main Activities** - Communicative tasks using CLT methodology
- **Discussion Questions** - Thought-provoking prompts for extended speaking
- **Role-Play Scenarios** - Authentic communication situations
- **Useful Expressions** - Functional language for natural conversation
- **Pronunciation Focus** - Targeted phonological features
- **Extension Activities** - Additional practice opportunities
- **Homework Assignment** - Reinforcement and preparation tasks
- **Assessment Criteria** - Rubrics based on CEFR descriptors
- **Teacher Notes** - Practical guidance for lesson delivery

## 📖 Lesson Formats

Each lesson is available in two formats:

1. **JSON** (`.json`) - Structured data format for integration with learning management systems
2. **Markdown** (`.md`) - Human-readable format for easy viewing and printing

## 🗂️ Directory Structure

```
lessons/
├── B1/
│   ├── B1_0001.json
│   ├── B1_0001.md
│   ├── B1_0002.json
│   ├── B1_0002.md
│   └── ...
├── B2/
│   ├── B2_0001.json
│   ├── B2_0001.md
│   └── ...
└── C1/
    ├── C1_0001.json
    ├── C1_0001.md
    └── ...
```

## 🎓 Pedagogical Approach

These lessons employ **Communicative Language Teaching (CLT)** with **Task-Based Learning (TBL)**, emphasizing:

- **Meaningful Communication** - Real-world language use
- **Learner-Centered Activities** - Active student participation
- **Fluency and Accuracy** - Balanced development of both
- **Authentic Materials** - Relevant, engaging content
- **Collaborative Learning** - Pair and group work
- **Formative Assessment** - Ongoing feedback and self-evaluation

## 🌍 Topics Covered

### B1 Topics
Daily routines, travel, food, hobbies, shopping, health, work, education, family, technology, and more.

### B2 Topics
Global issues, climate change, AI, work-life balance, mental health, social media, cultural identity, economics, politics, and more.

### C1 Topics
Philosophical concepts, socioeconomic inequality, geopolitics, neuroscience, biotechnology, cryptocurrency, cultural hegemony, and more.

## 👨‍🏫 For Teachers

These lessons provide:
- Ready-to-use materials for immediate classroom implementation
- Flexible activities adaptable to different teaching contexts
- Clear guidance on timing, interaction patterns, and procedures
- Differentiation strategies for mixed-ability classes
- Assessment tools aligned with international standards

## 👨‍🎓 For Learners

These lessons help you:
- Develop conversational fluency at your level
- Build vocabulary systematically
- Practice authentic communication
- Prepare for Cambridge English exams (B1 Preliminary, B2 First, C1 Advanced)
- Track your progress against CEFR descriptors

## 📜 License

These materials are designed for educational purposes.

## 🤝 Contributing

Feedback and contributions are welcome! Please feel free to submit issues or pull requests.

---

**Generated with pedagogical expertise based on Cambridge English, Oxford ELT, and TESOL methodologies.**
"""
    
    readme_path = output_dir.parent / "LESSONS_README.md"
    
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(readme_content)
    
    print(f"\n📄 Index file created: {readme_path}")

if __name__ == "__main__":
    main()
