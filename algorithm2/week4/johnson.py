# -*- coding:utf-8 -*- 
import sys
import numpy as np
import datetime
import heapq

''' use the johnson algorithm to solve the problem'''

def main():
    starttime = datetime.datetime.now()
    
    currentpath = sys.path[0]
    datapath = currentpath +'\large.txt'
    graph,headgraph,tailgraph,vertex_num,edge_num = loaddata(datapath)
    johnson(graph,headgraph,tailgraph,vertex_num,edge_num)
    
    endtime = datetime.datetime.now()
    print 'Elapsed time is %f' % (endtime - starttime).seconds


    
def johnson(graph,headgraph,tailgraph,v_num,e_num):
    #  step 1 add a new tail vertex s into the headgraph
    # turn it into headgraph_prim
    print 'step 1 add a new tail vertex s into the headgraph'
    s = v_num + 1
    headgraph_prim = headgraph.copy()
    for headv in xrange(1, v_num + 1):       
        edges = headgraph_prim[headv][:]
        edges.append([s,headv,0])
        headgraph_prim[headv] = edges
    headgraph_prim[s] = []     
    
    # step 2 run bellmam_ford on headgraph_prim
    print 'step 2 run bellmam_ford on headgraph_prim'
    v_num_prim = v_num + 1
    negflag, P = bellman_ford(headgraph_prim, v_num_prim, s)
    
    if negflag == True:
        print 'there is a negtive cycle'
    else:
        # step 3 update the cost by adding pu - pv
        print 'step 3 update the cost by adding pu - pv'
        for edge,cost in graph.iteritems():
            u = edge[0]
            v = edge[1]
            cost += P[u] - P[v]
            graph[edge] = cost
            
        # step 4 for each v run dijkstra on graph
        print 'step 4 for each v run dijkstra on graph'
        A = dijkstra(graph,tailgraph,v_num)
        
        # step 5 restore the distance
        print 'step 5 restore the distance'
        for u in xrange(1, v_num+1):
            for v in xrange(1, v_num+1):
                A[u,v] = A[u,v] - P[u] + P[v]
        print A[1:,1:].min()

def dijkstra(graph,tailgraph,v_num):
    A = np.zeros((v_num+1, v_num+1))
    for s in xrange(1, v_num+1):
        X = [s]
        myheap = []
        visitMark = {}.fromkeys(xrange(1,v_num+1),0)
        visitMark[s] = -1
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
            if visitMark[minheadv] == -1:
                continue
            A[s,minheadv] = A[s,mintailv] + mincost           
            X.append(minheadv)
            adjheadv = set(tailgraph[minheadv])
            for v in adjheadv:
                cost = graph[(minheadv,v)]
                heapq.heappush(myheap,(cost,minheadv,v))
    return A      
            
        
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
    

        
def loaddata(datapath):
    f = open(datapath)
    dataset = f.readlines()
    f.close()
    basic_info = dataset[0][:-1].split(' ')
    vertex_num = int(basic_info[0])
    edge_num = int(basic_info[1])
    graph = {}
    headgraph = {}.fromkeys(xrange(1,vertex_num+1),[])
    tailgraph = {}.fromkeys(xrange(1,vertex_num+1),set())
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
        
        edges = tailgraph[tailv].copy()
        edges.add(headv) # only store the head
        tailgraph[tailv] = edges
        
        
    return graph,headgraph,tailgraph,vertex_num,edge_num
    
    
    
    
    
if __name__=='__main__':
    main()