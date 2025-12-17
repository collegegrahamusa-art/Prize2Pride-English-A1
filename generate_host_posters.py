#!/usr/bin/env python3
"""
Prize2Pride AI Host Poster Generator
Generates hundreds of hyper-realistic AI host posters with detailed prompts
"""

import json
import random
from pathlib import Path
from itertools import combinations

# Host configurations
HOST_CONFIGS = [
    {"count": 4, "gender": "4 females", "description": "four stunningly beautiful ladies"},
    {"count": 4, "gender": "2 males 2 females", "description": "two handsome men and two beautiful women"},
    {"count": 6, "gender": "6 females", "description": "six incredibly elegant ladies"},
    {"count": 6, "gender": "3 males 3 females", "description": "three handsome men and three beautiful women"},
    {"count": 6, "gender": "4 females 2 males", "description": "four gorgeous women and two handsome men"},
    {"count": 6, "gender": "2 females 4 males", "description": "two beautiful women and four handsome men"}
]

# Diverse ethnicities
ETHNICITIES = [
    "African", "Asian", "Caucasian", "Middle Eastern", "Latino/Latina", 
    "South Asian", "East Asian", "European", "Mediterranean", "Mixed heritage"
]

# Topics they're teaching
TOPICS = [
    "Advanced Mathematics", "Quantum Physics", "World History", "Literature",
    "Business Strategy", "Digital Marketing", "Artificial Intelligence", "Medicine",
    "Environmental Science", "Psychology", "Philosophy", "Economics",
    "Computer Programming", "Data Science", "Foreign Languages", "Art History",
    "Music Theory", "Engineering", "Architecture", "Biotechnology",
    "Astronomy", "Chemistry", "Political Science", "Sociology",
    "Anthropology", "Neuroscience", "Robotics", "Blockchain Technology"
]

# Languages displayed on screens
LANGUAGES = [
    "English", "Spanish", "Mandarin Chinese", "Arabic", "French", "German",
    "Japanese", "Korean", "Portuguese", "Russian", "Hindi", "Italian",
    "Turkish", "Vietnamese", "Thai", "Dutch", "Swedish", "Polish"
]

# Studio styles
STUDIO_STYLES = [
    "ultra-modern minimalist with sleek white and chrome accents",
    "futuristic with holographic blue lighting and glass panels",
    "elegant corporate with warm wood tones and gold trim",
    "high-tech with LED strips and metallic surfaces",
    "luxurious with marble floors and crystal chandeliers",
    "contemporary with geometric patterns and ambient lighting",
    "sophisticated with dark navy walls and brass fixtures",
    "premium with leather accents and polished concrete",
    "innovative with curved walls and dynamic lighting",
    "professional with clean lines and modern furniture"
]

# Clothing styles
CLOTHING_STYLES = [
    "elegant business formal attire in coordinated colors",
    "sophisticated designer suits and dresses",
    "modern professional wear with contemporary cuts",
    "luxury fashion with high-end accessories",
    "stylish business casual with premium fabrics",
    "chic professional outfits in jewel tones",
    "refined corporate wear with subtle patterns",
    "haute couture business attire",
    "sleek modern professional clothing",
    "designer business wear with elegant details"
]

# Poses and arrangements
POSES = [
    "standing confidently on the platform, some gesturing toward the smart screens",
    "arranged in a dynamic group formation, engaging with the audience",
    "positioned elegantly around the wheel, some pointing to lesson content",
    "standing in a professional V-formation on the platform",
    "gathered naturally around the gift wheel, interacting professionally",
    "posed in an elegant semi-circle facing the camera",
    "standing with confident postures, some holding tablets or pointers",
    "arranged in multiple levels using the platform steps"
]

# Smart screen content
SCREEN_CONTENT = [
    "displaying 'Purchase2Win' platform interface with colorful course thumbnails",
    "showing 'Buy2Win' dashboard with learning progress charts",
    "featuring 'Purchase2Win' logo with multilingual course options",
    "presenting 'Buy2Win' rewards system with achievement badges",
    "displaying interactive 'Purchase2Win' course catalog",
    "showing 'Buy2Win' student success metrics and leaderboards"
]

