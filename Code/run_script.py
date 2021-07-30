# Import Packages
import glob, os
import requests
import json
import ntpath

# Change Directory To The Root Directory, please ensure that there is no slash symbol in the end
root_dir = "C:/Users/vg224_RS/sample_folder"
os.chdir(root_dir)
search_path = root_dir + "/**/"

# Extension To Be Searched
ext = "*.zip"
search_pattern = search_path + ext

# Change Access Token
ACCESS_TOKEN = "CHANGE_ME"

# Would you like to search the subdirectories in the directory as well? 
# "True" for Yes, "False" for No. 
# "True" by default.
subdir = True 

# Configuring Script For Zenodo Upload
params = {'access_token': ACCESS_TOKEN}
headers = {"Content-Type": "application/json"}
r = requests.post('https://zenodo.org/api/deposit/depositions',params = params, headers = headers, json = {})
bucket_url = r.json()['links']['bucket']

# Parsing through each file and uploading it
for file in glob.glob(search_pattern, recursive = subdir):
    filename = ntpath.basename(file)
    print("Starting upload for file: "+filename)
    path = os.path.abspath(file)

    # Uploading each file
    with open(path, "rb") as fp:
        r = requests.put("%s/%s" % (bucket_url, filename),data = fp,params = params)

        # Checking if upload was successful
        if (r.status_code!=200):
            print("Error Uploading File: {0}, Error Code: {1}".format(filename,r.status_code))

            # Logging an unsuccessful attempt in root directory
            with open((root_dir+"/error_log.txt"),"a+") as logger_file:
                logger_file.write(("Error Uploading File: {0}, Error Code: {1}".format(file,r.status_code))+"\n")
        else:
            print("Uploading Successful For: "+filename)

# Adding documentation for debugging errors
with open((root_dir+"/error_log.txt"),"a+") as logger_file:
    logger_file.write("Please check the descriptions of the error codes at: https://developers.zenodo.org/#http-status-codes"+"\n")

        
    
    