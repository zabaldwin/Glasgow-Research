#Python packages for manipulating the data
import numpy as np
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import sklearn
#from sklearn import svm
from glob import glob
import  root_numpy
from root_numpy import hist2array
import ROOT
from ROOT import *
import random
import scipy


def largestYValue(widthY,heightY):
        for y in range(1, widthY):
                if Yaxis[y] > heightY:
                        heightY = Yaxis[y]
        return heightY

def largestXValue(widthX, heightX):
        for x in range(1, widthX):
                if Xaxis[x] > heightX:
                        heightX = Xaxis[x]
        return heightX

def largest_inAll(entireWidth, entireHeight):
        for l in range(1, entireWidth):
                if yHist[l] > entireHeight:
                        entireHeight = yHist[l]
        return entireHeight

import math

def Euclidean_dist(point1, point2, length):
        dist =0
        for l in range(length):
                dist += pow(point1[l] - point2[l],2)
        return math.sqrt(dist)

import operator

def getNearNeighbors(trainSet, testInstance, k):
        Distances = []
        length = np.size(testInstance)
        for z in range(len(trainSet)):
                dist = Euclidean_dist(testInstance, trainSet[z], length)
                Distances.append((trainSet[z],dist))
        Distances.sort(key=operator.itemgetter(1))
        neighbors = []
        for w in range(k):
                neighbors.append(Distances[w][0])
                print "This is the neighbor: ", neighbors
        return neighbors

def getAttribute(neighbors):
        vote = {}
        for p in range(len(neighbors)):
                response = neighbors [p][-1]
                 if response in vote:
                        vote[response] += 1
                else:
                        vote[response] = 1
        arrangedVotes = sorted(vote.iteritems(),key = operator.itemgetter(1), reverse = True)
        return arrangedVotes [0][0]

def getAccuracy(testSet, predictions):
        correct = 0
        for g in range(len(testSet)):
                if testSet[g][-1] == predictions [g]:
                        correct += 1
        return (correct/float(len(testSet))) * 100


#def train_Input(PolAsym):

#Start______________________________________________________________

PolAsym_0 = glob("/w/work3/home/zach/PairPol/outFiles/methodicalPoldeg/PolAsym_0/400*.root")

PolAsym_23 = glob("/w/work3/home/zach/PairPol/outFiles/methodicalPoldeg/PolAsym_23/400*.root")

PolAsym_45 = glob("/w/work3/home/zach/PairPol/outFiles/methodicalPoldeg/PolAsym_45/400*.root")

PolAsym_67 = glob("/w/work3/home/zach/PairPol/outFiles/methodicalPoldeg/PolAsym_67/400*.root")

PolAsym_90 = glob("/w/work3/home/zach/PairPol/outFiles/methodicalPoldeg/PolAsym_90/400*.root")

PolAsym_0Med = glob("/w/work3/home/zach/PairPol/outFiles/methodicalPoldeg_medStats/PolAsym_0/400*.root")

PolAsym_23Med = glob("/w/work3/home/zach/PairPol/outFiles/methodicalPoldeg_medStats/PolAsym_23/400*.root")

PolAsym_45Med = glob("/w/work3/home/zach/PairPol/outFiles/methodicalPoldeg_medStats/PolAsym_45/400*.root")

PolAsym_67Med = glob("/w/work3/home/zach/PairPol/outFiles/methodicalPoldeg_medStats/PolAsym_67/400*.root")

PolAsym_90Med = glob("/w/work3/home/zach/PairPol/outFiles/methodicalPoldeg_medStats/PolAsym_90/400*.root")

PolAsym_0Low = glob("/w/work3/home/zach/PairPol/outFiles/methodicalPoldeg_lowStats/PolAsym_0/400*.root")

PolAsym_23Low = glob("/w/work3/home/zach/PairPol/outFiles/methodicalPoldeg_lowStats/PolAsym_23/400*.root")

PolAsym_45Low = glob("/w/work3/home/zach/PairPol/outFiles/methodicalPoldeg_lowStats/PolAsym_45/400*.root")

PolAsym_67Low = glob("/w/work3/home/zach/PairPol/outFiles/methodicalPoldeg_lowStats/PolAsym_67/400*.root")

PolAsym_90Low = glob("/w/work3/home/zach/PairPol/outFiles/methodicalPoldeg_lowStats/PolAsym_90/400*.root")

