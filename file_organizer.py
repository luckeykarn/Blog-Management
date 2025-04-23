import os
import shutil

# Define file type categories and their corresponding extensions
Filetype = {
        'images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
        'documents': ['.pdf', '.doc', '.docx', '.txt'],
        'videos': ['.mp4', '.mov', '.avi', '.mkv'],
        'audio': ['.mp3', '.wav', '.flac'],
        'archives': ['.zip', '.rar', '.7z', '.tar', '.gz'],
        'python':['.py']
    }

# Step 1: Ask user for the folder path
directory_path = input("Enter the directory path to organize: ")

# Step 2: Check if the path exists and is a folder
if os.path.exists(directory_path) and os.path.isdir(directory_path):
    print("\nDirectory found!")
    print("Listing files in:", directory_path)

    # Step 3: List all files
    all_files = os.listdir(directory_path)

    for file in all_files:
        full_path = os.path.join(directory_path, file)
        if os.path.isfile(full_path):
            print("The list of File:", file)
else:
    print("No valid directory found. Please check the path.")


def organize_files(directory_path):
    # Organize files in the given directory based on their types.
    # Iterate over each file in the specified directory
    for filename in os.listdir(directory_path):
        # Get the file extension
        file_extension = os.path.splitext(filename)[1].lower()

        # Determine the category for the file based on its extension
        category = get_category(file_extension)

        # If the file matches a known category, move it to the corresponding subdirectory
        if category:
            move_file(filename, category, directory_path)
        else:
            print(f"File '{filename}' does not match any known category.")

def get_category(file_extension):
    """Get the category for a file based on its extension."""
    for key, extensions in Filetype.items():
        if file_extension in extensions:
            return key
    return None

def move_file(filename, category, directory_path):
    """Move a file to the specified category directory."""
    category_path = os.path.join(directory_path, category)
    # Create the subdirectory if it doesn't exist
    os.makedirs(category_path, exist_ok=True)

    # Move the file to the subdirectory
    source = os.path.join(directory_path, filename)
    destination = os.path.join(category_path, filename)
    shutil.move(source, destination)
    print(f"Moved '{filename}' to '{category}/'")

# Call the organize_files function
organize_files(directory_path)