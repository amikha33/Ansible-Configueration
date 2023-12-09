#!/usr/bin/env python

import subprocess

# Set the playbook path
playbook_path = "Playbooks/executecommand_playbook.yml"

# Prompt the user for input_commands for the new playbook
input_commands_str = input("Enter input commands (comma-separated): ")
input_commands = [cmd.strip() for cmd in input_commands_str.split(',')]
extra_vars = {"input_commands": input_commands}

# Set other variables
ask_become_pass = True  # Set to True if you want to prompt for the become password

# Convert extra_vars to a string
extra_vars_str = ' '.join([f"{key}={value}" for key, value in extra_vars.items()])

# Build the ansible-playbook command
command = [
    'ansible-playbook',
    playbook_path,
    '--extra-vars', extra_vars_str,
]

# Include --ask-become-pass if necessary
if ask_become_pass:
    command.append('--ask-become-pass')
    become_pass = input("Enter become password: ")
    process = subprocess.Popen(command, stdin=subprocess.PIPE)
    process.communicate(input=become_pass.encode())
else:
    process = subprocess.run(command)

# Print the return code
print(f"Return code: {process.returncode}")
