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
         
            #findID = thisJson['image']
            #theID = (findID.rsplit('/', 1))[1]
            #theID = (theID.rsplit('.', 1))[0]
                        
            # thisJson["description"] = "Cthulhu Collection"
            # thisJson["name"] = "Cthulhu #" + theID
            #thisJson["external_url"] = "https://public-pre-ipfs.s3.us-east-1.amazonaws.com/xmartians/images/" + theID + ".png"
            #thisJson["image"] = "https://public-pre-ipfs.s3.us-east-1.amazonaws.com/xmartians/images/" + theID + ".png"
            # thisJson["animation_url"] = "ipfs://QmPFZGSXroikibbFAktxtDfRnzTKhQDAziBvdKwhW75GTx"
            # del thisJson['combination'] 
            #del thisJson["attributes"][0]

            result.append(thisJson)
            #finalJSON = json.dumps(thisJson, indent=4)
            #with open('src/output/xMartians/json2/' + theID + '.json', 'w') as output_file:
            #    output_file.write(finalJSON) 
        
    finalJSON2 = json.dumps(result, indent=4)
    with open('src/output/xMartians/all.json', 'w') as output_file:
        output_file.write(finalJSON2) 
                        

allthefiles = glob.glob("src/output/xMartians/json/*.json")

merge_JsonFiles(allthefiles)

def writeJSONFileForMint(jsonFilesFolder, stringCurrentID, json_object):
    with open(jsonFilesFolder + "/" + stringCurrentID + ".json", "w") as outfile:
        outfile.write(json_object)
#print(allthefiles)