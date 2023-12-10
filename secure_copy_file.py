import subprocess

def run_ansible_playbook(source_path, destination_path, sudo_password):
    playbook_content = f"""
---
- name: Copy File
  hosts: all
  become: yes
  gather_facts: false

  tasks:
    - name: Synchronize file
      ansible.builtin.synchronize:
        src: "{source_path}"
        dest: "{destination_path}"
"""

    playbook_path = "copy_file_playbook_dynamic.yml"

    with open(playbook_path, "w") as playbook_file:
        playbook_file.write(playbook_content)

    try:
        command = f"ansible-playbook --inventory-file=Playbooks/inventory.ini --extra-vars 'ansible_become_pass={sudo_password}' {playbook_path}"
        subprocess.run(command, shell=True, check=True)
        print("Ansible playbook executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error executing Ansible playbook: {e}")

if __name__ == "__main__":
    source_path = input("Enter source path: ")
    destination_path = input("Enter destination path: ")
    sudo_password = input("Enter sudo password: ")

    run_ansible_playbook(source_path, destination_path, sudo_password)
