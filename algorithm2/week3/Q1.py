import sys
import numpy as np

def main():
    currentPath = sys.path[0]
    dataPath = currentPath+'//knapsack1.txt'
    nodeList,n,W = LoadData(dataPath)
    A = np.zeros((n+1, W+1))
    for i in range(1,n+1):
        for x in range(0, W+1):
            valueI = nodeList[i][0]
            weightI = nodeList[i][1]
            if x < weightI:
                A[i,x] = A[i-1, x]
            else:
                A[i,x] = max(A[i-1, x], A[i-1, x - weightI] + valueI)

    print A[n,W]




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