from ROOT import *
import ROOT
import sys
import os

l=0
k=0

for l in range(0,5):
        for k in range(0,5):
                numb = ['0', '23', '45', '67', '90']
                #deg = ['0.125819975788', '0.45148837067', '0.470843382701', '0.635629120943', '0.809748334731', '0.978981968771']
                deg =['0', '0.25','0.5' ,'0.75', '1']
                in_pathWay = ['/w/work3/home/zach/PairPol/FarmGeneratedEvents/lowStats/PolAsym_0/',  '/w/work3/home/zach/PairPol/FarmGeneratedEvents/lowStats/PolAsym_23/','/w/work3/home/zach/PairPol/FarmGeneratedEvents/lowStats/PolAsym_45/',  '/w/work3/home/zach/PairPol/FarmGeneratedEvents/lowStats/PolAsym_67/','/w/work3/home/zach/PairPol/FarmGeneratedEvents/lowStats/PolAsym_90/']

                rootfile = '400MeV_' + numb[l] + 'degrees_0mm_'+ deg[k] +'Pol.root'

                Data = [in_pathWay[l] + rootfile]


                print("This is the file acessed: ")
                print(Data)

        #Not a TString because cant add it later
                out_pathWay = '/w/work3/home/zach/PairPol/outFiles/methodicalPoldeg_lowStats-known/PolAsym_' + numb[l] + '/'
        #Produces the output histograms of random Pol degrees 
                for i in Data:
                        print i
                        iFile = ROOT.TFile.Open(i)
                        oFileName = out_pathWay + os.path.basename(i)
                        treeGen = iFile.GenParam
                #Where the output will be
                        print(oFileName)
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
