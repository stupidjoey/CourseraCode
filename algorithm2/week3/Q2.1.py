import sys
import numpy as np
import datetime
import copy

def main():
    starttime = datetime.datetime.now()

    currentPath = sys.path[0]
    dataPath = currentPath+'//knapsacktt.txt'
    nodeList,n,W = LoadData(dataPath)
    A = {}
    solve(n,W,nodeList,A)   
    print A[(n,W)]

    



    endtime = datetime.datetime.now()
    print 'passed time is %f' % (endtime - starttime).seconds

def solve(i,x,nodeList,A):
    if i <= 0:
        A[(i,x)] = 0
        return 0
    else:
        v = nodeList[i][0]
        w = nodeList[i][1]
        if w > x:
            if (i-1,x) not in A.keys():
                A[(i-1,x)] = solve(i-1, x, nodeList,A)
                A[(i,x)] = A[(i-1,x)]
            else:
                A[(i,x)] = A[(i-1,x)]
                
        else:
            if (i-1,x) in A.keys() and (i-1,x-w) in A.keys():
                A[(i,x)] = max( A[(i-1,x)], A[(i-1,x-w)] + v )
            else:
                A[(i-1,x)] = solve(i-1,x,nodeList,A)
                A[(i-1,x-w)] = solve(i-1,x-w,nodeList,A)
                A[(i,x)] = max( A[(i-1,x)], A[(i-1,x-w)]+ v )
            
    

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