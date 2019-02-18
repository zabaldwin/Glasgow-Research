import os

path = '/w/work3/home/zach/PairPol/outFiles/methodicalPoldeg_medStats-known/PolAsym_0/'
files = os.listdir(path)

for file in files:
        os.rename(os.path.join(path, file), os.path.join(path, file.rsplit(".",1)[0] + '_test.root'))
