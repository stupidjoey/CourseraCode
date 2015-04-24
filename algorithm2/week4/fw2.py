# -*- coding:utf-8 -*- 
import sys
import numpy as np
import datetime

''' use the floyd_warshall algorithm to solve the problem'''
''' use n*n*1 to store A '''
INF = 999999
def main():
    starttime = datetime.datetime.now()
    
    currentpath = sys.path[0]
    datapath = currentpath +'\g1.txt'
    A,vertex_num,edge_num = loaddata(datapath)
    floyd_warshall(A,vertex_num,edge_num)
    
    endtime = datetime.datetime.now()
    print 'Elapsed time is %.2f' % (endtime - starttime).seconds

    
def floyd_warshall(A,v_num,e_num):
    for k in xrange(1, v_num+1):
        # print k
        case2Mat1 = A[:,k].reshape((-1,1)) 
        case2Mat2 = A[k,:].reshape((1,-1))
        case2Mat = case2Mat1 + case2Mat2
        idx = case2Mat <= A
        A[idx] = case2Mat[idx]
    
    # output the final result    
    negCycFlag = False       
    for i in xrange(1,v_num+1):
        if A[i,i] < 0 :
            negCycFlag = True
            break
    if  negCycFlag == True:
        print 'there is a negative cycle'
    else:
        print A.min()

        
def loaddata(datapath):
    f = open(datapath)
    dataset = f.readlines()
    f.close()
    basic_info = dataset[0][:-1].split(' ')
    vertex_num = int(basic_info[0])
    edge_num = int(basic_info[1])
    A = np.ones((vertex_num+1, vertex_num+1)) * INF
    for i in xrange(1, vertex_num+1):
        A[i,i] = 0
    for line in dataset[1:]:
        data = line[:-1].split(' ')
        data = map(int, data)
        tailv = data[0]
        headv = data[1]
        cost = data[2]
        A[tailv,headv] = cost
    return A,vertex_num,edge_num
    
    
    
    
    
    
    
if __name__=='__main__':
    import profile
    profile.run("main()")