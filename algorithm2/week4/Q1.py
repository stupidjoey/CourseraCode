# -*- coding:utf-8 -*- 
import sys
import numpy as np
import datetime

''' use the bellman_ford algorithm to solve the problem'''
def main():
    starttime = datetime.datetime.now()
    
    currentpath = sys.path[0]
    datapath = currentpath +'\g1.txt'
    graph,vertex_num,edge_num = loaddata(datapath)
    bellman_ford(graph,vertex_num,edge_num)
    
    endtime = datetime.datetime.now()
    print 'Elapsed time is %f' % (endtime - starttime).seconds

def bellman_ford(graph,v_num,e_num):

    for s in xrange(1, v_num+1):
        A = np.ones((2, v_num+1)) * 999999
        print s
        A[0, s] = 0
        for i in xrange(1, v_num+1):
            for v in xrange(1, v_num+1):
                case1 = A[0, v]
                case2 = 999999
                edges = graph[v]
                for edge in edges:
                    w = edge[0]
                    cost = edge[2]
                    if A[0, w] + cost <= case2:
                        case2 = A[0, w] + cost
                A[1,v] = min(case1, case2)
                
            if i != v_num:
                A[0,:] = A[1,:]
                
        print A[0,2]
        
        
    # minpath = 100000            
    # for s in xrange(1, v_num+1):
        # spath = A[v_num-1, s]
        # if spath != A[v_num, s]:
            # print 'there is a negative cycle'
            # break
        # if spath <= minpath:
            # minpath = spath
    # print minpath
        
    
    
    
      
def floyd_warshall(graph,v_num,e_num):
    A = np.zeros((v_num+1, v_num+1, e_num+1))
    edges = graph.keys()
    
    
def loaddata(datapath):
    f = open(datapath)
    dataset = f.readlines()
    f.close()
    basic_info = dataset[0][:-1].split(' ')
    vertex_num = int(basic_info[0])
    edge_num = int(basic_info[1])
    graph = {}.fromkeys(xrange(1,vertex_num+1),[])
    for line in dataset[1:]:
        data = line[:-1].split(' ')
        data = map(int, data)
        tailv = data[0]
        headv = data[1]
        cost = data[2]
        edges = graph[headv][:]
        edges.append([tailv,headv,cost])
        graph[headv] = edges
    return graph,vertex_num,edge_num
    
    
    
    
    
    
    
if __name__=='__main__':
    main()