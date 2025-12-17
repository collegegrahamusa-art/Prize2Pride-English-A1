#!/usr/bin/env python3
"""
Advanced Differentiated ESL Conversational Lessons Generator
1000+ Mega-Prompts with Learning Style Adaptations
Based on CEFR, Multiple Intelligences, and Universal Design for Learning (UDL)
"""

import json
import os
from pathlib import Path
from itertools import product

# Learning Styles based on VARK model and Multiple Intelligences
LEARNING_STYLES = {
    "visual": {
        "name": "Visual Learners",
        "description": "Learn best through seeing and visualizing",
        "strategies": [
            "Use of diagrams, charts, and mind maps",
            "Color-coding and highlighting",
            "Visual organizers and infographics",
            "Video demonstrations",
            "Written instructions with images"
        ]
    },
    "auditory": {
        "name": "Auditory Learners",
        "description": "Learn best through listening and speaking",
        "strategies": [
            "Listening activities and podcasts",
            "Group discussions and debates",
            "Oral presentations",
            "Audio recordings and repetition",
            "Verbal instructions and explanations"
        ]
    },
    "kinesthetic": {
        "name": "Kinesthetic Learners",
        "description": "Learn best through movement and hands-on activities",
        "strategies": [
            "Role-plays and simulations",
            "Physical games and activities",
            "Real-world tasks and projects",
            "Movement-based learning",
            "Hands-on experiments"
        ]
    },
    "reading_writing": {
        "name": "Reading/Writing Learners",
        "description": "Learn best through text-based input and output",
        "strategies": [
            "Reading comprehension activities",
            "Writing assignments and journals",
            "Note-taking and summarizing",
            "Text analysis and annotation",
            "Written reflections"
        ]
    }
}

# Cognitive Levels based on Bloom's Taxonomy
COGNITIVE_LEVELS = {
    "basic": {
        "name": "Basic/Foundational",
        "bloom_levels": ["Remember", "Understand"],
        "activities": [
            "Recall vocabulary and phrases",
            "Identify and recognize patterns",
            "Explain concepts in simple terms",
            "Summarize main ideas",
            "Match and categorize"
        ]
    },
    "intermediate": {
        "name": "Intermediate/Application",
        "bloom_levels": ["Apply", "Analyze"],
        "activities": [
            "Apply language in new contexts",
            "Compare and contrast ideas",
            "Analyze arguments and perspectives",
            "Solve communication problems",
            "Organize and structure discourse"
        ]
    },
    "advanced": {
        "name": "Advanced/Creative",
        "bloom_levels": ["Evaluate", "Create"],
        "activities": [
            "Evaluate arguments critically",
            "Create original content",
            "Synthesize multiple perspectives",
            "Design solutions to complex problems",
            "Critique and justify positions"
        ]
    }
}

# Multiple Intelligences (Gardner)
MULTIPLE_INTELLIGENCES = {
    "linguistic": "Word-smart: Reading, writing, storytelling",
    "logical_mathematical": "Number-smart: Logic, patterns, problem-solving",
    "spatial": "Picture-smart: Visualization, spatial reasoning",
    "bodily_kinesthetic": "Body-smart: Movement, hands-on activities",
    "musical": "Music-smart: Rhythm, melody, sound patterns",
    "interpersonal": "People-smart: Social interaction, collaboration",
    "intrapersonal": "Self-smart: Self-reflection, independent work",
    "naturalistic": "Nature-smart: Categorizing, environmental awareness"
}

