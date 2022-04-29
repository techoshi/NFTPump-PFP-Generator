import glob
import random
import shutil
import json
import asyncio
from sticher import stitch

def combineTypes(FileLocations):
    result = []
    FullArray = []
    currentID = 0
    for genType in FileLocations:
        thisGlob = glob.glob(genType["search"])

        for currentItem in thisGlob:
            currentID = currentID + 1
            FullArray.append({ "id": currentID, "type": genType["type"], "path" : currentItem, "image" : genType["image"]  })

    with open('src/output/NFTCC-Males.20220103123218/arraylist.json', 'w') as output_file:
        json.dump(FullArray, output_file)

    random.shuffle(FullArray)
    random.shuffle(FullArray)
    random.shuffle(FullArray)

    newID = 0

    for currentFile in FullArray:  
        newID = newID + 1
        theID = 0
        with open(currentFile["path"], 'r') as infile:
            thisJson = json.load(infile)    
         
            external_url = thisJson['external_url']
            theID = (external_url.rsplit('/', 1))[1]
        
        shutil.copy(currentFile["image"] + "/" + str(theID) + ".png", "src/output/NFTCC/images" + "/" + str(newID) + ".png" )

    newID = 0

    for currentFile in FullArray:       
        newID = newID + 1
        strNewID = str(newID)
        with open(currentFile["path"], 'r') as infile:
            thisJson = json.load(infile)    
         
            external_url = thisJson['external_url']
            theID = (external_url.rsplit('/', 1))[1]
                        
            thisJson["description"] = "NFTCC"
            thisJson["name"] = "NFTCC #" + strNewID
            thisJson["external_url"] = "https://www.thenftcc.io"
            thisJson["image"] = "ipfs://QmXWCNYcBkKJBUYgyi22BSUL5f1qqk2UEVYTmFv4JQ9cLs/" + strNewID + ".png"
            #del thisJson['combination'] 
            del thisJson["attributes"][0]
            finalJSON = json.dumps(thisJson, indent=4)
            
            with open('src/output/NFTCC/JSON/' + strNewID + '.json', 'w') as output_file:
                output_file.write(finalJSON) 


#allthefiles = glob.glob("src/output/xMartiansMale.20211111005517/json/*.json")

FileLocations = [{ 
    "type": "Male"
    , "image" : "src/output/NFTCC-Males.20220103123218/images"
    , "search" : "src/output/NFTCC-Males.20220103123218/json/*.json"
}, { 
    "type": "Female"
    , "image" : "src/output/NFTCC-Females.20220103171139/images" 
    , "search" : "src/output/NFTCC-Females.20220103171139/json/*.json"  
}]

combineTypes(FileLocations)