from lowerExtensions import renameFileExtensionsInDirectoryToLowerCase
import json

def CreateJSONFile(baseType, layerBase):
    thisGenJSON = {
        "type": baseType,
        "folder": baseType + "/",
        "max": 500,
        "meta": [],
        "layers": [],
        "extras": {
            "tiers": [{"type": 1}]
        }
    }

    baseJSON = {
        "Object": {
            "type": [
                
            ]
        }
    }

    for layerType in layerBase:
        
        layerBase = {
            "layer": layerType["type"],
            "folder": layerType["type"] + "/",
            "options": layerType[ "options"]
        }

        thisGenJSON["layers"].append(layerBase)

    #thisGenJSON["layers"] = baseJSON

    Final = {
        "Object":{
            "types" : [thisGenJSON]
        } 
    }


    with open("src/collections/WTF" + "/WTForks-" + baseType + ".json", "w") as outfile:
        outfile.write(json.dumps(Final, indent=4))


GenericFemales = [
    'Female Afro Head',
    'Female Backwards Bent Head',
    'Female Basic Head',
    'Female Cake Head',
    'Female Crown',
    'Female Curly Head',
    'Female Dread Head',
    'Female Forward Bent',
    'Female Pigtail Head',
    'Female Pizza Head',
    'Female Sweatband Head',
    'Male Afro Head',
    'Male Backwards Bent Head',
    'Male Basic Head',
    'Male Bravo Head',
    'Male Cake Head',
    'Male Crown',
    'Male Curly Head',
    'Male Dread Head',
    'Male Forward Bent',
    'Male Pizza Head',
    'Male Sweatband'
]

CurrentType = []

# for thisType in GenericFemales:
#     CurrentType = []
#     CurrentType.append({ "type": "Background", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/WTF/" + thisType + "/Background")})
#     CurrentType.append({ "type": "Head", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/WTF/" + thisType + "/Head")})
#     CurrentType.append({ "type": "Eyes", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/WTF/" + thisType + "/Eyes")})
#     CurrentType.append({ "type": "Mouth", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/WTF/" + thisType + "/Mouth")})
#     CurrentType.append({ "type": "Tattoo", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/WTF/" + thisType + "/Tattoo")})
#     CurrentType.append({ "type": "Clothing", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/WTF/" + thisType + "/Clothing")})
#     CurrentType.append({ "type": "Accessory", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/WTF/" + thisType + "/Accessory")})
#     CreateJSONFile(thisType, CurrentType)

