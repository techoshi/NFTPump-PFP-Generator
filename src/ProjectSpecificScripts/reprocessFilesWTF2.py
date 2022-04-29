import glob
import json
import asyncio
import os
import threading
from stichersquare import stitch

CollectionList = [
    # "Female Cake Head",
    # "Female Samurai",
    # "Female Pizza Head",
    # "Female Space",
    # "Female Afro Head",
    # "Female Curly Head",
    # "Female Devil",
    # "Female Dread Head",
    # "Female Backwards Bent Head", 
    # "Female Sweatband", 
    # "Female Pigtail Head", 
    # "Female Samurai", 
    # "Female Angel", 
    # "Female Forward Bent", 
    # "Female Basic Head", 
    # "Female Thanksgiving",
    # "Male Cake Head",
    # "Male Samurai",
    # "Male Pizza Head",
    # "Male Space",
    # "Male Afro Head",
    # "Male Curly Head",
    # "Male Devil",
    # "Male Dread Head",
    # "Male Backwards Bent Head", 
    # "Male Sweatband", 
    # "Male Bravo Head", 
    # "Male Samurai", 
    # "Male Angel", 
    # "Male Forward Bent", 
    # "Male Basic Head", 
    # "Male Thanksgiving",
    #"Male Crown",
    #"Female Crown",
    # "Male Christmas",
    # "Female Christmas"
]


gender = "Male"
endresultName = "total"

rootCollectionDirectory = "src/collections/WTF/"
rootSourceJSONFolder = "src/output/WTF/output/"
rootOutput = "src/output/WTF/" + "Formatted Output/"

async def cycleThroughCollections():
    for thisCollection in CollectionList:

        collectionLocation = rootCollectionDirectory + thisCollection + "/"
        sourceJSONFolder = rootSourceJSONFolder + thisCollection + "/"
        outputFolder = rootOutput + thisCollection + "/"

        if not os.path.exists(outputFolder):
            os.makedirs(outputFolder)


        listfiles = glob.glob(sourceJSONFolder + "json/*.json")
        newOutputFolder = (outputFolder + "images/")
        jsonOutputFolder = (outputFolder + "json/")

        if not os.path.exists(newOutputFolder):
            os.makedirs(newOutputFolder)
        if not os.path.exists(jsonOutputFolder):
            os.makedirs(jsonOutputFolder)

        await merge_JsonFiles(listfiles, collectionLocation, outputFolder, newOutputFolder, jsonOutputFolder)


async def writeJSONFileForMint(jsonFilesFolder, stringCurrentID, json_object):
     x = threading.Thread(target=writeJsonFile, args=(jsonFilesFolder,stringCurrentID,json_object,))
     x.start()
    #writeJsonFile(jsonFilesFolder, stringCurrentID, json_object)

def writeJsonFile(jsonFilesFolder, stringCurrentID, json_object):
    with open(jsonFilesFolder + "/" + stringCurrentID + ".json", "w") as outfile:
        outfile.write(json_object)

