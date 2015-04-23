# -*- coding:utf-8 -*- 
import sys
import numpy as np
import datetime
import heapq

''' use the johnson algorithm to solve the problem'''

def main():
    starttime = datetime.datetime.now()
    
    currentpath = sys.path[0]
    datapath = currentpath +'\gtest.txt'
    graph,headgraph,tailgraph,vertex_num,edge_num = loaddata(datapath)
    johnson(graph,headgraph,vertex_num,edge_num)
    
    endtime = datetime.datetime.now()
    print 'Elapsed time is %f' % (endtime - starttime).seconds


    
def johnson(graph,headgraph,tailgraph,v_num,e_num):

    #  step 1 add a new tail vertex s into the headgraph
    # turn it into headgraph_prim
    s = v_num + 1
    headgraph_prim = headgraph.copy()
    for headv in xrange(1, v_num + 1):       
        edges = headgraph_prim[headv][:]
        edges.append([s,headv,0])
        headgraph_prim[headv] = edges
    headgraph_prim[s] = []     
    
    # step 2 run bellmam_ford on headgraph_prim
    v_num_prim = v_num + 1
    negflag, P = bellman_ford(headgraph_prim, v_num_prim, s)
    
    if negflag == True:
        print 'there is a negtive cycle'
        break
    
    # step 3 update the cost by adding pu - pv
    for edge,cost in graph.iteritems():
        u = edge[0]
        v = edge[1]
        cost += P[u] - P[v]
        graph[edge] = cost
        
    # step 4 for each v run dijkstra on graph
    dijkstra(graph,tailgraph,v_num)


def dijkstra(graph,tailgraph,v_num):
    A = np.zeros((v_num+1, v_num+1))
    for s in xrange(1, v_num+1):
        X = [s]
        myheap = []
        heapq.heapify(myheap)
        adjV = set(tailgraph[s])
        for v in adjV:
            cost = graph[(s,v)]
            heapq.heappush(myheap,(cost,s,v))
        allV = set(range(1,v_num+1))
        leftV = allV - adjV - set([s])
        for v in leftV:
            cost = 999999
            heapq.heappush(myheap,(cost,s,v))
        while len(X) !=  v_num:
            minnode = heapq.heappop(myheap)
            mincost = minnode[0]
            mintailv = minnode[1]
            minheadv = minnode[2]
            A[s,headv] = A[s,tailv] + mincost
            X.append(headv)
            
            
    
        
def bellman_ford(headgraph, v_num, s):
    A = np.ones((2, v_num+1)) * 999999
    A[0, s] = 0
    for i in xrange(1, v_num+1):
        for v in xrange(1, v_num+1):
            case1 = A[0, v]
            case2 = 999999
            edges = headgraph[v]
            for edge in edges:
                w = edge[0]
                cost = edge[2]
                if A[0, w] + cost <= case2:
                    case2 = A[0, w] + cost
            A[1,v] = min(case1, case2)
            
        if i != v_num:
            A[0,:] = A[1,:]
            
    # check for negative cycle
    negflag = False
    for v in xrange(1, v_num+1):
        if A[0,v] != A[1,v]:
            negflag = True
            break
    return negflag, A[0,:]
    
      
    
    
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
    headgraph = {}.fromkeys(xrange(1,vertex_num+1),[])
    tailgraph = {}.fromkeys(xrange(1,vertex_num+1),[])
    for line in dataset[1:]:
        data = line[:-1].split(' ')
        data = map(int, data)
        tailv = data[0]
        headv = data[1]
        cost = data[2]
        graph[(tailv,headv)] = cost
        
        edges = headgraph[headv][:]
        edges.append([tailv,headv,cost])
        headgraph[headv] = edges
        
        edges = tailgraph[tailv][:]
        edges.append([headv]) # only store the head
        tailgraph[tailv] = edges
        
        
    return graph,headgraph,tailgraph,vertex_num,edge_num
    
    
    
    
    
    
    
if __name__=='__main__':
    main()