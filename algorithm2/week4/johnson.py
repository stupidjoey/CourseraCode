# -*- coding:utf-8 -*- 
import sys
import numpy as np
import datetime
import heapq

''' use the johnson algorithm to solve the problem'''
INF = float('inf')

def main():
    starttime = datetime.datetime.now()

    currentpath = sys.path[0]
    datapath = currentpath +'\large.txt'
    graph,headgraph,tailgraph,vertex_num,edge_num = loaddata(datapath)
    johnson(graph,headgraph,tailgraph,vertex_num,edge_num)
    
    endtime = datetime.datetime.now()
    print 'Elapsed time is %f' % (endtime - starttime).seconds


    
def johnson(graph,headgraph,tailgraph,v_num,e_num):

    print 'step 1 add a new tail vertex s into the headgraph'
    s = v_num + 1
    for headv in xrange(1, v_num + 1):       
        edges = headgraph[headv][:]
        vertexset = edges[0][:]
        costset = edges[1][:]
        vertexset.append(s)
        costset.append(0)
        edges = [vertexset,costset]
        headgraph[headv] = edges
    headgraph[s] = [[],[]]     


    print 'step 2 run bellmam_ford on headgraph'
    v_num_prim = v_num + 1 # include the s
    negflag, P = bellman_ford(headgraph, v_num_prim, s)
    
    # if negflag == True:
        # print 'there is a negtive cycle'
    # else:
 
        # print 'step 3 update the cost by adding pu - pv'
        # for edge,cost in graph.iteritems():
            # u = edge[0]
            # v = edge[1]
            # cost += P[u] - P[v]
            # graph[edge] = cost
            
  
        # print 'step 4 for each v run dijkstra on graph'
        # A = dijkstra(graph,tailgraph,v_num)
        

        # print 'step 5 restore the distance'
        # for u in xrange(1, v_num+1):
            # for v in xrange(1, v_num+1):
                # A[u,v] = A[u,v] - P[u] + P[v]
        # print A[1:,1:].min()

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
            cost = INF
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
    A = np.ones((1, v_num+1)) * INF
    A[0,s] = 0
    negflag = False
    for i in xrange(1, v_num+1):
        case2mat = np.zeros((1,v_num+1))
        for v in xrange(1, v_num+1):
            case1 = A[0,v]
            edges = headgraph[v]
            vertexset = edges[0][:]
            costset = edges[1][:]
            case2 = A[0,vertexset] + np.array(costset)
            if len(case2) > 0 : 
                mincase2 = case2.min()
            else: 
                mincase2 = INF
            case2mat[0,v] = mincase2
        idx = case2mat < A
        diffsum = idx.sum() 
        if i == v_num  and diffsum > 0:
            negflag = True
            break
        elif i < v_num-1 and diffsum == 0:
            print i
            break
        A[0,idx[0,:]] = case2mat[0,idx[0,:]]  
            

    return negflag, A
    

        
def loaddata(datapath):
    f = open(datapath)
    dataset = f.readlines()
    f.close()
    basic_info = dataset[0][:-1].split(' ')
    vertex_num = int(basic_info[0])
    edge_num = int(basic_info[1])
    graph = {}
    headgraph = {}.fromkeys(xrange(1,vertex_num+1),[[],[]])
    tailgraph = {}.fromkeys(xrange(1,vertex_num+1),set())
    for line in dataset[1:]:
        data = line[:-1].split(' ')
        data = map(int, data)
        tailv = data[0]
        headv = data[1]
        cost = data[2]
        graph[(tailv,headv)] = cost
        
        edges = headgraph[headv][:]
        vertexset = edges[0][:]
        costset = edges[1][:]
        vertexset.append(tailv)
        costset.append(cost)
        edges= [vertexset,costset] 
        headgraph[headv] = edges
        
               
        edgess = tailgraph[tailv].copy()
        edgess.add(headv) # only store the head
        tailgraph[tailv] = edgess
        

    return graph,headgraph,tailgraph,vertex_num,edge_num
    
    
    
    
    
if __name__=='__main__':
    import profile
    profile.run("main()")