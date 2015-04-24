# -*- coding:utf-8 -*- 
import sys
import numpy as np
import datetime

''' use the floyd_warshall algorithm to solve the problem'''
''' use n*n*2 to store A '''

def main():
    starttime = datetime.datetime.now()
    
    currentpath = sys.path[0]
    datapath = currentpath +'\g1.txt'
    graph,vertex_num,edge_num = loaddata(datapath)
    floyd_warshall(graph,vertex_num,edge_num)
    
    endtime = datetime.datetime.now()
    print 'Elapsed time is %.2f' % (endtime - starttime).seconds

    
def floyd_warshall(graph,v_num,e_num):
    A = np.ones((v_num+1, v_num+1, 2)) * 9999999
    for i in xrange(1, v_num+1):
        A[i,i,0] = 0
    edges = graph.keys()
    for edge,cost in graph.iteritems():
        i = edge[0]
        j = edge[1]
        A[i,j,0] = cost
    
    for k in xrange(1, v_num+1):
        # print k
        case1Mat = A[:,:,0]
        case2Mat1 = A[:,k,0].reshape((-1,1)) 
        case2Mat2 = A[k,:,0].reshape((1,-1))
        case2Mat = case2Mat1 + case2Mat2
        idx = case1Mat <= case2Mat
        A[:,:,1][idx] = case1Mat[idx]
        A[:,:,1][~idx] = case2Mat[~idx]
        if k != v_num:        
            A[:,:,0] = A[:,:,1]
  
       
    
    # output the final result    
    negCycFlag = False       
    for i in xrange(1,v_num+1):
        if A[i,i,1] < 0 :
            negCycFlag = True
            break
    if  negCycFlag == True:
        print 'there is a negative cycle'
    else:
        print A[:,:,1].min()

        
def loaddata(datapath):
    f = open(datapath)
    dataset = f.readlines()
    f.close()
    basic_info = dataset[0][:-1].split(' ')
    vertex_num = int(basic_info[0])
    edge_num = int(basic_info[1])
    graph = {}
    for line in dataset[1:]:
        data = line[:-1].split(' ')
        data = map(int, data)
        tailv = data[0]
        headv = data[1]
        cost = data[2]
        graph[(tailv,headv)] = cost
    return graph,vertex_num,edge_num
    
    
    
    
    
    
    
if __name__=='__main__':
    main()