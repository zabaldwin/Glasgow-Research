#Gathers the training data
import sklearn
from glob import glob
import numpy as np
import  root_numpy
from root_numpy import hist2array
import ROOT
from ROOT import *
import random
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt



PolAsym_0 = glob("/w/work3/home/zach/PairPol/outFiles/methodicalPoldeg_known/PolAsym_0/400*.root")

PolAsym_23 = glob("/w/work3/home/zach/PairPol/outFiles/methodicalPoldeg_known/PolAsym_23/400*.root")

PolAsym_45 = glob("/w/work3/home/zach/PairPol/outFiles/methodicalPoldeg_known/PolAsym_45/400*.root")

PolAsym_67 = glob("/w/work3/home/zach/PairPol/outFiles/methodicalPoldeg_known/PolAsym_67/400*.root")

PolAsym_90 = glob("/w/work3/home/zach/PairPol/outFiles/methodicalPoldeg_known/PolAsym_90/400*.root")

PolAsym_0Med = glob("/w/work3/home/zach/PairPol/outFiles/methodicalPoldeg_medStats-known/PolAsym_0/400*.root")

PolAsym_23Med = glob("/w/work3/home/zach/PairPol/outFiles/methodicalPoldeg_medStats-known/PolAsym_23/400*.root")

PolAsym_45Med = glob("/w/work3/home/zach/PairPol/outFiles/methodicalPoldeg_medStats-known/PolAsym_45/400*.root")

PolAsym_67Med = glob("/w/work3/home/zach/PairPol/outFiles/methodicalPoldeg_medStats-known/PolAsym_67/400*.root")

PolAsym_90Med = glob("/w/work3/home/zach/PairPol/outFiles/methodicalPoldeg_medStats-known/PolAsym_90/400*.root")

PolAsym_0Low = glob("/w/work3/home/zach/PairPol/outFiles/methodicalPoldeg_lowStats-known/PolAsym_0/400*.root")

PolAsym_23Low = glob("/w/work3/home/zach/PairPol/outFiles/methodicalPoldeg_lowStats-known/PolAsym_23/400*.root")

PolAsym_45Low = glob("/w/work3/home/zach/PairPol/outFiles/methodicalPoldeg_lowStats-known/PolAsym_45/400*.root")

PolAsym_67Low = glob("/w/work3/home/zach/PairPol/outFiles/methodicalPoldeg_lowStats-known/PolAsym_67/400*.root")

PolAsym_90Low = glob("/w/work3/home/zach/PairPol/outFiles/methodicalPoldeg_lowStats-known/PolAsym_90/400*.root")



yHist_trainSet  = list()
polValue_trainSet = list()
asymValue_trainSet = list()

yHist_testSet = list()
polValue_testSet= list()
asymValue_testSet = list()
'''
for i in PolAsym_90:
        iFile = ROOT.TFile.Open(i)
        iFile.DiffinY.Scale(1/iFile.DiffinY.Integral())
        diffY = root_numpy.hist2array(iFile.DiffinY)
        #Can split the data if needed but right now splitting it between methodical and irregular
        
        yHist_trainSet.append(diffY)
        iFile.GenParam.GetEntry(0)
        polValue_trainSet.append(iFile.GenParam.PolDeg)
        polValue_trainSet.append(90)
'''
yHist_trainSet0 = list()
polValue_trainSet0 = list()
asymValue_trainSet0 = list()
for a in PolAsym_0:
        iFile0 = ROOT.TFile.Open(a)
        iFile0.DiffinY.Scale(1/iFile0.DiffinY.Integral())
        yHist0 = root_numpy.hist2array(iFile0.DiffinY)
       #addClassifier0= np.append(yHist0, 0)
       #yHist_trainSet0.append(addClassifier0)

        yHist_trainSet0.append(yHist0)
        iFile0.GenParam.GetEntry(0)
        polValue_trainSet0.append(iFile0.GenParam.PolDeg)
       #polValue_trainSet0.append(90)
        iFile0.GenParam.GetEntry(1)
        asymValue_trainSet0.append(iFile0.GenParam.PolAng)

yHist_trainSet23 = list()
polValue_trainSet23 = list()
asymValue_trainSet23 = list()

for b in PolAsym_23:
        iFile23 = ROOT.TFile.Open(b)
