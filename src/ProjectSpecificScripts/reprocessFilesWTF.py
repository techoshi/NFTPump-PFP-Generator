import glob
import json
import asyncio
from sticher import stitch

# collectionLocation = "src/collections/WTF/" + "Female Cake Head" + "/"
# sourceJSONFolder = "src/output/WTF/" + "WTForks-Female Cake Head.20211223185839" + "/"
# outputFolder1 = ("src/output/WTF/output/" + "Female Cake Head" + "/")

# collectionLocation = "src/collections/WTF/" + "Female Samurai" + "/"
# sourceJSONFolder = "src/output/WTF/" + "WTForks-Female Japanese.20211223174102" + "/"
# outputFolder1 = ("src/output/WTF/output/" + "Female Samurai" + "/")

# collectionLocation = "src/collections/WTF/" + "Female Pizza Head" + "/"
# sourceJSONFolder = "src/output/WTF/" + "WTForks-Female Pizza Head.20211223231901" + "/"
# outputFolder1 = ("src/output/WTF/output/" + "Female Pizza Head" + "/")

# collectionLocation = "src/collections/WTF/" + "Female Space" + "/"
# sourceJSONFolder = "src/output/WTF/" + "WTForks-Female Space.20220114210735" + "/"
# outputFolder1 = ("src/output/WTF/output/" + "Female Space" + "/")

# collectionLocation = "src/collections/WTF/" + "Female Afro Head" + "/"
# sourceJSONFolder = "src/output/WTF/" + "WTForks-Female Afro Head.20211223170823" + "/"
# outputFolder1 = ("src/output/WTF/output/" + "Female Afro Head" + "/")

# collectionLocation = "src/collections/WTF/" + "Male Space" + "/"
# sourceJSONFolder = "src/output/WTF/" + "WTForks-Male Space.20220114220253" + "/"
# outputFolder1 = ("src/output/WTF/output/" + "Male Space" + "/")

# collectionLocation = "src/collections/WTF/" + "Male Afro Head" + "/"
# sourceJSONFolder = "src/output/WTF/" + "WTForks-Male Afro Head.20211223182559" + "/"
# outputFolder1 = ("src/output/WTF/output/" + "Male Afro Head" + "/")

# collectionLocation = "src/collections/WTF/" + "Male Crown" + "/"
# sourceJSONFolder = "src/output/WTF/" + "WTForks-Male Crown.20211223172453" + "/"
# outputFolder1 = ("src/output/WTF/output/" + "Male Crown" + "/")

# collectionLocation = "src/collections/WTF/" + "Male Dread Head" + "/"
# sourceJSONFolder = "src/output/WTF/" + "WTForks-Male Dread Head.20211223211403" + "/"
# outputFolder1 = ("src/output/WTF/output/" + "Male Dread Head" + "/")

# collectionLocation = "src/collections/WTF/" + "Male Christmas" + "/"
# sourceJSONFolder = "src/output/WTF/" + "WTForks-Male Christmas.20211223173654" + "/"
# outputFolder1 = ("src/output/WTF/output/" + "Male Christmas" + "/")

# collectionLocation = "src/collections/WTF/" + "Male Cake Head" + "/"
# sourceJSONFolder = "src/output/WTF/" + "WTForks-Male Cake Head.20211223222648" + "/"
# outputFolder1 = ("src/output/WTF/output/" + "Male Cake Head" + "/")

# collectionLocation = "src/collections/WTF/" + "Male Pizza Head" + "/"
# sourceJSONFolder = "src/output/WTF/" + "WTForks-Male Pizza Head.20220115231841" + "/"
# outputFolder1 = ("src/output/WTF/output/" + "Male Pizza Head" + "/")

# collectionLocation = "src/collections/WTF/" + "Female Curly Head" + "/"
# sourceJSONFolder = "src/output/WTF/" + "WTForks-Male Pizza Head.20220115231841" + "/"
# outputFolder1 = ("src/output/WTF/output/" + "Female Curly Head" + "/")

# collectionLocation = "src/collections/WTF/" + "Male Curly Head" + "/"
# sourceJSONFolder = "src/output/WTF/" + "WTForks-Male Curly Head.20220116032113" + "/"
# outputFolder1 = ("src/output/WTF/output/" + "Male Curly Head" + "/")

# collectionLocation = "src/collections/WTF/" + "Female Curly Head" + "/"
# sourceJSONFolder = "src/output/WTF/" + "WTForks-Female Curly Head.20220116035117" + "/"
# outputFolder1 = ("src/output/WTF/output/" + "Female Curly Head" + "/")

# collectionLocation = "src/collections/WTF/" + "Male Devil" + "/"
# sourceJSONFolder = "src/output/WTF/" + "WTForks-Male Devil.20220117192900" + "/"
# outputFolder1 = ("src/output/WTF/output/" + "Male Devil" + "/")


