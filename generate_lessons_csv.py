#!/usr/bin/env python3
"""
Lesson CSV Generator
Parses all JSON lesson files and creates a comprehensive CSV summary
"""

import json
import csv
from pathlib import Path
from datetime import datetime

def parse_all_lessons(lessons_dir):
    """Parse all JSON lesson files and extract key information"""
    
    lessons_data = []
    
    # Find all JSON files
    json_files = list(Path(lessons_dir).rglob("*.json"))
    
    print(f"Found {len(json_files)} JSON lesson files")
    print("Parsing lessons...")
    
    for i, json_file in enumerate(json_files, 1):
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                lesson = json.load(f)
            
            # Extract key information
            lesson_data = {
                'lesson_id': lesson.get('lesson_id', ''),
                'level': lesson.get('level', ''),
                'level_name': lesson.get('level_name', ''),
                'category': lesson.get('category', ''),
                'topic': lesson.get('topic', ''),
                'learning_style': lesson.get('learning_style', ''),
                'learning_style_name': lesson.get('learning_style_name', ''),
                'cognitive_level': lesson.get('cognitive_level', ''),
                'cognitive_level_name': lesson.get('cognitive_level_name', ''),
                'duration': lesson.get('duration', ''),
                'methodology': lesson.get('methodology', ''),
                
                # Frameworks
                'frameworks': ', '.join(lesson.get('frameworks', [])),
                
                # Objectives count
                'objectives_count': len(lesson.get('objectives', [])),
                
                # Activities count
                'main_activities_count': len(lesson.get('main_activities', [])),
                
                # Discussion prompts count
                'discussion_prompts_count': len(lesson.get('discussion_prompts', [])),
                
                # UDL principles
                'udl_representation': ', '.join(lesson.get('udl_principles', {}).get('representation', [])),
                'udl_action_expression': ', '.join(lesson.get('udl_principles', {}).get('action_expression', [])),
                'udl_engagement': ', '.join(lesson.get('udl_principles', {}).get('engagement', [])),
                
                # Multiple Intelligences
                'mi_linguistic': lesson.get('multiple_intelligences', {}).get('linguistic', ''),
                'mi_logical_mathematical': lesson.get('multiple_intelligences', {}).get('logical_mathematical', ''),
                'mi_spatial': lesson.get('multiple_intelligences', {}).get('spatial', ''),
                'mi_bodily_kinesthetic': lesson.get('multiple_intelligences', {}).get('bodily_kinesthetic', ''),
                'mi_musical': lesson.get('multiple_intelligences', {}).get('musical', ''),
                'mi_interpersonal': lesson.get('multiple_intelligences', {}).get('interpersonal', ''),
                'mi_intrapersonal': lesson.get('multiple_intelligences', {}).get('intrapersonal', ''),
                'mi_naturalistic': lesson.get('multiple_intelligences', {}).get('naturalistic', ''),
                
                # Differentiation
                'diff_content': str(lesson.get('differentiation', {}).get('content', '')),
                'diff_process_grouping': lesson.get('differentiation', {}).get('process', {}).get('grouping', ''),
                'diff_process_pacing': lesson.get('differentiation', {}).get('process', {}).get('pacing', ''),
                'diff_product': ', '.join(lesson.get('differentiation', {}).get('product', [])),
                'diff_environment': lesson.get('differentiation', {}).get('environment', ''),
                
                # Support materials
                'scaffolding_count': len(lesson.get('scaffolding', [])),
                'extension_count': len(lesson.get('extension_challenges', [])),
                'materials_count': len(lesson.get('materials_needed', [])),
                'tech_tools_count': len(lesson.get('technology_integration', [])),
                
                # Grammar and vocabulary
                'grammar_focus': ', '.join(lesson.get('grammar_focus', [])),
                'vocabulary_tiers': ', '.join([f"{k}: {v}" for k, v in lesson.get('vocabulary_support', {}).items()]),
                
                # File path
                'file_path': str(json_file.relative_to(lessons_dir))
            }
            
            lessons_data.append(lesson_data)
            
            if i % 500 == 0:
                print(f"  Processed {i}/{len(json_files)} lessons...")
        
        except Exception as e:
            print(f"  Error parsing {json_file}: {e}")
            continue
    
    print(f"Successfully parsed {len(lessons_data)} lessons")
    return lessons_data

