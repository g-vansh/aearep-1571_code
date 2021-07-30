# Zenodo Uploading Code

Python Directory Parsing and Uploading Code 

- File `run_script.py` does the following:
    1. Finds all files with a certain extension in a directory.
    2. Uploads them to `Zenodo` using their API.
    3. Generates a log file `error_log.txt` in the root directory to note any errors encountered from the Zenodo server.

- The code is platform agnostic, tested on Windows, and used in production on Linux. 

## How to run

```
python run_script.py (DIRECTORY) "(GLOBPAT)" APIKEY [DEPOSITID]
```
where parameters are as follows:

- `(DIRECTORY)`: directory containing the files to upload
- `(GLOBPAT)`: glob pattern for files to upload (e.g., `"*.7z"`). Should include the quotes.
- `APIKEY`: API key generated as per https://developers.zenodo.org/#authentication
- (optional) `DEPOSITID`: If a deposit has already been initiated manually on Zenodo, then specify it on the command line. Otherwise, a new deposit will be generated.

## Finalizing

The script only uploads the files. All metadata will need to be entered through the Zenodo web interface. The URL is printed to the console. Publishing the deposit is intentionally manual.

## Notes

- Relative paths have not been tested. They may work.
- The 4th argument is currently hard-coded into the script. 
- If you would like to search and upload the files from sub-directories in the directory as well, then change the value in Line 22 to "TRUE". 
    - Otherwise, it is "FALSE" by default and the program uploads all files with a certain extension in the directory, but none of its sub-directories.
