import subprocess
import sys

# Check if the correct number of arguments is provided
if len(sys.argv) != 4:
    print("Usage: python script.py <file_name> <file_directory> <file_action>")
    sys.exit(1)

# Parse command-line arguments
file_name = sys.argv[1]
file_directory = sys.argv[2]
file_action = sys.argv[3]

# Build the command
ansible_command = [
    "ansible-playbook",
    "file_create_delete.yml",
    "-e",
    f"file_name={file_name} file_directory={file_directory} file_action={file_action}",
]

# Run the command
try:
    subprocess.run(ansible_command, check=True)
    print("Ansible playbook executed successfully.")
except subprocess.CalledProcessError as e:
    print(f"Error executing Ansible playbook: {e}")