def generate_csv(lessons_data, output_file):
    """Generate CSV file from lessons data"""
    
    if not lessons_data:
        print("No lessons data to write!")
        return
    
    # Define CSV columns
    fieldnames = [
        'lesson_id',
        'level',
        'level_name',
        'category',
        'topic',
        'learning_style',
        'learning_style_name',
        'cognitive_level',
        'cognitive_level_name',
        'duration',
        'methodology',
        'frameworks',
        'objectives_count',
        'main_activities_count',
        'discussion_prompts_count',
        'udl_representation',
        'udl_action_expression',
        'udl_engagement',
        'mi_linguistic',
        'mi_logical_mathematical',
        'mi_spatial',
        'mi_bodily_kinesthetic',
        'mi_musical',
        'mi_interpersonal',
        'mi_intrapersonal',
        'mi_naturalistic',
        'diff_content',
        'diff_process_grouping',
        'diff_process_pacing',
        'diff_product',
        'diff_environment',
        'scaffolding_count',
        'extension_count',
        'materials_count',
        'tech_tools_count',
        'grammar_focus',
        'vocabulary_tiers',
        'file_path'
    ]
    
    # Write CSV
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(lessons_data)
    
    print(f"\n✅ CSV file created: {output_file}")
    print(f"   Total rows: {len(lessons_data)}")
    print(f"   Total columns: {len(fieldnames)}")

def generate_summary_stats(lessons_data, output_file):
    """Generate summary statistics file"""
    
    stats = {
        'total_lessons': len(lessons_data),
        'by_level': {},
        'by_learning_style': {},
        'by_cognitive_level': {},
        'by_category': {}
    }
    
    for lesson in lessons_data:
        # Count by level
        level = lesson['level']
        stats['by_level'][level] = stats['by_level'].get(level, 0) + 1
        
        # Count by learning style
        style = lesson['learning_style']
        stats['by_learning_style'][style] = stats['by_learning_style'].get(style, 0) + 1
        
        # Count by cognitive level
        cog = lesson['cognitive_level']
        stats['by_cognitive_level'][cog] = stats['by_cognitive_level'].get(cog, 0) + 1
        
        # Count by category
        cat = lesson['category']
        stats['by_category'][cat] = stats['by_category'].get(cat, 0) + 1
    
    # Write summary
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("# Lessons Summary Statistics\n\n")
        f.write(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write(f"**Total Lessons:** {stats['total_lessons']}\n\n")
        
        f.write("## By CEFR Level\n\n")
        for level, count in sorted(stats['by_level'].items()):
            f.write(f"- **{level}:** {count} lessons\n")
        
        f.write("\n## By Learning Style\n\n")
        for style, count in sorted(stats['by_learning_style'].items()):
            f.write(f"- **{style}:** {count} lessons\n")
        
        f.write("\n## By Cognitive Level\n\n")
        for cog, count in sorted(stats['by_cognitive_level'].items()):
            f.write(f"- **{cog}:** {count} lessons\n")
        
        f.write("\n## By Category\n\n")
        for cat, count in sorted(stats['by_category'].items()):
            f.write(f"- **{cat}:** {count} lessons\n")
        
        f.write("\n---\n\n")
        f.write("*This summary was automatically generated from all lesson JSON files.*\n")
    
    print(f"✅ Summary statistics created: {output_file}")

def main():
    """Main function"""
    
    print("=" * 70)
    print("📊 ESL Lessons CSV Generator")
    print("=" * 70)
    print()
    
    lessons_dir = Path("/home/ubuntu/Prize2Pride-English-A1/lessons")
    output_csv = Path("/home/ubuntu/Prize2Pride-English-A1/LESSONS_SUMMARY.csv")
    output_stats = Path("/home/ubuntu/Prize2Pride-English-A1/LESSONS_STATISTICS.md")
    
    # Parse all lessons
    lessons_data = parse_all_lessons(lessons_dir)
    
    # Generate CSV
    generate_csv(lessons_data, output_csv)
    
    # Generate summary statistics
    generate_summary_stats(lessons_data, output_stats)
    
    print()
    print("=" * 70)
    print("✅ All files generated successfully!")
    print("=" * 70)

if __name__ == "__main__":
    main()
