import subprocess

def playbook_one():
    print("Running Package Playbook")
    subprocess.run(["python3", "package_tasks.py"])

def playbook_two():
    print("Running File Playbook")
    subprocess.run(["python3", "run_file_playbook_create_delete.py"])

def playbook_three():
    print("Running Service Playbook")
    subprocess.run(["python3", "service_playbook_run.py"])

def playbook_four():
    print("Running Updates Package Manager Playbook")
    subprocess.run(["python3", "update_packages.py"])

def playbook_five():
    print("Running Drectory Playbook")
    subprocess.run(["python3", "directory_tasks.py"])

def playbook_six():
    print("Running Shell Execute Playbook")
    subprocess.run(["python3", "random_playbook_execute_shell.py"])

def run_playbook(playbook_function):
    playbook_function()

# Present a clearer prompt for playbook selection
print("Choose a playbook to run:")
print("1. Run Package Playbook ")
print("2. Run File Playbook")
print("3. Run Service  Three")
print("4. Run Package Manager")
print("5. Run Directory Five")
print("6. Run Command Six")

# Get user input for playbook selection
try:
    playbook_option = int(input("Enter the number corresponding to the playbook you want to run (1-6): "))
except ValueError:
    print("Invalid input. Please enter a valid number.")

# Map options to playbook functions
playbook_functions = {
    1: playbook_one,
    2: playbook_two,
    3: playbook_three,
    4: playbook_four,
    5: playbook_five,
    6: playbook_six,
}

# Check if the selected playbook option exists in the dictionary
if playbook_option in playbook_functions:
    run_playbook(playbook_functions[playbook_option])
else:
    print("Invalid playbook option. Please enter a number between 1 and 6.")