# Expanded Topics (1000+ combinations)
TOPIC_CATEGORIES = {
    "B1": {
        "daily_life": [
            "Morning Routines", "Evening Activities", "Weekend Plans", "Household Chores",
            "Shopping for Groceries", "Cooking at Home", "Eating Out", "Personal Hygiene",
            "Getting Dressed", "Commuting to Work", "Running Errands", "Paying Bills"
        ],
        "social": [
            "Making Friends", "Keeping in Touch", "Social Gatherings", "Celebrating Birthdays",
            "Wedding Customs", "Family Reunions", "Neighborhood Events", "Community Activities",
            "Volunteering", "Helping Others", "Making Small Talk", "Introducing People"
        ],
        "work": [
            "Job Interviews", "First Day at Work", "Office Etiquette", "Team Meetings",
            "Email Communication", "Phone Calls at Work", "Customer Service", "Time Management",
            "Work-Life Balance", "Career Goals", "Professional Development", "Workplace Problems"
        ],
        "leisure": [
            "Hobbies and Interests", "Sports Activities", "Watching Movies", "Reading Books",
            "Listening to Music", "Playing Video Games", "Outdoor Activities", "Indoor Entertainment",
            "Arts and Crafts", "Collecting Things", "Gardening", "Photography"
        ],
        "travel": [
            "Planning a Trip", "Booking Accommodation", "At the Airport", "On the Plane",
            "Checking into a Hotel", "Asking for Directions", "Using Public Transport", "Renting a Car",
            "Visiting Tourist Attractions", "Trying Local Food", "Shopping for Souvenirs", "Travel Problems"
        ],
        "health": [
            "Visiting the Doctor", "At the Pharmacy", "Healthy Eating", "Exercise Routines",
            "Sleep Habits", "Stress Management", "Common Illnesses", "Injuries and Accidents",
            "Mental Wellbeing", "Preventive Care", "Health Insurance", "Emergency Situations"
        ],
        "education": [
            "School Subjects", "Study Habits", "Exam Preparation", "Homework Help",
            "Learning Languages", "Online Courses", "Library Resources", "Group Projects",
            "Teacher-Student Communication", "Parent-Teacher Meetings", "School Events", "Graduation"
        ],
        "technology": [
            "Using Smartphones", "Social Media Apps", "Online Shopping", "Email Basics",
            "Video Calls", "Taking Photos", "Listening to Podcasts", "Streaming Services",
            "Computer Problems", "Internet Safety", "Digital Privacy", "Tech Support"
        ]
    },
    "B2": {
        "society": [
            "Social Inequality", "Education Reform", "Healthcare Access", "Housing Crisis",
            "Urban Development", "Rural Decline", "Generation Gap", "Youth Culture",
            "Aging Population", "Immigration Policies", "Cultural Integration", "Social Mobility"
        ],
        "environment": [
            "Climate Change Effects", "Renewable Energy", "Plastic Pollution", "Deforestation",
            "Water Scarcity", "Air Quality", "Biodiversity Loss", "Sustainable Agriculture",
            "Carbon Footprint", "Green Technology", "Environmental Activism", "Conservation Efforts"
        ],
        "economy": [
            "Global Trade", "Economic Inequality", "Unemployment Issues", "Gig Economy",
            "Automation Impact", "Minimum Wage Debate", "Consumer Behavior", "Stock Markets",
            "Cryptocurrency", "Economic Recession", "Inflation Concerns", "Small Business Challenges"
        ],
        "media": [
            "Fake News", "Media Bias", "Social Media Influence", "Celebrity Culture",
            "Advertising Ethics", "Journalism Standards", "Freedom of Press", "Digital Journalism",
            "Influencer Marketing", "Streaming vs Traditional TV", "Podcast Popularity", "News Consumption"
        ],
        "technology": [
            "Artificial Intelligence", "Machine Learning", "Big Data", "Internet of Things",
            "Cybersecurity Threats", "Online Privacy", "Digital Addiction", "Remote Work Technology",
            "E-learning Platforms", "Telemedicine", "Smart Cities", "Autonomous Vehicles"
        ],
        "culture": [
            "Cultural Appropriation", "Cultural Preservation", "Pop Culture Trends", "Art Movements",
            "Literature Genres", "Film Industry", "Music Evolution", "Fashion Trends",
            "Food Culture", "Festival Traditions", "Language Evolution", "Cultural Exchange"
        ],
        "politics": [
            "Democratic Systems", "Electoral Processes", "Political Polarization", "Populism Rise",
            "Government Transparency", "Corruption Issues", "Civil Rights", "Protest Movements",
            "International Relations", "Diplomatic Negotiations", "Political Leadership", "Policy Making"
        ],
        "ethics": [
            "Medical Ethics", "Business Ethics", "Environmental Ethics", "Digital Ethics",
            "Animal Rights", "Human Rights", "Privacy Rights", "Ethical Consumerism",
            "Corporate Responsibility", "Ethical AI", "Bioethics", "Research Ethics"
        ]
    },
    "C1": {
        "philosophy": [
            "Existentialism", "Utilitarianism", "Deontological Ethics", "Virtue Ethics",
            "Epistemology", "Metaphysics", "Philosophy of Mind", "Political Philosophy",
            "Aesthetics", "Logic and Reasoning", "Phenomenology", "Postmodernism"
        ],
        "science": [
            "Quantum Mechanics", "Neuroscience", "Genetic Engineering", "CRISPR Technology",
            "Stem Cell Research", "Nanotechnology", "Astrophysics", "Climate Science",
            "Evolutionary Biology", "Cognitive Science", "Biotechnology", "Scientific Method"
        ],
        "global_issues": [
            "Geopolitical Tensions", "Global Governance", "International Law", "Human Trafficking",
            "Refugee Crisis", "Food Security", "Water Politics", "Energy Security",
            "Nuclear Proliferation", "Terrorism", "Cybersecurity Warfare", "Pandemic Preparedness"
        ],
        "economics": [
            "Behavioral Economics", "Game Theory", "Macroeconomic Policy", "Monetary Policy",
            "Fiscal Policy", "Trade Agreements", "Economic Development", "Wealth Distribution",
            "Universal Basic Income", "Stakeholder Capitalism", "Impact Investing", "Economic Models"
        ],
        "sociology": [
            "Social Constructionism", "Structural Functionalism", "Conflict Theory", "Symbolic Interactionism",
            "Social Stratification", "Institutional Racism", "Gender Studies", "Intersectionality",
            "Globalization Effects", "Urbanization Trends", "Social Movements", "Cultural Hegemony"
        ],
        "psychology": [
            "Cognitive Biases", "Behavioral Psychology", "Developmental Psychology", "Social Psychology",
            "Neuropsychology", "Psychotherapy Approaches", "Mental Health Stigma", "Addiction Neuroscience",
            "Positive Psychology", "Trauma Psychology", "Evolutionary Psychology", "Consciousness Studies"
        ],
        "technology": [
            "Artificial General Intelligence", "Quantum Computing", "Blockchain Technology", "Transhumanism",
            "Brain-Computer Interfaces", "Synthetic Biology", "Augmented Reality", "Virtual Reality",
            "Internet Governance", "Algorithmic Bias", "Surveillance Capitalism", "Digital Divide"
        ],
        "arts_humanities": [
            "Literary Theory", "Critical Theory", "Postcolonial Studies", "Feminist Theory",
            "Cultural Studies", "Media Theory", "Art History", "Musicology",
            "Film Theory", "Performance Studies", "Digital Humanities", "Comparative Literature"
        ]
    }
}

# Differentiation Strategies
DIFFERENTIATION_STRATEGIES = {
    "content": [
        "Tiered reading materials",
        "Multiple text complexity levels",
        "Visual and audio alternatives",
        "Simplified vs complex explanations",
        "Scaffolded vocabulary support"
    ],
    "process": [
        "Varied activity structures",
        "Flexible grouping options",
        "Choice in task approach",
        "Multiple pathways to learning",
        "Differentiated questioning"
    ],
    "product": [
        "Choice in assessment format",
        "Multiple demonstration options",
        "Varied output modalities",
        "Flexible deadlines",
        "Personalized projects"
    ],
    "environment": [
        "Flexible seating arrangements",
        "Quiet vs collaborative spaces",
        "Technology integration options",
        "Time flexibility",
        "Support resources availability"
    ]
}

