import sys
import numpy as np
import copy
import datetime

def main():
    starttime = datetime.datetime.now()

    currentPath = sys.path[0]
    dataPath = currentPath + '/clustering_big.txt'
    nodeSet,leaderPointer,leaderDict,nodeNum,bitNum = LoadData(dataPath)
    xorNodeSet = GetXORNodeSet(bitNum)
    for node1 in nodeSet:
        intNode1 = int(node1,2)
        
        for xorNode in xorNodeSet:
            intXorNode = int(xorNode, 2)
            node2 = bin(intNode1 ^ intXorNode)
            # if node2 in nodeSet:
                # intNode2 = int(node2,2)          
                # node1Leader = leaderPointer[intNode1,1]
                # node2Leader = leaderPointer[intNode2,1]               
                # if node1Leader != node2Leader:
                    # union1Idx = leaderDict[node1Leader][:]
                    # union2Idx = leaderDict[node2Leader][:]
                    # union1Num = len(union1Idx)
                    # union2Num = len(union2Idx)
                    # if union1Num >= union2Num:  
                        # leaderDict[node1Leader].extend(union2Idx)
                        # leaderPointer[union2Idx,1] = node1Leader
                        # del leaderDict[node2Leader]
                    # else:
                        # leaderDict[node2Leader].append(union1Idx)
                        # leaderPointer[union1Idx,1] = node2Leader
                        # del leaderDict[node1Leader]
                    # nodeSet = nodeSet - set([node2])

    # clusterSet = set(leaderPointer[:,1])
    # print len(clusterSet) - 1

    endtime = datetime.datetime.now()
    print 'passed time is %f' % (endtime - starttime).seconds

def GetXORNodeSet(bitNum):
    xorNodeSet = set()
    baseNodeStr =  '0' * 24
    baseNode =  int( baseNodeStr , 2)

    for i in range(bitNum):
        
        xorNode = baseNode ^ (1 << i)
        bxorNode = bin(xorNode)
        xorNodeSet.add(bxorNode)

    for i in range(0, bitNum-1):
        tempXorNodeI = baseNode ^ (1 << i)
        for j in range(i+1,bitNum):
            tempXorNodeJ = tempXorNodeI ^ (1 << j)
            bxorNode = bin(tempXorNodeJ)
            xorNodeSet.add(bxorNode)

    return xorNodeSet


def LoadData(dataPath):
    f = open(dataPath)
    dataSet = f.readlines()
    f.close()
    basicInfoStr = dataSet[0]
    basicInfo = basicInfoStr[:-1].split(' ')
    bitNum = int(basicInfo[1])
    nodeSet = set()
    leaderPointer = np.zeros((2**24,2))
    leaderDict = dict()
    for dataStr in dataSet[1:2000]:
        binaryStr =  dataStr[:-1].replace(' ','')
        intValue = int(binaryStr,2)
        binValue = bin(intValue)
        nodeSet.add(binValue)
        leaderPointer[intValue,1] = intValue
        leaderDict[intValue] = [intValue]
    nodeNum = len(nodeSet)
    
    
    return nodeSet,leaderPointer,leaderDict,nodeNum,bitNum
            






if __name__=='__main__':
    import profile
    profile.run("main()")