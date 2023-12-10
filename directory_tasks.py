import subprocess

# Get directory name and operation interactively
DIRECTORY_NAME = input("Enter directory name: ")
DIRECTORY_OPERATION = input("Enter directory operation (e.g., create, delete): ")

# Construct the ansible-playbook command
command = [
    "ansible-playbook",
    "-i", "Playbooks/inventory.ini,",
    "Playbooks/directory_playbook.yml",
    "--tags", DIRECTORY_OPERATION,
    "--extra-vars", f"directory_name={DIRECTORY_NAME}"
]

# Run the command
try:
    subprocess.run(command, check=True)
    print("Ansible playbook executed successfully.")
except subprocess.CalledProcessError as e:
    print(f"Error executing Ansible playbook: {e}")
