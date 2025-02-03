import os
import sys
import shutil
from zipfile import ZipFile, ZIP_DEFLATED
from tqdm import tqdm

def get_all_file_paths(directory):
    """Return a list of file paths for the given directory."""
    file_paths = []

    for root, directories, files in os.walk(directory):
        for filename in files:

            filepath = os.path.join(root, filename)
            file_paths.append(filepath)
    return file_paths

def create_zip_chunks(directory, output_folder):
    """Create ZIP file chunks from the given directory."""
    CHUNK_SIZE = 1.8 * (1024**3)

    if not os.path.exists(directory):
        print(f"Error: The source directory '{directory}' does not exist.")
        sys.exit(1)

    free_space = shutil.disk_usage(output_folder).free
    if free_space < CHUNK_SIZE:
        print("Error: Not enough disk space on the output directory to create ZIP files.")
        sys.exit(1)

    file_paths = get_all_file_paths(directory)

    zip_file = None
    current_size = 0
    chunk_number = 0
    
    for file in tqdm(file_paths, unit="file", desc="Zipping files"):
        file_size = os.path.getsize(file)
        if current_size + file_size > CHUNK_SIZE or zip_file is None:
            if zip_file:
                zip_file.close()

            zip_filename = os.path.join(output_folder, f"archive_part_{chunk_number}.zip")
            zip_file = ZipFile(zip_filename, 'w', ZIP_DEFLATED)
            current_size = 0
            chunk_number += 1

        zip_file.write(file, os.path.relpath(file, directory))
        current_size += file_size

    if zip_file:
        zip_file.close()

if __name__ == "__main__":

    directory = r'RootDirectoryAddess'
    
    output_folder = r'DestinationDirectoryAddess'

    create_zip_chunks(directory, output_folder)
