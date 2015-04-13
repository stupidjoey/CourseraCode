import sys
import numpy as np

''' using the kruskal algorithm to solve the single-link clustering problem'''
''' speed up kruskal by union find data structure '''


def main():
    currentPath = sys.path[0]
    dataPath = currentPath+'//clustering1.txt'
    edgeList, nodeNum = LoadData(dataPath)
    sortedEdgeList = sorted(edgeList, key = lambda x:x[2], reverse = False )
    leaderPointer = GetUnionData(nodeNum)  # with 0 in the first row
    K = 4
    minCost = 0

    ## kruskal algorithm
    for edge in sortedEdgeList:
        node1 = edge[0]
        node2 = edge[1]
        cost = edge[2]
        node1Leader = leaderPointer[node1,1]
        node2Leader = leaderPointer[node2,1]
        if node1Leader != node2Leader:
            clusterSet = set(leaderPointer[:,1])
            if len(clusterSet) - 1 == K:   # exclude the 0 in the first row of leaderPointer
                minCost = cost
                break
            else:
                union1Idx = leaderPointer[:,1] == node1Leader
                union2Idx = leaderPointer[:,1] == node2Leader
                union1Num = sum(union1Idx)
                union2Num = sum(union2Idx)
                if union1Num >= union2Num:  
                    leaderPointer[union2Idx,1] = node1Leader
                else:
                    leaderPointer[union1Idx,1] = node2Leader
        else:
            continue

    np.set_printoptions(threshold='nan')       
    print len(set(leaderPointer[:,1]))
    print minCost



## the union find data structure
def GetUnionData(nodeNum):
    leaderPointer = [[0,0]]
    for i in range(nodeNum):
        leaderPointer.append([i+1,i+1])
    leaderPointer = np.array(leaderPointer)
    return leaderPointer


def LoadData(dataPath):
    f = open(dataPath)
    dataSet = f.readlines()
    f.close()
    edgeList = []
    nodeNum = int(dataSet[0][:-1])
    dataSet = dataSet[1:]
    for dataStr in dataSet:
        data = dataStr[:-1].split(' ')
        node1 = int(data[0])
        node2 = int(data[1])
        cost = int(data[2])
        edgeList.append([node1,node2,cost])

    return edgeList,nodeNum





if __name__=='__main__':
    main()