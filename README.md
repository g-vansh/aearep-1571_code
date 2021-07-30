# AEAREP-1571 Zenodo Uploading Code
Python Directory Parsing and Uploading Code for AEAREP-1571

- File `run_script.py` contains code which does the following:
    1. Finds all files with a certain extension in a directory.
    2. Uploads them to `Zenodo` using their API.
    3. Generates a log file `error_log.txt` in the root directory to note any errors encountered from the Zenodo server.

- The code is platform agnostic, written in Windows, but is intended to run on Linux. 

Manual Modification Instructions:
- The path for the directory to be searched can be changed in Line 8.
- The extension to be searched can be changed in Line 13. 
- [REQUIRED] The Access Token needs to be changed in Line 17. 
    - Steps to generate an access token are given here: https://developers.zenodo.org/#authentication
- If you would NOT like to search and upload the files from sub-directories in the directory as well, then change the value in Line 22 to "False". 
    - Otherwise, it is "True" by default and the program uploads all files with a certain extension in the directory and all its sub-directories.
