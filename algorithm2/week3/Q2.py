import sys
import numpy as np
import datetime
import copy

def main():
    starttime = datetime.datetime.now()

    currentPath = sys.path[0]
    dataPath = currentPath+'//knapsack1.txt'
    nodeList,n,W = LoadData(dataPath)
    nodeArray = np.array(nodeList)
    A = np.zeros((1, W+1))
    for i in range(1,n+1):
        print i
        valueI = int(nodeArray[i, 0])
        weightI = int(nodeArray[i, 1])

        xIdx21 = range(weightI, W+1)
        xIdx22 = range(0, W+1 - weightI)
        compare = A[0,xIdx21] + valueI > A[0, xIdx22]

        xIdx2 = xIdx21 * compare
        xIdx2[xIdx2 == 0 ] = []
        print len(list(xIdx2))
        print len(list(xIdx2 - weightI))


        print A[0, list(xIdx2)]
        print 'ha'
        print valueI
        A[0, list(xIdx2)] = A[0, list(xIdx2 - weightI) ]
        A[0, list(xIdx2)] = A[0, list(xIdx2)] + 1111
        # A[0,list(xIdx2)] += valueI

    print A[0,W]


    endtime = datetime.datetime.now()
    print 'passed time is %f' % (endtime - starttime).seconds



def LoadData(dataPath):
    f = open(dataPath)
    dataSet = f.readlines()
    f.close()

    baseInfoStr = dataSet[0]
    baseInfo = baseInfoStr[:-1].split(' ')
    maxW = int(baseInfo[0])
    nodeNum = int(baseInfo[1])
    
    nodeList = [[0,0]]
    for dataStr in dataSet[1:]:
        data = dataStr[:-1].split(' ')
        value = int(data[0])
        weight = int(data[1])
        nodeList.append([value,weight])

    return nodeList,nodeNum,maxW

if __name__=='__main__':
    main()