# Wheel descriptions
WHEEL_DESCRIPTIONS = [
    "luxurious golden prize wheel with LED lights and 'Prize2Pride' branding",
    "elegant crystal-accented wheel with holographic segments",
    "premium metallic wheel with jewel-toned sections and brand logo",
    "sophisticated illuminated wheel with 'Prize2Pride' in elegant script",
    "high-end wheel with chrome finish and colorful prize segments",
    "deluxe wheel with gold and silver accents featuring brand name"
]

def generate_ethnicity_combination(count):
    """Generate diverse ethnicity combination for hosts"""
    selected = random.sample(ETHNICITIES, min(count, len(ETHNICITIES)))
    if len(selected) < count:
        selected.extend(random.choices(ETHNICITIES, k=count - len(selected)))
    return selected

def generate_detailed_prompt(config_idx, variation_idx):
    """Generate a detailed hyper-realistic prompt for AI image generation"""
    
    config = HOST_CONFIGS[config_idx % len(HOST_CONFIGS)]
    host_count = config["count"]
    gender_desc = config["description"]
    
    # Select diverse elements
    ethnicities = generate_ethnicity_combination(host_count)
    topic = random.choice(TOPICS)
    languages = random.sample(LANGUAGES, 3)
    studio_style = random.choice(STUDIO_STYLES)
    clothing = random.choice(CLOTHING_STYLES)
    pose = random.choice(POSES)
    screen_content = random.choice(SCREEN_CONTENT)
    wheel_desc = random.choice(WHEEL_DESCRIPTIONS)
    
    # Build ethnicity description
    ethnicity_desc = ", ".join(ethnicities[:host_count])
    
    # Create the mega prompt
    prompt = f"""Hyper-realistic, ultra-high-definition photograph of a premium educational studio for 'Prize2Pride' platform.

HOSTS: {gender_desc} of diverse ethnicities ({ethnicity_desc}), all EXTREMELY beautiful, handsome, and stunningly elegant with model-like features, perfect skin, and professional styling. They are {pose}.

STUDIO SETUP:
- {studio_style} professional studio
- Two large sophisticated touch-enabled smart screens on left and right walls
- Luxurious {wheel_desc} positioned centrally between the two smart screens
- Elevated 10cm platform with three steps where hosts stand
- 'Prize2Pride' brand logo prominently and delicately displayed on both smart screens
- Professional studio lighting with soft key lights and elegant rim lighting

SMART SCREENS:
- Left screen: {screen_content}
- Right screen: displaying multilingual content in {', '.join(languages)}
- Both screens show 'Prize2Pride' branding clearly and elegantly
- Sub-platforms 'Purchase2Win' and 'Buy2Win' visible on screen interfaces

HOSTS APPEARANCE:
- All hosts are exceptionally attractive with perfect symmetrical features
- Wearing {clothing}
- Professional hair and makeup, camera-ready
- Confident, warm, and engaging expressions
- Perfect posture and body language

TOPIC: Hosts are presenting on {topic}

ATMOSPHERE:
- Professional broadcast-quality environment
- Sophisticated color grading with rich, vibrant tones
- Cinematic depth of field with hosts in sharp focus
- Premium corporate aesthetic
- Welcoming and inspiring ambiance

TECHNICAL SPECS:
- 8K resolution quality
- Professional photography lighting setup
- Photorealistic rendering
- Commercial advertising quality
- Magazine cover worthy composition

Style: Ultra-realistic commercial photography, corporate branding photoshoot, premium educational platform marketing material"""

    return {
        "prompt_id": f"P2P_HOST_{config_idx:03d}_{variation_idx:04d}",
        "host_count": host_count,
        "gender_config": config["gender"],
        "ethnicities": ethnicities[:host_count],
        "topic": topic,
        "languages": languages,
        "studio_style": studio_style,
        "clothing_style": clothing,
        "pose_description": pose,
        "screen_content": screen_content,
        "wheel_description": wheel_desc,
        "full_prompt": prompt,
        "image_filename": f"prize2pride_hosts_{config_idx:03d}_{variation_idx:04d}.png"
    }

