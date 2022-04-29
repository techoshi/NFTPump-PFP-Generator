import asyncio
from numpy import true_divide
import pandas as pd
import glob
from random import randrange, choice, choices
import string
import json
import os
import datetime
import sys
import argparse
import numpy as np
import random
from random import choice
from sticher import stitch

numberToGenerate = 50
output = "src/output/"


async def ImageGenerator():

    print('Number of arguments:', len(sys.argv), 'arguments.')

    print('Argument List:', str(sys.argv))

    parser = argparse.ArgumentParser()
    #parser.add_argument("app", help="The directory of background images.")
    parser.add_argument("run", help="The directory of background images.")
    parser.add_argument("sample", help="The directory of background images.")
    parser.add_argument("weightedMultiplier",
                        help="The directory of background images.")
    parser.add_argument(
        "startingNumber", help="The directory of background images.")
    parser.add_argument(
        "folderPath", help="The directory of background images.")
    parser.add_argument("JSONFile", help="The directory of background images.")
    parser.add_argument("x", help="The directory of background images.")
    parser.add_argument("y", help="The directory of background images.")
    parser.add_argument("amount", help="The directory of background images.")
    args = parser.parse_args()

    numberToGenerate = int(args.amount)
    if bool(args.run) == True:
        folderPath = args.folderPath  # "src/xMooneyCollection/"
        JSONFile = args.JSONFile  # "xMartiansGenerator.json"
        jsonName = JSONFile.split('.')[0]
        print(jsonName)
        totalmints = 0
        startingID = int(args.startingNumber)
        currentID = startingID
        attemptedCombo = 0
        weightedMultiplier = float(args.weightedMultiplier)

        datestring = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        print(datestring)
        sourceFolder = output + jsonName + "." + datestring
        os.mkdir(sourceFolder)
        jsonFilesFolder = sourceFolder + "/json"
        imagesFilesFolder = sourceFolder + "/images"
        os.mkdir(jsonFilesFolder)
        stageOutput = sourceFolder + "/"

        startTime = datetime.datetime.now()
        logFile = open(stageOutput + 'log.txt', 'a+')
        genFile = open(stageOutput + 'generated.csv', 'a+')

        logFile.write("Generator Started at " + str(startTime) + "\n")

        # Open JSON File
        with open(folderPath + JSONFile) as json_file:
            jsonData = json.load(json_file)
            currentTypes = jsonData["Object"]["types"]
            print(str(len(currentTypes)) + " Unique Types")
            idInventory = []
            # Loop Through Object Types
            for martianIndex, objectTypes in enumerate(currentTypes):
                print("Current Type: " + objectTypes["type"])
                stichLayers = []
                layers = []
                weightedObjects = {}
                totalTypeMints = 0

                # if "meta" in objectTypes:
                #     for metaIndex, objectMeta in enumerate(objectTypes["meta"]):
                #         currentMeta = objectMeta
                #         currentMetaProperty = currentMeta["property"]
                #         for  thisOption in currentMeta["options"]:
                #             weightedObjects[currentMetaProperty + "_" + thisOption["name"]
                #                             ] = {"max": thisOption["count"], "minted": 0}

                #print(len(currentTypes) + " Unique Types")
                # Loop Through Object Types Layers
                for layerIndex, thisLayer in enumerate(objectTypes["layers"]):
                    print("Current: " +
                          objectTypes["type"] + " " + thisLayer["layer"])

                    gen_type_1 = []
                    gen_obj_1 = []

                    currentLayers = thisLayer
                    currentLayer = thisLayer["layer"]
                    stichLayers.append(currentLayer)
                    currentOptions = currentLayers["options"]

                    runPercentConvert = False

                    if objectTypes["countType"] == "Percent":
                        runPercentConvert = True
                    # print(objectTypes["countType"])   
                    # print(runPercentConvert)   
                    # print(str(objectTypes["countType"] == "Percent") + " " + str(objectTypes["countType"]))   

                    for thisOption in currentOptions:
                        gen_type_1.append(1)
                        gen_obj_1.append(thisOption["name"])


                        finalAmount = thisOption["count"]

                        print(str(runPercentConvert))   
                        if runPercentConvert:
                            finalAmount = (thisOption["count"]/100)*objectTypes["max"]                                              
                                                    
                        print(currentLayer + "_" + thisOption["name"] + " " + str(finalAmount))   

                        weightedObjects[currentLayer + "_" + thisOption["name"]
                                        ] = {"max": finalAmount, "minted": 0}

                    raw_data = {
                        'type_' + str(layerIndex): gen_type_1,
                        currentLayer: gen_obj_1,
                        "folderpath": thisLayer["folder"]
                    }

                    temp_df = pd.DataFrame(
                        raw_data, columns=['type_' + str(layerIndex), currentLayer])
                    temp_df_index = temp_df.set_index(
                        ['type_' + str(layerIndex)]).rename_axis(['type'])
                    layers.append(temp_df_index)

                newUniqueDataframe = layers[0]

                # Outer Joins of Data Sets
                for index, dataFrame in enumerate(layers):
                    if index > 0:
                        newUniqueDataframe = newUniqueDataframe.join(
                            dataFrame, how='outer')

                print(str(len(newUniqueDataframe)) + " unique combinations")
                logFile.write(str(len(newUniqueDataframe)) + " of unique " +
                              objectTypes["type"] + " combinations" + "\n")
                numberToSample = float(len(newUniqueDataframe))*float(1)
                logFile.close()
                logFile = open(stageOutput + 'log.txt', 'a+')
                # should we sample?
                if bool(args.sample) == True:
                    uniqueDataframe = newUniqueDataframe.sample(frac=1)
                else:
                    uniqueDataframe = newUniqueDataframe

                newUniqueDataframe = None
                #allCombos = uniqueDataframe.iterrows()
                # Loop through every Sample Combination
                print("Start Loop")
                for index, uniqueCombinationRow in uniqueDataframe.iterrows():
                    stichArray = []
                    comboArray = []
                    layerMeta = {
                        "attributes": []
                    }

                    shouldWeStich = True
                    layerMeta["attributes"].append({
                        "trait_type": "Type",
                        "value": objectTypes["type"]
                    })
                    # Check if you should create the combination
                    for layer in stichLayers:
                        tempLayer = layer + "_" + uniqueCombinationRow[layer]
                        if (weightedObjects[tempLayer]["max"]*weightedMultiplier) <= weightedObjects[tempLayer]["minted"]:
                            shouldWeStich = False
                        stichArray.append(
                            folderPath + objectTypes["type"] + "/" + layer + "/" + uniqueCombinationRow[layer] + ".png")

                        layerMeta["attributes"].append({
                            "trait_type": layer,
                            "value": uniqueCombinationRow[layer].replace("_", " ").title()
                        })
                        comboArray.append(layer + "/" + uniqueCombinationRow[layer])

                    attemptedCombo = attemptedCombo+1

                    description = "General"

                    if "description" in objectTypes:
                         description = objectTypes["description"]
                    print("---Checking Combination --" + description + " #:" + str(attemptedCombo) + " -- Last Mint" + str(totalmints))

                    if shouldWeStich == True:
                        totalmints = totalmints+1
                        currentID = currentID+1
                        currentIDrando = currentID

                        #randomID = choice([i for i in range(startingID,numberToGenerate+startingID) if i not in idInventory])
                        #idInventory.append(randomID)
                        
                        #currentIDrando = randomID

                        totalTypeMints = totalTypeMints+1
                        #newpath = r'' + stageOutput + objectTypes["type"] + "/" + str(currentID)
                        newpath = imagesFilesFolder + "/"

                        stringCurrentID = str(currentIDrando)
                        layerMeta["description"] = "Default Collection."
                        layerMeta["external_url"] = "https://exanoke.com/" + stringCurrentID
                        layerMeta["image"] = "ipfs://QmQjz8JcdhfWkVGpRMD2q93bdr6xgA9btaTK4XzG3pvnda/" + stringCurrentID + ".png"
                        layerMeta["name"] = "Generated #" + stringCurrentID.zfill(5)

                        if not os.path.exists(newpath):
                            os.makedirs(newpath)


                        if 1 == 1:
                            asyncio.ensure_future(stitch(newpath + "/", stringCurrentID, stichArray, int(args.x), int(args.y)))
                            genFile.write(",".join(comboArray) + "\n")
                            # Serializing json
                            #layerMeta["combination"] = ",".join(comboArray)
                            json_object = json.dumps(layerMeta, indent=4)

                            # Writing to sample.json
                            # str(martianIndex)
                            asyncio.ensure_future(writeJSONFileForMint(jsonFilesFolder, stringCurrentID, json_object))

                        print("---Mint#:" + str(totalmints))
                        for layer in stichLayers:
                            tempLayer = layer + "_" + uniqueCombinationRow[layer]
                            weightedObjects[tempLayer]["minted"] = weightedObjects[tempLayer]["minted"]+1

                        if totalmints >= numberToGenerate or totalTypeMints >= objectTypes["max"]:
                            break

                logFile.write("Generated " + str(totalTypeMints) +
                              " " + objectTypes["type"] + " combinations" + "\n")

                weightedObjectsjson_object = json.dumps(
                    weightedObjects, indent=4)
                # Writing to sample.json
                with open(stageOutput + "_" + objectTypes["type"] + "_" + "weightedresults.json", "w") as outfile:
                    outfile.write(weightedObjectsjson_object)

                if totalmints >= numberToGenerate:
                    break

        logFile.write("Generated " + str(totalmints) + " combinations" + "\n")
        endTime = datetime.datetime.now()
        logFile.write("Generator Ended at " + str(endTime) + "\n")
        logFile.close()

async def writeJSONFileForMint(jsonFilesFolder, stringCurrentID, json_object):
    with open(jsonFilesFolder + "/" + stringCurrentID + ".json", "w") as outfile:
        outfile.write(json_object)


asyncio.run(ImageGenerator())
