import glob
import json
import asyncio
from sticher import stitch

collectionLocation = "src/collections/StuffyBunny/" + "StuffyBunny" + "/"
outputFolder = "src/output/" + "Stuffy Bunny" + "/"
newOutputFolder = (
    "src/output/" + "Stuffy Bunny" + "/images2/"
)
endresultName = "mergeJsonStuffy"


async def merge_JsonFiles(filename):
    result = []
    for f1 in filename:
        with open(f1, "r") as infile:
            thisJson = json.load(infile)
            # = [x for x in thisJson["attributes"] if x['trait_type'] == 'Hat' and x['value'] == 'xMooney Cap']
            # if len(hasGad) > 0:
            external_url = thisJson["image"]
            theID = ((external_url.rsplit("/", 1))[1]).rsplit(".",1)[0]
            result.append(thisJson)

            backgroundLayer = thisJson["attributes"][0]["value"].replace(" ", "_")
            badgeLayer = thisJson["attributes"][1]["value"].replace(" ", "_")
            baseLayer = thisJson["attributes"][2]["value"].replace(" ", "_")
            eyesLayer = thisJson["attributes"][3]["value"].replace(" ", "_")
            mouthLayer = thisJson["attributes"][4]["value"].replace(" ", "_")
            faceAccLayer = thisJson["attributes"][5]["value"].replace(" ", "_") 
            hatLayer = thisJson["attributes"][6]["value"].replace(" ", "_")
            accLayer = thisJson["attributes"][7]["value"].replace(" ", "_")

            ArrayOfFiles = [
                collectionLocation + "Background/" + backgroundLayer + ".PNG",
                collectionLocation + "Badge/" + badgeLayer + ".PNG",
                collectionLocation + "Base/" + baseLayer + ".PNG",
                collectionLocation + "Eyes/" + eyesLayer + ".PNG",
                collectionLocation + "Mouth/" + mouthLayer + ".PNG",
                collectionLocation + "Face Accessory/" + faceAccLayer + ".PNG",
                collectionLocation + "Hat/" + hatLayer + ".PNG",
                collectionLocation + "Accessory/" + accLayer + ".PNG"
            ]

            asyncio.ensure_future(
                stitch(newOutputFolder, theID, ArrayOfFiles, 1050, 1250)
            )

    with open(outputFolder + endresultName + ".json", "w") as output_file:
        json.dump(result, output_file)


allthefiles = glob.glob(outputFolder + "newJSON/*.json")

asyncio.run(merge_JsonFiles(allthefiles))


# print(allthefiles)
