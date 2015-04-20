import sys
import numpy as np
import datetime
import copy

def main():
    starttime = datetime.datetime.now()

    currentPath = sys.path[0]
    dataPath = currentPath+'//knapsack_big.txt'
    nodeList,n,W = LoadData(dataPath)
    nodeArray = np.array(nodeList)
    A = np.zeros((2, W+1))

    for i in range(1,n+1):
        print i
        valueI = nodeArray[i, 0]
        weightI = nodeArray[i, 1]
        
        # xIdx21 = xrange(weightI, W+1)        
        # xIdx22 = xrange(0, W+1 - weightI)
        
        for x in range(weightI, W+1):
            A[1,x] = max(A[0,x], A[0, x-weightI] + valueI)
        
        A[0,:] = A[1,:]
        

    print A[1,W]

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