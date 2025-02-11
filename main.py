import os
import subprocess

def convert_to_unix(directory):
    """Convert all files in a directory to Unix line endings using dos2unix."""
    
    # Ensure the directory exists
    if not os.path.isdir(directory):
        print(f"❌ Error: Directory '{directory}' not found!")
        return

    # Walk through all files and subdirectories
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            
            try:
                # Run dos2unix on each file
                subprocess.run(["dos2unix", file_path], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                print(f"✅ Converted: {file_path}")
            except subprocess.CalledProcessError as e:
                print(f"⚠️ Skipped (error): {file_path} -> {e}")

# Run the script on the target directory
if __name__ == "__main__":
    repo_path = input("Enter the repository path: ").strip()
    convert_to_unix(repo_path)
