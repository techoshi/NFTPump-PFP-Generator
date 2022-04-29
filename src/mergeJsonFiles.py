import glob
import json
import asyncio
from sticher import stitch

def merge_JsonFiles(filename):
    result = []
    for f1 in filename:
        with open(f1, 'r') as infile:
            thisJson = json.load(infile)
            hasGad = [x for x in thisJson["attributes"] if x['trait_type'] == 'Hat' and x['value'] == 'xMooney Cap']
            if len(hasGad) > 0:
                external_url = thisJson['external_url']
                theID = (external_url.rsplit('/', 1))[1]
                result.append(thisJson)
                ArrayOfFiles = [
                    'src/collections/xMooneyMale/Male/Background/' +  thisJson["attributes"][1]['value'].replace(" ", "_") + ".png",
                    'src/collections/xMooneyMale/Male/Base/' +  thisJson["attributes"][2]['value'].replace(" ", "_") + ".png",
                    'src/collections/xMooneyMale/Male/Clothes/' +  thisJson["attributes"][3]['value'].replace(" ", "_") + ".png",
                    'src/collections/xMooneyMale/Male/Accessories/' +  thisJson["attributes"][6]['value'].replace(" ", "_") + ".png",
                    'src/collections/xMooneyMale/Male/Hat/' +  thisJson["attributes"][4]['value'].replace(" ", "_") + ".png",
                    'src/collections/xMooneyMale/Male/Mouths/' +  thisJson["attributes"][5]['value'].replace(" ", "_") + ".png"                   
                ]

                stitch('src/output/xMartiansMale.20211111005517/replacehats' + "/", theID, ArrayOfFiles, 900, 900)

    with open('src/output/xMartiansMale.20211111005517/mergeJsonHats.json', 'w') as output_file:
        json.dump(result, output_file)

allthefiles = glob.glob("src/output/xMartiansMale.20211111005517/json/*.json")

merge_JsonFiles(allthefiles)



#print(allthefiles)