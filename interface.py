import os

# List of common image file extensions
image_extensions = ['.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff', '.svg']

def count_lines_of_code(repo_path):
    non_image_file_line_counts = {}
    all_file_line_counts = {}
    for root, _, files in os.walk(repo_path):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'r', errors='ignore') as f:
                    line_count = sum(1 for _ in f)
                    all_file_line_counts[file_path] = line_count
                    # Check if the file is not an image
                    if not any(file.lower().endswith(ext) for ext in image_extensions):
                        non_image_file_line_counts[file_path] = line_count
            except:
                pass  # Ignore files that can't be read
    return non_image_file_line_counts, all_file_line_counts

if __name__ == "__main__":
    repo_path = input("Enter the path to the Git repository: ")
    try:
        if not os.path.isdir(repo_path):
            raise ValueError("Invalid repository path")
        
        non_image_file_line_counts, all_file_line_counts = count_lines_of_code(repo_path)
        
        print("Lines of code in non-image files:")
        for file_path, line_count in non_image_file_line_counts.items():
            print(f"{file_path}: {line_count} lines")
        
        print("\nLines of code in all files:")
        for file_path, line_count in all_file_line_counts.items():
            print(f"{file_path}: {line_count} lines")
        
        total_non_image_lines = sum(non_image_file_line_counts.values())
        total_all_lines = sum(all_file_line_counts.values())
        
        print(f"\nTotal lines of code in non-image files: {total_non_image_lines}")
        print(f"Total lines of code in all files: {total_all_lines}")
    except Exception as e:
        print(f"Error: {e}")