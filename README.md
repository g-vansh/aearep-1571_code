# AEAREP-1571 Zenodo Uploading Code
Python Directory Parsing, Downloading and Uploading Code for AEAREP-1571

- File `run_script_upload.py` contains code which does the following:
    1. Finds all files with a certain extension in a directory.
    2. Uploads them to `Zenodo` using their API.
    3. Generates a log file `upload_error_log.txt` in the root directory to note any errors encountered from the Zenodo server.

- File `run_script_download.py` contains code which does the following:
    1. Finds all files with a certain extension in a `Zenodo` repository.
    2. Downloads them to a pre-specified root directory using their API.
    3. Generates a log file `download_error_log.txt` in the root directory to note any errors encountered from the Zenodo server.

- The codes are platform agnostic, written in Windows, but are intended to run on Linux.

Manual Modification Instructions:
- For `run_script_upload.py`:
    - The path for the directory to be searched can be changed in Line 8.
    - The extension to be searched can be changed in Line 13. 
    - [REQUIRED] The Access Token needs to be changed in Line 17. 
        - Steps to generate an access token are given here: https://developers.zenodo.org/#authentication
    - If you would NOT like to search and upload the files from sub-directories in the directory as well, then change the value in Line 22 to "False". 
        - Otherwise, it is "True" by default and the program uploads all files with a certain extension in the directory and all its sub-directories.

- For `run_script_download.py`:
    - The path for the directory to be searched can be changed in Line 9.
    - The extension to be searched can be changed in Line 13. 
    - [REQUIRED] Deposit ID needs to be changed in Line 18. Instructions about how to find it can be found in Lines 15 to 17. 
    - [REQUIRED] The Access Token needs to be changed in Line 21. 
        - Steps to generate an access token are given here: https://developers.zenodo.org/#authentication

