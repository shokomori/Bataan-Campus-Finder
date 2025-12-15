#!/usr/bin/env python3
"""
Update all BPSU campus HTML files with modern gradient design
"""
import os
import glob

base_path = r'c:\Users\YUKI\Documents\Bataan-Campus-Finder'
bpsu_files = [
    'schools/bpsu/bpsu-abucay.html',
    'schools/bpsu/bpsu-bagac.html',
    'schools/bpsu/bpsu-balanga.html',
    'schools/bpsu/bpsu-dinalupihan.html',
    'schools/bpsu/bpsu.html'
]

# Color replacements
color_replacements = {
    '#2542ff': '#667eea',
    '#1a32cc': '#764ba2',
}

# CSS replacements (old -> new)
css_replacements = {
    'background: #f5f5f5;\n    color: #333;': 'background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);\n    color: #333;\n    min-height: 100vh;',
    'padding: 1rem 5%;\n    background: white;\n    box-shadow: 0 2px 10px rgba(0,0,0,0.1);\n    position: relative;': 'padding: 1.5rem 5%;\n    background: rgba(255, 255, 255, 0.95);\n    backdrop-filter: blur(10px);\n    box-shadow: 0 4px 30px rgba(0,0,0,0.1);\n    position: sticky;\n    top: 0;\n    z-index: 1000;',
}

for file_rel in bpsu_files:
    file_path = os.path.join(base_path, file_rel.replace('/', '\\\\'))
    if os.path.exists(file_path):
        print(f"Processing {file_rel}...")
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Apply CSS replacements
        for old, new in css_replacements.items():
            content = content.replace(old, new)
        
        # Apply color replacements (but be careful with #-patterns)
        for old_color, new_color in color_replacements.items():
            # Only replace in CSS/style context
            content = content.replace(f'color: {old_color}', f'color: {new_color}')
            content = content.replace(f'background: {old_color}', f'background: {new_color}')
            content = content.replace(f'border: 2px solid {old_color}', f'border: 2px solid {new_color}')
            content = content.replace(f'solid {old_color}', f'solid {new_color}')
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✓ Updated {file_rel}")
    else:
        print(f"✗ File not found: {file_path}")

print("\n✓ All BPSU files updated with modern design!")