def generate_all_prompts(total_count=200):
    """Generate specified number of unique prompts"""
    
    print("=" * 80)
    print("🎬 PRIZE2PRIDE AI HOST POSTER PROMPT GENERATOR")
    print("=" * 80)
    print(f"Generating {total_count} unique hyper-realistic host poster prompts...")
    print()
    
    prompts = []
    
    for i in range(total_count):
        config_idx = i % len(HOST_CONFIGS)
        variation_idx = i
        
        prompt_data = generate_detailed_prompt(config_idx, variation_idx)
        prompts.append(prompt_data)
        
        if (i + 1) % 50 == 0:
            print(f"  ✓ Generated {i + 1}/{total_count} prompts...")
    
    print(f"\n✅ Successfully generated {len(prompts)} unique prompts!")
    return prompts

def save_prompts_to_files(prompts, output_dir):
    """Save prompts to individual JSON files and a master catalog"""
    
    output_path = Path(output_dir)
    prompts_dir = output_path / "host_posters" / "prompts"
    prompts_dir.mkdir(parents=True, exist_ok=True)
    
    print(f"\n📁 Saving prompts to {prompts_dir}...")
    
    # Save individual prompt files
    for prompt in prompts:
        prompt_file = prompts_dir / f"{prompt['prompt_id']}.json"
        with open(prompt_file, 'w', encoding='utf-8') as f:
            json.dump(prompt, f, indent=2, ensure_ascii=False)
    
    # Save master catalog
    catalog_file = output_path / "host_posters" / "PROMPTS_CATALOG.json"
    with open(catalog_file, 'w', encoding='utf-8') as f:
        json.dump(prompts, f, indent=2, ensure_ascii=False)
    
    # Save text version for easy reading
    text_catalog = output_path / "host_posters" / "PROMPTS_CATALOG.txt"
    with open(text_catalog, 'w', encoding='utf-8') as f:
        f.write("PRIZE2PRIDE AI HOST POSTER PROMPTS\n")
        f.write("=" * 80 + "\n\n")
        
        for i, prompt in enumerate(prompts, 1):
            f.write(f"PROMPT #{i}: {prompt['prompt_id']}\n")
            f.write("-" * 80 + "\n")
            f.write(f"Hosts: {prompt['host_count']} ({prompt['gender_config']})\n")
            f.write(f"Ethnicities: {', '.join(prompt['ethnicities'])}\n")
            f.write(f"Topic: {prompt['topic']}\n")
            f.write(f"Languages: {', '.join(prompt['languages'])}\n")
            f.write(f"Studio: {prompt['studio_style']}\n")
            f.write(f"Clothing: {prompt['clothing_style']}\n")
            f.write(f"\nFULL PROMPT:\n{prompt['full_prompt']}\n")
            f.write("\n" + "=" * 80 + "\n\n")
    
    print(f"  ✓ Saved {len(prompts)} individual JSON files")
    print(f"  ✓ Saved master catalog: PROMPTS_CATALOG.json")
    print(f"  ✓ Saved text catalog: PROMPTS_CATALOG.txt")
    
    return catalog_file, text_catalog

