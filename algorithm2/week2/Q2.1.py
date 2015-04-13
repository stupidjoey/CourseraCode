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
        anotherKeySet = set()
        for xorNode in xorNodeList:
            xorNode = int(xorNode, 2)
            anotherKey = bin(key ^ xorNode)
            anotherKeySet.add(anotherKey)
        hitKeySet = anotherKeySet & nodeValueSet
        if len(hitKeySet) != 0:
            hitNodeList = [ nodeDict[hitkey] for hitkey in hitKeySet]
            node1Leader = int(leaderPointer[node1,1])
            node2Leaders = list(leaderPointer[hitNodeList,1])
            union1Idx = leaderDict[node1Leader][:]
            maxUnionNum = len(union1Idx)
            maxUnionLeader = node1Leader

            unionIdxList = []
            unionIdxList.extend(union1Idx)
            nodeLeaders = []
            nodeLeaders.extend(node2Leaders)
            nodeLeaders.append(node1Leader)

            for node2Leader in node2Leaders:
                union2Idx = leaderDict[node2Leader][:]
                unionIdxList.extend(union2Idx)
                if len(union2Idx) > maxUnionNum:
                    maxUnionLeader = node2Leader
                    maxUnionNum = len(union2Idx)

            leaderDict[maxUnionLeader] = unionIdxList
            nodeLeaders.remove(maxUnionLeader)
            leaderPointer[unionIdxList,1] = maxUnionLeader
            # for nodeLeader in nodeLeaders:
                # del leaderDict[nodeLeader]
            nodeValueSet = nodeValueSet - hitKeySet

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