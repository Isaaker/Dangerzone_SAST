import os
import subprocess

def scan_repository_with_dangerzone(repository_path):
    """
    Scans a local repository with Dangerzone using its CLI.
    
    Args:
        repository_path (str): The path to the repository directory to be scanned.
    """
    # List of file extensions compatible with Dangerzone.
    # This list may need to be adjusted based on your needs.
    allowed_extensions = ('.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx', '.jpg', '.jpeg', '.png', '.gif')

    if not os.path.isdir(repository_path):
        print(f"Error: The directory '{repository_path}' does not exist.")
        return

    print(f"Starting repository scan at '{repository_path}'...")

    for root, dirs, files in os.walk(repository_path):
        for file in files:
            file_path = os.path.join(root, file)
            # Check if the file extension is in the allowed list
            if file.lower().endswith(allowed_extensions):
                print(f"Processing file: {file_path}")
                try:
                    # Dangerzone command. The '--input' flag specifies the file to be scanned.
                    # Make sure 'dangerzone-cli' is in your PATH or use the full path to it.
                    subprocess.run(
                        ["dangerzone-cli", "--input", file_path],
                        check=True,
                        capture_output=True,
                        text=True
                    )
                    print(f"✅ File processed successfully: {file_path}")
                except subprocess.CalledProcessError as e:
                    print(f"❌ Error processing '{file_path}':")
                    print(f"  Standard Output: {e.stdout}")
                    print(f"  Standard Error: {e.stderr}")
                except FileNotFoundError:
                    print("❌ Error: 'dangerzone-cli' was not found.")
                    print("Please ensure Dangerzone is installed and 'dangerzone-cli' is in your system's PATH.")
            else:
                print(f"Skipping unsupported file: {file_path}")

# Example usage
if __name__ == "__main__":
    # Replace 'path/to/your/repository' with the actual path to your directory
    scan_repository_with_dangerzone("path/to/your/repository")