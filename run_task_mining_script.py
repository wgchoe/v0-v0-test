# run_task_mining_script.py
# This script executes another Python script (task_mining.py) using the subprocess module.

import subprocess
import sys
import os

# Path to the task_mining.py script.
# If task_mining.py is not in the same directory as this script,
# or not on the system's PATH, provide the full path to it.
# Example: task_mining_script_path = "/path/to/your/task_mining.py"
# Example: task_mining_script_path = "C:/Users/YourUser/Documents/task_mining.py"
task_mining_script_path = "task_mining.py"

def execute_script(script_path):
    """
    Executes the specified Python script using the current Python interpreter.
    Prints its stdout and stderr.
    """
    print(f"Attempting to execute script: {script_path}")

    # Check if the script file exists before attempting to run
    if not os.path.exists(script_path):
        print(f"Error: The script '{script_path}' was not found.")
        print("Please ensure the 'task_mining_script_path' variable is set correctly,")
        print("and the 'task_mining.py' script exists at that location.")
        return

    try:
        # sys.executable ensures that we use the same Python interpreter
        # that is running this current script.
        command = [sys.executable, script_path]
        
        print(f"Running command: {' '.join(command)}")

        # Execute the script
        # - capture_output=True to get stdout and stderr
        # - text=True to decode output as text (universal_newlines=True in older Python)
        # - check=False to manually handle errors based on returncode
        result = subprocess.run(command, capture_output=True, text=True, check=False)

        # Print stdout from the executed script
        if result.stdout:
            print("\n--- Output from task_mining.py (stdout) ---")
            print(result.stdout)
            print("--- End of task_mining.py stdout ---\n")
        else:
            print("\n--- task_mining.py produced no stdout ---")

        # Print stderr from the executed script (if any)
        if result.stderr:
            print("\n--- Errors from task_mining.py (stderr) ---")
            print(result.stderr)
            print("--- End of task_mining.py stderr ---\n")
        else:
            print("\n--- task_mining.py produced no stderr ---")
            
        # Check if the script executed successfully
        if result.returncode == 0:
            print(f"Script '{script_path}' executed successfully.")
        else:
            print(f"Script '{script_path}' finished with return code: {result.returncode}")
            print("Review the stderr output above for potential error messages from the script.")

    except FileNotFoundError:
        # This specific exception might occur if sys.executable is somehow invalid,
        # or if the script_path is a directory (though os.path.exists should catch non-files).
        # The primary FileNotFoundError for script_path itself is handled by the os.path.exists check.
        print(f"Error: Could not find the Python interpreter '{sys.executable}' or the script path is problematic.")
        print("Ensure Python is correctly installed and in your PATH.")
    except Exception as e:
        print(f"An unexpected error occurred while trying to run the script: {e}")

if __name__ == "__main__":
    print("--------------------------------------------------------------------")
    print("This script will now attempt to run 'task_mining.py'.")
    # As a safety/usability measure, we'll create a dummy task_mining.py if it doesn't exist,
    # so this wrapper script can be tested.
    if not os.path.exists(task_mining_script_path):
        print(f"Note: '{task_mining_script_path}' does not exist. ")
        print(f"Creating a dummy '{task_mining_script_path}' for demonstration purposes.")
        try:
            with open(task_mining_script_path, "w") as f:
                f.write("# Dummy task_mining.py\n")
                f.write("import sys\n")
                f.write("print('Hello from task_mining.py!')\n")
                f.write("print('This is a standard output message.', file=sys.stdout)\n")
                f.write("print('This is an error message simulation.', file=sys.stderr)\n")
                # sys.exit(1) # Uncomment to test error handling
            print(f"Dummy '{task_mining_script_path}' created successfully.")
        except IOError as e:
            print(f"Could not create dummy '{task_mining_script_path}': {e}")
            print("Proceeding with execution attempt, but it will likely fail if the script is still missing.")
    print("--------------------------------------------------------------------")
    
    execute_script(task_mining_script_path)
