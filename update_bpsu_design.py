#!/usr/bin/env python3
import os
import re

files_to_update = [
    'schools/bpsu/bpsu-abucay.html',
    'schools/bpsu/bpsu-bagac.html',
    'schools/bpsu/bpsu-balanga.html',
    'schools/bpsu/bpsu-dinalupihan.html',
    'schools/bpsu/bpsu.html'
]

replacements = [
    (r'background: #f5f5f5;', 'background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);\\n    min-height: 100vh;'),
    (r'padding: 1rem 5%;\\s+background: white;\\s+box-shadow: 0 2px 10px rgba\(0,0,0,0.1\);\\s+position: relative;',
     'padding: 1.5rem 5%;\\n    background: rgba(255, 255, 255, 0.95);\\n    backdrop-filter: blur(10px);\\n    box-shadow: 0 4px 30px rgba(0,0,0,0.1);\\n    position: sticky;\\n    top: 0;\\n    z-index: 1000;'),
    (r'color: #2542ff;', 'color: #667eea;'),
]

for file_path in files_to_update:
    full_path = os.path.join('c:\\Users\\YUKI\\Documents\\Bataan-Campus-Finder', file_path)
    if os.path.exists(full_path):
        print(f"Processing {file_path}...")
        with open(full_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Apply replacements
        for old, new in replacements:
            content = re.sub(old, new, content)
        
        with open(full_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✓ Updated {file_path}")
    else:
        print(f"✗ File not found: {full_path}")

print("Done!")
