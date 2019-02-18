#!/usr/bin/python
#PBS -N PairPolSim
#PBS -V 
#PBS -l walltime=999:00:00,file=20000000kb

import os
import subprocess
import glob


os.chdir("/home/zach/geant4/pairPol/")

outFile   = os.environ['outFile']
outDir    = os.environ['outDir']
macro     = os.environ['Macro']

#Directories
ProcessingDir = "/scratch/zach/"
if not os.path.exists(ProcessingDir):
    os.makedirs(ProcessingDir)

subprocess.call(["pairPol", "-m", macro, "-s", os.environ['Seed']])

subprocess.call(["cp", ProcessingDir+outFile, outDir + outFile])

subprocess.call(["rm", ProcessingDir+outFile])

print "DONE"
