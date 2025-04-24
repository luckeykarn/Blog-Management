import os
import shutil

# Define file type categories and their corresponding extensions
Filetype = {
    'images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'documents': ['.pdf', '.doc', '.docx', '.txt'],
    'videos': ['.mp4', '.mov', '.avi', '.mkv'],
    'audio': ['.mp3', '.wav', '.flac'],
    'archives': ['.zip', '.rar', '.7z', '.tar', '.gz'],
    'python': ['.py']
}

# Ask user for the folder path
directory_path = input("Enter the directory path to organize: ")

# Check if path exists and is a directory
if not os.path.exists(directory_path) or not os.path.isdir(directory_path):
    print("Invalid directory path. Please try again.")
    exit()

def get_category(file_extension):
    """Return category name for a given file extension."""
    for category, extensions in Filetype.items():
        if file_extension in extensions:
            return category
    return None

def move_file(source_path, filename, category, base_directory):
    """Move the file to a categorized folder inside base_directory."""
    destination_folder = os.path.join(base_directory, category)
    os.makedirs(destination_folder, exist_ok=True)

    destination_path = os.path.join(destination_folder, filename)

    # Avoid overwriting files with same name
    if os.path.exists(destination_path):
        print(f"File already exists: {destination_path}, skipping.")
    else:
        shutil.move(source_path, destination_path)
        print(f"Moved '{filename}' to '{category}/'")

def organize_with_walk(directory_path):
    print("\nOrganizing files...\n")
    for root, dirs, files in os.walk(directory_path):
        # Skip organizing already organized folders
        if os.path.abspath(root) in [os.path.abspath(os.path.join(directory_path, category)) for category in Filetype]:
            continue

        for file in files:
            file_path = os.path.join(root, file)
            file_extension = os.path.splitext(file)[1].lower()
            category = get_category(file_extension)

            if category:
                move_file(file_path, file, category, directory_path)
            else:
                print(f"No category for: {file}")

# Call the function
organize_with_walk(directory_path)
