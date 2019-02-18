#!/usr/bin/python

import os
import sys
import subprocess
import glob
import time
import random

#---------------------------------------------------------------
#Script to run through data files creating weight files
#-----------------------------------------------------------------

energyMin      = 200
energyMax      = 1000
energyRangeMin = 0
energyRangeMax = 5

collimationMin = 1
collimationMax = 4

xOffMax     = 3
yOffMax     = 3

outDirectory = "/w/work1/home/simong/PairPol/FarmGeneratedEventsRandom/"
os.environ['outDir']  = outDirectory
os.environ['Nevents'] = str(100)

maxq = 500
nTypes = 3

seedOffset = 456789

jobprocessed = 0
basesprocessed = 0

for eventType in range(0,nTypes):
    energy = random.uniform(energyMin,energyMax)
    os.environ["energyMin"] = str(energy)
    os.environ["energyMax"] = str(energy+random.uniform(energyRangeMin,energyRangeMax))
    os.environ["spotR"]     = str(random.uniform(collimationMin,collimationMax))
    os.environ["polangle"]  = str(random.uniform(0,180))
    os.environ["poldegree"] = str(random.uniform(0,1))
    os.environ["beamX"]     = str(random.uniform(-xOffMax,xOffMax))
    os.environ["beamY"]     = str(random.uniform(-yOffMax,yOffMax))
    os.environ['Seed']      = str(jobprocessed+seedOffset)
    jobprocessed+=1
    subprocess.call(["qsub", "/home/simong/geant4/pairPol/scripts/jobSimRandomAll.py"],env=dict(os.environ))
    time.sleep(0.1)
    jobcount = subprocess.check_output(["qstat | grep \'R\|Q\'"], shell=True).count(os.environ['USER'])
    print jobcount
    while jobcount>maxq:
        time.sleep(1)
        jobcount = subprocess.check_output(["qstat | grep \'R\|Q\'"], shell=True).count(os.environ['USER'])

print 'All Done'
