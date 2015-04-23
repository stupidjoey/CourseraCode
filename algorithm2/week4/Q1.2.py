# -*- coding:utf-8 -*- 
import sys
import numpy as np
import datetime

''' use the floyd_warshall algorithm to solve the problem'''
'''  use dict instead of numpy array to store the A matrix '''

def main():
    starttime = datetime.datetime.now()
    
    currentpath = sys.path[0]
    datapath = currentpath +'\g1.txt'
    graph,vertex_num,edge_num = loaddata(datapath)
    floyd_warshall(graph,vertex_num,edge_num)
    
    endtime = datetime.datetime.now()
    print 'Elapsed time is %f' % (endtime - starttime).seconds

    
def floyd_warshall(graph,v_num,e_num):
    alledges = [(i,j) for i in xrange(1,v_num+1) for j in xrange(1,v_num+1)]
    A0 = {}.fromkeys(alledges,9999999)
    A1 = {}.fromkeys(alledges,9999999)   
    for i in xrange(1, v_num+1):
        A0[(i,i)] = 0
    edges = graph.keys()
    for edge,cost in graph.iteritems():
        i = edge[0]
        j = edge[1]
        A0[(i,j)] = cost
    
    for k in xrange(1, v_num+1):
        print k
        for i in xrange(1, v_num+1):
            for j in xrange(1, v_num+1):
                case1 = A0[(i,j)]
                # case2 = A0[(i,k)] + A0[(k,j)]
                # A1[(i,j)] = min(case1, case2)
        if k != v_num:        
            A0 = A1.copy()
    
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