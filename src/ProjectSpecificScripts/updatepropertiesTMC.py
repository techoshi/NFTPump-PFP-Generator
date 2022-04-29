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
         
            findID = thisJson['image']
            theID = (findID.rsplit('/', 1))[1]
            theID = (theID.rsplit('.', 1))[0]
                        
           thisJson["description"] = "The Monster Community"
           # thisJson["name"] = "Stuffy Bunny #" + theID
           thisJson["external_url"] = "https://www.themonstercommunity.com"
            thisJson["image"] = "ipfs://QmQB9HPRzXEDD7bNQjPuZ2EKYofm8oXyMotMvfLYLwUJgy/" + theID + ".png"
           # del thisJson['combination'] 
            #del thisJson["attributes"][0]
            finalJSON = json.dumps(thisJson, indent=4)
            with open('src/output/sb/sb/Update 1/json1/' + theID + '.json', 'w') as output_file:
                output_file.write(finalJSON) 
                        

allthefiles = glob.glob("src/output/TMC.20220406203830/json/*.json")

merge_JsonFiles(allthefiles)

def writeJSONFileForMint(jsonFilesFolder, stringCurrentID, json_object):
    with open(jsonFilesFolder + "/" + stringCurrentID + ".json", "w") as outfile:
        outfile.write(json_object)
#print(allthefiles)