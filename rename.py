import os

def rename_files(folder_path, new_name):
    # List all files in the folder
    files = os.listdir(folder_path)
    
    for index, file in enumerate(files):
        file_path = os.path.join(folder_path, file)
        
        # Check if it's a file
        if os.path.isfile(file_path):
            # Get file extension
            file_extension = os.path.splitext(file)[1]
            
            # Create new filename
            new_filename = f"{new_name}_{index+1}{file_extension}"
            new_file_path = os.path.join(folder_path, new_filename)
            
            # Rename the file
            os.rename(file_path, new_file_path)
            print(f"Renamed: {file} -> {new_filename}")

# Example usage
folder_path = r"C:\Users\arman\Desktop\Rope-detection-v3\Dataset\consent"  # Replace with your folder path
new_name = 'consent'             # Desired base name for files
rename_files(folder_path, new_name)
