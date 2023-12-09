import subprocess
import os

# Get input from the user
package_name = input("Enter the package name (e.g., nginx): ")

# Ensure a valid package state is provided
valid_states = ['absent', 'present']
package_state = input(f"Enter the package state ({', '.join(valid_states)}): ").lower()

while package_state not in valid_states:
    print(f"Invalid package state. Please enter one of: {', '.join(valid_states)}")
    package_state = input(f"Enter the package state ({', '.join(valid_states)}): ").lower()

# Set environment variables for the playbook
os.environ['PACKAGE_NAME'] = package_name
os.environ['PACKAGE_STATE'] = package_state

# Define the command to run the playbook
command = ['ansible-playbook', 'Playbooks/package_playbook.yml', '--ask-become-pass']

# Run the command
process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
output, error = process.communicate()

# Print the playbook output
print(output)

# Check the result
if process.returncode == 0:
    print("Playbook executed successfully")
else:
    print(f"Error running playbook. Return code: {process.returncode}")
    print("Error output:")
    print(error)
