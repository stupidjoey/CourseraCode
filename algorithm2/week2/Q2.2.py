import sys
import numpy as np
import copy
import datetime

def main():
    starttime = datetime.datetime.now()

    currentPath = sys.path[0]
    dataPath = currentPath + '/clustering_big.txt'
    nodeDict,nodeNum,bitNum,maxIntValue,minIntValue = LoadData(dataPath)
    xorNodeList = GetXORNodeList(bitNum)
    nodeSet = nodeDict.keys()[:]
    clusterNum = 0
    for node in nodeSet:
        if nodeDict[node] == 0:
            nodeDict = BFS(nodeDict,nodeSet,node,xorNodeList)
            clusterNum += 1

 
    print clusterNum
    endtime = datetime.datetime.now()
    print 'passed time is %f' % (endtime - starttime).seconds

    
def BFS(nodeDict,nodeSet,node,xorNodeList):
    nodeDict[node] = 1
    nodeQueue = []
    nodeQueue.append(node)
    while len(nodeQueue) != 0 :
        print len(nodeQueue)
        v = nodeQueue.pop(0)
        intV = int(v,2)
        for xorNode in xorNodeList:
            intXorNode = int(xorNode, 2)
            intW = intV ^ intXorNode
            w = bin(intW)
            if w in nodeSet:
                if nodeDict[w] == 0:
                    nodeDict[w] = 1
                    nodeQueue.append(w)
    return nodeDict
    
    
def GetXORNodeList(bitNum):
    xorNodeList = []
    baseNodeStr =  '0' * 24
    baseNode =  int( baseNodeStr , 2)

    for i in range(bitNum):
        
        xorNode = baseNode ^ (1 << i)
        bxorNode = bin(xorNode)
        xorNodeList.append(bxorNode)

    for i in range(0, bitNum-1):
        tempXorNodeI = baseNode ^ (1 << i)
        for j in range(i+1,bitNum):
            tempXorNodeJ = tempXorNodeI ^ (1 << j)
            bxorNode = bin(tempXorNodeJ)
            xorNodeList.append(bxorNode)

    return xorNodeList



def LoadData(dataPath):
    f = open(dataPath)
    dataSet = f.readlines()
    f.close()
    basicInfoStr = dataSet[0]
    basicInfo = basicInfoStr[:-1].split(' ')
    bitNum = int(basicInfo[1])
    nodeValueSet = set()
    
    maxIntValue = 0
    minIntValue = 1000000000
    nodeDict = dict()
    for dataStr in dataSet[1:4000]:
        binaryStr =  dataStr[:-1].replace(' ','')
        intValue = int(binaryStr,2)
        binValue = bin(intValue)
        nodeDict[binValue] = 0
        if intValue <= minIntValue:
            minIntValue = intValue
        if intValue >= maxIntValue:
            maxIntValue = intValue
        
        
    nodeNum = len(nodeDict.keys())
    return nodeDict,nodeNum,bitNum,maxIntValue,minIntValue
            




if __name__=='__main__':
    import profile
    profile.run("main()")