iFile23.DiffinY.Scale(1/iFile23.DiffinY.Integral())
        yHist23 = root_numpy.hist2array(iFile23.DiffinY)
       #addClassifier23 = np.append(yHist23, 23)
       #yHist_trainSet23.append(addClassifier23)

        yHist_trainSet23.append(yHist23)
        iFile23.GenParam.GetEntry(0)
        polValue_trainSet23.append(iFile23.GenParam.PolDeg)
        iFile23.GenParam.GetEntry(1)
        asymValue_trainSet23.append(iFile23.GenParam.PolAng)


yHist_trainSet45 = list()
polValue_trainSet45 = list()
asymValue_trainSet45 = list()

for c in PolAsym_45:
        iFile45 = ROOT.TFile.Open(c)
        iFile45.DiffinY.Scale(1/iFile45.DiffinY.Integral())
        yHist45 = root_numpy.hist2array(iFile45.DiffinY)
       #addClassifier45= np.append(yHist45, 45)
       #yHist_trainSet45.append(addClassifier45)

        yHist_trainSet45.append(yHist45)
        iFile45.GenParam.GetEntry(0)
        polValue_trainSet45.append(iFile45.GenParam.PolDeg)
        iFile45.GenParam.GetEntry(1)
        asymValue_trainSet45.append(iFile45.GenParam.PolAng)


yHist_trainSet67 = list()
polValue_trainSet67 = list()
asymValue_trainSet67 = list()

for d in PolAsym_67:
        iFile67 = ROOT.TFile.Open(d)
        iFile67.DiffinY.Scale(1/iFile67.DiffinY.Integral())
        yHist67 = root_numpy.hist2array(iFile67.DiffinY)
       #addClassifier67 = np.append(yHist67, 67)
       #yHist_trainSet67.append(addClassifier67)

        yHist_trainSet67.append(yHist67)
        iFile67.GenParam.GetEntry(0)
        polValue_trainSet67.append(iFile67.GenParam.PolDeg)
        iFile67.GenParam.GetEntry(1)
        asymValue_trainSet67.append(iFile67.GenParam.PolAng)


yHist_trainSet90 = list()
polValue_trainSet90 = list()
asymValue_trainSet90 = list()

for e in PolAsym_90:
        iFile90 = ROOT.TFile.Open(e)
        iFile90.DiffinY.Scale(1/iFile90.DiffinY.Integral())
        yHist90 = root_numpy.hist2array(iFile90.DiffinY)
       #addClassifier90 = np.append(yHist90, 90)
       #yHist_trainSet90.append(addClassifier90)

        yHist_trainSet90.append(yHist90)
        iFile90.GenParam.GetEntry(0)
polValue_trainSet90.append(iFile90.GenParam.PolDeg)
        iFile90.GenParam.GetEntry(1)
        asymValue_trainSet90.append(iFile90.GenParam.PolAng)

asymValue_trainSetlow0 =list()
polValue_trainSetlow0= list()
yHist_trainSet0Low = list()
for f in PolAsym_0Low:
        iFile0Low = ROOT.TFile.Open(f)
        iFile0Low.DiffinY.Scale(1/iFile0Low.DiffinY.Integral())
        yHist0Low = root_numpy.hist2array(iFile0Low.DiffinY)
       #addClassifier0Low= np.append(yHist0Low, 0)
       #yHist_trainSet0Low.append(addClassifier0Low)

        yHist_trainSet0Low.append(yHist0Low)
        iFile0Low.GenParam.GetEntry(0)
        polValue_trainSetlow0.append(iFile0Low.GenParam.PolDeg)
        iFile0Low.GenParam.GetEntry(1)
        asymValue_trainSetlow0.append(iFile0Low.GenParam.PolAng)

asymValue_trainSetlow23 =list()
polValue_trainSetlow23= list()
yHist_trainSet23Low = list()
for g in PolAsym_23Low:
        iFile23Low = ROOT.TFile.Open(g)
        iFile23Low.DiffinY.Scale(1/iFile23Low.DiffinY.Integral())
        yHist23Low = root_numpy.hist2array(iFile23Low.DiffinY)
        #addClassifier23Low = np.append(yHist23Low, 23)
        #yHist_trainSet23Low.append(addClassifier23Low)

        yHist_trainSet23Low.append(yHist23Low)
        iFile23Low.GenParam.GetEntry(0)
        polValue_trainSetlow23.append(iFile23Low.GenParam.PolDeg)
        iFile23Low.GenParam.GetEntry(1)
        asymValue_trainSetlow23.append(iFile23Low.GenParam.PolAng)


