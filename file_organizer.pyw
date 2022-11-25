import os
import shutil
from pathlib import Path
import time


# Get home path
home_path = Path.home()
# Creating needed folders
folders_list = ["PDF", "DOCX", "EXCEL", "TXT"]
# Path to directory to create folders in 
documents_dir = os.path.join(home_path, "Documents")


# Looping over folders list
for folder in folders_list:
    # Joining folder with parent directory
    path = os.path.join(documents_dir, folder)
    # Check if folder already exists
    if not os.path.exists(path):
        # If it doesn't exist create
        os.mkdir(path)
    else:
        # If it exists don't create
        # print(f"{folder}: This folder already exists!")
        continue


# creating file extension list
file_extensions = ['.txt', '.docx', '.pdf', '.xlsx', '.png', '.jpg', '.jpeg']
downloads_path = os.path.join(home_path, "Downloads")

# Change directory to files directory
os.chdir(downloads_path)

destination = documents_dir
# Create a list to store files
files = []

# Get files
def get_files():

    for file in os.listdir():
        if os.path.exists(file):
            file_path, file_extension = os.path.splitext(file)
            if file_extension in file_extensions:
                files.append(file)


# Move files
def move_files():
              
    for f in files:
        file_path, file_extension = os.path.splitext(f)
        if os.path.exists(f):
            if file_extension == '.pdf':
                shutil.move(f, destination + '/PDF')
                # print(f'{f} moved successfully')
            elif file_extension == '.docx':
                shutil.move(f, destination + '/DOCX')
                # print(f'{f} moved successfully')
            elif file_extension == '.txt':
                shutil.move(f, destination + '/TXT')
                # print(f'{f} moved successfully')
            elif file_extension == '.xlsx':
                shutil.move(f, destination + '/EXCEL')
                # print(f'{f} moved successfully')
            elif file_extension == '.png' or file_extension == '.jpg' or file_extension == '.jpeg':
                img_dir = os.path.join(home_path, "Saved Pictures")
                shutil.move(f, img_dir)
        else:
            continue
            # print(f"{f} doesn't exist or already moved")



while True:
    time.sleep(30)
    get_files()
    move_files()
