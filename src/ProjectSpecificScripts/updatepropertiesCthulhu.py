import glob
import json
import random
import asyncio
from sticher import stitch

def merge_JsonFiles(allFiles):
    result = []
    folder = "Female"

    for currentFile in allFiles:       

        with open(currentFile, 'r') as infile:
            thisJson = json.load(infile)    
         
            external_url = thisJson['external_url']
            theID = (external_url.rsplit('/', 1))[1]
                        
            thisJson["description"] = "Cthulhu Collection"
            thisJson["name"] = "Cthulhu #" + theID
            thisJson["external_url"] = ""
            thisJson["image"] = "ipfs://QmWKcs7gYtMKcfPzMPS7q7D7mPf6tN1QTjjjRStnPY9Ee5/" + theID + ".png"
            thisJson["animation_url"] = "ipfs://QmPFZGSXroikibbFAktxtDfRnzTKhQDAziBvdKwhW75GTx"
            del thisJson['combination'] 
            del thisJson["attributes"][0]
            finalJSON = json.dumps(thisJson, indent=4)
            with open('src/output/Cthulhu.20211215035307/newJSON/' + theID + '.json', 'w') as output_file:
                output_file.write(finalJSON) 
                        

allthefiles = glob.glob("src/output/Cthulhu.20211215035307/json/*.json")

merge_JsonFiles(allthefiles)

def writeJSONFileForMint(jsonFilesFolder, stringCurrentID, json_object):
    with open(jsonFilesFolder + "/" + stringCurrentID + ".json", "w") as outfile:
        outfile.write(json_object)
#print(allthefiles)