def generate_differentiated_lesson(level, category, topic_num, topic, learning_style, cognitive_level):
    """Generate a comprehensive differentiated lesson"""
    
    lesson_id = f"{level}_{category}_{learning_style}_{cognitive_level}_{topic_num:04d}"
    
    lesson = {
        "lesson_id": lesson_id,
        "level": level,
        "category": category,
        "topic": topic,
        "learning_style": learning_style,
        "learning_style_name": LEARNING_STYLES[learning_style]["name"],
        "cognitive_level": cognitive_level,
        "cognitive_level_name": COGNITIVE_LEVELS[cognitive_level]["name"],
        "duration": "45-60 minutes",
        
        # Core Components
        "objectives": generate_differentiated_objectives(level, topic, cognitive_level),
        "learning_style_adaptations": LEARNING_STYLES[learning_style]["strategies"],
        "cognitive_activities": COGNITIVE_LEVELS[cognitive_level]["activities"],
        "multiple_intelligences": generate_mi_activities(topic),
        
        # UDL Framework
        "udl_principles": {
            "representation": generate_representation_options(learning_style),
            "action_expression": generate_action_options(learning_style),
            "engagement": generate_engagement_options(cognitive_level)
        },
        
        # Differentiation
        "differentiation": {
            "content": generate_content_differentiation(level, topic, cognitive_level),
            "process": generate_process_differentiation(learning_style, cognitive_level),
            "product": generate_product_differentiation(level, learning_style),
            "environment": generate_environment_setup(learning_style)
        },
        
        # Lesson Structure
        "warm_up": generate_adapted_warmup(level, topic, learning_style),
        "main_activities": generate_adapted_activities(level, topic, learning_style, cognitive_level),
        "discussion_prompts": generate_leveled_prompts(level, topic, cognitive_level),
        "assessment": generate_differentiated_assessment(level, learning_style, cognitive_level),
        
        # Support Materials
        "scaffolding": generate_scaffolding(level, cognitive_level),
        "extension_challenges": generate_extensions(level, cognitive_level),
        "vocabulary_support": generate_vocabulary_tiers(level, topic),
        "grammar_focus": generate_grammar_points(level),
        
        # Resources
        "materials_needed": generate_materials(learning_style),
        "technology_integration": generate_tech_tools(learning_style),
        "homework_options": generate_differentiated_homework(level, learning_style, cognitive_level),
        
        # Teacher Support
        "teacher_notes": generate_teacher_guidance(learning_style, cognitive_level),
        "common_difficulties": generate_anticipated_challenges(level, topic),
        "intervention_strategies": generate_interventions(cognitive_level),
        
        # Metadata
        "methodology": "UDL + Differentiated Instruction + CLT + Multiple Intelligences",
        "frameworks": [
            "Universal Design for Learning (CAST)",
            "Differentiated Instruction (Tomlinson)",
            "Multiple Intelligences (Gardner)",
            "Bloom's Taxonomy (Revised)",
            "CEFR Framework",
            "VARK Learning Styles"
        ],
        "references": [
            "Cambridge English Language Assessment",
            "Oxford English Language Teaching",
            "TESOL International Standards",
            "CAST Universal Design for Learning Guidelines",
            "Tomlinson, C.A. (2014). The Differentiated Classroom"
        ]
    }
    
    return lesson

def generate_differentiated_objectives(level, topic, cognitive_level):
    """Generate objectives based on cognitive level"""
    base_objectives = {
        "B1": {
            "basic": [
                f"Identify and recall key vocabulary related to {topic.lower()}",
                f"Understand main ideas in conversations about {topic.lower()}",
                f"Recognize common phrases and expressions"
            ],
            "intermediate": [
                f"Apply learned vocabulary in conversations about {topic.lower()}",
                f"Compare different perspectives on {topic.lower()}",
                f"Analyze simple arguments and opinions"
            ],
            "advanced": [
                f"Evaluate different viewpoints on {topic.lower()}",
                f"Create original dialogues about {topic.lower()}",
                f"Synthesize information from multiple sources"
            ]
        },
        "B2": {
            "basic": [
                f"Understand complex texts about {topic.lower()}",
                f"Identify main arguments and supporting details",
                f"Recognize implicit meanings"
            ],
            "intermediate": [
                f"Apply critical thinking to analyze {topic.lower()}",
                f"Compare and contrast multiple perspectives",
                f"Organize coherent arguments"
            ],
            "advanced": [
                f"Evaluate evidence and reasoning about {topic.lower()}",
                f"Create well-structured presentations",
                f"Synthesize complex information effectively"
            ]
        },
        "C1": {
            "basic": [
                f"Comprehend sophisticated discourse on {topic.lower()}",
                f"Identify nuanced arguments and implications",
                f"Understand theoretical frameworks"
            ],
            "intermediate": [
                f"Apply theoretical concepts to analyze {topic.lower()}",
                f"Examine underlying assumptions and biases",
                f"Structure complex academic arguments"
            ],
            "advanced": [
                f"Critically evaluate scholarly perspectives on {topic.lower()}",
                f"Create original research-based content",
                f"Synthesize interdisciplinary perspectives"
            ]
        }
    }
    return base_objectives[level][cognitive_level]

def generate_mi_activities(topic):
    """Generate activities for multiple intelligences"""
    return {
        "linguistic": f"Write a story or essay about {topic.lower()}",
        "logical_mathematical": f"Analyze patterns and create logical arguments about {topic.lower()}",
        "spatial": f"Create visual representations or mind maps of {topic.lower()}",
        "bodily_kinesthetic": f"Role-play or act out scenarios related to {topic.lower()}",
        "musical": f"Create a song or rhythm exercise about {topic.lower()}",
        "interpersonal": f"Collaborate in groups to discuss {topic.lower()}",
        "intrapersonal": f"Reflect individually on personal connection to {topic.lower()}",
        "naturalistic": f"Categorize and classify concepts related to {topic.lower()}"
    }

