import os
import zipfile

def get_all_file_paths(directory):
    """
    Get all file paths in the given directory.
    
    :param directory: The root directory to start searching for files.
    :return: A list of absolute file paths.
    """
    file_paths = []
    for root, directories, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)
    return file_paths

def create_zip_chunks(directory, output_folder, max_size=1.8*1024*1024*1024):
    """
    Zips files into chunks without exceeding the max_size.
    
    :param directory: The root directory containing files to be zipped.
    :param output_folder: The folder where zip files will be saved.
    :param max_size: The maximum size for each zip file in bytes. Default is 1.8GB.
    """
    files = get_all_file_paths(directory)
    zip_num = 1
    current_zip_size = 0
    zip_file = None
    
    def start_new_zip():
        """
        Starts a new zip file, closes the previous one if it exists.
        
        :return: The filename of the new zip file.
        """
        nonlocal zip_file, zip_num, current_zip_size
        if zip_file:
            zip_file.close()
        zip_filename = os.path.join(output_folder, f'archive_{zip_num}.zip')
        zip_file = zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED)
        zip_num += 1
        current_zip_size = 0
        return zip_filename
    
    zip_filename = start_new_zip()  # Start the first zip file

    for file in files:
        file_size = os.path.getsize(file)
        
        # If adding the next file will exceed the max_size, start a new zip file
        if current_zip_size + file_size > max_size:
            zip_filename = start_new_zip()
        
        zip_file.write(file, os.path.relpath(file, directory))
        current_zip_size += file_size
    
    if zip_file:  # Close the last zip file if it's still open
        zip_file.close()

if __name__ == '__main__':
    # Root directory containing files to be zipped
    directory = r'E:\PICS'
    
    # Destination directory for saving the zip files
    output_folder = r'E:\justZIPs'
    
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Start the zipping process
    create_zip_chunks(directory, output_folder)