PolAsym_0Rand = glob("/w/work3/home/zach/PairPol/outFiles/ireggularPoldeg/PolAsym_0/400*.root")

PolAsym_23Rand = glob("/w/work3/home/zach/PairPol/outFiles/irregularPoldeg/PolAsym_23/400*.root")

PolAsym_45Rand = glob("/w/work3/home/zach/PairPol/outFiles/irregularPoldeg/PolAsym_45/400*.root")

PolAsym_67Rand = glob("/w/work3/home/zach/PairPol/outFiles/irregularPoldeg/PolAsym_67/400*.root")

PolAsym_90Rand = glob("/w/work3/home/zach/PairPol/outFiles/irrgegularPoldeg/PolAsym_90/400*.root")

PolAsym_0RandMed = glob("/w/work3/home/zach/PairPol/outFiles/ireggularPoldeg_medStats/PolAsym_0/400*.root")
PolAsym_23RandMed = glob("/w/work3/home/zach/PairPol/outFiles/irregularPoldeg_medStats/PolAsym_23/400*.root")

PolAsym_45RandMed = glob("/w/work3/home/zach/PairPol/outFiles/irregularPoldeg_medStats/PolAsym_45/400*.root")

PolAsym_67RandMed = glob("/w/work3/home/zach/PairPol/outFiles/irregularPoldeg_medStats/PolAsym_67/400*.root")

PolAsym_90RandMed = glob("/w/work3/home/zach/PairPol/outFiles/irrgegularPoldeg_medStats/PolAsym_90/400*.root")

PolAsym_0RandLow = glob("/w/work3/home/zach/PairPol/outFiles/ireggularPoldeg_lowStats/PolAsym_0/400*.root")

PolAsym_23RandLow = glob("/w/work3/home/zach/PairPol/outFiles/irregularPoldeg_lowStats/PolAsym_23/400*.root")

PolAsym_45RandLow = glob("/w/work3/home/zach/PairPol/outFiles/irregularPoldeg_lowStats/PolAsym_45/400*.root")

PolAsym_67RandLow = glob("/w/work3/home/zach/PairPol/outFiles/irregularPoldeg_lowStats/PolAsym_67/400*.root")

PolAsym_90RandLow = glob("/w/work3/home/zach/PairPol/outFiles/irrgegularPoldeg_lowStats/PolAsym_90/400*.root")




yHist_trainSet0 = list()
for a in PolAsym_0:
        iFile0 = ROOT.TFile.Open(a)
        iFile0.DiffinY.Scale(1/iFile0.DiffinY.Integral())
        yHist0 = root_numpy.hist2array(iFile0.DiffinY)
        addClassifier0= np.append(yHist0, 0)
        yHist_trainSet0.append(addClassifier0)

yHist_trainSet23 = list()
for b in PolAsym_23:
        iFile23 = ROOT.TFile.Open(b)
        iFile23.DiffinY.Scale(1/iFile23.DiffinY.Integral())
        yHist23 = root_numpy.hist2array(iFile23.DiffinY)
        addClassifier23 = np.append(yHist23, 23)
        yHist_trainSet23.append(addClassifier23)

yHist_trainSet45 = list()
for c in PolAsym_45:
        iFile45 = ROOT.TFile.Open(c)
        iFile45.DiffinY.Scale(1/iFile45.DiffinY.Integral())
        yHist45 = root_numpy.hist2array(iFile45.DiffinY)
        addClassifier45= np.append(yHist45, 45)
        yHist_trainSet45.append(addClassifier45)


yHist_trainSet67 = list()
for d in PolAsym_67:
        iFile67 = ROOT.TFile.Open(d)
        iFile67.DiffinY.Scale(1/iFile67.DiffinY.Integral())
        yHist67 = root_numpy.hist2array(iFile67.DiffinY)
        addClassifier67 = np.append(yHist67, 67)
        yHist_trainSet67.append(addClassifier67)

yHist_trainSet90 = list()
for e in PolAsym_90:
        iFile90 = ROOT.TFile.Open(e)
        iFile90.DiffinY.Scale(1/iFile90.DiffinY.Integral())
        yHist90 = root_numpy.hist2array(iFile90.DiffinY)
        addClassifier90 = np.append(yHist90, 90)
        yHist_trainSet90.append(addClassifier90)

