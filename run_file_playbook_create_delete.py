import subprocess
import sys

# Check if the correct number of arguments is provided
if len(sys.argv) != 1:
    print("Usage: python script.py")
    sys.exit(1)

# Take file_name and file_directory as input
file_name = input("Enter the file name: ")
file_directory = input("Enter the file directory: ")
file_action = input("Enter the file action: ")

# Build the command
ansible_command = [
    "ansible-playbook",
    "Playbooks/file_playbook_create_delete.yml",
    "-e",
    f"file_name={file_name} file_directory={file_directory} file_action={file_action}",
]

# Run the command
try:
    subprocess.run(ansible_command, check=True)
    print("Ansible playbook executed successfully.")
except subprocess.CalledProcessError as e:
    print(f"Error executing Ansible playbook: {e}")
