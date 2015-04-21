import sys
import numpy as np
import datetime
import copy

def main():
    starttime = datetime.datetime.now()

    currentPath = sys.path[0]
    dataPath = currentPath+'//knapsack_big.txt'
    nodeList,n,W = LoadData(dataPath)
    A = {}
    IXset = set()
    stack = [(n,W)]
    search(nodeList,A,IXset,stack)
    print A[(n,W)]

    



    endtime = datetime.datetime.now()
    print 'passed time is %f' % (endtime - starttime).seconds

def search(nodeList,A,IXset,stack):
    while(len(stack) >0):
        i,x = stack[0]
        if i<=0:
            A[(i,x)] = 0
            IXset.add((i,x))
            stack.pop(0)
        else:
            v = nodeList[i][0]
            w = nodeList[i][1]
            if w > x:
                if (i-1,x) not in IXset:
                    stack.insert(0,(i-1,x))
                    continue
                    
                A[(i,x)] = A[(i-1,x)]
                stack.pop(0)
                IXset.add((i,x))            
            else:
                if (i-1,x) not in IXset :
                    stack.insert(0,(i-1,x))
                    continue
                if (i-1,x-w) not in IXset:
                    stack.insert(0,(i-1,x-w))
                    continue
                    
                A[(i,x)] = max( A[(i-1,x)], A[(i-1,x-w)]+ v )
                stack.pop(0)
                IXset.add((i,x))     


            
   
   
    
def solve(i,x,nodeList,A,IXset):
    if i <= 0:
        A[(i,x)] = 0
        IXset.add((i,x))
        return A[(i,x)]
    else:
        v = nodeList[i][0]
        w = nodeList[i][1]
        if w > x:
            if (i-1,x) not in IXset:
                A[(i-1,x)] = solve(i-1, x, nodeList,A,IXset)
                IXset.add((i-1,x))
            A[(i,x)] = A[(i-1,x)]
            
         
              
        else:
            if (i-1,x) not in IXset :
                A[(i-1,x)] = solve(i-1,x,nodeList,A,IXset)
                IXset.add((i-1, x))
            if (i-1,x-w) not in IXset:
                A[(i-1,x-w)] = solve(i-1,x-w,nodeList,A,IXset)   
                IXset.add((i-1, x-w))                
            A[(i,x)] = max( A[(i-1,x)], A[(i-1,x-w)]+ v )
            
        IXset.add((i,x))
        return A[(i,x)]
            
    

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