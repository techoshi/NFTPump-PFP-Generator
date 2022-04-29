import glob
import json
import random
import asyncio
from sticher import stitch

def merge_JsonFiles(filename):
    result = []
    folder = "Female"

    Levels = {
        # "Male" : [
        #     {
        #         "Level" : "Hyper Rare",
        #         "Count" : 75,
        #         "Used" : 0
        #     }
        # ],
        # "Female" : [
        #     {
        #         "Level" : "Hyper Rare",
        #         "Count" : 75,
        #         "Used" : 0
        #     }
        # ],
        "Male" : [
            {
                "Level" : "Galaxy",
                "Count" : 3900,
                "Used" : 0
            },
            {
                "Level" : "Nebula",
                "Count" : 1700,
                "Used" : 0
            },
            {
                "Level" : "Supernova",
                "Count" : 1050,
                "Used" : 0
            }
        ],
        "Female" : [
            {
                "Level" : "Galaxy",
                "Count" : 1800,
                "Used" : 0
            },
            {
                "Level" : "Nebula",
                "Count" : 800,
                "Used" : 0
            },
            {
                "Level" : "Supernova",
                "Count" : 400,
                "Used" : 0
            }
        ]
    }

    for f1 in filename:       

        with open(f1, 'r') as infile:
            thisJson = json.load(infile)    
         
            external_url = thisJson['external_url']
            theID = (external_url.rsplit('/', 1))[1]
            thisSlot = 0
            # while True:
            #     thisSlot =random.randint(0,2)
            #     maxCount = Levels[folder][thisSlot]["Count"]
            #     nextCount = (Levels[folder][thisSlot]["Used"]+1)

            #     if nextCount <= maxCount:                    
            #         break

            thisSlot = 0

            if Levels[folder][thisSlot]["Level"] != 'Galaxy':
                print(Levels[folder][thisSlot]["Level"] + theID)

            Levels[folder][thisSlot]["Used"] = Levels[folder][thisSlot]["Used"]+1
            thisJson["attributes"][0]['value'] = Levels[folder][thisSlot]["Level"]
            thisJson["attributes"].append({ "trait_type": "Gender", "value": folder })
            thisJson["description"] = "xMartian Collection One"
            del thisJson['combination'] 
            finalJSON = json.dumps(thisJson, indent=4)
            with open('src/output/newJSON/' + theID + '.json', 'w') as output_file:
                output_file.write(finalJSON) 
                        

allthefiles = glob.glob("src/output/xMartiansHyperFemale.20211111014300/json/*.json")

merge_JsonFiles(allthefiles)


def writeJSONFileForMint(jsonFilesFolder, stringCurrentID, json_object):
    with open(jsonFilesFolder + "/" + stringCurrentID + ".json", "w") as outfile:
        outfile.write(json_object)
#print(allthefiles)