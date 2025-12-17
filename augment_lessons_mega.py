#!/usr/bin/env python3
"""
MEGA LESSON AUGMENTATION SYSTEM
Transform any lesson across language registers and genre themes
Creates exponential variations with one-click generation
"""

import json
import os
from pathlib import Path
from itertools import product

# LANGUAGE REGISTERS - From casual to expert
LANGUAGE_REGISTERS = {
    "slang": {
        "name": "Slang/Street",
        "description": "Casual street language, colloquialisms, youth speak",
        "characteristics": [
            "Contractions everywhere (gonna, wanna, ain't)",
            "Slang terms and expressions",
            "Informal grammar",
            "Shortened words",
            "Very casual tone"
        ],
        "example_phrases": [
            "What's up?", "That's dope!", "No cap", "For real?", "Chill out"
        ]
    },
    "informal": {
        "name": "Informal/Conversational",
        "description": "Friendly, relaxed everyday speech",
        "characteristics": [
            "Common contractions (I'm, you're, it's)",
            "Simple vocabulary",
            "Personal pronouns",
            "Conversational expressions",
            "Relaxed grammar"
        ],
        "example_phrases": [
            "How's it going?", "That's great!", "I think so", "Really?", "Take it easy"
        ]
    },
    "neutral": {
        "name": "Neutral/Standard",
        "description": "Standard professional communication",
        "characteristics": [
            "Clear and direct",
            "Standard grammar",
            "Professional vocabulary",
            "Balanced tone",
            "Appropriate for most contexts"
        ],
        "example_phrases": [
            "How are you?", "That's excellent", "I believe so", "Is that correct?", "Please proceed"
        ]
    },
    "formal": {
        "name": "Formal/Business",
        "description": "Professional, business-appropriate language",
        "characteristics": [
            "No contractions",
            "Formal vocabulary",
            "Complete sentences",
            "Professional expressions",
            "Polite and respectful"
        ],
        "example_phrases": [
            "How do you do?", "That is commendable", "I concur", "Would you confirm?", "Kindly continue"
        ]
    },
    "expert": {
        "name": "Expert/Academic",
        "description": "Scholarly, technical, high-level discourse",
        "characteristics": [
            "Academic vocabulary",
            "Technical terminology",
            "Complex sentence structures",
            "Theoretical frameworks",
            "Scholarly tone"
        ],
        "example_phrases": [
            "What is your assessment?", "That demonstrates excellence", "I posit that", "Could you substantiate?", "Please elucidate further"
        ]
    }
}

