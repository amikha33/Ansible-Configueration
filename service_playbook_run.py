import subprocess

# Get service_name and desired_state as user inputs
service_name = input("Enter the service name: ")
desired_state = input("Enter the desired state (e.g., started or stopped): ")

# Define the Ansible command with input variables
ansible_command = [
    'ansible-playbook',
    '-i', 'localhost,',
    'service_playbook.yaml',
    '-e', f'service_name={service_name} desired_state={desired_state}'
]

# Run the Ansible command using subprocess
try:
    subprocess.run(ansible_command, check=True, shell=False)
    print("Ansible playbook executed successfully.")
except subprocess.CalledProcessError as e:
    print(f"Error executing Ansible playbook: {e}")
