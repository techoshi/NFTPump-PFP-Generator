import threading
import glob
import random
import shutil
import json
import asyncio
from sticher import stitch

async def runCopy(output_dir, filename1):

    # x = threading.Thread(target=copyFile, args=(output_dir,filename1,))    
    # x.start()
    copyFile(output_dir, filename1)
    #saveFile(output_dir, filename, img_args, x, y)  
    return True

def copyFile(output_dir1, filename1):
    shutil.copy(output_dir1, filename1)

async def combineTypes(FileLocations):
    result = []
    FullArray = []
    currentID = 0
    for genType in FileLocations:
        thisGlob = glob.glob(genType["search"])

        for currentItem in thisGlob:
            currentID = currentID + 1
            FullArray.append(
                {"id": currentID, "type": genType["type"], "path": currentItem, "image": genType["image"]})

    with open('src/output/WTF/Shuffled/arraylist.json', 'w') as output_file:
        json.dump(FullArray, output_file)

    random.shuffle(FullArray)
    random.shuffle(FullArray)
    random.shuffle(FullArray)
    random.shuffle(FullArray)
    random.shuffle(FullArray)
    random.shuffle(FullArray)
    random.shuffle(FullArray)
    random.shuffle(FullArray)
    random.shuffle(FullArray)
    random.shuffle(FullArray)
    random.shuffle(FullArray)
    random.shuffle(FullArray)
    random.shuffle(FullArray)
    random.shuffle(FullArray)
    random.shuffle(FullArray)
    random.shuffle(FullArray)
    random.shuffle(FullArray)
    random.shuffle(FullArray)

    newID = 123

    for currentFile in FullArray:
        newID = newID + 1
        strNewID = str(newID)
        
        with open(currentFile["path"], 'r') as infile:
            thisJson = json.load(infile)

            #external_url = thisJson['external_url']
            theID = (currentFile["path"].rsplit('/', 1))[1]
            theID = (theID.rsplit('\\', 1))[1]
            theID = (theID.rsplit('.', 1))[0]

            # thisJson["description"] = "NFTCC"
            thisJson["name"] = "#" + strNewID
            # thisJson["external_url"] = "https://www.thenftcc.io"
            thisJson["image"] = "https://wtforks-general.s3.amazonaws.com/images/" + \
                strNewID + ".png"
            #del thisJson['combination']
            # del thisJson["attributes"][0]
            finalJSON = json.dumps(thisJson, indent=4)

            with open('src/output/WTF/Shuffled/JSON/' + strNewID + '.json', 'w') as output_file:
                output_file.write(finalJSON)

    newID = 123

    for currentFile in FullArray:
        newID = newID + 1
        theID = 0

        theID = (currentFile["path"].rsplit('/', 1))[1]
        theID = (theID.rsplit('\\', 1))[1]
        theID = (theID.rsplit('.', 1))[0]

        # with open(currentFile["path"], 'r') as infile:
        #     thisJson = json.load(infile)
        #     external_url = thisJson['external_url']
        #     theID = (external_url.rsplit('/', 1))[1]
        await runCopy(currentFile["image"] + "/" + str(theID) + ".png", "src/output/WTF/Shuffled/images" + "/" + str(newID) + ".png")
        

    


#allthefiles = glob.glob("src/output/xMartiansMale.20211111005517/json/*.json")

