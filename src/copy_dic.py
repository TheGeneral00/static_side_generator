import os
import shutil
from functions import markdown_to_html_node, extract_title

def copy_dic(source_dir, target_dir):
    #setting up the required pathes
    root_dir = os.getcwd()
    #supporting dynamic path
    if not os.path.isabs(source_dir):
        source_dir = os.path.join(root_dir, source_dir)
    if not os.path.isabs(target_dir):
        target_dir = os.path.join(root_dir, target_dir)
    if not os.path.exists(source_dir):
        raise ValueError(f"Source path '{source_dir}' not found")

    #removing the old tree and creating the new tree to ensure its clean
    if os.path.exists(target_dir):
        shutil.rmtree(target_dir)
    os.mkdir(target_dir)
    
    #looking for contents in current directory
    items = os.listdir(source_dir)
    for item in items:
        #creating the item path
        item_path = os.path.join(source_dir, item)
        target_path = os.path.join(target_dir, item)

        #copying if item is file
        if os.path.isfile(item_path):
            print(f"Copying file: {item_path} to {target_path}")
            shutil.copy(item_path, target_path)

        #recursive call if item is directory
        else:
            #giving feedback on directories to be created
            print(f"Copying directory: {item_path} to {target_path}")
            copy_dic( item_path, target_path)

def generate_page(from_path, template_path, dest_path):
    print(f'Generating page from {from_path} to {dest_path} using {template_path}')
    
    # Read markdown and template files
    with open(from_path, 'r') as md_file:
        markdown = md_file.read()
        
    with open(template_path, 'r') as tpl_file:
        template = tpl_file.read()
        
    # Generate HTML
    HTML_string = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)
    
    # Replace placeholders in the template
    template = template.replace('{{ Title }}', title)
    template = template.replace('{{ Content }}', HTML_string)
    
    # Ensure the destination directory exists
    directory = os.path.dirname(dest_path)
    if not os.path.exists(directory):
        os.makedirs(directory)
        
    # Write the full HTML to the destination path
    with open(dest_path, 'w') as output_file:
        output_file.write(template)
    