yHist_trainSet0Rand = list()
for f in PolAsym_0Rand:
        iFile0Rand = ROOT.TFile.Open(f)
        iFile0Rand.DiffinY.Scale(1/iFile0Rand.DiffinY.Integral())
        yHist0Rand = root_numpy.hist2array(iFile0Rand.DiffinY)
        addClassifier0Rand= np.append(yHist0Rand, 0)
        yHist_trainSet0Rand.append(addClassifier0Rand)

yHist_trainSet23Rand = list()
for g in PolAsym_23Rand:
        iFile23Rand = ROOT.TFile.Open(g)
        iFile23Rand.DiffinY.Scale(1/iFile23Rand.DiffinY.Integral())
        yHist23Rand = root_numpy.hist2array(iFile23Rand.DiffinY)
        addClassifier23Rand = np.append(yHist23Rand, 23)
        yHist_trainSet23Rand.append(addClassifier23Rand)

yHist_trainSet45Rand = list()
for h in PolAsym_45Rand:
        iFile45Rand = ROOT.TFile.Open(h)
        iFile45Rand.DiffinY.Scale(1/iFile45Rand.DiffinY.Integral())
        yHist45Rand = root_numpy.hist2array(iFile45Rand.DiffinY)
        addClassifier45Rand= np.append(yHist45Rand, 45)
        yHist_trainSet45Rand.append(addClassifier45Rand)


yHist_trainSet67Rand = list()
for i in PolAsym_67Rand:
        iFile67Rand = ROOT.TFile.Open(i)
        iFile67Rand.DiffinY.Scale(1/iFile67Rand.DiffinY.Integral())
        yHist67Rand = root_numpy.hist2array(iFile67Rand.DiffinY)
        addClassifier67Rand = np.append(yHist67Rand, 67)
        yHist_trainSet67Rand.append(addClassifier67Rand)

yHist_trainSet90Rand = list()
for j in PolAsym_90Rand:
        iFile90Rand = ROOT.TFile.Open(j)
        iFile90Rand.DiffinY.Scale(1/iFile90Rand.DiffinY.Integral())
        yHist90Rand = root_numpy.hist2array(iFile90Rand.DiffinY)
        addClassifier90Rand = np.append(yHist90Rand, 90)
        yHist_trainSet90Rand.append(addClassifier90Rand)

yHist_trainSet0Low = list()
for k in PolAsym_0Low:
        iFile0Low = ROOT.TFile.Open(k)
        iFile0Low.DiffinY.Scale(1/iFile0Low.DiffinY.Integral())
        yHist0Low = root_numpy.hist2array(iFile0Low.DiffinY)
        addClassifier0Low= np.append(yHist0Low, 0)
        yHist_trainSet0Low.append(addClassifier0Low)

yHist_trainSet23Low = list()
for l in PolAsym_23Low:
        iFile23Low = ROOT.TFile.Open(l)
        iFile23Low.DiffinY.Scale(1/iFile23Low.DiffinY.Integral())
        yHist23Low = root_numpy.hist2array(iFile23Low.DiffinY)
        addClassifier23Low = np.append(yHist23Low, 23)
        yHist_trainSet23Low.append(addClassifier23Low)

yHist_trainSet45Low = list()
for m in PolAsym_45Low:
iFile45Low = ROOT.TFile.Open(m)
        iFile45Low.DiffinY.Scale(1/iFile45Low.DiffinY.Integral())
        yHist45Low= root_numpy.hist2array(iFile45Low.DiffinY)
        addClassifier45Low= np.append(yHist45Low, 45)
        yHist_trainSet45Low.append(addClassifier45Low)


yHist_trainSet67Low = list()
for n in PolAsym_67Low:
        iFile67Low = ROOT.TFile.Open(n)
        iFile67Low.DiffinY.Scale(1/iFile67Low.DiffinY.Integral())
        yHist67Low = root_numpy.hist2array(iFile67Low.DiffinY)
        addClassifier67Low = np.append(yHist67Low, 67)
        yHist_trainSet67Low.append(addClassifier67Low)

yHist_trainSet90Low= list()
for o in PolAsym_90Low:
        iFile90Low = ROOT.TFile.Open(o)
        iFile90Low.DiffinY.Scale(1/iFile90Low.DiffinY.Integral())
        yHist90Low = root_numpy.hist2array(iFile90Low.DiffinY)
        addClassifier90Low = np.append(yHist90Low, 90)
        yHist_trainSet90Low.append(addClassifier90Low)