CurrentType = []
CurrentType.append({ "type": "Background", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/WTF/Female Angel/Background")})
CurrentType.append({ "type": "Head", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/WTF/Female Angel/Head")})
CurrentType.append({ "type": "Tattoo", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/WTF/Female Angel/Tattoo")})
CurrentType.append({ "type": "Eyes", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/WTF/Female Angel/Eyes")})
CurrentType.append({ "type": "Mouth", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/WTF/Female Angel/Mouth")})
CurrentType.append({ "type": "Clothing", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/WTF/Female Angel/Clothing")})
CurrentType.append({ "type": "Accessory", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/WTF/Female Angel/Accessory")})
CreateJSONFile("Female Angel", CurrentType)

# CurrentType = []
# CurrentType.append({ "type": "Background", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/WTF/Female Christmas/Background")})
# CurrentType.append({ "type": "Head", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/WTF/Female Christmas/Head")})
# CurrentType.append({ "type": "Eyes", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/WTF/Female Christmas/Eyes")})
# CurrentType.append({ "type": "Mouth", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/WTF/Female Christmas/Mouth")})
# CurrentType.append({ "type": "Tattoo", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/WTF/Female Christmas/Tattoo")})
# CurrentType.append({ "type": "Clothing", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/WTF/Female Christmas/Clothing")})
# CurrentType.append({ "type": "Accessory", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/WTF/Female Christmas/Accessory")})
# CurrentType.append({ "type": "Extras", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/WTF/Female Christmas/Extras")})
# CreateJSONFile("Female Christmas", CurrentType)

# CurrentType = []
# CurrentType.append({ "type": "Background", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/WTF/Female Devil/Background")})
# CurrentType.append({ "type": "Head", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/WTF/Female Devil/Head")})
# CurrentType.append({ "type": "Eyes", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/WTF/Female Devil/Eyes")})
# CurrentType.append({ "type": "Mouth", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/WTF/Female Devil/Mouth")})
# CurrentType.append({ "type": "Tattoo", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/WTF/Female Devil/Tattoo")})
# CurrentType.append({ "type": "Clothing", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/WTF/Female Devil/Clothing")})
# CurrentType.append({ "type": "Accessory", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/WTF/Female Devil/Accessory")})
# CreateJSONFile("Female Devil", CurrentType)

# CurrentType = []
# CurrentType.append({ "type": "Background", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/WTF/Female Japanese/Background")})
# CurrentType.append({ "type": "Head", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/WTF/Female Japanese/Head")})
# CurrentType.append({ "type": "Tattoo", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/WTF/Female Japanese/Tattoo")})
# CurrentType.append({ "type": "Eyes", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/WTF/Female Japanese/Eyes")})
# CurrentType.append({ "type": "Mouth", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/WTF/Female Japanese/Mouth")})
# CurrentType.append({ "type": "Clothing", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/WTF/Female Japanese/Clothing")})
# CurrentType.append({ "type": "Accessory", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/WTF/Female Japanese/Accessory")})
# CurrentType.append({ "type": "Extras", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/WTF/Female Japanese/Extras")})
# CreateJSONFile("Female Japanese", CurrentType)

# CurrentType = []
# CurrentType.append({ "type": "Background", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/WTF/Female Space/Background")})
# CurrentType.append({ "type": "Head", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/WTF/Female Space/Head")})
# CurrentType.append({ "type": "Tattoo", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/WTF/Female Space/Tattoo")})
# CurrentType.append({ "type": "Eyes", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/WTF/Female Space/Eyes")})
# CurrentType.append({ "type": "Mouth", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/WTF/Female Space/Mouth")})
# CurrentType.append({ "type": "Space Suit", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/WTF/Female Space/Space Suit")})
# CreateJSONFile("Female Space", CurrentType)

# CurrentType = []
# CurrentType.append({ "type": "Background", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/WTF/Female Thanksgiving/Background")})
# CurrentType.append({ "type": "Head", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/WTF/Female Thanksgiving/Head")})
# CurrentType.append({ "type": "Tattoo", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/WTF/Female Thanksgiving/Tattoo")})
# CurrentType.append({ "type": "Clothing", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/WTF/Female Thanksgiving/Clothing")})
# CurrentType.append({ "type": "Eyes", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/WTF/Female Thanksgiving/Eyes")})
# CurrentType.append({ "type": "Mouth", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/WTF/Female Thanksgiving/Mouth")})
# CurrentType.append({ "type": "Accessory", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/WTF/Female Thanksgiving/Accessory")})
# CurrentType.append({ "type": "Extras", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/WTF/Female Thanksgiving/Extras")})
# CreateJSONFile("Female Thanksgiving", CurrentType)

# CurrentType = []
# CurrentType.append({ "type": "Background", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/WTF/Male Angel/Background")})
# CurrentType.append({ "type": "Head", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/WTF/Male Angel/Head")})
# CurrentType.append({ "type": "Eyes", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/WTF/Male Angel/Eyes")})
# CurrentType.append({ "type": "Mouth", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/WTF/Male Angel/Mouth")})
# CurrentType.append({ "type": "Tattoo", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/WTF/Male Angel/Tattoo")})
# CurrentType.append({ "type": "Clothing", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/WTF/Male Angel/Clothing")})
# CurrentType.append({ "type": "Accessory", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/WTF/Male Angel/Accessory")})
# CreateJSONFile("Male Angel", CurrentType)

# CurrentType = []
# CurrentType.append({ "type": "Background", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/WTF/Male Christmas/Background")})
# CurrentType.append({ "type": "Head", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/WTF/Male Christmas/Head")})
# CurrentType.append({ "type": "Tattoo", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/WTF/Male Christmas/Tattoo")})
# CurrentType.append({ "type": "Clothing", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/WTF/Male Christmas/Clothing")})
# CurrentType.append({ "type": "Eyes", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/WTF/Male Christmas/Eyes")})
# CurrentType.append({ "type": "Mouth", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/WTF/Male Christmas/Mouth")})
# CurrentType.append({ "type": "Accessory", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/WTF/Male Christmas/Accessory")})
# CreateJSONFile("Male Christmas", CurrentType)

# CurrentType = []
# CurrentType.append({ "type": "Background", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/WTF/Male Devil/Background")})
# CurrentType.append({ "type": "Head", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/WTF/Male Devil/Head")})
# CurrentType.append({ "type": "Eyes", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/WTF/Male Devil/Eyes")})
# CurrentType.append({ "type": "Mouth", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/WTF/Male Devil/Mouth")})
# CurrentType.append({ "type": "Tattoo", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/WTF/Male Devil/Tattoo")})
# CurrentType.append({ "type": "Clothing", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/WTF/Male Devil/Clothing")})
# CurrentType.append({ "type": "Accessory", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/WTF/Male Devil/Accessory")})
# CreateJSONFile("Male Devil", CurrentType)

# CurrentType = []
# CurrentType.append({ "type": "Background", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/WTF/Male Japanese/Background")})
# CurrentType.append({ "type": "Head", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/WTF/Male Japanese/Head")})
# CurrentType.append({ "type": "Eyes", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/WTF/Male Japanese/Eyes")})
# CurrentType.append({ "type": "Mouth", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/WTF/Male Japanese/Mouth")})
# CurrentType.append({ "type": "Tattoo", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/WTF/Male Japanese/Tattoo")})
# CurrentType.append({ "type": "Clothing", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/WTF/Male Japanese/Clothing")})
# CurrentType.append({ "type": "Accessory", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/WTF/Male Japanese/Accessory")})
# CurrentType.append({ "type": "Extras", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/WTF/Male Japanese/Extras")})
# CreateJSONFile("Male Japanese", CurrentType)

# CurrentType = []
# CurrentType.append({ "type": "Background", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/WTF/Male Space/Background")})
# CurrentType.append({ "type": "Head", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/WTF/Male Space/Head")})
# CurrentType.append({ "type": "Tattoo", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/WTF/Male Space/Tattoo")})
# CurrentType.append({ "type": "Eyes", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/WTF/Male Space/Eyes")})
# CurrentType.append({ "type": "Mouth", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/WTF/Male Space/Mouth")})
# CurrentType.append({ "type": "Space Suit", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/WTF/Male Space/Space Suit")})
# CreateJSONFile("Male Space", CurrentType)

# CurrentType = []
# CurrentType.append({ "type": "Background", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/WTF/Male Thanksgiving/Background")})
# CurrentType.append({ "type": "Eyes", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/WTF/Male Thanksgiving/Eyes")})
# CurrentType.append({ "type": "Head", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/WTF/Male Thanksgiving/Head")})
# CurrentType.append({ "type": "Tattoo", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/WTF/Male Thanksgiving/Tattoo")})
# CurrentType.append({ "type": "Mouth", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/WTF/Male Thanksgiving/Mouth")})
# CurrentType.append({ "type": "Clothing", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/WTF/Male Thanksgiving/Clothing")})
# CurrentType.append({ "type": "Accessory", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/WTF/Male Thanksgiving/Accessory")})
# CurrentType.append({ "type": "Extras", "options": renameFileExtensionsInDirectoryToLowerCase("src/collections/WTF/Male Thanksgiving/Extras")})
# CreateJSONFile("Male Thanksgiving", CurrentType)