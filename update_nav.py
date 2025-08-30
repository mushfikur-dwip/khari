#!/usr/bin/env python3
import os
import re

# HTML files to update
html_files = [
    'history.html',
    'student-info.html', 
    'vacant-posts.html',
    'holidays.html',
    'class-routine.html'
]

# Updated links dropdown HTML
new_links_section = '''          <li class="dropdown relative">
            <a href="#" class="text-white hover:text-yellow-300 transition-colors flex items-center"
              onclick="toggleDropdown('links-dropdown')">
              গুরুত্বপূর্ণ লিংক <i class="fas fa-chevron-down ml-1 text-xs"></i>
            </a>
            <ul id="links-dropdown"
              class="dropdown-menu absolute top-full left-0 bg-white shadow-lg rounded-md py-2 w-48 hidden z-50">
              <li><a href="https://bise-ctg.portal.gov.bd/" target="_blank" class="block px-4 py-2 text-gray-800 hover:bg-blue-50">চট্টগ্রাম শিক্ষা বোর্ড</a></li>
              <li><a href="https://dshe.gov.bd/" target="_blank" class="block px-4 py-2 text-gray-800 hover:bg-blue-50">শিক্ষা অধিদপ্তর</a></li>
              <li><a href="https://shed.gov.bd/" target="_blank" class="block px-4 py-2 text-gray-800 hover:bg-blue-50">শিক্ষা মন্ত্রণালয়</a></li>
              <li><a href="https://nctb.portal.gov.bd/site/page/52ce556f-6fbe-429a-8211-2704050f115e" target="_blank" class="block px-4 py-2 text-gray-800 hover:bg-blue-50">এনসিটিবি</a></li>
            </ul>
          </li>
          <li><a href="contact.html" class="text-white hover:text-yellow-300 transition-colors">যোগাযোগ</a></li>'''

for file_name in html_files:
    if os.path.exists(file_name):
        print(f"Processing {file_name}...")
        
        with open(file_name, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Remove managing committee dropdown and replace with updated links
        pattern = r'<li class="dropdown relative">\s*<a href="#"[^>]*toggleDropdown\(\'committee-dropdown\'\)[^>]*>\s*ম্যানেজিং কমিটি[^<]*</a>\s*<ul id="committee-dropdown"[^>]*>.*?</ul>\s*</li>\s*<li class="dropdown relative">\s*<a href="#"[^>]*toggleDropdown\(\'links-dropdown\'\)[^>]*>\s*গুরুত্বপূর্ণ লিংক[^<]*</a>\s*<ul id="links-dropdown"[^>]*>.*?</ul>\s*</li>\s*<li><a href="[^"]*"[^>]*>যোগাযোগ</a></li>'
        
        # Use a more targeted approach for each file
        if 'ম্যানেজিং কমিটি' in content:
            # Find and replace the managing committee section
            lines = content.split('\n')
            new_lines = []
            skip_until_end_managing = False
            skip_until_contact = False
            
            i = 0
            while i < len(lines):
                line = lines[i]
                
                if 'ম্যানেজিং কমিটি' in line and 'dropdown' in line:
                    # Skip managing committee dropdown entirely
                    skip_until_end_managing = True
                    i += 1
                    continue
                    
                if skip_until_end_managing:
                    if '</li>' in line and 'dropdown relative' not in lines[i+1] if i+1 < len(lines) else True:
                        skip_until_end_managing = False
                    i += 1
                    continue
                
                if 'গুরুত্বপূর্ণ লিংক' in line and 'dropdown' in line:
                    # Replace links section
                    new_lines.append(new_links_section)
                    skip_until_contact = True
                    i += 1
                    continue
                    
                if skip_until_contact:
                    if 'যোগাযোগ</a></li>' in line:
                        skip_until_contact = False
                    i += 1
                    continue
                
                new_lines.append(line)
                i += 1
            
            # Write back to file
            with open(file_name, 'w', encoding='utf-8') as f:
                f.write('\n'.join(new_lines))
            
            print(f"✓ Updated {file_name}")
        else:
            print(f"- No managing committee found in {file_name}")
    else:
        print(f"✗ File {file_name} not found")

print("Navigation update completed!")