def generate_representation_options(learning_style):
    """UDL: Multiple means of representation"""
    options = {
        "visual": ["Infographics", "Video content", "Diagrams", "Color-coded materials"],
        "auditory": ["Audio recordings", "Podcasts", "Verbal explanations", "Music"],
        "kinesthetic": ["Physical demonstrations", "Interactive models", "Hands-on materials"],
        "reading_writing": ["Text documents", "Written instructions", "Articles", "Handouts"]
    }
    return options[learning_style]

def generate_action_options(learning_style):
    """UDL: Multiple means of action and expression"""
    options = {
        "visual": ["Create posters", "Draw diagrams", "Make videos", "Design presentations"],
        "auditory": ["Give presentations", "Record podcasts", "Lead discussions", "Oral reports"],
        "kinesthetic": ["Perform role-plays", "Create demonstrations", "Build models", "Act out scenarios"],
        "reading_writing": ["Write essays", "Create reports", "Compose blogs", "Draft scripts"]
    }
    return options[learning_style]

def generate_engagement_options(cognitive_level):
    """UDL: Multiple means of engagement"""
    options = {
        "basic": ["Clear structure", "Immediate feedback", "Achievable goals", "Positive reinforcement"],
        "intermediate": ["Moderate challenge", "Choice in activities", "Collaborative work", "Real-world relevance"],
        "advanced": ["Complex challenges", "Autonomy", "Creative freedom", "Intellectual stimulation"]
    }
    return options[cognitive_level]

def generate_content_differentiation(level, topic, cognitive_level):
    """Generate differentiated content options"""
    return {
        "basic": f"Simplified texts and basic vocabulary about {topic.lower()}",
        "intermediate": f"Standard complexity materials with support about {topic.lower()}",
        "advanced": f"Complex authentic materials and academic texts about {topic.lower()}"
    }

def generate_process_differentiation(learning_style, cognitive_level):
    """Generate differentiated process options"""
    return {
        "grouping": "Individual, pairs, small groups, or whole class based on preference",
        "pacing": "Self-paced with checkpoints" if cognitive_level == "advanced" else "Teacher-paced with flexibility",
        "support": "Scaffolded support decreasing over time",
        "choice": "Multiple activity options aligned with learning style"
    }

def generate_product_differentiation(level, learning_style):
    """Generate differentiated product options"""
    products = {
        "visual": ["Poster", "Infographic", "Video", "Photo essay"],
        "auditory": ["Podcast", "Oral presentation", "Audio recording", "Interview"],
        "kinesthetic": ["Role-play performance", "Demonstration", "Interactive presentation"],
        "reading_writing": ["Essay", "Report", "Blog post", "Written dialogue"]
    }
    return products[learning_style]

def generate_environment_setup(learning_style):
    """Generate environment recommendations"""
    environments = {
        "visual": "Well-lit space with visual displays and projection capabilities",
        "auditory": "Quiet space with good acoustics and audio equipment",
        "kinesthetic": "Open space allowing movement and hands-on activities",
        "reading_writing": "Quiet study area with writing materials and references"
    }
    return environments[learning_style]

def generate_adapted_warmup(level, topic, learning_style):
    """Generate learning-style adapted warm-up"""
    warmups = {
        "visual": {
            "activity": "Image Analysis",
            "description": f"Students examine images related to {topic.lower()} and discuss",
            "materials": "Images, photos, or video clips"
        },
        "auditory": {
            "activity": "Listen and Discuss",
            "description": f"Students listen to audio about {topic.lower()} and share reactions",
            "materials": "Audio recording or podcast excerpt"
        },
        "kinesthetic": {
            "activity": "Movement Activity",
            "description": f"Students move around and interact physically related to {topic.lower()}",
            "materials": "Space for movement, props if needed"
        },
        "reading_writing": {
            "activity": "Quick Write",
            "description": f"Students write quick responses about {topic.lower()}",
            "materials": "Paper and pens or digital writing tools"
        }
    }
    return warmups[learning_style]

def generate_adapted_activities(level, topic, learning_style, cognitive_level):
    """Generate adapted main activities"""
    activities = []
    
    # Activity 1: Input-focused
    activities.append({
        "number": 1,
        "type": "Input Activity",
        "learning_style_adaptation": LEARNING_STYLES[learning_style]["strategies"][0],
        "cognitive_level": COGNITIVE_LEVELS[cognitive_level]["bloom_levels"][0],
        "description": f"Students receive information about {topic.lower()} through {learning_style} modality",
        "time": "10-15 minutes"
    })
    
    # Activity 2: Practice-focused
    activities.append({
        "number": 2,
        "type": "Practice Activity",
        "learning_style_adaptation": LEARNING_STYLES[learning_style]["strategies"][1],
        "cognitive_level": COGNITIVE_LEVELS[cognitive_level]["bloom_levels"][1] if len(COGNITIVE_LEVELS[cognitive_level]["bloom_levels"]) > 1 else COGNITIVE_LEVELS[cognitive_level]["bloom_levels"][0],
        "description": f"Students practice language related to {topic.lower()} using {learning_style} approach",
        "time": "15-20 minutes"
    })
    
    # Activity 3: Production-focused
    activities.append({
        "number": 3,
        "type": "Production Activity",
        "learning_style_adaptation": LEARNING_STYLES[learning_style]["strategies"][2],
        "cognitive_level": COGNITIVE_LEVELS[cognitive_level]["activities"][0],
        "description": f"Students produce original content about {topic.lower()} demonstrating {cognitive_level} thinking",
        "time": "15-20 minutes"
    })
    
    return activities