asymValue_trainSetlow45 =list()
polValue_trainSetlow45 = list()
yHist_trainSet45Low = list()
for h in PolAsym_45Low:
        iFile45Low = ROOT.TFile.Open(h)
        iFile45Low.DiffinY.Scale(1/iFile45Low.DiffinY.Integral())
        yHist45Low= root_numpy.hist2array(iFile45Low.DiffinY)
        #addClassifier45Low= np.append(yHist45Low, 45)
        #yHist_trainSet45Low.append(addClassifier45Low)

        yHist_trainSet45Low.append(yHist45Low)
        iFile45Low.GenParam.GetEntry(0)
        polValue_trainSetlow45.append(iFile45Low.GenParam.PolDeg)
        iFile45Low.GenParam.GetEntry(1)
        asymValue_trainSetlow45.append(iFile45Low.GenParam.PolAng)


asymValue_trainSetlow67 =list()
polValue_trainSetlow67 = list()
yHist_trainSet67Low = list()
for i in PolAsym_67Low:
        iFile67Low = ROOT.TFile.Open(i)
        iFile67Low.DiffinY.Scale(1/iFile67Low.DiffinY.Integral())
yHist67Low = root_numpy.hist2array(iFile67Low.DiffinY)
        #addClassifier67Low = np.append(yHist67Low, 67)
        #yHist_trainSet67Low.append(addClassifier67Low)

        yHist_trainSet67Low.append(yHist67Low)
        iFile67Low.GenParam.GetEntry(0)
        polValue_trainSetlow67.append(iFile67Low.GenParam.PolDeg)
        iFile67Low.GenParam.GetEntry(1)
        asymValue_trainSetlow67.append(iFile67Low.GenParam.PolAng)


asymValue_trainSetlow90 =list()
polValue_trainSetlow90= list()
yHist_trainSet90Low= list()
for j in PolAsym_90Low:
        iFile90Low = ROOT.TFile.Open(j)
        iFile90Low.DiffinY.Scale(1/iFile90Low.DiffinY.Integral())
        yHist90Low = root_numpy.hist2array(iFile90Low.DiffinY)
        #addClassifier90Low = np.append(yHist90Low, 90)
        #yHist_trainSet90Low.append(addClassifier90Low)

        yHist_trainSet90Low.append(yHist90Low)
        iFile90Low.GenParam.GetEntry(0)
        polValue_trainSetlow90.append(iFile90Low.GenParam.PolDeg)
        iFile90Low.GenParam.GetEntry(1)
        asymValue_trainSetlow90.append(iFile90Low.GenParam.PolAng)



asymValue_trainSetmed0 =list()
polValue_trainSetmed0= list()
yHist_trainSet0Med = list()
for k in PolAsym_0Med:
        iFile0Med = ROOT.TFile.Open(k)
        iFile0Med.DiffinY.Scale(1/iFile0Med.DiffinY.Integral())
        yHist0Med = root_numpy.hist2array(iFile0Med.DiffinY)
        #addClassifier0Med = np.append(yHist0Med, 0)
        #yHist_trainSet0Med.append(addClassifier0Med)

        yHist_trainSet0Med.append(yHist0Med)
        iFile0Med.GenParam.GetEntry(0)
        polValue_trainSetmed0.append(iFile0Med.GenParam.PolDeg)
        iFile0Med.GenParam.GetEntry(1)
        asymValue_trainSetmed0.append(iFile0Med.GenParam.PolAng)


asymValue_trainSetmed23 =list()
polValue_trainSetmed23 = list()
yHist_trainSet23Med = list()
for l in PolAsym_23Med:
        iFile23Med = ROOT.TFile.Open(l)
        iFile23Med.DiffinY.Scale(1/iFile23Med.DiffinY.Integral())
        yHist23Med = root_numpy.hist2array(iFile23Med.DiffinY)
        #addClassifier23Med = np.append(yHist23Med, 23)
        #yHist_trainSet23Med.append(addClassifier23Med)

        yHist_trainSet23Med.append(yHist23Med)
        iFile23Med.GenParam.GetEntry(0)
        polValue_trainSetmed23.append(iFile23Med.GenParam.PolDeg)
        iFile23Med.GenParam.GetEntry(1)
asymValue_trainSetmed23.append(iFile23Med.GenParam.PolAng)


