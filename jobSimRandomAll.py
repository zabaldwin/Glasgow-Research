#!/usr/bin/python
#PBS -N PairPolSim
#PBS -V 
#PBS -l walltime=999:00:00,file=20000000kb

import os
import subprocess
import glob

#---------------------------------------------------------------
#Script to run through data files creating weight files
#-----------------------------------------------------------------
os.chdir("/home/simong/geant4/pairPol/")

#Directorys
ProcessingDir = "/scratch/simong/"
if not os.path.exists(ProcessingDir):
    os.makedirs(ProcessingDir)

#Define macro name
macroBase = os.environ["energyMin"] + "-" + os.environ["energyMax"] +  "MeV_" + os.environ["spotR"] + "Cmm_" +  os.environ["beamX"] + "Xmm_"+  os.environ["beamY"] + "Ymm_" + os.environ["polangle"] + "degrees_" +  os.environ["poldegree"] + "Pol"
macroFile = ProcessingDir + macroBase + ".mac"
outFile   = macroBase + ".root"

outDir    = os.environ['outDir']

#Make macro file
File = open(macroFile,"w")
File.write("/process/verbose 0\n")
File.write("/control/verbose 0\n")
File.write("/run/verbose 0\n")
File.write("/vis/verbose 0\n")
File.write("/run/initialize\n")

File.write("/PairPol/generator/setBeamType            0\n")
File.write("/PairPol/generator/useConverterThickness  0\n")
File.write("/PairPol/generator/usePhaseSpaceGen       0\n")
File.write("/PairPol/generator/setBeamX               "+ os.environ["beamX"] +" mm\n")
File.write("/PairPol/generator/setBeamY               "+ os.environ["beamY"] +" mm\n")
File.write("/PairPol/generator/setBeamZ               0. mm\n")
File.write("/PairPol/generator/setSpotRadius          "+ os.environ["spotR"] +" mm\n")
File.write("/PairPol/generator/setLowBeamEnergy       "+ os.environ["energyMin"] +" MeV\n")
File.write("/PairPol/generator/setHighBeamEnergy      "+ os.environ["energyMax"] +" MeV\n")
File.write("/PairPol/generator/setAsymAngle           "+ os.environ["polangle"] +" deg\n")
File.write("/PairPol/generator/setAsymDegree          "+ os.environ["poldegree"] + "\n")

File.write("/PairPol/event/setOutput " + ProcessingDir + outFile + "\n")

File.write("/run/beamOn " + os.environ['Nevents'] + "\n")

#Run simulation
subprocess.call(["pairPol", "-m", macroFile, "-s", os.environ['Seed']])

subprocess.call(["cp", ProcessingDir+outFile, outDir+outFile])

subprocess.call(["rm", ProcessingDir+outFile])
subprocess.call(["rm", macroFile])

print "DONE"
