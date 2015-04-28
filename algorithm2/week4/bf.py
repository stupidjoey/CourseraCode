# -*- coding:utf-8 -*- 
import sys
import numpy as np
import datetime

''' use the bellman_ford algorithm to solve the APSP problem'''
''' the shortest path from all vertices to all vertices '''

INF = 999999
def main():
    starttime = datetime.datetime.now()
    
    currentpath = sys.path[0]
    datapath = currentpath +'\g3.txt'
    graph,vertex_num,edge_num = loaddata(datapath)
    bellman_ford(graph,vertex_num,edge_num)
    
    endtime = datetime.datetime.now()
    print 'Elapsed time is %f' % (endtime - starttime).seconds

def bellman_ford(graph,v_num,e_num):
    A = np.ones((v_num+1, v_num+1)) * INF
    negflag = False
    for s in xrange(1, v_num+1):
        print s
        A[s, s] = 0
        for i in xrange(1, v_num+1):
            case2mat = np.zeros((1,v_num+1))
            for v in xrange(1, v_num+1):
                edges = graph[v]
                vertexset = edges[0][:]
                costset = edges[1][:]
                case2 = A[vertexset,s] + np.array(costset)
                if len(case2) > 0 : 
                    mincase2 = case2.min()
                else: 
                    mincase2 = INF
                case2mat[0,v] = mincase2        
            idx = case2mat < A[:,s]
            diffsum = idx.sum() 
            if i == v_num  and diffsum > 0:
                negflag = True
                break
            elif i < v_num-1 and diffsum == 0:
                # print i
                break
            A[idx[0,:],s] = case2mat[idx] 

    if negflag == True:
        print 'there is a negative cycle'
    else:
        minpath = INF         
        for s in xrange(1, v_num+1):
            spath = A[:, s].min()
            if spath <= minpath:
                minpath = spath
        print minpath

        
    
def loaddata(datapath):
    f = open(datapath)
    dataset = f.readlines()
    f.close()
    basic_info = dataset[0][:-1].split(' ')
    vertex_num = int(basic_info[0])
    edge_num = int(basic_info[1])
    graph = {}.fromkeys(xrange(1,vertex_num+1),[[],[]])
    for line in dataset[1:]:
        data = line[:-1].split(' ')
        data = map(int, data)
        tailv = data[0]
        headv = data[1]
        cost = data[2]
        edges = graph[headv][:]
        vertexset = edges[0][:]
        costset = edges[1][:]
        vertexset.append(tailv)
        costset.append(cost)
        edges= [vertexset,costset] 
        graph[headv] = edges

    return graph,vertex_num,edge_num
    
    
    
if __name__=='__main__':
    main()