async def merge_JsonFiles(filename, collectionLocation, outputFolder, newOutputFolder, jsonOutputFolder):
    result = []
    for f1 in filename:
        with open(f1, "r") as infile:
            thisJson = json.load(infile)
            # = [x for x in thisJson["attributes"] if x['trait_type'] == 'Hat' and x['value'] == 'xMooney Cap']
            # if len(hasGad) > 0:
            external_url = thisJson["image"]
            theID = (external_url.rsplit("/", 1))[1].rsplit(".", 1)[0]
            
            if 1 == 1: #theID == "1" or theID == "38" or theID == "7" or theID == "13":
                wtfType = ""
                propBackground = ""
                propHead = ""
                propEyes = ""
                propMouth = ""
                propTattoo = ""
                propClothing = ""
                propAccessory = ""
                propExtras = ""
                propGender = ""

                for jsonProperties in thisJson["attributes"]:
                    if jsonProperties["trait_type"] == "WTFork Type":
                        wtfType = jsonProperties["value"]
                    if jsonProperties["trait_type"] == "Background":
                        propBackground = jsonProperties["value"]
                        if propBackground == 'Fire Ice':
                            propBackground = 'Fire_Ice'
                        if propBackground == 'Dread Head Gold':
                            propBackground = 'Dread_Head Gold'
                        if propBackground == 'Backwards Bent (M)':
                            propBackground = 'Backwards_Bent_(M)'
                    if jsonProperties["trait_type"] == "Head":
                        propHead = jsonProperties["value"]
                        if propHead == 'Black Chocolate Cake ':
                            propHead = 'Black Chocolate Cake'
                    if jsonProperties["trait_type"] == "Eyes":
                        propEyes = jsonProperties["value"]
                        if propEyes == 'Closed ':
                            propEyes = 'Closed'  
                        if propEyes == 'Hypnotic':
                            propEyes = 'Hypnotized'
                    if jsonProperties["trait_type"] == "Mouth":
                        propMouth = jsonProperties["value"]
                    if jsonProperties["trait_type"] == "Tattoo":
                        propTattoo = jsonProperties["value"]
                        if propTattoo == 'Cherry ':
                            propTattoo = 'Cherry'
                    if jsonProperties["trait_type"] == "Clothing":
                        propClothing = jsonProperties["value"]
                        if propClothing == 'Male Clothing  2':
                            propClothing = 'Male_Clothing_ 2'
                        if propClothing == 'I  3 Nft s Hoodie':
                            propClothing = 'I _3 Nft_s Hoodie'
                        if propClothing == 'Painter s Apron':
                            propClothing = 'Painter_s Apron'
                        if propClothing == 'Golden Suit ':
                            propClothing = 'Golden Suit'
                    if jsonProperties["trait_type"] == "Accessory":
                        propAccessory = jsonProperties["value"]
                    if jsonProperties["trait_type"] == "Extras":
                        propExtras = jsonProperties["value"]
                    if jsonProperties["trait_type"] == "Gender":
                        propGender = jsonProperties["value"]

                ArrayOfFiles = [
                    collectionLocation + "Background/" + propBackground + ".png",
                    collectionLocation + "Head/" + propHead + ".png",
                    collectionLocation + "Tattoo/" + propTattoo + ".png",                
                    collectionLocation + "Clothing/" + propClothing + ".png",
                    collectionLocation + "Eyes/" + propEyes + ".png",
                    collectionLocation + "Mouth/" + propMouth + ".png"       
                ]

                thisJson["attributes"] = []

                thisJson["attributes"].append({ "trait_type": "Gender", "value": propGender })
                thisJson["attributes"].append({ "trait_type": "WTFork Type", "value": wtfType })
                thisJson["attributes"].append({ "trait_type": "Background", "value": propBackground })
                thisJson["attributes"].append({ "trait_type": "Head", "value": propHead })
                thisJson["attributes"].append({ "trait_type": "Tattoo", "value": propTattoo })
                thisJson["attributes"].append({ "trait_type": "Clothing", "value": propClothing })
                thisJson["attributes"].append({ "trait_type": "Eyes", "value": propEyes })
                thisJson["attributes"].append({ "trait_type": "Mouth", "value": propMouth })

                if propAccessory != "":
                    ArrayOfFiles.append(collectionLocation + "Accessory/" + propAccessory + ".png")
                    thisJson["attributes"].append({ "trait_type": "Accessory", "value": propAccessory })

                if propExtras != "":
                    ArrayOfFiles.append(collectionLocation + "Extras/" + propExtras + ".png")
                    thisJson["attributes"].append({ "trait_type": "Extras", "value": propExtras })
            
                thisJson["description"] = "WTForksNFT Collection"
                thisJson["external_url"] = "wtforksnft.com"
                thisJson["image"] = "ipfs://QmQjz8JcdhfWkVGpRMD2q93bdr6xgA9btaTK4XzG3pvnda/" + theID + ".png"
                thisJson["name"] = "WTFork"

                result.append(thisJson)

                json_object = json.dumps(thisJson, indent=4)
                asyncio.ensure_future(writeJSONFileForMint(jsonOutputFolder, theID, json_object))
                asyncio.ensure_future(stitch(newOutputFolder, theID, ArrayOfFiles, 1474, 1024))

    final_json_object = json.dumps(result, indent=4)
    with open(outputFolder + endresultName + ".json", "w") as output_file:
        output_file.write(final_json_object)
        #json.dump(result, output_file)

asyncio.run(cycleThroughCollections())


# print(allthefiles)
