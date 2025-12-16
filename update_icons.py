#!/usr/bin/env python3
# -*- coding: utf-8 -*-

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace tech icons - first occurrence (HTML)
content = content.replace(
    '<div class="tech-icon">️</div>',
    '<img src="htmlicon.png" alt="HTML5" class="tech-icon-img" />'
)

# Replace CSS icon
content = content.replace(
    '<div class="tech-icon">🖌️</div>',
    '<img src="cssicon.png" alt="CSS3" class="tech-icon-img" />'
)

# Replace JavaScript icon
content = content.replace(
    '<div class="tech-icon">⚡</div>',
    '<img src="javascripticon.png" alt="JavaScript" class="tech-icon-img" />'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('✓ Icon replacement completed!')