asymValue_trainSetmed45 =list()
polValue_trainSetmed45 = list()
yHist_trainSet45Med = list()
for m in PolAsym_45Med:
        iFile45Med = ROOT.TFile.Open(m)
        iFile45Med.DiffinY.Scale(1/iFile45Med.DiffinY.Integral())
        yHist45Med= root_numpy.hist2array(iFile45Med.DiffinY)
        #addClassifier45Med= np.append(yHist45Med, 45)
        #yHist_trainSet45Med.append(addClassifier45Med)

        yHist_trainSet45Med.append(yHist45)
        iFile45Med.GenParam.GetEntry(0)
        polValue_trainSetmed45.append(iFile45Med.GenParam.PolDeg)
        iFile45Med.GenParam.GetEntry(1)
        asymValue_trainSetmed45.append(iFile45Med.GenParam.PolAng)


asymValue_trainSetmed67 =list()
polValue_trainSetmed67 = list()
yHist_trainSet67Med = list()
for n in PolAsym_67Med:
        iFile67Med = ROOT.TFile.Open(n)
        iFile67Med.DiffinY.Scale(1/iFile67Med.DiffinY.Integral())
        yHist67Med = root_numpy.hist2array(iFile67Med.DiffinY)
        #addClassifier67Med = np.append(yHist67Med, 67)
        #yHist_trainSet67Med.append(addClassifier67Med)

        yHist_trainSet67Med.append(yHist67)
        iFile67Med.GenParam.GetEntry(0)
        polValue_trainSetmed67.append(iFile67Med.GenParam.PolDeg)
        iFile67Med.GenParam.GetEntry(1)
        asymValue_trainSetmed67.append(iFile67Med.GenParam.PolAng)


asymValue_trainSetmed90 =list()
polValue_trainSetmed90= list()
yHist_trainSet90Med= list()
for o in PolAsym_90Med:
        iFile90Med = ROOT.TFile.Open(o)
        iFile90Med.DiffinY.Scale(1/iFile90Med.DiffinY.Integral())
        yHist90Med = root_numpy.hist2array(iFile90Med.DiffinY)
        #addClassifier90Med = np.append(yHist90Med, 90)
        #yHist_trainSet90Med.append(addClassifier90Med)

        yHist_trainSet90Med.append(yHist90)
        iFile90Med.GenParam.GetEntry(0)
        polValue_trainSetmed90.append(iFile90Med.GenParam.PolDeg)
        iFile90Med.GenParam.GetEntry(1)
        asymValue_trainSetmed90.append(iFile90Med.GenParam.PolAng)

yHist_trainSet = yHist_trainSet0 + yHist_trainSet23 + yHist_trainSet45 + yHist_trainSet67 + yHist_trainSet90 + yHist_trainSet0Med + yHist_trainSet23Med + yHist_trainSet45Med + yHist_trainSet67Med + yHist_trainSet90Med + yHist_trainSet0Low + yHist_trainSet23Low + yHist_trainSet45Low + yHist_trainSet67Low + yHist_trainSet90Low

polValue_trainSet = polValue_trainSet0 + polValue_trainSet23 + polValue_trainSet45 + polValue_trainSet67 + polValue_trainSet90 + polValue_trainSetmed0 + polValue_trainSetmed23 + polValue_trainSetmed45 + polValue_trainSetmed67 + polValue_trainSetmed90 + polValue_trainSetlow0 + polValue_trainSetlow23 + polValue_trainSetlow45 + polValue_trainSetlow67 + polValue_trainSetlow90

asymValue_trainSet = asymValue_trainSet0 + asymValue_trainSet23 + asymValue_trainSet45 + asymValue_trainSet67 + asymValue_trainSet90 + asymValue_trainSetmed0 + asymValue_trainSetmed23 + asymValue_trainSetmed45 + asymValue_trainSetmed67 + asymValue_trainSetmed90 + asymValue_trainSetlow0 + asymValue_trainSetlow23 + asymValue_trainSetlow45 + asymValue_trainSetlow67 + asymValue_trainSetlow90
subB=list()
subLR=list()
l=0
b=0
sub = TH1F("Sub", "Sub", 500, -3, 1)

