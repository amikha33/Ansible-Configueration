import subprocess
import json

def run_playbook(playbook_path, extra_vars=None, ask_become_pass=False, tags=None):
    extra_vars_str = f"--extra-vars '{json.dumps(extra_vars)}'" if extra_vars else ""
    ask_become_pass_str = "--ask-become-pass" if ask_become_pass else ""
    tags_str = f"--tags {tags}" if tags else ""
    command = f"ansible-playbook {playbook_path} {extra_vars_str} {ask_become_pass_str} {tags_str}"
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    return process.returncode, stdout, stderr

def main():
    playbook_choice = input("Enter the playbook number (1, 2, 3, or 4): ")

    if playbook_choice == "1":
        playbook_path = "playbook1.yml"
        extra_vars = None  # No input variables for playbook 1
        ask_become_pass = False
    elif playbook_choice == "2":
        playbook_path = "playbook2.yml"
        # Prompt the user for service_name and desired_state for playbook 2
        service_name = input("Enter service name: ")
        desired_state = input("Enter desired state (default is started): ") or "started"
        extra_vars = {"service_name": service_name, "desired_state": desired_state}
        ask_become_pass = True
    elif playbook_choice == "3":
        playbook_path = "random_playbook.yml"
        # Prompt the user for input_commands for the new playbook
        input_commands_str = input("Enter input commands (comma-separated): ")
        input_commands = [cmd.strip() for cmd in input_commands_str.split(',')]
        extra_vars = {"input_commands": input_commands}
        ask_become_pass = False
    elif playbook_choice == "4":
        playbook_path = "package_playbook.yml"
        # Prompt the user for package_name and tag for playbook 4
        package_name = input("Enter package name (default is nginx): ") or "nginx"
        tag = input("Enter tag to execute (install-package or remove-package): ")
        extra_vars = {"PACKAGE_NAME": package_name}
        ask_become_pass = True
    else:
        print("Invalid playbook choice.")
        return

    return_code, stdout, stderr = run_playbook(playbook_path, extra_vars, ask_become_pass, tag)

    print(f"Playbook exit code: {return_code}")
    print(f"Playbook stdout:\n{stdout.decode()}")
    print(f"Playbook stderr:\n{stderr.decode()}")

if name == "main":
    main()
