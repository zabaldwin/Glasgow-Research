from ROOT import *
import ROOT
import sys
import os

l=1
k=0

for l in range(1,5):
        for k in range(0,1):
                numb = ['23', '0', '45',  '67', '90']
                irrdeg = ['0.125819975788', '0.470843382701', '0.809748334731', '0.45148837067', '0.635629120943', '0.978981968771']#, '0.995944522669', '0.728366465977', '0.985203431157', '0.823105104033', '0.825558559999']
                deg = ['0', '0.25', '0.5', '0.75', '1']
                in_pathWay = ['/w/work3/home/zach/PairPol/FarmGeneratedEvents/Randpoldeg_med/PolAsym_23/', '/w/work3/home/zach/PairPol/FarmGeneratedEvents/Randpoldeg_med/PolAsym_0/','/w/work3/home/zach/PairPol/FarmGeneratedEvents/Randpoldeg_med/PolAsym_45/', '/w/work3/home/zach/PairPol/FarmGeneratedEvents/Randpoldeg_med/PolAsym_67/', '/w/work3/home/zach/PairPol/FarmGeneratedEvents/Randpoldeg_med/PolAsym_90/']

                rootfile = '400MeV_' + numb[l] + 'degrees_0mm_'+ irrdeg[k] +'Pol.root'

                Data = [in_pathWay[l] + rootfile]


                print("This is the file acessed: ")
                print(Data)

        #Not a TString because cant add it later
                out_pathWay = '/w/work3/home/zach/PairPol/outFiles/irregularPoldeg_medStats/'
        #Produces the output histograms of random Pol degrees 
                for i in Data:
                        print i
                        iFile = ROOT.TFile.Open(i)
                        oFileName = out_pathWay + os.path.basename(i)
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