count = 0
for b in range(0,4):
        for l in range(0,5):
                PDlist = ['0.125819975788',  '0.45148837067', '0.470843382701',   '0.635629120943',    '0.809748334731']
                PAlist = ['0', '45', '67', '90']

                fileName = "/w/work3/home/zach/PairPol/outFiles/irregularPoldeg_known/PolAsym_" + PAlist[b] + "/400MeV_" + PAlist[b] + "degrees_0mm_" + PDlist[l]+ "Pol_test.root"
                iFileTest = ROOT.TFile.Open(fileName)
                iFileTest.DiffinY.Scale(1/iFileTest.DiffinY.Integral())
                yHist_test = root_numpy.hist2array(iFileTest.DiffinY)
                yHist_testSet = [yHist_test]
                iFileTest.GenParam.GetEntry(0)
                polValue_testSet = [iFileTest.GenParam.PolDeg]
                asymValue_testSet = [iFileTest.GenParam.PolAng]

                import sklearn
                from sklearn.linear_model import LinearRegression, BayesianRidge
                from sklearn import linear_model
                from sklearn.gaussian_process import GaussianProcessRegressor

                predictorLR = LinearRegression()
                predictorLR_Asym = LinearRegression()
                predictorLR.fit(X=yHist_trainSet, y=polValue_trainSet)
                predictorLR_Asym.fit(X=yHist_trainSet, y=asymValue_trainSet)

                predictorB = BayesianRidge()
                predictorB_Asym = BayesianRidge()
                predictorB.fit(X=yHist_trainSet, y=polValue_trainSet)
                predictorB_Asym.fit(X=yHist_trainSet, y=asymValue_trainSet)

                predictorSGD = linear_model.SGDRegressor()
                predictorSGD_Asym = linear_model.SGDRegressor()
                predictorSGD.fit(X=yHist_trainSet, y=polValue_trainSet)
                predictorSGD_Asym.fit(X=yHist_trainSet, y=asymValue_trainSet)

                predictorGPR = GaussianProcessRegressor()
                predictorGPR_Asym = GaussianProcessRegressor()
                predictorGPR.fit(X=yHist_trainSet, y=polValue_trainSet)
                predictorGPR_Asym.fit(X=yHist_trainSet, y=asymValue_trainSet)

                outcomeGPR = predictorGPR.predict(X= yHist_testSet)
                #coefficientsGPR = predictorGPR.coef_
                outcomeGPR_Asym = predictorGPR_Asym.predict(X= yHist_testSet)


                outcomeLR = predictorLR.predict(X= yHist_testSet)

coefficientsLR = predictorLR.coef_

                outcomeB = predictorB.predict(X= yHist_testSet)
                coefficientsB = predictorB.coef_

                outcomeLR_Asym = predictorLR_Asym.predict(X= yHist_testSet)
                coefficientsLR_Asym = predictorLR_Asym.coef_

                outcomeB_Asym = predictorB_Asym.predict(X= yHist_testSet)
                coefficientsB_Asym = predictorB_Asym.coef_

                outcomeSGD = predictorSGD.predict(X= yHist_testSet)
                coefficientsSGD = predictorSGD.coef_

                outcomeSGD_Asym = predictorSGD_Asym.predict(X= yHist_testSet)
                coefficientsSGD_Asym = predictorSGD_Asym.coef_



                print('\n')
                print('------LINEAR--------')
                print(b)
                print('This is what the degree of polarization should be: {}  This is what the angle of polarization should be: {}\n'.format(polValue_testSet,np.degrees(asymValue_testSet)))
                print('This is what the ML algorithm said the degree of polarization should be: {}  And the angle of polarization: {}\n'.format(outcomeLR, np.degrees(outcomeLR_Asym)))
#print('Coefficients : {}'.format( coefficientsLR))

                subLR = np.subtract(outcomeLR,polValue_testSet)
                print "This is subLR: ", abs(subLR*100)

                print('------BAYESIAN------')
                print(b)
                print('This is what the degree of polarization should be: {}  This is what the angle of polarization should be: {}\n'.format(polValue_testSet,np.degrees(asymValue_testSet)))
                print('This is what the ML algorithm said the degree of polarization should be : {}  And the angle of polarization: {} \n'.format(outcomeB, np.degrees(outcomeB_Asym)))
#print('Coefficients : {}'.format( coefficientsB))

                subB = np.subtract(outcomeB,polValue_testSet)

                print "This is subB: ", abs(subB*100)

#               sub = TH1F("Sub", "Sub", 500, -8, 8)

                #sub.Fill(subLR)

                print('------GPR------')
                print(b)
                print('This is what the degree of polarization should be: {}  This is what the angle of polarization should be: {}\n'.format(polValue_testSet,np.degrees(asymValue_testSet)))
                print('This is what the ML algorithm said the degree of polarization should be : {}  And the angle of polarization: {} \n'.format(outcomeGPR, np.degrees(outcomeGPR_Asym)))


                subGPR = np.subtract(outcomeGPR, polValue_testSet)
                print "This the subGPR: ", abs(subGPR*100)
                count = count + 1


f, axarr = plt.subplots()

axarr.plot(sub)

f.savefig("sub.png")

print count
