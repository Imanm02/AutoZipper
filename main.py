import os
import sys
import shutil
from zipfile import ZipFile, ZIP_DEFLATED
from tqdm import tqdm

def get_all_file_paths(directory):
    """Return a list of file paths for the given directory."""
    file_paths = []

    # os.walk gives us a generator of tuples (dirpath, dirnames, filenames)
    for root, directories, files in os.walk(directory):
        for filename in files:

            # construct full file path
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)
    return file_paths

def create_zip_chunks(directory, output_folder):
    """Create ZIP file chunks from the given directory."""
    # Define the maximum chunk size as 1.8 GB
    CHUNK_SIZE = 1.8 * (1024**3)

    # Check if the provided source directory exists
    if not os.path.exists(directory):
        print(f"Error: The source directory '{directory}' does not exist.")
        sys.exit(1)

    # Check if there's enough free space in the output directory
    free_space = shutil.disk_usage(output_folder).free
    if free_space < CHUNK_SIZE:
        print("Error: Not enough disk space on the output directory to create ZIP files.")
        sys.exit(1)

    # Get the list of all files from the source directory
    file_paths = get_all_file_paths(directory)

    # Initialize variables
    zip_file = None
    current_size = 0
    chunk_number = 0
    
    # Loop through each file to add to zip
    for file in tqdm(file_paths, unit="file", desc="Zipping files"):
        file_size = os.path.getsize(file)
        # If current file won't fit in current zip chunk, or no chunk is opened yet, open a new chunk
        if current_size + file_size > CHUNK_SIZE or zip_file is None:
            # Close the current chunk if it exists
            if zip_file:
                zip_file.close()

            # Create a new chunk zip file
            zip_filename = os.path.join(output_folder, f"archive_part_{chunk_number}.zip")
            zip_file = ZipFile(zip_filename, 'w', ZIP_DEFLATED)
            current_size = 0
            chunk_number += 1

        # Add the current file to the current chunk
        zip_file.write(file, os.path.relpath(file, directory))
        current_size += file_size

    # Close the last zip chunk if it exists
    if zip_file:
        zip_file.close()

if __name__ == "__main__":

    # Root directory containing files to be zipped
    directory = r'E:\RootDirectory'
    
    # Destination directory for saving the zip files
    output_folder = r'E:\DestinationDirectory'

    # Start the process to create zip chunks
    create_zip_chunks(directory, output_folder)