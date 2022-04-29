import json
import os
import glob

json1 = {
    "attributes": [
        {
            "trait_type": "Stuffy Bunny",
            "value": "Custom"
        }
    ],
    "description": "Stuffy Bunny Collection",
    "external_url": "https://www.stuffybunnynft.com",
    "image": "ipfs://QmSFpGP4td2B26tM3wtBxdfw9hybKowq6gbrNizQSm9wSj",
    "name": "Custom Stuffy Bunny"#,
    #"animation_url": "ipfs://QmPFZGSXroikibbFAktxtDfRnzTKhQDAziBvdKwhW75GTx"
}


def writeJSONFileForMint(jsonFilesFolder, stringCurrentID, json_object):
    json_object = json.dumps(json_object, indent=4)
    with open(jsonFilesFolder + "/" + str(stringCurrentID) + ".json", "w") as outfile:
        outfile.write(json_object)

for x in range(1, 350):
    writeJSONFileForMint("src/output/sb", x, json1)

#print(glob.glob("src/output/NFTCC/*.txt"))