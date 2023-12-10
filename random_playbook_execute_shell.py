import subprocess
import yaml

def run_ansible_playbook(commands):
    # Split user input into a list of commands
    commands_list = [cmd.strip() for cmd in commands.split(',')]

    # Format input commands for YAML
    input_commands_yaml = "\n      - ".join(f'"{cmd}"' for cmd in commands_list)

    # Create a temporary YAML file with the provided commands
    playbook_content = f"""
---
- name: Execute Commands on Target
  hosts: all
  become: yes

  vars:
    input_commands:
      - {input_commands_yaml}

  tasks:
    - name: Run Custom Commands
      command: "{{{{ item }}}}"
      register: command_output
      with_items: "{{{{ input_commands }}}}"

    - name: Display Command Output
      debug:
        var: item.stdout_lines
      with_items: "{{{{ command_output.results }}}}"
"""
    with open('temp_playbook.yml', 'w') as temp_playbook:
        temp_playbook.write(playbook_content)

    # Run Ansible playbook using subprocess
    subprocess.run(['ansible-playbook', 'temp_playbook.yml','-i', 'Playbooks/inventory.ini',])

    # Remove the temporary playbook file
    subprocess.run(['rm', 'temp_playbook.yml'])

if __name__ == "__main__":
    # Get user input for commands
    user_input = input("Enter commands separated by commas (e.g., df -h, ls -l): ")
    
    # Run Ansible playbook with user-provided commands
    run_ansible_playbook(user_input)
