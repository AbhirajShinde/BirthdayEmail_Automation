import os
import shutil

def delete_subfolder(folder_path, subfolder_name):
    # Construct the path to the subfolder
    subfolder_path = os.path.join(folder_path, subfolder_name)

    # Check if the subfolder exists
    if os.path.exists(subfolder_path):
        # Use shutil.rmtree() to recursively delete the subfolder and its contents
        shutil.rmtree(subfolder_path)
        print(f"Subfolder '{subfolder_name}' deleted successfully.")
    else:
        print(f"Subfolder '{subfolder_name}' does not exist.")

def main():
    # Specify the folder path and the subfolder name to delete
    folder_path = os.getcwd()
    subfolder_name = "images"  # Change this to the name of the subfolder you want to delete

    # Call the delete_subfolder function
    delete_subfolder(folder_path, subfolder_name)

if __name__ == "__main__":
    main()