def generate_leveled_prompts(level, topic, cognitive_level):
    """Generate discussion prompts by cognitive level"""
    prompts = {
        "basic": [
            f"What is {topic.lower()}?",
            f"Can you describe {topic.lower()}?",
            f"What do you know about {topic.lower()}?"
        ],
        "intermediate": [
            f"How does {topic.lower()} affect people?",
            f"What are the advantages and disadvantages of {topic.lower()}?",
            f"How would you solve problems related to {topic.lower()}?"
        ],
        "advanced": [
            f"What are the implications of {topic.lower()} for society?",
            f"How would you design a better approach to {topic.lower()}?",
            f"What criteria would you use to evaluate {topic.lower()}?"
        ]
    }
    return prompts[cognitive_level]

def generate_differentiated_assessment(level, learning_style, cognitive_level):
    """Generate assessment options"""
    return {
        "formative": [
            "Ongoing observation during activities",
            "Quick checks for understanding",
            "Peer feedback sessions",
            "Self-assessment checklists"
        ],
        "summative": [
            f"Final product in {learning_style} format",
            f"Assessment at {cognitive_level} level",
            "Rubric-based evaluation",
            "Portfolio assessment option"
        ],
        "alternative": [
            "Choice in demonstration method",
            "Multiple attempt options",
            "Collaborative assessment",
            "Process-focused evaluation"
        ]
    }

def generate_scaffolding(level, cognitive_level):
    """Generate scaffolding strategies"""
    scaffolds = {
        "basic": [
            "Sentence starters provided",
            "Word banks available",
            "Model examples given",
            "Step-by-step instructions",
            "Visual supports"
        ],
        "intermediate": [
            "Graphic organizers",
            "Guiding questions",
            "Peer support",
            "Reference materials",
            "Partial models"
        ],
        "advanced": [
            "Minimal scaffolding",
            "Complex resources available",
            "Peer collaboration",
            "Independent research",
            "Self-directed learning"
        ]
    }
    return scaffolds[cognitive_level]

def generate_extensions(level, cognitive_level):
    """Generate extension activities"""
    extensions = {
        "basic": [
            "Additional practice with similar tasks",
            "Vocabulary expansion activities",
            "Repetition with variation"
        ],
        "intermediate": [
            "Apply learning to new contexts",
            "Research and present findings",
            "Create teaching materials for others"
        ],
        "advanced": [
            "Conduct independent research project",
            "Create original theoretical framework",
            "Mentor other students"
        ]
    }
    return extensions[cognitive_level]

def generate_vocabulary_tiers(level, topic):
    """Generate tiered vocabulary"""
    return {
        "tier_1": "High-frequency everyday words",
        "tier_2": f"Academic and topic-specific words for {topic.lower()}",
        "tier_3": f"Domain-specific technical terms related to {topic.lower()}"
    }

def generate_grammar_points(level):
    """Generate grammar focus by level"""
    grammar = {
        "B1": ["Present perfect", "Modal verbs", "First conditional"],
        "B2": ["Passive voice", "Reported speech", "Mixed conditionals"],
        "C1": ["Inversion", "Cleft sentences", "Subjunctive mood"]
    }
    return grammar[level]

def generate_materials(learning_style):
    """Generate materials list"""
    materials = {
        "visual": ["Projector/screen", "Images", "Videos", "Colored markers", "Chart paper"],
        "auditory": ["Audio player", "Microphones", "Recording device", "Speakers"],
        "kinesthetic": ["Props", "Realia", "Movement space", "Manipulatives"],
        "reading_writing": ["Texts", "Handouts", "Writing materials", "Reference books"]
    }
    return materials[learning_style]

def generate_tech_tools(learning_style):
    """Generate technology integration"""
    tools = {
        "visual": ["PowerPoint/Slides", "Canva", "YouTube", "Infographic tools"],
        "auditory": ["Podcasts", "Audio recording apps", "Voice notes", "Music platforms"],
        "kinesthetic": ["Interactive whiteboards", "VR/AR apps", "Simulation software"],
        "reading_writing": ["Google Docs", "Blogs", "Digital portfolios", "E-books"]
    }
    return tools[learning_style]

def generate_differentiated_homework(level, learning_style, cognitive_level):
    """Generate homework options"""
    return {
        "required": f"Core assignment at {cognitive_level} level using {learning_style} approach",
        "choice_1": "Alternative format option",
        "choice_2": "Extended project option",
        "support": "Scaffolded version available",
        "challenge": "Advanced extension available"
    }

def generate_teacher_guidance(learning_style, cognitive_level):
    """Generate teacher notes"""
    return {
        "preparation": f"Prepare materials for {learning_style} learners",
        "differentiation_tips": f"Adjust complexity for {cognitive_level} level",
        "grouping_suggestions": "Flexible grouping based on readiness and interest",
        "time_management": "Build in flexibility for different pacing needs",
        "assessment_notes": "Use multiple assessment methods"
    }

def generate_anticipated_challenges(level, topic):
    """Generate common difficulties"""
    return [
        f"Students may lack background knowledge about {topic.lower()}",
        "Vocabulary may be challenging for some students",
        "Cultural differences may affect understanding",
        "Some students may need more processing time"
    ]

def generate_interventions(cognitive_level):
    """Generate intervention strategies"""
    interventions = {
        "basic": [
            "Provide additional modeling",
            "Simplify language",
            "Increase scaffolding",
            "Allow more time"
        ],
        "intermediate": [
            "Provide graphic organizers",
            "Offer peer support",
            "Break tasks into steps",
            "Give specific feedback"
        ],
        "advanced": [
            "Provide complex resources",
            "Encourage independent problem-solving",
            "Facilitate peer teaching",
            "Challenge with extensions"
        ]
    }
    return interventions[cognitive_level]