# GENRE THEMES - Transform content into different narrative styles
GENRE_THEMES = {
    "romance": {
        "name": "Romance",
        "description": "Love, relationships, emotional connections",
        "vocabulary": ["heart", "passion", "affection", "devotion", "chemistry", "attraction"],
        "scenario_twist": "romantic encounter or relationship development",
        "tone": "emotional, heartfelt, intimate"
    },
    "drama": {
        "name": "Drama",
        "description": "Intense emotions, conflicts, life challenges",
        "vocabulary": ["conflict", "tension", "struggle", "revelation", "confrontation", "dilemma"],
        "scenario_twist": "dramatic conflict or emotional crisis",
        "tone": "intense, emotional, serious"
    },
    "horror": {
        "name": "Horror",
        "description": "Fear, suspense, supernatural elements",
        "vocabulary": ["terror", "darkness", "mysterious", "haunting", "eerie", "sinister"],
        "scenario_twist": "frightening or supernatural situation",
        "tone": "suspenseful, dark, unsettling"
    },
    "action": {
        "name": "Action/Adventure",
        "description": "High energy, excitement, physical challenges",
        "vocabulary": ["chase", "pursuit", "danger", "adrenaline", "mission", "explosive"],
        "scenario_twist": "high-stakes action sequence",
        "tone": "fast-paced, energetic, thrilling"
    },
    "comedy": {
        "name": "Comedy",
        "description": "Humor, wit, funny situations",
        "vocabulary": ["hilarious", "amusing", "ridiculous", "witty", "absurd", "comical"],
        "scenario_twist": "humorous misunderstanding or funny situation",
        "tone": "lighthearted, funny, entertaining"
    },
    "mystery": {
        "name": "Mystery/Detective",
        "description": "Investigation, puzzles, solving problems",
        "vocabulary": ["clue", "investigation", "suspect", "evidence", "puzzle", "revelation"],
        "scenario_twist": "mysterious problem to solve",
        "tone": "intriguing, analytical, suspenseful"
    },
    "scifi": {
        "name": "Science Fiction",
        "description": "Futuristic, technology, space, innovation",
        "vocabulary": ["technology", "innovation", "futuristic", "artificial", "quantum", "cyber"],
        "scenario_twist": "futuristic or technological scenario",
        "tone": "innovative, speculative, advanced"
    },
    "fantasy": {
        "name": "Fantasy",
        "description": "Magic, mythical creatures, imaginary worlds",
        "vocabulary": ["magical", "enchanted", "mystical", "legendary", "mythical", "supernatural"],
        "scenario_twist": "magical or fantastical situation",
        "tone": "imaginative, wondrous, epic"
    },
    "thriller": {
        "name": "Thriller/Suspense",
        "description": "Tension, danger, psychological intensity",
        "vocabulary": ["suspense", "threat", "danger", "pursuit", "conspiracy", "betrayal"],
        "scenario_twist": "dangerous or threatening situation",
        "tone": "tense, gripping, intense"
    },
    "historical": {
        "name": "Historical",
        "description": "Past eras, historical events, period settings",
        "vocabulary": ["tradition", "heritage", "legacy", "era", "chronicle", "antiquity"],
        "scenario_twist": "historical period or event",
        "tone": "reflective, educational, period-appropriate"
    },
    "business": {
        "name": "Business/Corporate",
        "description": "Professional scenarios, workplace situations",
        "vocabulary": ["strategy", "negotiation", "stakeholder", "synergy", "leverage", "optimize"],
        "scenario_twist": "corporate or business challenge",
        "tone": "professional, strategic, goal-oriented"
    },
    "sports": {
        "name": "Sports/Competition",
        "description": "Athletic challenges, competition, teamwork",
        "vocabulary": ["competition", "victory", "training", "championship", "teamwork", "performance"],
        "scenario_twist": "competitive sports scenario",
        "tone": "energetic, competitive, motivational"
    }
}

def augment_lesson_content(original_lesson, register, genre):
    """
    Transform a lesson into a specific language register and genre theme
    """
    
    lesson_id = original_lesson.get('lesson_id', 'unknown')
    base_topic = original_lesson.get('topic', 'General Topic')
    
    # Create augmented lesson ID
    augmented_id = f"{lesson_id}_REG_{register}_GENRE_{genre}"
    
    # Create augmented lesson
    augmented_lesson = {
        "lesson_id": augmented_id,
        "original_lesson_id": lesson_id,
        "augmentation_type": "register_genre_transformation",
        "language_register": register,
        "language_register_name": LANGUAGE_REGISTERS[register]["name"],
        "genre_theme": genre,
        "genre_theme_name": GENRE_THEMES[genre]["name"],
        
        # Copy base information
        "level": original_lesson.get('level', ''),
        "level_name": original_lesson.get('level_name', ''),
        "category": original_lesson.get('category', ''),
        "original_topic": base_topic,
        "augmented_topic": f"{base_topic} ({GENRE_THEMES[genre]['name']} Theme)",
        "learning_style": original_lesson.get('learning_style', ''),
        "cognitive_level": original_lesson.get('cognitive_level', ''),
        "duration": original_lesson.get('duration', '45-60 minutes'),
        
        # Augmentation details
        "register_characteristics": LANGUAGE_REGISTERS[register]["characteristics"],
        "register_example_phrases": LANGUAGE_REGISTERS[register]["example_phrases"],
        "genre_vocabulary": GENRE_THEMES[genre]["vocabulary"],
        "genre_scenario_twist": GENRE_THEMES[genre]["scenario_twist"],
        "genre_tone": GENRE_THEMES[genre]["tone"],
        
        # Transformed objectives
        "objectives": transform_objectives(
            original_lesson.get('objectives', []),
            register,
            genre,
            base_topic
        ),
        
        # Transformed warm-up
        "warm_up": transform_warmup(
            original_lesson.get('warm_up', {}),
            register,
            genre,
            base_topic
        ),
        
        # Transformed activities
        "main_activities": transform_activities(
            original_lesson.get('main_activities', []),
            register,
            genre,
            base_topic
        ),
        
        # Transformed discussion questions
        "discussion_questions": transform_discussion_questions(
            original_lesson.get('discussion_prompts', []),
            register,
            genre,
            base_topic
        ),
        
        # Transformed role-play scenarios
        "role_play_scenarios": transform_roleplay(
            original_lesson.get('role_play_scenarios', []),
            register,
            genre,
            base_topic
        ),
        
        # Register-specific expressions
        "useful_expressions": generate_register_expressions(register, genre),
        
        # Genre-specific vocabulary
        "genre_vocabulary_list": generate_genre_vocabulary(genre, base_topic),
        
        # Transformation guide for teachers
        "teacher_transformation_guide": {
            "register_guidance": f"Use {LANGUAGE_REGISTERS[register]['name']} throughout: {LANGUAGE_REGISTERS[register]['description']}",
            "genre_guidance": f"Frame all content with {GENRE_THEMES[genre]['name']} theme: {GENRE_THEMES[genre]['description']}",
            "tone": GENRE_THEMES[genre]['tone'],
            "key_vocabulary": GENRE_THEMES[genre]['vocabulary']
        },
        
        # Assessment adapted to register and genre
        "assessment": {
            "register_focus": f"Students demonstrate mastery of {LANGUAGE_REGISTERS[register]['name']} register",
            "genre_focus": f"Students engage with {GENRE_THEMES[genre]['name']} themed content",
            "criteria": [
                f"Appropriate use of {register} register language",
                f"Engagement with {genre} theme elements",
                "Comprehension of topic within new context",
                "Creative application of vocabulary"
            ]
        },
        
        # Metadata
        "methodology": f"Augmented CLT with Register & Genre Transformation",
        "augmentation_frameworks": [
            "Sociolinguistic Register Theory",
            "Genre-Based Pedagogy",
            "Content Transformation Methodology",
            "Narrative Language Teaching"
        ],
        "original_frameworks": original_lesson.get('frameworks', [])
    }
    
    return augmented_lesson

