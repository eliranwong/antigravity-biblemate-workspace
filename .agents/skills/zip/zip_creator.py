import os
import sys
import zipfile

# Get workspace root dynamically
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, '..', '..', '..'))

def main():
    zip_path = os.path.join(REPO_ROOT, 'manual_setup.zip')
    
    # 1. Remove the old zip if it exists
    if os.path.exists(zip_path):
        try:
            os.remove(zip_path)
            print(f"Removed existing manual_setup.zip at {zip_path}")
        except Exception as e:
            print(f"Error removing existing manual_setup.zip: {e}")
            sys.exit(1)
            
    print("Creating manual_setup.zip...")
    
    # Folders to zip
    folders_to_zip = ['.agents', 'preferences']
    
    try:
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for folder in folders_to_zip:
                folder_path = os.path.join(REPO_ROOT, folder)
                if not os.path.exists(folder_path):
                    print(f"Warning: Folder '{folder}' does not exist, skipping.")
                    continue
                # Walk through the folder
                for root, dirs, files in os.walk(folder_path):
                    # Sort dirs and files to ensure deterministic zip order
                    dirs.sort()
                    files.sort()
                    for file in files:
                        file_path = os.path.join(root, file)
                        # The relative path within the zip archive
                        arcname = os.path.relpath(file_path, REPO_ROOT)
                        zipf.write(file_path, arcname)
                        
        print(f"Successfully created manual_setup.zip at: {zip_path}")
        print("This zip file includes the '.agents/' and 'preferences/' folders, offering users an easy way to set up manually.")
    except Exception as e:
        print(f"Error creating zip file: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
