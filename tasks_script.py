import subprocess
import json

def run_playbook(playbook_path, extra_vars=None):
    extra_vars_str = f"--extra-vars '{json.dumps(extra_vars)}'" if extra_vars else ""
    command = f"ansible-playbook {playbook_path} {extra_vars_str}"
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    return process.returncode, stdout, stderr

def main():
    playbook_choice = input("Enter the playbook number (1 or 2): ")

    if playbook_choice == "1":
        playbook_path = "update_packages.yml"
        extra_vars = None  # No input variables for playbook 1
    elif playbook_choice == "2":
        playbook_path = "service_playbook.yaml"
        # Prompt the user for service_name and desired_state for playbook 2
        service_name = input("Enter service name: ")
        desired_state = input("Enter desired state (default is started): ") or "started"
        extra_vars = {"service_name": service_name, "desired_state": desired_state}
    else:
        print("Invalid playbook choice.")
        return

    return_code, stdout, stderr = run_playbook(playbook_path, extra_vars)

    print(f"Playbook exit code: {return_code}")
    print(f"Playbook stdout:\n{stdout.decode()}")
    print(f"Playbook stderr:\n{stderr.decode()}")

if __name__ == "__main__":
    main()