def transform_objectives(original_objectives, register, genre, topic):
    """Transform learning objectives to match register and genre"""
    
    register_name = LANGUAGE_REGISTERS[register]["name"]
    genre_name = GENRE_THEMES[genre]["name"]
    
    transformed = [
        f"Students will discuss {topic.lower()} using {register_name} register language",
        f"Students will engage with {genre_name} themed scenarios related to {topic.lower()}",
        f"Students will demonstrate appropriate use of {register} level vocabulary and expressions",
        f"Students will create dialogues combining {topic.lower()} content with {genre_name} narrative elements"
    ]
    
    return transformed

def transform_warmup(original_warmup, register, genre, topic):
    """Transform warm-up activity"""
    
    return {
        "activity": f"{GENRE_THEMES[genre]['name']} Scenario Introduction",
        "register": LANGUAGE_REGISTERS[register]["name"],
        "description": f"Students explore {topic.lower()} through a {GENRE_THEMES[genre]['name']} lens using {LANGUAGE_REGISTERS[register]['name']} language",
        "scenario": f"Imagine a {GENRE_THEMES[genre]['scenario_twist']} involving {topic.lower()}",
        "tone": GENRE_THEMES[genre]['tone'],
        "time": "5-10 minutes"
    }

def transform_activities(original_activities, register, genre, topic):
    """Transform main activities"""
    
    activities = []
    
    activities.append({
        "number": 1,
        "type": f"{GENRE_THEMES[genre]['name']} Vocabulary Building",
        "description": f"Students learn and practice {register} register vocabulary related to {topic.lower()} in a {genre} context",
        "genre_element": GENRE_THEMES[genre]['scenario_twist'],
        "register_focus": LANGUAGE_REGISTERS[register]['name'],
        "time": "15 minutes"
    })
    
    activities.append({
        "number": 2,
        "type": f"{GENRE_THEMES[genre]['name']} Role-Play",
        "description": f"Students engage in {genre} themed role-play about {topic.lower()} using {register} register",
        "genre_element": GENRE_THEMES[genre]['tone'],
        "register_focus": LANGUAGE_REGISTERS[register]['name'],
        "time": "20 minutes"
    })
    
    activities.append({
        "number": 3,
        "type": f"{GENRE_THEMES[genre]['name']} Creative Production",
        "description": f"Students create original {genre} themed content about {topic.lower()} in {register} register",
        "genre_element": "narrative creation",
        "register_focus": LANGUAGE_REGISTERS[register]['name'],
        "time": "15 minutes"
    })
    
    return activities

