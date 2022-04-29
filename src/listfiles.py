
import glob

allthefiles = glob.glob("src/output/xMartiansFemale.20211111010332/images/*.png")
allthefiles2 = glob.glob("src/output/xMartiansFemale.20211111005517/images/*.png")
allthefiles3 = glob.glob("src/output/xMartiansFemale.20211111010332/images/*.png")
allthefiles4 = glob.glob("src/output/xMartiansHyperMale.20211111014507/images/*.png")

with open('src/output/your_file.txt', 'w') as f:
    for item in allthefiles:
        f.write("%s\n" % item.rsplit('\\', 1)[1])
    for item in allthefiles2:
        f.write("%s\n" % item.rsplit('\\', 1)[1])
    for item in allthefiles3:
        f.write("%s\n" % item.rsplit('\\', 1)[1])
    for item in allthefiles4:
        f.write("%s\n" % item.rsplit('\\', 1)[1])
