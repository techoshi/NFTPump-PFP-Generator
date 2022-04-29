import glob
import random
import shutil
import json
import asyncio
from sticher import stitch

def combineTypes(FileLocations):
    result = []
    FullArray = []
    startingNumber = 4100

    currentID = startingNumber
    for genType in FileLocations:
        thisGlob = glob.glob(genType["search"])

        for currentItem in thisGlob:
            currentID = currentID + 1
            FullArray.append({ "id": currentID, "type": genType["type"], "path" : currentItem, "image" : genType["image"]  })

    with open('src/output/xMartians/arraylist.json', 'w') as output_file:
        json.dump(FullArray, output_file)

    random.shuffle(FullArray)
    random.shuffle(FullArray)
    random.shuffle(FullArray)

    newID = startingNumber

    for currentFile in FullArray:  
        newID = newID + 1
        theID = 0
        with open(currentFile["path"], 'r') as infile:
            thisJson = json.load(infile)    
         
            external_url = thisJson['external_url']
            theID = (external_url.rsplit('/', 1))[1]
        
        shutil.copy(currentFile["image"] + "/" + str(theID) + ".png", "src/output/xMartians/images" + "/" + str(newID) + ".png" )

    newID = startingNumber

    for currentFile in FullArray:       
        newID = newID + 1
        strNewID = str(newID)
        with open(currentFile["path"], 'r') as infile:
            thisJson = json.load(infile)    
         
            external_url = thisJson['external_url']
            theID = (external_url.rsplit('/', 1))[1]
                        
            thisJson["description"] = "xMartian NFT"
            thisJson["name"] = "xMartian #" + strNewID
            thisJson["external_url"] = "https://xMartianNFT.com/"
            thisJson["image"] = "ipfs://QmXWCNYcBkKJBUYgyi22BSUL5f1qqk2UEVYTmFv4JQ9cLs/" + strNewID + ".png"
            thisJson["attributes"][0]["value"] = "Galaxy"
            thisJson["attributes"].append({
                "trait_type": "Gender",
                "value": currentFile["type"]
            })
            #del thisJson['combination'] 
            # del thisJson["attributes"][0]
            finalJSON = json.dumps(thisJson, indent=4)
            
            with open('src/output/xMartians/JSON/' + strNewID + '.json', 'w') as output_file:
                output_file.write(finalJSON) 


#allthefiles = glob.glob("src/output/xMartiansMale.20211111005517/json/*.json")

FileLocations = [{ 
    "type": "Male"
    , "image" : "src/output/1xMartians/4101-9800/male/images" 
    , "search" : "src/output/1xMartians/4101-9800/male/json/*.json"
}, { 
    "type": "Female"
    , "image" : "src/output/1xMartians/4101-9800/female/images" 
    , "search" : "src/output/1xMartians/4101-9800/female/json/*.json"
}]

combineTypes(FileLocations)