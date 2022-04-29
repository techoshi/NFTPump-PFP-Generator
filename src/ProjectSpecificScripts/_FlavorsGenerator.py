import pandas as pd
import glob
from random import randrange, choice, choices
import string

from sticher import stitch

numberToGenerate = 50
output = "src/output"

# root_dir needs a trailing slash (i.e. /root/dir/)
def getPNGFilesDataFrame(folderPath, folderName, layerOrder):
    gen_type_1 = []
    gen_obj_1 = []

    folderpath = folderPath + folderName + "/"
    for filename in glob.iglob(folderpath + '*.png', recursive=True):
        gen_type_1.append(1)
        gen_obj_1.append(filename.split('\\')[-1])

    raw_data = {
        'type_' + layerOrder: gen_type_1,
        folderName: gen_obj_1
    }
    df_main = pd.DataFrame(
        raw_data, columns=['type_' + layerOrder, folderName])
    return df_main

def FlavorGenerator(numberToGenerate):
    #numberToGenerate = 10000

    stichLayers = ["Background", "Base", "Accessories", "Expression", "Eyes"]
    layers = []
    folderPath = "src/Flavors Generative/"

    for index, layer in enumerate(stichLayers):
        temp_df = getPNGFilesDataFrame(folderPath, layer, str(index))
        temp_df_index = temp_df.set_index(['type_' + str(index)]).rename_axis(['type'])
        layers.append(temp_df_index)

    newUniqueDataframe = layers[0]

    for index, dataFrame in enumerate(layers):
        if index > 0:
            newUniqueDataframe = newUniqueDataframe.join(
                dataFrame, how='outer')

    uniqueDataframe = newUniqueDataframe.sample(n=numberToGenerate)

    for index, row in uniqueDataframe.iterrows():
        stichArray = []

        for layer in stichLayers:
            stichArray.append(folderPath + layer + "/" + row[layer])

        stitch("src/output/", "", stichArray, 1500, 1500)

FlavorGenerator(5)
