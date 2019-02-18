#!/usr/bin/python

import os
import sys
import subprocess
import glob
import time



def makeMacroFile(FileName,events,Ene,Col,PolDeg,PolAng):
    File = open(FileName,"w")
    File.write("/process/verbose 0\n")
    File.write("/control/verbose 0\n")
    File.write("/run/verbose 0\n")
    File.write("/vis/verbose 0\n")
    File.write("/run/initialize\n")

    File.write("/PairPol/generator/setBeamType            0\n")
    File.write("/PairPol/generator/useConverterThickness  0\n")
    File.write("/PairPol/generator/usePhaseSpaceGen       0\n")
    File.write("/PairPol/generator/setBeamX               0. mm\n")
    File.write("/PairPol/generator/setBeamY               0. mm\n")
    File.write("/PairPol/generator/setBeamZ               0. mm\n")
    File.write("/PairPol/generator/setSpotRadius          "+ Col +" mm\n")
    File.write("/PairPol/generator/setLowBeamEnergy       "+ str(Ene[0]) +" MeV\n")
    File.write("/PairPol/generator/setHighBeamEnergy      "+ str(Ene[0]+Ene[1]) +" MeV\n")
    File.write("/PairPol/generator/setAsymAngle           "+ PolAng +" deg\n")
    File.write("/PairPol/generator/setAsymDegree          "+ PolDeg + "\n")


    File.write("/PairPol/event/setOutput /scratch/zach/" + macro + ".root\n")

    File.write("/run/beamOn " + str(events) + "\n")
    return;

energylist = [[400,0]]
collimationlist = ["0"]
poldegreelist = ["1","0.75","0.5","0.25","0"]
polanglelist = ["90", "67", "45", "23", "0"]

outDirectory = "/w/work3/home/zach/PairPol/FarmGeneratedEvents/medStats/"

os.environ['outDir'] = outDirectory

maxq = 250
Nevents = 50000
nFiles = 10

jobprocessed = 0
basesprocessed = 0

for energy in energylist:
    macroA = str(energy[0]) + "MeV"
    for polangle in polanglelist:
        macroB = macroA + "_" + polangle + "degrees"
        for collimation in collimationlist:
            macroC = macroB + "_" + collimation + "mm"
            for poldegree in poldegreelist:
                macro = macroC + "_" + poldegree + "Pol"
                basesprocessed+=1
                os.environ['Macro'] = "macros/" + macro + ".mac"
                print os.environ['Macro']
                makeMacroFile("../"+os.environ['Macro'],Nevents,energy,collimation,poldegree,polangle)
                baseprocessed = 0
                for x in range(1, nFiles+1):
                    os.environ['Seed'] = str(x)
                    outfile = macro + "_" + str(x) + ".root"
                    print outfile
                    if( os.path.exists(outDirectory+outfile) ):
                        print "exists"
                        continue
                    os.environ['outFile'] = outfile
                    jobprocessed+=1
                    baseprocessed+=1
                    subprocess.call(["qsub", "/home/zach/geant4/pairPol/scripts/jobSim.py"],env=dict(os.environ))
                    time.sleep(1)
                    jobcount = subprocess.check_output(["qstat | grep \'R\|Q\'"], shell=True).count(os.environ['USER'])
                    print jobcount
                    while jobcount>maxq:
                        time.sleep(1)
                        jobcount = subprocess.check_output(["qstat | grep \'R\|Q\'"], shell=True).count(os.environ['USER'])



print 'All Done'
