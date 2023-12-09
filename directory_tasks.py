import subprocess
import sys

# Check if the correct number of command-line arguments is provided
if len(sys.argv) != 3:
    print("Usage: python your_script_name.py <DIRECTORY_NAME> <DIRECTORY_OPERATION>")
    sys.exit(1)

# Get directory name and operation from command-line arguments
DIRECTORY_NAME = sys.argv[1]
DIRECTORY_OPERATION = sys.argv[2]

# Construct the ansible-playbook command
command = [
    "ansible-playbook",
    "-i", "localhost,",
    "directory_playbook.yml",
    "--tags", DIRECTORY_OPERATION,
    "--extra-vars", f"directory_name={DIRECTORY_NAME}"
]

# Run the command
try:
    subprocess.run(command, check=True)
    print("Ansible playbook executed successfully.")
except subprocess.CalledProcessError as e:
    print(f"Error executing Ansible playbook: {e}")



# How to run this 
# python3 directory_tasks.py /home/agad/booking_example  create