# collectionLocation = "src/collections/WTF/" + "Female Devil" + "/"
# sourceJSONFolder = "src/output/WTF/" + "WTForks-Female Devil.20220117193542" + "/"
# outputFolder1 = ("src/output/WTF/output/" + "Female Devil" + "/")


collectionLocation = "src/collections/WTF/" + "Female Dread Head" + "/"
sourceJSONFolder = "src/output/WTF/" + "WTForks-Female Dread Head.20220117194015" + "/"
outputFolder1 = ("src/output/WTF/output/" + "Female Dread Head" + "/")

# collectionLocation = "src/collections/WTF/" + "Female Backwards Bent Head" + "/"
# sourceJSONFolder = "src/output/WTF/" + "WTForks-Female Backwards Bent Head.20220117210832" + "/"
# outputFolder1 = ("src/output/WTF/output/" + "Female Backwards Bent Head" + "/")

# collectionLocation = "src/collections/WTF/" + "Male Backwards Bent Head" + "/"
# sourceJSONFolder = "src/output/WTF/" + "WTForks-Male Backwards Bent Head.20220117214643" + "/"
# outputFolder1 = ("src/output/WTF/output/" + "Male Backwards Bent Head" + "/")

# collectionLocation = "src/collections/WTF/" + "Male Sweatband" + "/"
# sourceJSONFolder = "src/output/WTF/" + "WTForks-Male Sweatband.20220117231809" + "/"
# outputFolder1 = ("src/output/WTF/output/" + "Male Sweatband" + "/")

# collectionLocation = "src/collections/WTF/" + "Female Sweatband" + "/"
# sourceJSONFolder = "src/output/WTF/" + "WTForks-Female Sweatband.20220118000353" + "/"
# outputFolder1 = ("src/output/WTF/output/" + "Female Sweatband" + "/")

# collectionLocation = "src/collections/WTF/" + "Male Bravo Head" + "/"
# sourceJSONFolder = "src/output/WTF/" + "WTForks-Male Bravo Head.20220118003416" + "/"
# outputFolder1 = ("src/output/WTF/output/" + "Male Bravo Head" + "/")

# collectionLocation = "src/collections/WTF/" + "Female Pigtail Head" + "/"
# sourceJSONFolder = "src/output/WTF/" + "WTForks-Female Pigtail Head.20220118004436" + "/"
# outputFolder1 = ("src/output/WTF/output/" + "Female Pigtail Head" + "/")

# collectionLocation = "src/collections/WTF/" + "Male Angel" + "/"
# sourceJSONFolder = "src/output/WTF/" + "WTForks-Male Angel.20220118010013" + "/"
# outputFolder1 = ("src/output/WTF/output/" + "Male Angel" + "/")

# collectionLocation = "src/collections/WTF/" + "Female Samurai" + "/"
# sourceJSONFolder = "src/output/WTF/" + "WTForks-Female Samurai.20220118132620" + "/"
# outputFolder1 = ("src/output/WTF/output/" + "Female Samurai" + "/")

# collectionLocation = "src/collections/WTF/" + "Female Angel" + "/"
# sourceJSONFolder = "src/output/WTF/" + "WTForks-Female Angel.20220119082214" + "/"
# outputFolder1 = ("src/output/WTF/output/" + "Female Angel" + "/")

# collectionLocation = "src/collections/WTF/" + "Male Samurai" + "/"
# sourceJSONFolder = "src/output/WTF/" + "WTForks-Male Samurai.20220119082920" + "/"
# outputFolder1 = ("src/output/WTF/output/" + "Male Samurai" + "/")

# collectionLocation = "src/collections/WTF/" + "Female Forward Bent" + "/"
# sourceJSONFolder = "src/output/WTF/" + "WTForks-Female Forward Bent.20220119094041" + "/"
# outputFolder1 = ("src/output/WTF/output/" + "Female Forward Bent" + "/")

# collectionLocation = "src/collections/WTF/" + "Male Forward Bent" + "/"
# sourceJSONFolder = "src/output/WTF/" + "WTForks-Male Forward Bent.20220119084011" + "/"
# outputFolder1 = ("src/output/WTF/output/" + "Male Forward Bent" + "/")

# collectionLocation = "src/collections/WTF/" + "Male Basic Head" + "/"
# sourceJSONFolder = "src/output/WTF/" + "WTForks-Male Basic Head.20220120002116" + "/"
# outputFolder1 = ("src/output/WTF/output/" + "Male Basic Head" + "/")

# collectionLocation = "src/collections/WTF/" + "Female Basic Head" + "/"
# sourceJSONFolder = "src/output/WTF/" + "WTForks-Female Basic Head.20220120004007" + "/"
# outputFolder1 = ("src/output/WTF/output/" + "Female Basic Head" + "/")

# collectionLocation = "src/collections/WTF/" + "Female Thanksgiving" + "/"
# sourceJSONFolder = "src/output/WTF/" + "WTForks-Female Thanksgiving.20220120223031" + "/"
# outputFolder1 = ("src/output/WTF/output/" + "Female Thanksgiving" + "/")

