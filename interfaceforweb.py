import os
import git
import tempfile
import shutil

# List of common image file extensions
image_extensions = ['.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff', '.svg']

def count_lines_of_code(repo_path):
    file_line_counts = {}
    for root, _, files in os.walk(repo_path):
        for file in files:
            file_path = os.path.join(root, file)
            # Check if the file is not an image
            if not any(file.lower().endswith(ext) for ext in image_extensions):
                try:
                    with open(file_path, 'r', errors='ignore') as f:
                        line_count = sum(1 for _ in f)
                        file_line_counts[file_path] = line_count
                except:
                    pass  # Ignore files that can't be read
    return file_line_counts

def clone_repo(repo_url):
    temp_dir = tempfile.mkdtemp()
    try:
        git.Repo.clone_from(repo_url, temp_dir)
        return temp_dir
    except Exception as e:
        shutil.rmtree(temp_dir)
        raise e

def remove_readonly(func, path, excinfo):
    os.chmod(path, 0o777)
    func(path)

if __name__ == "__main__":
    repo_url = input("Enter the GitHub repository URL: ")
    try:
        repo_path = clone_repo(repo_url)
        file_line_counts = count_lines_of_code(repo_path)
        for file_path, line_count in file_line_counts.items():
            print(f"{file_path}: {line_count} lines")
        total_lines = sum(file_line_counts.values())
        print(f"Total lines of code: {total_lines}")
    except Exception as e:
        print(f"Failed to clone repository: {e}")
    finally:
        if 'repo_path' in locals():
            shutil.rmtree(repo_path, onerror=remove_readonly)