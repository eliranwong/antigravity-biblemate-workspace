import os
import sys
import subprocess

def main():
    # Get workspace root dynamically
    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.abspath(os.path.join(script_dir, '..', '..', '..'))
    
    # 1. Condition 1: If device os is macOS or Linux
    current_os = sys.platform
    if not (current_os.startswith('linux') or current_os == 'darwin'):
        print(f"Error: Operating system '{current_os}' is not supported. This command only runs on macOS or Linux.")
        sys.exit(1)
        
    # 2. Condition 2: If the workspace folder is NOT `antigravity-biblemate-workspace`
    repo_name = os.path.basename(os.path.normpath(repo_root))
    if repo_name == 'antigravity-biblemate-workspace':
        print("Error: The workspace folder is 'antigravity-biblemate-workspace'. Update command is not allowed to run in the source repository to prevent overwriting files.")
        sys.exit(1)
        
    print(f"Conditions met. Running update command in workspace: {repo_root}")
    
    # Command to run:
    # curl -L -O https://github.com/eliranwong/antigravity-biblemate-workspace/raw/main/manual_setup.zip && unzip -o manual_setup.zip && rm manual_setup.zip && mkdir -p biblemate notes images export
    cmd = (
        "curl -L -O https://github.com/eliranwong/antigravity-biblemate-workspace/raw/main/manual_setup.zip "
        "&& unzip -o manual_setup.zip "
        "&& rm manual_setup.zip "
        "&& mkdir -p biblemate notes images export"
    )
    
    try:
        # Run command with repo_root as the current working directory
        result = subprocess.run(cmd, shell=True, cwd=repo_root, check=True, capture_output=True, text=True)
        print("Update command completed successfully!")
        if result.stdout:
            print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error executing update command (exit code {e.returncode}):")
        if e.stdout:
            print("Standard Output:\n", e.stdout)
        if e.stderr:
            print("Standard Error:\n", e.stderr)
        sys.exit(e.returncode)

if __name__ == '__main__':
    main()