def transform_discussion_questions(original_questions, register, genre, topic):
    """Transform discussion questions"""
    
    genre_vocab = GENRE_THEMES[genre]['vocabulary']
    
    questions = [
        f"How would you describe {topic.lower()} in a {GENRE_THEMES[genre]['name']} scenario?",
        f"What {genre_vocab[0]} or {genre_vocab[1]} might be involved in {topic.lower()}?",
        f"Can you create a {GENRE_THEMES[genre]['name']} story about {topic.lower()}?",
        f"How does {topic.lower()} change when viewed through a {GENRE_THEMES[genre]['name']} perspective?",
        f"What {register} register expressions would you use to discuss this {genre} scenario?"
    ]
    
    return questions

def transform_roleplay(original_roleplay, register, genre, topic):
    """Transform role-play scenarios"""
    
    scenarios = [
        {
            "scenario": f"{GENRE_THEMES[genre]['name']} situation involving {topic.lower()}",
            "register": LANGUAGE_REGISTERS[register]['name'],
            "genre_twist": GENRE_THEMES[genre]['scenario_twist'],
            "roles": [
                f"Character A: Using {register} register in {genre} context",
                f"Character B: Responding in {register} register within {genre} theme"
            ],
            "tone": GENRE_THEMES[genre]['tone'],
            "vocabulary_focus": GENRE_THEMES[genre]['vocabulary'][:3]
        }
    ]
    
    return scenarios

def generate_register_expressions(register, genre):
    """Generate useful expressions for the register"""
    
    expressions = {
        "greeting": LANGUAGE_REGISTERS[register]["example_phrases"][0],
        "positive_reaction": LANGUAGE_REGISTERS[register]["example_phrases"][1],
        "agreement": LANGUAGE_REGISTERS[register]["example_phrases"][2],
        "question": LANGUAGE_REGISTERS[register]["example_phrases"][3],
        "closing": LANGUAGE_REGISTERS[register]["example_phrases"][4]
    }
    
    return expressions

def generate_genre_vocabulary(genre, topic):
    """Generate genre-specific vocabulary list"""
    
    vocab = {
        "core_genre_terms": GENRE_THEMES[genre]['vocabulary'],
        "topic_genre_blend": [
            f"{topic.lower()} with {word}" for word in GENRE_THEMES[genre]['vocabulary'][:3]
        ],
        "narrative_elements": [
            f"{GENRE_THEMES[genre]['name']} scenario",
            f"{GENRE_THEMES[genre]['tone']} atmosphere",
            f"{GENRE_THEMES[genre]['scenario_twist']}"
        ]
    }
    
    return vocab

def save_augmented_lesson(lesson, output_dir):
    """Save augmented lesson to JSON and Markdown"""
    
    level = lesson['level']
    register = lesson['language_register']
    genre = lesson['genre_theme']
    lesson_id = lesson['lesson_id']
    
    # Create directory structure
    subdir = output_dir / level / "augmented" / register / genre
    subdir.mkdir(parents=True, exist_ok=True)
    
    # Save JSON
    json_path = subdir / f"{lesson_id}.json"
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(lesson, f, indent=2, ensure_ascii=False)
    
    # Save Markdown
    md_path = subdir / f"{lesson_id}.md"
    md_content = generate_augmented_markdown(lesson)
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(md_content)
    
    return json_path, md_path

