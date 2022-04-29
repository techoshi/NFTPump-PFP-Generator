import shutil

maxAmount = 3334

for i in range(maxAmount):
    shutil.copy2('src/output/TMC-Unrevealed/reveal.json', 'src/output/TMC-Unrevealed/{}.json'.format(i))