# collectionLocation = "src/collections/WTF/" + "Male Thanksgiving" + "/"
# sourceJSONFolder = "src/output/WTF/" + "WTForks-Male Thanksgiving.20220120222959" + "/"
# outputFolder1 = ("src/output/WTF/output/" + "Male Thanksgiving" + "/")

newOutputFolder = (outputFolder1 + "images/")
jsonOutputFolder = (outputFolder1 + "json/")
gender = "Female"
endresultName = "total"

async def writeJSONFileForMint(jsonFilesFolder, stringCurrentID, json_object):
    with open(jsonFilesFolder + "/" + stringCurrentID + ".json", "w") as outfile:
        outfile.write(json_object)

async def merge_JsonFiles(filename):
    result = []
    for f1 in filename:
        with open(f1, "r") as infile:
            thisJson = json.load(infile)
            # = [x for x in thisJson["attributes"] if x['trait_type'] == 'Hat' and x['value'] == 'xMooney Cap']
            # if len(hasGad) > 0:
            external_url = thisJson["external_url"]
            theID = (external_url.rsplit("/", 1))[1]
            result.append(thisJson)

            wtfType = thisJson["attributes"][0]["value"]
            if "Japanese" in wtfType:
                wtfType = wtfType.replace("Japanese", "Samurai", 1)
                thisJson["attributes"][0]["value"] = wtfType

            backgroundLayer = thisJson["attributes"][1]["value"]
            if backgroundLayer == 'Fire Ice':
                backgroundLayer = 'Fire_Ice'
            if backgroundLayer == 'Dread Head Gold':
                backgroundLayer = 'Dread_Head Gold'
            if backgroundLayer == 'Backwards Bent (M)':
                backgroundLayer = 'Backwards_Bent_(M)'

            headLayer = thisJson["attributes"][2]["value"]
            if "Japanese" in headLayer:
                thisJson["attributes"][2]["value"] = headLayer.replace("Japanese", "Samurai", 1) + " Headband"
                headLayer = thisJson["attributes"][2]["value"]
            if headLayer == 'Black Chocolate Cake ':
                headLayer = 'Black Chocolate Cake'

            tattooLayer = thisJson["attributes"][3]["value"]
            if tattooLayer == 'Cherry ':
                tattooLayer = 'Cherry'  

            eyesLayer = thisJson["attributes"][4]["value"]
            if eyesLayer == 'Closed ':
                eyesLayer = 'Closed'  
            if eyesLayer == 'Hypnotic':
                eyesLayer = 'Hypnotized'      

            mouthLayer = thisJson["attributes"][5]["value"]                     
            
            clothingLayer = thisJson["attributes"][6]["value"]
            if clothingLayer == 'Male Clothing  2':
                clothingLayer = 'Male_Clothing_ 2'
            if clothingLayer == 'I  3 Nft s Hoodie':
                clothingLayer = 'I _3 Nft_s Hoodie'
            if clothingLayer == 'Painter s Apron':
                clothingLayer = 'Painter_s Apron'
            if clothingLayer == 'Golden Suit ':
                clothingLayer = 'Golden Suit'
            
            accessoryLayer = thisJson["attributes"][7]["value"]
            #extrasLayer = thisJson["attributes"][8]["value"]

            ArrayOfFiles = [
                collectionLocation + "Background/" + backgroundLayer + ".png",
                collectionLocation + "Head/" + headLayer + ".png",
                collectionLocation + "Tattoo/" + tattooLayer + ".png",                
                collectionLocation + "Eyes/" + eyesLayer + ".png",
                collectionLocation + "Mouth/" + mouthLayer + ".png",
                collectionLocation + "Clothing/" + clothingLayer + ".png",
                collectionLocation + "Accessory/" + accessoryLayer + ".png",
                #collectionLocation + "Extras/" + extrasLayer + ".png"
            ]

            thisJson["attributes"][0]["trait_type"] = "WTFork Type"
            thisJson["attributes"].append({  
                "trait_type": "Gender",
                "value": gender })
            thisJson["description"] = "WTForksNFT Collection"
            thisJson["external_url"] = "wtforksnft.com"
            thisJson["image"] = "ipfs://QmQjz8JcdhfWkVGpRMD2q93bdr6xgA9btaTK4XzG3pvnda/" + theID + ".png"
            thisJson["name"] = "WTFork"

            json_object = json.dumps(thisJson, indent=4)
            #asyncio.ensure_future(writeJSONFileForMint(jsonOutputFolder, theID, json_object))
            asyncio.ensure_future(stitch(newOutputFolder, theID, ArrayOfFiles, 2360, 1640))

    with open(outputFolder1 + endresultName + ".json", "w") as output_file:
        json.dump(result, output_file)


allthefiles = glob.glob(sourceJSONFolder + "json/*.json")

asyncio.run(merge_JsonFiles(allthefiles))


# print(allthefiles)
