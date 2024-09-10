import os

def create_folders(base_path, start, end):
    for i in range(start, end + 1):
        folder_name = f"step{i}"
        folder_path = os.path.join(base_path, folder_name)
        try:
            os.makedirs(folder_path)
            print(f"Created: {folder_path}")
        except FileExistsError:
            print(f"Folder already exists: {folder_path}")

# Ask the user for input
base_path = input("Enter the base path where the folders should be created: ")
start = int(input("Enter the starting number (e.g., 21): "))
end = int(input("Enter the ending number (e.g., 91): "))

# Create the folders
create_folders(base_path, start, end)
