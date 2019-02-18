from ROOT import *
import ROOT
import sys
import os
import glob
import subprocess

l=0
k=0
count= 0
List = list()
for l in range(0,5):
        for k in range(0,5):
                numb = ['0', '23', '45', '67', '90']
                #deg = ['0.125819975788', '0.45148837067', '0.470843382701', '0.635629120943', '0.809748334731', '0.978981968771']
                deg =['0', '0.25','0.5' ,'0.75', '1']
                in_pathWay = ['/w/work3/home/zach/PairPol/FarmGeneratedEvents/highStats/PolAsym_90/old/']#,  '/w/work3/home/zach/PairPol/FarmGeneratedEvents/highStats/PolAsym_23/old/','/w/work3/home/zach/PairPol/FarmGeneratedEvents/highStats/PolAsym_45/old/',  '/w/work3/home/zach/PairPol/FarmGeneratedEvents/highStats/PolAsym_67/old/','/w/work3/home/zach/PairPol/FarmGeneratedEvents/highStats/PolAsym_90/old/']
                #underScore = ['_0', '_1', '_2', '_3', '_4', '_5', '_6', '_7', '_8', '_9', '_10']

                count += 1
                underScore = str(count)
                for files in glob.glob(in_pathWay[l]+"*"):
                        dataList = [files]

                        #rootfile = '400MeV_' + numb[l] + 'degrees_0mm_'+ deg[k] +'Pol_'+ underScore + '.root'

                        #Data = [in_pathWay[l] + List]


                        print("This is the file acessed: ")
                        print(files)

        #Not a TString because cant add it later
                        out_pathWay = '/w/work3/home/zach/PairPol/outFiles/highStatsLR/'
        #Produces the output histograms of random Pol degrees 
                        for i in dataList:
                                print i
                                iFile = ROOT.TFile.Open(i)
                                oFileName = out_pathWay + os.path.basename(i)
                                treeGen = iFile.GenParam
                #Where the output will be
                                #print(oFileName)
                #Creates output file 
                                oFile = TFile(oFileName, "recreate")
                                yHist = TH1F("DiffinY", "DiffinY", 500, -8, 8)

                                for j in iFile.SD:
                        #print j.nhit
                                        if j.nhit == 2:
                                                yHist.Fill((j.hity[j.hiti[0]]-j.hity[j.hiti[1]]))
                                yHist.Sumw2()
                                yHist.Write()
                                treeGen.CloneTree().Write()
