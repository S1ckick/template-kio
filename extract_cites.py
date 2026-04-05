#!/usr/bin/env python3
import re
import sys
import os

def extract_citation_keys(input_file):
    """Extract unique citation keys from \cite{...} commands."""
    if not os.path.exists(input_file):
        sys.exit(f"Error: File '{input_file}' not found.")
        
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Matches \cite, \cite*, \cite[...], etc. Captures only the content inside {}
    pattern = r'\\cite\*?(?:\[[^\]]*\])?\{([^}]*)\}'
    matches = re.findall(pattern, content)
    
    seen = set()
    unique_keys = []
    for m in matches:
        # Handle comma-separated lists: \cite{key1, key2, key3}
        keys = [k.strip() for k in m.split(',')]
        for k in keys:
            if k and k not in seen:
                seen.add(k)
                unique_keys.append(k)
                
    return unique_keys

def insert_nocites(template_file, output_file, keys):
    """Insert \nocite commands after the first \begin{refsection}."""
    if not os.path.exists(template_file):
        sys.exit(f"Error: Template file '{template_file}' not found.")
        
    with open(template_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    found_refsection = False
    new_lines = []
    
    for line in lines:
        new_lines.append(line)
        if not found_refsection and re.search(r'\\begin\{refsection\}', line):
            found_refsection = True
            new_lines.append('% Auto-inserted nocites\n')
            for k in keys:
                new_lines.append(f'\\nocite{{{k}}}\n')
                
    if not found_refsection:
        print("⚠️  Warning: \\begin{refsection} not found in template file.")
        
    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: python extract_cites_to_nocites.py <source.tex> <template.tex> <output.tex>")
        sys.exit(1)
        
    source, template, output = sys.argv[1], sys.argv[2], sys.argv[3]
    
    print(f"🔍 Scanning '{source}' for \\cite keys...")
    keys = extract_citation_keys(source)
    print(f"✅ Found {len(keys)} unique citation keys.")
    
    print(f"📝 Writing \\nocite commands into '{template}' after \\begin{{refsection}}...")
    insert_nocites(template, output, keys)
    print(f"📄 Result saved to '{output}'")