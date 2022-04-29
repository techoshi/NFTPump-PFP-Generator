import glob
import json
import random
import asyncio
from sticher import stitch

def merge_JsonFiles(allFiles):
    result = []
    folder = "Female"

    for currentFile in allFiles:       
        print(currentFile)              
        with open(currentFile, 'r') as infile:
            thisJson = json.load(infile)    
         
        #     findID = thisJson['image']
            theID = (currentFile.rsplit('/', 1))[1]
            theID = (theID.rsplit('\\', 1))[1]
            theID = (theID.rsplit('.', 1))[0]
            print(theID)   
        #     theID = (theID.rsplit('.', 1))[0]
                        
        #    # thisJson["description"] = "Stuffy Bunny Collection"
            thisJson["name"] = "#" + theID
        #    # thisJson["external_url"] = "https://www.stuffybunnynft.com"
            thisJson["image"] = "https://wtforks-general.s3.amazonaws.com/images/" + theID + ".png"
        #    # del thisJson['combination'] 
        #     #del thisJson["attributes"][0]
            finalJSON = json.dumps(thisJson, indent=4)
            with open('src/output/WTF/Formatted Output/_/json/' + theID + '.json', 'w') as output_file:
                output_file.write(finalJSON) 
                        

allthefiles = glob.glob("src/output/WTF/Formatted Output/First 120/json/*.json")

merge_JsonFiles(allthefiles)

def writeJSONFileForMint(jsonFilesFolder, stringCurrentID, json_object):
    with open(jsonFilesFolder + "/" + stringCurrentID + ".json", "w") as outfile:
        outfile.write(json_object)
#print(allthefiles)