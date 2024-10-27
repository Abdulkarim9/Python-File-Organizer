import os
import shutil
from pathlib import Path
import time


def organize_downloads():
    """Organizes files in the Downloads folder based on their extensions."""

    home_path = Path.home()

    target_folders = [
        home_path / "Downloads",
        home_path / "Desktop",
    ]

    documents_path = home_path / "Documents"

    # Create destination folders if they don't exist
    folder_list = ["PDF", "DOCX", "EXCEL", "TXT", "PowerPoint", "Saved-Pictures"]
    for folder in folder_list:
        folder_path = documents_path / folder
        folder_path.mkdir(exist_ok=True)

    # Define file extensions and their corresponding destination folders
    file_extensions_mapping = {
        ".pdf": "PDF",
        ".docx": "DOCX",
        ".txt": "TXT",
        ".xlsx": "EXCEL",
        ".pptx": "PowerPoint",
        (".png", ".jpg", ".jpeg"): "Saved-Pictures",
    }

    while True:
        for folder in target_folders:
            for filename in os.listdir(folder):
                file_path = folder / filename
                
                if file_path.is_file():
                    extension = file_path.suffix.lower()
                    destination_folder = None

                    # Determine the destination folder based on the file extension
                    for key, value in file_extensions_mapping.items():
                        if (isinstance(key, tuple) and extension in key) or extension == key:
                            destination_folder = value
                            break

                    if destination_folder:
                        destination_path = documents_path / destination_folder
                        if destination_folder == "Saved-Pictures":
                            destination_path = home_path / "Saved-Pictures"
                        destination_path.mkdir(exist_ok=True)  # Ensure folder exists
                        shutil.move(file_path, destination_path)

        time.sleep(30)


if __name__ == "__main__":
    organize_downloads()
