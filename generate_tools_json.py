#!/usr/bin/env python3
import os
import json
from pathlib import Path

def generate_tools_json():
    # Get the current directory
    current_dir = Path('.')
    
    # Find all HTML files
    html_files = [f.name for f in current_dir.glob('*.html')]
    
    # Write to tools.json
    with open('tools.json', 'w') as f:
        json.dump(html_files, f, indent=2)

if __name__ == '__main__':
    generate_tools_json() 