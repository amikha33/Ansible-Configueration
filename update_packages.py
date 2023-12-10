import subprocess

def run_ansible_command(tags=None):
    command = [
        "ansible-playbook", "Playbooks/update_packagemanager_playbook.yml", "-i", "Playbooks/inventory.ini",
        "--ask-become-pass"
    ]

    if tags:
        command.extend(["--tags", tags])

    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    return process.returncode, stdout, stderr

def main():
    custom_tags = input("Enter custom tags (leave blank for 'update_packages'): ")
    return_code, stdout, stderr = run_ansible_command(tags=custom_tags or "update_packages")

    print(f"Ansible exit code: {return_code}")
    print(f"Ansible stdout:\n{stdout.decode()}")
    print(f"Ansible stderr:\n{stderr.decode()}")

if __name__ == "__main__":
    main()