FileLocations = [
{
    "type": "Female",
    "image": "src/output/WTF/Formatted Output/Female Afro Head/images",
    "search": "src/output/WTF/Formatted Output/Female Afro Head/json/*.json"
},
{
    "type": "Female",
    "image": "src/output/WTF/Formatted Output/Female Angel/images",
    "search": "src/output/WTF/Formatted Output/Female Angel/json/*.json"
},
{
    "type": "Female",
    "image": "src/output/WTF/Formatted Output/Female Backwards Bent Head/images",
    "search": "src/output/WTF/Formatted Output/Female Backwards Bent Head/json/*.json"
},
{
    "type": "Female",
    "image": "src/output/WTF/Formatted Output/Female Basic Head/images",
    "search": "src/output/WTF/Formatted Output/Female Basic Head/json/*.json"
},
{
    "type": "Female",
    "image": "src/output/WTF/Formatted Output/Female Cake Head/images",
    "search": "src/output/WTF/Formatted Output/Female Cake Head/json/*.json"
},
{
    "type": "Female",
    "image": "src/output/WTF/Formatted Output/Female Christmas/images",
    "search": "src/output/WTF/Formatted Output/Female Christmas/json/*.json"
},
{
    "type": "Female",
    "image": "src/output/WTF/Formatted Output/Female Crown/images",
    "search": "src/output/WTF/Formatted Output/Female Crown/json/*.json"
}, 
{
    "type": "Female",
    "image": "src/output/WTF/Formatted Output/Female Curly Head/images",
    "search": "src/output/WTF/Formatted Output/Female Curly Head/json/*.json"
},
{
    "type": "Female",
    "image": "src/output/WTF/Formatted Output/Female Devil/images",
    "search": "src/output/WTF/Formatted Output/Female Devil/json/*.json"
},
{
    "type": "Female",
    "image": "src/output/WTF/Formatted Output/Female Dread Head/images",
    "search": "src/output/WTF/Formatted Output/Female Dread Head/json/*.json"
},
{
    "type": "Female",
    "image": "src/output/WTF/Formatted Output/Female Forward Bent/images",
    "search": "src/output/WTF/Formatted Output/Female Forward Bent/json/*.json"
},
{
    "type": "Female",
    "image": "src/output/WTF/Formatted Output/Female Pigtail Head/images",
    "search": "src/output/WTF/Formatted Output/Female Pigtail Head/json/*.json"
},
{
    "type": "Female",
    "image": "src/output/WTF/Formatted Output/Female Pizza Head/images",
    "search": "src/output/WTF/Formatted Output/Female Pizza Head/json/*.json"
},
{
    "type": "Female",
    "image": "src/output/WTF/Formatted Output/Female Samurai/images",
    "search": "src/output/WTF/Formatted Output/Female Samurai/json/*.json"
},
{
    "type": "Female",
    "image": "src/output/WTF/Formatted Output/Female Space/images",
    "search": "src/output/WTF/Formatted Output/Female Space/json/*.json"
},
{
    "type": "Female",
    "image": "src/output/WTF/Formatted Output/Female Sweatband/images",
    "search": "src/output/WTF/Formatted Output/Female Sweatband/json/*.json"
},
{
    "type": "Female",
    "image": "src/output/WTF/Formatted Output/Female Thanksgiving/images",
    "search": "src/output/WTF/Formatted Output/Female Thanksgiving/json/*.json"
},
{
    "type": "Male", 
    "image": "src/output/WTF/Formatted Output/Male Afro Head/images", 
    "search": "src/output/WTF/Formatted Output/Male Afro Head/json/*.json"
},
{
    "type": "Male", 
    "image": "src/output/WTF/Formatted Output/Male Angel/images", 
    "search": "src/output/WTF/Formatted Output/Male Angel/json/*.json"
},
{
    "type": "Male", 
    "image": "src/output/WTF/Formatted Output/Male Backwards Bent Head/images", 
    "search": "src/output/WTF/Formatted Output/Male Backwards Bent Head/json/*.json"
},
{
    "type": "Male", 
    "image": "src/output/WTF/Formatted Output/Male Basic Head/images", 
    "search": "src/output/WTF/Formatted Output/Male Basic Head/json/*.json"
},
{
    "type": "Male", 
    "image": "src/output/WTF/Formatted Output/Male Bravo Head/images", 
    "search": "src/output/WTF/Formatted Output/Male Bravo Head/json/*.json"
},
{
    "type": "Male", 
    "image": "src/output/WTF/Formatted Output/Male Cake Head/images", 
    "search": "src/output/WTF/Formatted Output/Male Cake Head/json/*.json"
},
{
    "type": "Male", 
    "image": "src/output/WTF/Formatted Output/Male Christmas/images", 
    "search": "src/output/WTF/Formatted Output/Male Christmas/json/*.json"
},
{
    "type": "Male", 
    "image": "src/output/WTF/Formatted Output/Male Crown/images", 
    "search": "src/output/WTF/Formatted Output/Male Crown/json/*.json"
},
{
    "type": "Male", 
    "image": "src/output/WTF/Formatted Output/Male Curly Head/images", 
    "search": "src/output/WTF/Formatted Output/Male Curly Head/json/*.json"
},
{
    "type": "Male", 
    "image": "src/output/WTF/Formatted Output/Male Devil/images", 
    "search": "src/output/WTF/Formatted Output/Male Devil/json/*.json"
},
{
    "type": "Male", 
    "image": "src/output/WTF/Formatted Output/Male Dread Head/images", 
    "search": "src/output/WTF/Formatted Output/Male Dread Head/json/*.json"
},
{
    "type": "Male", 
    "image": "src/output/WTF/Formatted Output/Male Forward Bent/images", 
    "search": "src/output/WTF/Formatted Output/Male Forward Bent/json/*.json"
},
{
    "type": "Male", 
    "image": "src/output/WTF/Formatted Output/Male Pizza Head/images", 
    "search": "src/output/WTF/Formatted Output/Male Pizza Head/json/*.json"
},
{
    "type": "Male", 
    "image": "src/output/WTF/Formatted Output/Male Samurai/images", 
    "search": "src/output/WTF/Formatted Output/Male Samurai/json/*.json"
},
{
    "type": "Male", 
    "image": "src/output/WTF/Formatted Output/Male Space/images", 
    "search": "src/output/WTF/Formatted Output/Male Space/json/*.json"
},
{
    "type": "Male", 
    "image": "src/output/WTF/Formatted Output/Male Sweatband/images", 
    "search": "src/output/WTF/Formatted Output/Male Sweatband/json/*.json"
},
{
    "type": "Male", 
    "image": "src/output/WTF/Formatted Output/Male Thanksgiving/images", 
    "search": "src/output/WTF/Formatted Output/Male Thanksgiving/json/*.json"
}]

asyncio.run(combineTypes(FileLocations))

