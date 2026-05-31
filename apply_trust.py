import os

def process_file(filepath, insert_marker):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    start_str = "    <!-- Global Trust-Building Sections -->"
    end_str = "    <!-- End Global Trust-Building Sections -->\n"
    
    start_idx = content.find(start_str)
    if start_idx != -1:
        end_idx = content.find(end_str) + len(end_str)
        # Remove the block if it exists
        content = content[:start_idx] + content[end_idx:]
    else:
        print(f"Warning: Trust block not found in {filepath} to remove.")

    with open('trust_block.html', 'r', encoding='utf-8') as f:
        trust_block = f.read()

    insert_idx = content.find(insert_marker)
    if insert_idx != -1:
        # Insert before the marker
        content = content[:insert_idx] + trust_block + "\n" + content[insert_idx:]
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filepath}")
    else:
        print(f"Error: insert marker '{insert_marker}' not found in {filepath}")

# Update main files
process_file('index.html', '    <!-- Global CTA -->')
process_file('about.html', '    <!-- Global CTA -->')
process_file('services.html', '    <!-- Global CTA -->')
process_file('contact.html', '    <!-- Contact Page Specific FAQs -->')
