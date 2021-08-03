# Import Packages
import os
import requests
import json
import pandas as pd
import fnmatch

# Change Directory To The Download Directory, please ensure that there is no slash symbol in the end
root_dir = "C:/Users/vg224_RS"
os.chdir(root_dir)

# Glob Pattern To Be Searched
search_pattern = "*.json"

# Deposition ID, Is The Numeric Part In The Deposit URL 
# For Ex.: "https://zenodo.org/deposit/5148837". "5148837" is the Deposition ID
# Please enter in a String format
depo_id = "5148837"

# Change Access Token
ACCESS_TOKEN = "CHANGE_ME"

# Accessing List Of Files
params = {'access_token': ACCESS_TOKEN}
r = requests.get("https://zenodo.org/api/deposit/depositions/{}/files".format(depo_id),params = params)
df = pd.read_json(r.content)

# Creating a dataframe of file names
df = df.drop(["checksum","filesize","id"], axis = 1)
df["links"] = df["links"].map(lambda x: x["download"])
df["filepath"] = df["filename"].map(lambda x: root_dir+"/"+x)
df = df.set_index(["filename"])

# Downloading Code 
for fname in fnmatch.filter(df.index, search_pattern):
        url = df.loc[fname][0]
        fp = df.loc[fname][1]
        r = requests.get(url,params = params)
        with open(fp,"wb") as f:
            f.write(r.content)
            
            # Checking if download was successful
            if (r.status_code!=200):
                print("Error Downloading File: {0}, Error Code: {1}".format(fname,r.status_code))

                # Logging an unsuccessful attempt in root directory
                with open((root_dir+"/download_error_log.txt"),"a+") as logger_file:
                    logger_file.write(("Error Downloading File: {0}, Error Code: {1}".format(fp,r.status_code))+"\n")
            else:
                print("Downloading Successful For: "+fname)
                
# Adding documentation for debugging errors
with open((root_dir+"/download_error_log.txt"),"a+") as logger_file:
    logger_file.write("Please check the descriptions of the error codes at: https://developers.zenodo.org/#http-status-codes"+"\n")