def save_lesson(lesson, output_dir):
    """Save lesson to JSON and Markdown files"""
    level = lesson["level"]
    category = lesson["category"]
    learning_style = lesson["learning_style"]
    cognitive_level = lesson["cognitive_level"]
    lesson_id = lesson["lesson_id"]
    
    # Create subdirectory structure
    subdir = output_dir / level / category / learning_style / cognitive_level
    subdir.mkdir(parents=True, exist_ok=True)
    
    # Save JSON
    json_path = subdir / f"{lesson_id}.json"
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(lesson, f, indent=2, ensure_ascii=False)
    
    # Save Markdown
    md_path = subdir / f"{lesson_id}.md"
    md_content = generate_markdown(lesson)
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(md_content)
    
    return json_path, md_path

def generate_markdown(lesson):
    """Generate markdown version of lesson"""
    md = f"""# {lesson['topic']}

**Level:** {lesson['level']} | **Category:** {lesson['category']}  
**Learning Style:** {lesson['learning_style_name']}  
**Cognitive Level:** {lesson['cognitive_level_name']}  
**Lesson ID:** {lesson['lesson_id']}  
**Duration:** {lesson['duration']}

---

## Learning Objectives

"""
    
    for obj in lesson['objectives']:
        md += f"- {obj}\n"
    
    md += f"""
---

## Learning Style Adaptations ({lesson['learning_style_name']})

"""
    
    for strategy in lesson['learning_style_adaptations']:
        md += f"- {strategy}\n"
    
    md += f"""
---

## Cognitive Activities ({lesson['cognitive_level_name']})

"""
    
    for activity in lesson['cognitive_activities']:
        md += f"- {activity}\n"
    
    md += """
---

## Multiple Intelligences Activities

"""
    
    for mi, activity in lesson['multiple_intelligences'].items():
        md += f"- **{mi.replace('_', ' ').title()}:** {activity}\n"
    
    md += """
---

## Universal Design for Learning (UDL)

### Multiple Means of Representation

"""
    
    for option in lesson['udl_principles']['representation']:
        md += f"- {option}\n"
    
    md += "\n### Multiple Means of Action and Expression\n\n"
    
    for option in lesson['udl_principles']['action_expression']:
        md += f"- {option}\n"
    
    md += "\n### Multiple Means of Engagement\n\n"
    
    for option in lesson['udl_principles']['engagement']:
        md += f"- {option}\n"
    
    md += """
---

## Differentiation Strategies

### Content Differentiation

"""
    
    for key, value in lesson['differentiation']['content'].items():
        md += f"- **{key.title()}:** {value}\n"
    
    md += "\n### Process Differentiation\n\n"
    
    for key, value in lesson['differentiation']['process'].items():
        md += f"- **{key.title()}:** {value}\n"
    
    md += "\n### Product Options\n\n"
    
    for product in lesson['differentiation']['product']:
        md += f"- {product}\n"
    
    md += f"\n### Environment Setup\n\n{lesson['differentiation']['environment']}\n"
    
    md += f"""
---

## Lesson Structure

### Warm-Up Activity

**Activity:** {lesson['warm_up']['activity']}  
**Description:** {lesson['warm_up']['description']}  
**Materials:** {lesson['warm_up']['materials']}

### Main Activities

"""
    
    for activity in lesson['main_activities']:
        md += f"""
#### Activity {activity['number']}: {activity['type']}

- **Learning Style Adaptation:** {activity['learning_style_adaptation']}
- **Cognitive Level:** {activity['cognitive_level']}
- **Description:** {activity['description']}
- **Time:** {activity['time']}

"""
    
    md += "### Discussion Prompts\n\n"
    
    for i, prompt in enumerate(lesson['discussion_prompts'], 1):
        md += f"{i}. {prompt}\n"
    
    md += """
---

## Assessment

### Formative Assessment

"""
    
    for method in lesson['assessment']['formative']:
        md += f"- {method}\n"
    
    md += "\n### Summative Assessment\n\n"
    
    for method in lesson['assessment']['summative']:
        md += f"- {method}\n"
    
    md += "\n### Alternative Assessment\n\n"
    
    for method in lesson['assessment']['alternative']:
        md += f"- {method}\n"
    
    md += """
---

## Support and Extension

### Scaffolding Strategies

"""
    
    for scaffold in lesson['scaffolding']:
        md += f"- {scaffold}\n"
    
    md += "\n### Extension Challenges\n\n"
    
    for extension in lesson['extension_challenges']:
        md += f"- {extension}\n"
    
    md += """
---

## Language Focus

### Vocabulary Support

"""
    
    for tier, description in lesson['vocabulary_support'].items():
        md += f"- **{tier.replace('_', ' ').title()}:** {description}\n"
    
    md += "\n### Grammar Focus\n\n"
    
    for grammar in lesson['grammar_focus']:
        md += f"- {grammar}\n"
    
    md += """
---

## Resources and Materials

### Materials Needed

"""
    
    for material in lesson['materials_needed']:
        md += f"- {material}\n"
    
    md += "\n### Technology Integration\n\n"
    
    for tool in lesson['technology_integration']:
        md += f"- {tool}\n"
    
    md += """
---

## Homework Options

"""
    
    for key, value in lesson['homework_options'].items():
        md += f"- **{key.replace('_', ' ').title()}:** {value}\n"
    
    md += """
---

## Teacher Support

### Teacher Notes

"""
    
    for key, value in lesson['teacher_notes'].items():
        md += f"- **{key.replace('_', ' ').title()}:** {value}\n"
    
    md += "\n### Common Difficulties\n\n"
    
    for difficulty in lesson['common_difficulties']:
        md += f"- {difficulty}\n"
    
    md += "\n### Intervention Strategies\n\n"
    
    for intervention in lesson['intervention_strategies']:
        md += f"- {intervention}\n"
    
    md += f"""
---

## Methodology and Frameworks

**Methodology:** {lesson['methodology']}

**Frameworks:**

"""
    
    for framework in lesson['frameworks']:
        md += f"- {framework}\n"
    
    md += "\n**References:**\n\n"
    
    for ref in lesson['references']:
        md += f"- {ref}\n"
    
    md += "\n---\n\n*This differentiated lesson was generated using evidence-based pedagogical frameworks and best practices in ESL instruction.*\n"
    
    return md

