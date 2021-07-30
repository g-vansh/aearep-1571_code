# AEAREP-1571 Zenodo Uploading Code
Python Directory Parsing and Uploading Code for AEAREP-1571

- File `run_script.py` contains code which does the following:
    1. Finds all files with a certain extension in a directory.
    2. Uploads them to `Zenodo` using their API.

- The code is platform agnostic, written in Windows, but is intended to run on Linux. 

Manual Modification Instructions:
- The path for the directory to be searched can be changed in Line 8.
- The extension to be searched can be changed in Line 9. 