def generate_augmented_markdown(lesson):
    """Generate markdown for augmented lesson"""
    
    md = f"""# {lesson['augmented_topic']}

**Original Topic:** {lesson['original_topic']}  
**Language Register:** {lesson['language_register_name']}  
**Genre Theme:** {lesson['genre_theme_name']}  
**Level:** {lesson['level']} - {lesson['level_name']}  
**Lesson ID:** {lesson['lesson_id']}  
**Duration:** {lesson['duration']}

---

## 🎭 Augmentation Details

### Language Register: {lesson['language_register_name']}
**Description:** {LANGUAGE_REGISTERS[lesson['language_register']]['description']}

**Characteristics:**
"""
    
    for char in lesson['register_characteristics']:
        md += f"- {char}\n"
    
    md += f"""
**Example Phrases:**
"""
    
    for phrase in lesson['register_example_phrases']:
        md += f"- '{phrase}'\n"
    
    md += f"""
### Genre Theme: {lesson['genre_theme_name']}
**Description:** {GENRE_THEMES[lesson['genre_theme']]['description']}

**Tone:** {lesson['genre_tone']}  
**Scenario Twist:** {lesson['genre_scenario_twist']}

**Key Vocabulary:**
"""
    
    for word in lesson['genre_vocabulary']:
        md += f"- {word}\n"
    
    md += """
---

## 📚 Learning Objectives

"""
    
    for obj in lesson['objectives']:
        md += f"- {obj}\n"
    
    md += f"""
---

## 🎬 Warm-Up Activity

**Activity:** {lesson['warm_up']['activity']}  
**Register:** {lesson['warm_up']['register']}  
**Tone:** {lesson['warm_up']['tone']}  
**Time:** {lesson['warm_up']['time']}

**Description:** {lesson['warm_up']['description']}

**Scenario:** {lesson['warm_up']['scenario']}

---

## 🎯 Main Activities

"""
    
    for activity in lesson['main_activities']:
        md += f"""
### Activity {activity['number']}: {activity['type']}

- **Description:** {activity['description']}
- **Genre Element:** {activity['genre_element']}
- **Register Focus:** {activity['register_focus']}
- **Time:** {activity['time']}

"""
    
    md += """
---

## 💬 Discussion Questions

"""
    
    for i, question in enumerate(lesson['discussion_questions'], 1):
        md += f"{i}. {question}\n"
    
    md += """
---

## 🎭 Role-Play Scenarios

"""
    
    for i, scenario in enumerate(lesson['role_play_scenarios'], 1):
        md += f"""
### Scenario {i}: {scenario['scenario']}

**Register:** {scenario['register']}  
**Genre Twist:** {scenario['genre_twist']}  
**Tone:** {scenario['tone']}

**Roles:**
"""
        for role in scenario['roles']:
            md += f"- {role}\n"
        
        md += "\n**Vocabulary Focus:**\n"
        for vocab in scenario['vocabulary_focus']:
            md += f"- {vocab}\n"
    
    md += """
---

## 📝 Useful Expressions

"""
    
    for category, expression in lesson['useful_expressions'].items():
        md += f"- **{category.replace('_', ' ').title()}:** '{expression}'\n"
    
    md += """
---

## 🎨 Genre Vocabulary

"""
    
    for category, words in lesson['genre_vocabulary_list'].items():
        md += f"\n### {category.replace('_', ' ').title()}\n\n"
        for word in words:
            md += f"- {word}\n"
    
    md += """
---

## 👨‍🏫 Teacher Transformation Guide

"""
    
    guide = lesson['teacher_transformation_guide']
    md += f"""
**Register Guidance:** {guide['register_guidance']}

**Genre Guidance:** {guide['genre_guidance']}

**Tone:** {guide['tone']}

**Key Vocabulary:**
"""
    
    for word in guide['key_vocabulary']:
        md += f"- {word}\n"
    
    md += f"""
---

## 📊 Assessment

**Register Focus:** {lesson['assessment']['register_focus']}  
**Genre Focus:** {lesson['assessment']['genre_focus']}

**Criteria:**
"""
    
    for criterion in lesson['assessment']['criteria']:
        md += f"- {criterion}\n"
    
    md += f"""
---

## 🔬 Methodology

**Approach:** {lesson['methodology']}

**Augmentation Frameworks:**
"""
    
    for framework in lesson['augmentation_frameworks']:
        md += f"- {framework}\n"
    
    md += """
---

*This augmented lesson demonstrates the power of register and genre transformation in language teaching.*
"""
    
    return md