def main():
    """Main function to generate 1000+ differentiated lessons"""
    output_dir = Path("/home/ubuntu/Prize2Pride-English-A1/lessons")
    
    print("🎓 Advanced Differentiated ESL Lessons Generator")
    print("=" * 70)
    print("Generating 1000+ Mega-Prompt Lessons with:")
    print("- VARK Learning Styles (Visual, Auditory, Kinesthetic, Reading/Writing)")
    print("- Bloom's Taxonomy Cognitive Levels (Basic, Intermediate, Advanced)")
    print("- Multiple Intelligences (Gardner)")
    print("- Universal Design for Learning (UDL)")
    print("- Differentiated Instruction (Tomlinson)")
    print("=" * 70)
    print()
    
    total_lessons = 0
    
    for level in ["B1", "B2", "C1"]:
        print(f"\n📚 Generating {level} lessons...")
        
        for category, topics in TOPIC_CATEGORIES[level].items():
            print(f"\n  📂 Category: {category}")
            
            for topic_num, topic in enumerate(topics, 1):
                # Generate lessons for each combination of learning style and cognitive level
                for learning_style in LEARNING_STYLES.keys():
                    for cognitive_level in COGNITIVE_LEVELS.keys():
                        lesson = generate_differentiated_lesson(
                            level, category, topic_num, topic, 
                            learning_style, cognitive_level
                        )
                        
                        json_path, md_path = save_lesson(lesson, output_dir)
                        total_lessons += 1
                        
                        if total_lessons % 100 == 0:
                            print(f"    ✓ Generated {total_lessons} lessons...")
    
    print(f"\n{'=' * 70}")
    print(f"🎉 Successfully generated {total_lessons} differentiated lessons!")
    print(f"📁 Output directory: {output_dir}")
    print(f"{'=' * 70}")
    
    # Generate comprehensive README
    generate_mega_readme(output_dir, total_lessons)
    
    return total_lessons

