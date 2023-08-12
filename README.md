# AutoZipper

AutoZipper is a Python script designed to automate the task of compressing files from a directory into multiple zip archives. Each archive is carefully segmented to ensure it remains below a specified size limit, making it ideal for situations where there are restrictions on individual file sizes, such as uploads to certain platforms.

## Features

- **Automatic Segmentation**: Ensures each zip archive remains below the specified size limit.
- **Full Directory Compression**: Capable of traversing through a directory and zipping all files, maintaining the original folder structure.
- **Optimized for Large File Collections**: Built to handle directories with a large number of files without compromising on efficiency or speed.
- **Customizable Size Limit**: Users can easily modify the maximum allowed size for each zip archive.
- **Progress Bar**: Using the `tqdm` library, the script provides a real-time progress bar in the console, allowing users to track the zipping process visually.
- **Robust Error Handling**: The script incorporates robust error handling, including checking for:
  - Existence of the source directory
  - Adequate free disk space in the output directory

## Code Walkthrough

Here's a brief overview of how the script operates:

1. **Importing Libraries**: Essential libraries are imported to handle file paths, zipping operations, and directory traversal.

\```python
import os
import zipfile
\```

2. **Fetching All File Paths**: The `get_all_file_paths()` function recursively collects all file paths within the specified directory.

```python
def get_all_file_paths(directory):
    ...
```

3. **Creating ZIP Chunks**: Main function to create the zip chunks. This function incorporates:
  - Checking for source directory existence
  - Verifying enough free disk space
  - Zipping files while ensuring each archive remains below the size limit

```python
def create_zip_chunks(directory, output_folder):
    ...
`

4. **Main Execution**: The script's entry point. This segment defines the source directory and the destination for the zip archives, and then calls the main functions.

```python
if __name__ == '__main__':
    ...
    create_zip_chunks(directory, output_folder)
```

## Usage

1. **Set Up**: Ensure your Python environment includes the `os`, `zipfile` and `tqdm` libraries. These are standard in Python, so no additional installation is typically required.

2. **Modify Source & Destination**: Within the main execution section of the script (`if __name__ == '__main__':`), set the `directory` variable to point to the source directory of your files, and `output_folder` to your desired zip archive destination.

3. **Run the Script**: Execute the script using your Python interpreter. 

4. **Check the Output**: Navigate to your specified output folder. You should see multiple zip archives, each staying below the size limit defined in the script (default is 1.8GB).

_Note_: Ensure you have adequate disk space in the output directory. The sum of the sizes of the zip archives will be close to the total size of the original files.

## Customization

- **Size Limit**: To modify the size limit for each zip archive, adjust the `max_size` parameter within the `create_zip_chunks()` function.

# Maintainer
- [Iman Mohammadi](https://github.com/Imanm02)
