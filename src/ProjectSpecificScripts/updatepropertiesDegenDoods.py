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
                        
           # thisJson["description"] = "Stuffy Bunny Collection"
           # thisJson["name"] = "Stuffy Bunny #" + theID
           # thisJson["external_url"] = "https://www.stuffybunnynft.com"
            thisJson["image"] = "ipfs://QmdU2RbGqaAcv9CVw5WFsTEtkeJfLtMynXmgbu67Xk9sts/" + theID + ".png"
           # del thisJson['combination'] 
            #del thisJson["attributes"][0]
            thisIndex = 0
            for currentAttribute in thisJson["attributes"]:
                thisJson["attributes"][thisIndex]["value"] = currentAttribute["value"].title()
                thisIndex = thisIndex + 1

            finalJSON = json.dumps(thisJson, indent=4)
            with open('src/output/dgen.20220130212242/json2/' + theID + '.json', 'w') as output_file:
                output_file.write(finalJSON) 
                        

allthefiles = glob.glob("src/output/dgen.20220130212242/json/*.json")

merge_JsonFiles(allthefiles)

def writeJSONFileForMint(jsonFilesFolder, stringCurrentID, json_object):
    with open(jsonFilesFolder + "/" + stringCurrentID + ".json", "w") as outfile:
        outfile.write(json_object)
#print(allthefiles)