def generate_mega_readme(output_dir, total_lessons):
    """Generate comprehensive README for mega lessons"""
    
    readme = f"""# Advanced Differentiated ESL Conversational Lessons
## 1000+ Mega-Prompts for B1, B2, C1 Levels

This repository contains **{total_lessons} comprehensive, differentiated English conversational lessons** designed according to cutting-edge pedagogical frameworks and research-based best practices.

---

## 🎯 Pedagogical Frameworks

### 1. **CEFR (Common European Framework of Reference)**
- Aligned with B1, B2, and C1 proficiency descriptors
- Based on Cambridge English and Oxford ELT standards

### 2. **Universal Design for Learning (UDL)**
- Multiple means of representation
- Multiple means of action and expression
- Multiple means of engagement

### 3. **Differentiated Instruction (Tomlinson)**
- Content differentiation
- Process differentiation
- Product differentiation
- Environment differentiation

### 4. **VARK Learning Styles**
- **Visual learners:** Charts, diagrams, videos, visual organizers
- **Auditory learners:** Discussions, podcasts, oral presentations
- **Kinesthetic learners:** Role-plays, movement, hands-on activities
- **Reading/Writing learners:** Texts, essays, written reflections

### 5. **Multiple Intelligences (Gardner)**
- Linguistic, Logical-Mathematical, Spatial, Bodily-Kinesthetic
- Musical, Interpersonal, Intrapersonal, Naturalistic

### 6. **Bloom's Taxonomy (Revised)**
- **Basic:** Remember, Understand
- **Intermediate:** Apply, Analyze
- **Advanced:** Evaluate, Create

---

## 📊 Lesson Matrix

Each lesson is uniquely designed for:

| Dimension | Options | Count |
|-----------|---------|-------|
| **CEFR Levels** | B1, B2, C1 | 3 |
| **Learning Styles** | Visual, Auditory, Kinesthetic, Reading/Writing | 4 |
| **Cognitive Levels** | Basic, Intermediate, Advanced | 3 |
| **Topic Categories** | 8 per level | 24 |
| **Topics per Category** | 8-12 | ~240 |

**Total Unique Lessons:** {total_lessons}

---

## 📂 Repository Structure

```
lessons/
├── B1/
│   ├── daily_life/
│   │   ├── visual/
│   │   │   ├── basic/
│   │   │   │   ├── B1_daily_life_visual_basic_0001.json
│   │   │   │   └── B1_daily_life_visual_basic_0001.md
│   │   │   ├── intermediate/
│   │   │   └── advanced/
│   │   ├── auditory/
│   │   ├── kinesthetic/
│   │   └── reading_writing/
│   ├── social/
│   ├── work/
│   ├── leisure/
│   ├── travel/
│   ├── health/
│   ├── education/
│   └── technology/
├── B2/
│   ├── society/
│   ├── environment/
│   ├── economy/
│   ├── media/
│   ├── technology/
│   ├── culture/
│   ├── politics/
│   └── ethics/
└── C1/
    ├── philosophy/
    ├── science/
    ├── global_issues/
    ├── economics/
    ├── sociology/
    ├── psychology/
    ├── technology/
    └── arts_humanities/
```

---

## 🎓 What Each Lesson Includes

### Core Components
- **Learning Objectives** (differentiated by cognitive level)
- **Learning Style Adaptations** (VARK-specific strategies)
- **Cognitive Activities** (Bloom's Taxonomy aligned)
- **Multiple Intelligences Activities** (8 intelligence types)

### UDL Framework
- Multiple means of **representation**
- Multiple means of **action and expression**
- Multiple means of **engagement**

### Differentiation Strategies
- **Content:** Tiered materials, varied complexity
- **Process:** Flexible grouping, varied pacing
- **Product:** Choice in assessment format
- **Environment:** Flexible learning spaces

### Lesson Structure
- **Warm-Up Activity** (learning style adapted)
- **Main Activities** (3 activities with differentiation)
- **Discussion Prompts** (leveled by cognitive complexity)
- **Assessment Options** (formative, summative, alternative)

### Support Materials
- **Scaffolding Strategies** (by cognitive level)
- **Extension Challenges** (for advanced learners)
- **Vocabulary Support** (3-tier system)
- **Grammar Focus** (level-appropriate)

### Resources
- **Materials Needed** (by learning style)
- **Technology Integration** (digital tools)
- **Homework Options** (differentiated choices)

### Teacher Support
- **Teacher Notes** (preparation and tips)
- **Common Difficulties** (anticipated challenges)
- **Intervention Strategies** (support for struggling learners)

---

## 🌟 Key Features

### 1. **Truly Differentiated**
Every lesson offers multiple pathways to learning, ensuring all students can access content and demonstrate mastery.

### 2. **Evidence-Based**
Built on decades of research in second language acquisition, cognitive psychology, and educational neuroscience.

### 3. **Practical and Ready-to-Use**
Complete lesson plans with all materials, activities, and assessments included.

### 4. **Flexible and Adaptable**
Teachers can mix and match components based on their specific classroom needs.

### 5. **Technology-Enhanced**
Integrates modern educational technology while maintaining traditional teaching strengths.

### 6. **Culturally Responsive**
Acknowledges diverse backgrounds and learning experiences.

---

## 👨‍🏫 For Teachers

### How to Use These Lessons

1. **Identify Your Students' Needs**
   - Assess CEFR level (B1, B2, or C1)
   - Identify predominant learning styles
   - Determine cognitive readiness

2. **Select Appropriate Lessons**
   - Choose topic category and specific topic
   - Select learning style version
   - Pick cognitive level

3. **Customize as Needed**
   - Mix activities from different versions
   - Adjust timing based on your class
   - Add your own cultural examples

4. **Implement with Flexibility**
   - Use formative assessment to adjust
   - Provide choices when possible
   - Celebrate diverse approaches

### Professional Development

These lessons model best practices in:
- Differentiated instruction
- Universal Design for Learning
- Communicative Language Teaching
- Task-Based Learning
- Assessment for learning

---

## 👨‍🎓 For Learners

### Find Your Learning Style

**Visual Learners:** You prefer lessons with images, videos, diagrams, and color-coding.

**Auditory Learners:** You prefer lessons with discussions, podcasts, and oral presentations.

**Kinesthetic Learners:** You prefer lessons with movement, role-plays, and hands-on activities.

**Reading/Writing Learners:** You prefer lessons with texts, essays, and written reflections.

### Progress at Your Own Level

**Basic/Foundational:** Focus on remembering and understanding core concepts.

**Intermediate/Application:** Apply knowledge and analyze different perspectives.

**Advanced/Creative:** Evaluate critically and create original content.

---

## 📚 Topic Coverage

### B1 (Intermediate) - 8 Categories
- Daily Life, Social, Work, Leisure, Travel, Health, Education, Technology

### B2 (Upper Intermediate) - 8 Categories
- Society, Environment, Economy, Media, Technology, Culture, Politics, Ethics

### C1 (Advanced) - 8 Categories
- Philosophy, Science, Global Issues, Economics, Sociology, Psychology, Technology, Arts & Humanities

---

## 🔬 Research Foundation

This curriculum is grounded in:

- **Second Language Acquisition Theory** (Krashen, Long, Swain)
- **Cognitive Load Theory** (Sweller)
- **Zone of Proximal Development** (Vygotsky)
- **Multiple Intelligences** (Gardner)
- **Universal Design for Learning** (CAST)
- **Differentiated Instruction** (Tomlinson)
- **Bloom's Taxonomy** (Anderson & Krathwohl)
- **CEFR Framework** (Council of Europe)

---

## 📖 References

- Anderson, L. W., & Krathwohl, D. R. (Eds.). (2001). *A taxonomy for learning, teaching, and assessing*
- CAST (2018). *Universal Design for Learning Guidelines version 2.2*
- Council of Europe (2020). *Common European Framework of Reference for Languages: Companion Volume*
- Gardner, H. (2011). *Frames of mind: The theory of multiple intelligences*
- Tomlinson, C. A. (2014). *The differentiated classroom: Responding to the needs of all learners*
- Cambridge English Language Assessment. *Teaching and Learning Resources*
- Oxford University Press. *English Language Teaching Methodology*
- TESOL International Association. *Standards for ESL/EFL Teachers*

---

## 🤝 Contributing

We welcome feedback and contributions from:
- ESL/EFL teachers
- Applied linguistics researchers
- Curriculum developers
- Educational technology specialists

---

## 📜 License

These materials are designed for educational purposes.

---

## 🌍 Impact

By providing **{total_lessons} differentiated lessons**, we ensure that:
- Every learner can access content in their preferred modality
- Teachers have flexible, research-based resources
- Language learning is inclusive and effective
- Students can progress at their optimal pace

---

**Generated with pedagogical expertise based on Cambridge English, Oxford ELT, TESOL, CAST UDL, and differentiated instruction best practices.**

*Empowering every English language learner to succeed.*
"""
    
    readme_path = output_dir.parent / "MEGA_LESSONS_README.md"
    
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(readme)
    
    print(f"\n📄 Comprehensive README created: {readme_path}")

if __name__ == "__main__":
    total = main()
    print(f"\n✅ Generation complete! Total lessons: {total}")
