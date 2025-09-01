import os       
import shutil   

#Folder path you want to organize (change as needed)
path = "D:/python_files/"

#Mapping of folder names to the file extensions they should contain
folders_name = {
    "images": (".jpg", ".jpeg", ".png"),
    "csv files": (".csv",),
    "pdfs": (".pdf",),
    "mp3 files": (".mp3",),
    "zip files": (".zip",)
}

#Create folders if they don't already exist
for folder in folders_name.keys():
    os.makedirs(os.path.join(path, folder), exist_ok=True)

#Get all files in the target path
files_name = os.listdir(path)

#Move files into their respective folders
for file in files_name:
    src = os.path.join(path, file)

    # Skip if it's already a folder
    if os.path.isdir(src):
        continue

    moved = False  # Tracks whether file has been moved

    # Match file extensions with destination folder
    for folder, extensions in folders_name.items():
        if file.lower().endswith(extensions):
            dst = os.path.join(path, folder, file)

            if not os.path.exists(dst):   # Avoid overwriting
                shutil.move(src, dst)
                print(f"Moved {file} → {folder}")
            else:
                print(f"Skipped {file}, already exists in {folder}")

            moved = True
            break

    # If no matching folder was found
    if not moved:
        print(f"Skipped: {file} (no matching folder)")
