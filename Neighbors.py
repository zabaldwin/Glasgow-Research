import math

def Euclidean_dist(point1, point2, length):
        dist =0
        for l in range(length):
                dist += pow(point1[l] - point2[l],2)
        return math.sqrt(dist)


distance = Euclidean_dist([5,5,5, 'a'], [4, 4,4, 'b'], 2)
print distance

import operator

def getNearNeighbors(trainSet, testInstance, k):
        Distances = []
        length = len(testInstance)-1
        for z in range(len(trainSet)):
                dist = Euclidean_dist(testInstance, trainSet[z], length)
                Distances.append((trainSet[z],dist))
        Distances.sort(key=operator.itemgetter(1))
        neighbors = []
        for w in range(k):
                neighbors.append(Distances[w][0])
        return neighbors






trainSet = [[1,1,1,1], [3,3,3,3], [6,6,6,6], [5,5,5,5]]
testInstance = [4,4,4,4]
k = 3
neighbors = getNearNeighbors(trainSet, testInstance, 1)
print neighbors

import operator
def getResponse(neighbors):
        classVotes = {}
        for x in range(len(neighbors)):
                response = neighbors[x][-1]
                #print response
                if response in classVotes:
                        classVotes[response] += 1
                else:
                        classVotes[response] = 1
        sortedVotes = sorted(classVotes.iteritems(), key=operator.itemgetter(1), reverse=True)
        return sortedVotes[0][0]





neighbors = [[1,1,1,'a'], [2,2,2,'b'], [3,3,3,'c']]
response = getResponse(neighbors)

print response
