import os

# Take drive letter as input (like C, D, E)
drive_letter = input("Enter drive letter (e.g., C, D, E): ").strip().upper()

# Add :\ to make it a proper drive path
drive_path = f"{drive_letter}:\\"  

# File to search
target_file = "virus"

found = False

# Walk through the directory
for foldername, subfolders, filenames in os.walk(drive_path):
    if target_file in filenames:
        full_path = os.path.join(foldername, target_file)
        print(f"Found: {full_path}")
        found = True
        break  # remove if you want to find all matches
    else:
        print(filenames)

if not found:
    print(f"'{target_file}' not found in {drive_path}")
