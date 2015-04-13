import sys
import numpy as np
import copy
import datetime

def main():
    starttime = datetime.datetime.now()

    currentPath = sys.path[0]
    dataPath = currentPath + '/clustering_big.txt'
    nodeDict,nodeNum,bitNum = LoadData(dataPath)
    xorNodeList = GetXORNodeList(bitNum)
    leaderPointer,leaderDict = GetUnionData(nodeNum)  # with 0 in the first row
    nodeValueSet = set(nodeDict.keys())

    # print nodeValueSet
    # print 'hahahaha'
    # a = '0b1000110110000010'
    # y = set([a])
    # print y
    # print len(nodeValueSet)
    # print len(nodeValueSet - y)
    # a = set(('0b0011','0b0101'))
    # print a

    for key in nodeValueSet:
        print len(nodeValueSet)
        node1 = nodeDict[key]
        key = int(key,2)
        for xorNode in xorNodeList:
            xorNode = int(xorNode, 2)
            anotherKey = bin(key ^ xorNode)
            if anotherKey in nodeValueSet:
                node2 = nodeDict[anotherKey]
                node1Leader = leaderPointer[node1,1]
                node2Leader = leaderPointer[node2,1]
                if node1Leader != node2Leader:
                    union1Idx = leaderDict[node1Leader][:]
                    union2Idx = leaderDict[node2Leader][:]
                    union1Num = len(union1Idx)
                    union2Num = len(union2Idx)
                    if union1Num >= union2Num:  
                        leaderDict[node1Leader].extend(union2Idx)
                        leaderPointer[union2Idx,1] = node1Leader
                        del leaderDict[node2Leader]
                    else:
                        leaderDict[node2Leader].append(union1Idx)
                        leaderPointer[union1Idx,1] = node2Leader
                        del leaderDict[node1Leader]
                    nodeValueSet = nodeValueSet - set([anotherKey])

    clusterSet = set(leaderPointer[:,1])
    print len(clusterSet) - 1

    endtime = datetime.datetime.now()
    print 'passed time is %f' % (endtime - starttime).seconds

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

def GetUnionData(nodeNum):
    leaderPointer = [[0,0]]
    leaderDict = dict()
    for i in range(nodeNum):
        node = i + 1
        leaderPointer.append([node,node])
        leaderDict[node] = [i+1]
    leaderPointer = np.array(leaderPointer)
    return leaderPointer,leaderDict


def LoadData(dataPath):
    f = open(dataPath)
    dataSet = f.readlines()
    f.close()
    basicInfoStr = dataSet[0]
    basicInfo = basicInfoStr[:-1].split(' ')
    bitNum = int(basicInfo[1])

    nodeDict = dict()
    

    nodeValueSet = set()
    for dataStr in dataSet[1:]:
        binaryStr =  dataStr[:-1].replace(' ','')
        a = int(binaryStr,2)
        b = bin(a)
        nodeValue = b
        nodeValueSet.add(nodeValue)
    nodeIdx = 0
    for nodeValue in nodeValueSet:
        nodeIdx +=1
        nodeDict[nodeValue] = nodeIdx
    nodeNum = len(nodeValueSet)
    return nodeDict,nodeNum,bitNum
            






if __name__=='__main__':
    main()