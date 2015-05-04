import sys
import numpy as np 


def main():
    currentpath = sys.path[0]
    datapath = currentpath + '//2sat_test2.txt'
    graph,graph_rev,v_num = load_data(datapath)
    print graph_rev
    finishtime,time = first_DFS(graph_rev,v_num)
    print finishtime
    # scc = second_DFS(graph,v_num,finishtime)
    # print scc
    

def second_DFS(graph,v_num,finishtime):
    scc = {}
    visited = {}.fromkeys( range(1, 2*v_num+1), 0)
    for time in range( 2*v_num,0,-1):
        s = finishtime[time]
        scc.setdefault(s,[]).append(s)
        visited[s] = 1
        adj = graph[s][:]
        stack = []
        for vertex in adj:
            if visited[vertex] != 1:
                stack.append(vertex)    
        while len(stack) != 0:
            current_vertex = stack.pop()
            scc.setdefault(s,[]).append(current_vertex)
            visited[current_vertex] = 1
            adj_vertex = graph_rev[current_vertex][:]
            for vertex in adj_vertex:
                if visited[vertex] != 1:
                    stack.append(vertex)

    return scc     
    
def first_DFS(graph_rev,v_num):
    finishtime = {}  # key:time value: id
    time = 0
    visited = np.zeros((2*v_num+1,1))
    visit_path = []
    for i in range(v_num*2,0,-1):
        if visited[i] != 1:
            stack = [i]
            while len(stack) != 0:
                print stack
                current_vertex = stack[-1]
                if visited[current_vertex] == 1:
                    continue
                adj_vertex = graph_rev[current_vertex][:]
                temp_count = 0 
                for vertex in adj_vertex:
                    if visited[vertex] != 1:
                        stack.append(vertex)
                        temp_count += 1
                if temp_count == 0:
                    time += 1
                    finishtime[time] = current_vertex
                    stack.pop()
                    visited[current_vertex] = 1
            
    return finishtime, time            




def load_data(datapath):
    f = open(datapath)
    dataset = f.readlines()
    f.close()
    v_num = int(dataset[0][:-1])
    graph = {}.fromkeys(range(1,2*v_num+1),list())
    graph_rev = {}.fromkeys(range(1,2*v_num+1),list())
    for line in dataset[1:]:
        data = map(int, line[:-1].split(' '))
        x1 = data[0]
        x2 = data[1]
        notx1 = -x1
        notx2 = -x2
        
        x1_id = get_id(x1,v_num)
        x2_id = get_id(x2,v_num)
        
        notx1_id = get_id(notx1,v_num)
        notx2_id = get_id(notx2,v_num)       
        # edge1 : notx1 --> x2  edge2 : notx2 --> x1
        
        adj_vertex = graph[notx1_id][:]
        adj_vertex.append(x2_id)
        graph[notx1_id] = adj_vertex
        
        adj_vertex = graph[notx2_id][:]
        adj_vertex.append(x1_id)
        graph[notx2_id] = adj_vertex
        
        adj_vertex = graph_rev[x2_id][:]
        adj_vertex.append(notx1_id)
        graph_rev[x2_id] = adj_vertex
     
        adj_vertex = graph_rev[x1_id][:]
        adj_vertex.append(notx2_id)
        graph_rev[x1_id] = adj_vertex
     
     
        
    return graph,graph_rev,v_num

def get_id(x,v_num):
    if x < 0:
        xid = abs(x) + v_num  
    else:
        xid = x
    return xid



if __name__=='__main__':
    main()