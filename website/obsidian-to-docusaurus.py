#!/usr/bin/env python3

import os
import re
import shutil
import sys

import regex

vault_directory = '../vault/docs'
docs_directory = 'docs'
attachments_directory = 'public'

def change_callout(match):
    callout_content = match.captures(3)
    callout_title = match.groups(2)[0]
    callout_type = match.groups(1)[0].lstrip(" [!").rstrip("]").replace(" ", "-")
    docusaurus_callout = f":::{callout_type}[{callout_title}] \n"
    for line in callout_content:
        docusaurus_callout += '\n' + line.lstrip("\n> ")

    docusaurus_callout += "\n\n:::"
    return docusaurus_callout


def process_file(file_path):
    print(file_path)
    with open(file_path, 'r') as file:

        # Change obsidian backlink [[]] to docusaurus []() markdown link
        # TODO: Test for both backlink and image in the same line (if possible)
        lines = file.readlines()
        for i in range(len(lines)):
            backlink = re.search(r'\[\[(.*?)\]\]', lines[i])
            if backlink:
                pattern = backlink.group(1)
                filepath = next((os.path.join(root, name) for root, dirs, files in os.walk(directory) for name in files if pattern in name), None)

                # Backlink is a reference to a static asset
                if filepath:
                    filename = os.path.basename(filepath).rstrip(".md")
                    lines[i] = f'[{filename}](</{filepath}>)'

            attachment = re.search(r'!\[\[(.*?)\]\]', lines[i])
            if attachment:
                pattern = attachment.group(1)
                pattern = pattern.replace(" ", "-")
                filepath = next((os.path.join(root, name) for root, dirs, files in os.walk(attachments_directory) for name in files if pattern in name), None)
                if filepath in filepath:
                    # omit duplicate public/
                    filepath = filepath.replace(" ", "-")
                    filepath = filepath[7:]
                    lines[i] = f'![{pattern}](</{filepath}>)\n'
                    print(lines[i])

    with open(file_path, 'w') as file:
        file.writelines(lines)

    # Change obsidian callouts [!note]\n<TEXT to docusaurus ***note TEXT\n***
    with open(file_path, 'r') as file:
        # pattern = re.compile(r">(\[!\D+?\])(\n>.+)*")
        reg0 = regex.compile(r"> ?\[!(.+?)\]\+?(.*)(\n>.+)*", regex.MULTILINE)
        # reg0 = regex.compile(r"> (\[!\D+?\]).*", regex.MULTILINE)
        modified_callouts = reg0.sub(lambda m: change_callout(m), file.read())

    with open(file_path, 'w') as file:
        file.writelines(modified_callouts)
directory = 'docs'

# Delete the directory and all its contents
directories_to_delete = ['docs', 'public']
try:
    for dir in directories_to_delete:
        if os.path.isdir(dir):
            shutil.rmtree(dir)
            print("Directory '{}' and its contents have been successfully deleted.".format(dir))
except Exception as e:
    print("An error occurred:", e)


def copy_vault(src, docs_dir, attachments_dir):
    try:
        # Copy all markdown files
        shutil.copytree(src, docs_dir, ignore=shutil.ignore_patterns('attachments'))

        # Copy all attachments
        shutil.copytree('../vault/attachments', attachments_dir) 

    except PermissionError:
        print("Error: Permission denied while copying directory '{}'.".format(src))
    except Exception as e:
        print("An error occurred:", e)

# Copy the source directory and all its contents to the destination directory

copy_vault(vault_directory, docs_directory, attachments_directory)

#Rename attachments
for root,dirs,files in os.walk(attachments_directory):
    for f in files:
        os.rename(root+"/"+f,root+"/"+f.replace(" ", "-"))

#Process all .md files in the directory and its subdirectories
for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith(".md"):
            file_path = os.path.join(root, file)
            process_file(file_path)
            print("Processed:", file_path)


