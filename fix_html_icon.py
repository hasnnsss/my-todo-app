#!/usr/bin/env python3
# -*- coding: utf-8 -*-

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find and replace the corrupted HTML icon - more flexible approach
import re

# Replace any remaining emoji-like patterns in tech-icon divs
pattern = r'<div class="tech-icon">[^<]*?</div>'

def replace_icon(match):
    original = match.group(0)
    if 'HTML' in content[max(0, match.start()-100):match.end()+100]:
        return '<img src="htmlicon.png" alt="HTML5" class="tech-icon-img" />'
    return original

# Use a more aggressive approach - find the pattern and replace all tech-icon divs
lines = content.split('\n')
new_lines = []
icon_count = 0

for i, line in enumerate(lines):
    if '<div class="tech-icon">' in line:
        # Check the next few lines to determine which tech this is
        context = '\n'.join(lines[max(0, i-5):min(len(lines), i+5)])
        
        if 'HTML5' in context and icon_count == 0:
            new_lines.append(line.replace(
                re.search(r'<div class="tech-icon">[^<]*?</div>', line).group(0),
                '<img src="htmlicon.png" alt="HTML5" class="tech-icon-img" />'
            ) if '<div class="tech-icon">' in line else line)
            icon_count += 1
        elif 'CSS3' in context and icon_count == 1:
            new_lines.append(line.replace(
                re.search(r'<div class="tech-icon">[^<]*?</div>', line).group(0),
                '<img src="cssicon.png" alt="CSS3" class="tech-icon-img" />'
            ) if '<div class="tech-icon">' in line else line)
            icon_count += 1
        elif 'JavaScript' in context and icon_count == 2:
            new_lines.append(line.replace(
                re.search(r'<div class="tech-icon">[^<]*?</div>', line).group(0),
                '<img src="javascripticon.png" alt="JavaScript" class="tech-icon-img" />'
            ) if '<div class="tech-icon">' in line else line)
            icon_count += 1
        else:
            new_lines.append(line)
    else:
        new_lines.append(line)

content = '\n'.join(new_lines)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('✓ All icons replacement completed!')