yHist_trainSet0Med = list()
for p in PolAsym_0Med:
        iFile0Med = ROOT.TFile.Open(p)
        iFile0Med.DiffinY.Scale(1/iFile0Med.DiffinY.Integral())
        yHist0Med = root_numpy.hist2array(iFile0Med.DiffinY)
        addClassifier0Med = np.append(yHist0Med, 0)
        yHist_trainSet0Med.append(addClassifier0Med)

yHist_trainSet23Med = list()
for q in PolAsym_23Med:
        iFile23Med = ROOT.TFile.Open(q)
        iFile23Med.DiffinY.Scale(1/iFile23Med.DiffinY.Integral())
        yHist23Med = root_numpy.hist2array(iFile23Med.DiffinY)
        addClassifier23Med = np.append(yHist23Med, 23)
        yHist_trainSet23Med.append(addClassifier23Med)

yHist_trainSet45Med = list()
for r in PolAsym_45Med:
        iFile45Med = ROOT.TFile.Open(r)
        iFile45Med.DiffinY.Scale(1/iFile45Med.DiffinY.Integral())
        yHist45Med= root_numpy.hist2array(iFile45Med.DiffinY)
        addClassifier45Med= np.append(yHist45Med, 45)
        yHist_trainSet45Med.append(addClassifier45Med)


yHist_trainSet67Med = list()
for s in PolAsym_67Med:
        iFile67Med = ROOT.TFile.Open(s)
        iFile67Med.DiffinY.Scale(1/iFile67Med.DiffinY.Integral())
        yHist67Med = root_numpy.hist2array(iFile67Med.DiffinY)
        addClassifier67Med = np.append(yHist67Med, 67)
        yHist_trainSet67Med.append(addClassifier67Med)

yHist_trainSet90Med= list()
for t in PolAsym_90Med:
        iFile90Med = ROOT.TFile.Open(t)
        iFile90Med.DiffinY.Scale(1/iFile90Med.DiffinY.Integral())
        yHist90Med = root_numpy.hist2array(iFile90Med.DiffinY)
        addClassifier90Med = np.append(yHist90Med, 90)
        yHist_trainSet90Med.append(addClassifier90Med)



yHist_trainSet = yHist_trainSet0 + yHist_trainSet23 + yHist_trainSet45 +  yHist_trainSet67 + yHist_trainSet90 + yHist_trainSet0Rand + yHist_trainSet23Rand + yHist_trainSet45Rand + yHist_trainSet67Rand + yHist_trainSet90Rand + yHist_trainSet0Low + yHist_trainSet23Low + yHist_trainSet45Low + yHist_trainSet67Low + yHist_trainSet90Low + yHist_trainSet0Med + yHist_trainSet23Med + yHist_trainSet45Med + yHist_trainSet67Med + yHist_trainSet90Med

iFileTest = ROOT.TFile.Open("/w/work3/home/zach/PairPol/outFiles/irregularPoldeg/PolAsym_%d/400MeV_%ddegrees_0mm_0.45148837067Pol_Y.root" % (90, 90))
#iFileTest = ROOT.TFile.Open("/w/work3/home/zach/PairPol/outFiles/irregularPoldeg_medStats/PolAsym_%d/400MeV_%ddegrees_0mm_0.809748334731Pol_Y.root" % (90, 90))
#iFileTest = ROOT.TFile.Open("/w/work3/home/zach/PairPol/outFiles/methodicalPoldeg_lowStats/PolAsym_67/400MeV_67degrees_0mm_0Pol_Y.root")
iFileTest.DiffinY.Scale(1/iFileTest.DiffinY.Integral())
yHist_test = root_numpy.hist2array(iFileTest.DiffinY)
yHist_testSet = [yHist_test]


k = 1
for x in range(len(yHist_testSet)):
        neighbors = getNearNeighbors(yHist_trainSet, yHist_testSet[x], k)
        result = getAttribute(neighbors)
#print "The PolAsym is: ", int(result)

f, axarr = plt.subplots()

axarr.plot(yHist_test)

polAsym = 'The PolAsym for this graph is:  %d' %(result,)
axarr.set_title(polAsym)
f.savefig("PolAsym")
plt.show()