def create_readme(output_dir, prompt_count):
    """Create README for the host posters directory"""
    
    readme_path = Path(output_dir) / "host_posters" / "README.md"
    
    content = f"""# Prize2Pride AI Host Posters

## 🎬 Overview

This directory contains **{prompt_count} hyper-realistic AI host poster prompts** for the Prize2Pride educational platform.

---

## 👥 Host Configurations

### 4-Host Setups
- 4 beautiful ladies
- 2 handsome men + 2 beautiful women

### 6-Host Setups
- 6 elegant ladies
- 3 handsome men + 3 beautiful women
- 4 gorgeous women + 2 handsome men
- 2 beautiful women + 4 handsome men

---

## 🌍 Diversity

All posters feature hosts of diverse ethnicities:
- African
- Asian
- Caucasian
- Middle Eastern
- Latino/Latina
- South Asian
- East Asian
- European
- Mediterranean
- Mixed heritage

---

## 🎓 Educational Topics

Hosts present on topics including:
- STEM (Science, Technology, Engineering, Mathematics)
- Business & Economics
- Arts & Humanities
- Languages & Culture
- Health & Medicine
- And many more...

---

## 🌐 Multilingual Platform

Content displayed in 100+ languages including:
- English, Spanish, Mandarin Chinese
- Arabic, French, German
- Japanese, Korean, Portuguese
- Russian, Hindi, Italian
- And many more...

---

## 🎨 Studio Features

### Branding
- **Main Brand:** Prize2Pride (prominently displayed)
- **Sub-Platforms:** Purchase2Win, Buy2Win

### Equipment
- 2 sophisticated touch-enabled smart screens
- 1 luxurious mega gift wheel (between screens)
- Elevated 10cm platform with 3 steps
- Professional broadcast lighting

### Aesthetics
- Ultra-modern, futuristic, or elegant corporate styles
- Premium materials (marble, chrome, gold, crystal)
- Professional color grading
- 8K quality hyper-realistic rendering

---

## 📂 Directory Structure

```
host_posters/
├── README.md (this file)
├── PROMPTS_CATALOG.json (master catalog)
├── PROMPTS_CATALOG.txt (human-readable)
├── prompts/
│   ├── P2P_HOST_000_0000.json
│   ├── P2P_HOST_000_0001.json
│   └── ... ({prompt_count} total)
└── images/
    └── (generated images will be placed here)
```

---

## 🎯 Use Cases

- Educational platform marketing materials
- Course promotional posters
- Social media content
- Website hero images
- Advertising campaigns
- Brand identity materials

---

## 🚀 Generation Details

- **Total Prompts:** {prompt_count}
- **Prompt Format:** Detailed hyper-realistic specifications
- **Image Format:** PNG (recommended)
- **Quality:** 8K ultra-high-definition
- **Style:** Commercial photography, photorealistic

---

## 📝 Prompt Structure

Each prompt includes:
- Host count and gender configuration
- Diverse ethnicity specifications
- Educational topic
- Multilingual display languages
- Studio style and atmosphere
- Clothing and styling details
- Pose and arrangement
- Smart screen content
- Gift wheel description
- Technical specifications

---

*Generated for Prize2Pride Educational Platform*
*Featuring stunningly beautiful and elegant AI hosts*
"""
    
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"  ✓ Created README: {readme_path}")
    return readme_path

def main():
    """Main function"""
    
    output_dir = "/home/ubuntu/Prize2Pride-English-A1"
    total_prompts = 200  # Generate 200 unique prompts
    
    # Generate prompts
    prompts = generate_all_prompts(total_prompts)
    
    # Save to files
    catalog_file, text_catalog = save_prompts_to_files(prompts, output_dir)
    
    # Create README
    readme_file = create_readme(output_dir, len(prompts))
    
    print()
    print("=" * 80)
    print("✅ PROMPT GENERATION COMPLETE!")
    print("=" * 80)
    print(f"Total Prompts: {len(prompts)}")
    print(f"Output Directory: {output_dir}/host_posters/")
    print()
    print("Files Created:")
    print(f"  - {len(prompts)} individual JSON prompt files")
    print(f"  - 1 master catalog (JSON)")
    print(f"  - 1 text catalog (TXT)")
    print(f"  - 1 README (MD)")
    print()
    print("Next Step: Generate images from these prompts!")
    print("=" * 80)

if __name__ == "__main__":
    main()