def generate_augmentation_index(output_dir, total_augmented):
    """Generate index of all augmentations"""
    
    readme = f"""# Augmented Lessons - Register & Genre Transformations

## 🎭 Augmentation System

This directory contains **{total_augmented} augmented lessons** created through systematic transformation across:

### 📊 Language Registers (5 levels)

1. **Slang/Street** - Casual street language, youth speak
2. **Informal/Conversational** - Friendly everyday speech
3. **Neutral/Standard** - Professional standard communication
4. **Formal/Business** - Business-appropriate language
5. **Expert/Academic** - Scholarly, technical discourse

### 🎬 Genre Themes (12 types)

1. **Romance** - Love, relationships, emotional connections
2. **Drama** - Intense emotions, conflicts, life challenges
3. **Horror** - Fear, suspense, supernatural elements
4. **Action/Adventure** - High energy, excitement, challenges
5. **Comedy** - Humor, wit, funny situations
6. **Mystery/Detective** - Investigation, puzzles, problem-solving
7. **Science Fiction** - Futuristic, technology, innovation
8. **Fantasy** - Magic, mythical creatures, imaginary worlds
9. **Thriller/Suspense** - Tension, danger, psychological intensity
10. **Historical** - Past eras, historical events
11. **Business/Corporate** - Professional workplace scenarios
12. **Sports/Competition** - Athletic challenges, teamwork

## 🔢 Augmentation Mathematics

- **Base Lessons:** 3,608
- **Registers:** 5
- **Genres:** 12
- **Possible Combinations:** 5 × 12 = 60 per lesson
- **Total Potential:** 3,608 × 60 = **216,480 augmented lessons**

## 📂 Directory Structure

```
lessons/
├── B1/
│   └── augmented/
│       ├── slang/
│       │   ├── romance/
│       │   ├── drama/
│       │   ├── horror/
│       │   └── ... (all 12 genres)
│       ├── informal/
│       ├── neutral/
│       ├── formal/
│       └── expert/
├── B2/
│   └── augmented/
└── C1/
    └── augmented/
```

## 🎯 Use Cases

### For Teachers
- Adapt lessons to student preferences
- Match content to classroom context
- Engage different learning personalities
- Create variety in curriculum

### For Students
- Learn language in preferred contexts
- Practice register appropriateness
- Develop genre literacy
- Enhance creative language use

### For Curriculum Designers
- Massive content library
- Systematic differentiation
- Context-appropriate materials
- Scalable lesson generation

## 🚀 One-Click Transformation

Each lesson can be instantly transformed:
- **Click Register Button** → Change language formality
- **Click Genre Button** → Change thematic context
- **Combine Both** → Create unique variations

## 📖 Pedagogical Foundation

**Register Theory** - Understanding sociolinguistic appropriateness  
**Genre-Based Pedagogy** - Learning through narrative contexts  
**Content Transformation** - Systematic material adaptation  
**Narrative Language Teaching** - Story-based language acquisition

---

*Powered by the Mega Augmentation System - Infinite lesson possibilities*
"""
    
    readme_path = output_dir / "AUGMENTATION_README.md"
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(readme)
    
    print(f"📄 Augmentation index created: {readme_path}")

def main():
    """Main augmentation function"""
    
    print("=" * 80)
    print("🎭 MEGA LESSON AUGMENTATION SYSTEM")
    print("=" * 80)
    print("Transform lessons across Language Registers × Genre Themes")
    print()
    
    lessons_dir = Path("/home/ubuntu/Prize2Pride-English-A1/lessons")
    output_dir = lessons_dir
    
    # Find original lessons (non-augmented)
    print("🔍 Finding original lessons...")
    original_lessons = []
    
    for json_file in lessons_dir.rglob("*.json"):
        # Skip already augmented lessons
        if "augmented" in str(json_file):
            continue
        
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                lesson = json.load(f)
                original_lessons.append(lesson)
        except:
            continue
    
    print(f"   Found {len(original_lessons)} original lessons")
    print()
    
    # Generate sample augmentations (not all 216k!)
    # Let's create 10 augmentations per register/genre combination as demonstration
    print("🎨 Generating augmented lessons...")
    print("   (Creating sample set: 5 registers × 12 genres = 60 variations)")
    print()
    
    total_augmented = 0
    sample_size = min(10, len(original_lessons))  # Use first 10 lessons as samples
    
    for lesson in original_lessons[:sample_size]:
        for register in LANGUAGE_REGISTERS.keys():
            for genre in GENRE_THEMES.keys():
                augmented = augment_lesson_content(lesson, register, genre)
                json_path, md_path = save_augmented_lesson(augmented, output_dir)
                total_augmented += 1
                
                if total_augmented % 100 == 0:
                    print(f"   ✓ Generated {total_augmented} augmented lessons...")
    
    print(f"\n✅ Generated {total_augmented} augmented lessons!")
    print(f"   ({sample_size} base lessons × 5 registers × 12 genres)")
    print()
    
    # Generate index
    generate_augmentation_index(output_dir, total_augmented)
    
    print()
    print("=" * 80)
    print("🎉 AUGMENTATION COMPLETE!")
    print("=" * 80)
    print(f"Total Augmented Lessons: {total_augmented}")
    print(f"Potential Full Augmentation: {len(original_lessons)} × 60 = {len(original_lessons) * 60:,}")
    print("=" * 80)

if __name__ == "__main__":
    main()
