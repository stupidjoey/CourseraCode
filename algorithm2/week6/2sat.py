import sys
import numpy as np 


def main():
    currentpath = sys.path[0]
    datapath = currentpath + '//2sat6.txt'
    graph,graph_rev,v_num = load_data(datapath)
    finishtime,time = first_DFS(graph_rev,v_num)
    scc = second_DFS(graph,v_num,finishtime)
    # print scc
    sat_flag = True
    for key in scc.keys():
        vertexset = scc[key]
        flag = check_sat(vertexset,v_num)
        if flag == False:
            sat_flag = False
            break
    if sat_flag == False:
        print 'unsat'
    else:
        print 'sat'

def check_sat(vertexset,v_num):
    setlen = len(vertexset)
    if setlen == 1:
        return True
    else:
        for i in range(0,setlen-1):
            for j in range(i+1,setlen):
                diff = vertexset[i] - vertexset[j]
                if abs(diff) == v_num:
                    print vertexset[i],vertexset[j]
                    return False

    

def second_DFS(graph,v_num,finishtime):
    scc = {}
    visited = [0] * (v_num*2 + 1)
    for time in range( 2*v_num,0,-1):
        s = finishtime[time]     
        if visited[s] != 1:
            stack = [s]
            while len(stack) != 0:
                current_vertex = stack[-1]
                visited[current_vertex] = 1
                adj_vertex = graph[current_vertex][:]
                temp_count = 0 
                for vertex in adj_vertex:
                    if visited[vertex] != 1 and visited[vertex] != 0.5:
                        visited[vertex] = 0.5
                        stack.append(vertex)
                        temp_count += 1
                if temp_count == 0:
                    stack.pop()
                    scc.setdefault(s,[]).append(current_vertex)
        
    return scc     
    
def first_DFS(graph_rev,v_num):
    finishtime = {}  # key:time value: id
    time = 0
    visited = [0] * (v_num*2 + 1)
    visit_path = []
    for i in range(v_num*2,0,-1):
        if visited[i] != 1:
            stack = [i]
            while len(stack) != 0:
                current_vertex = stack[-1]
                visited[current_vertex] = 1
                adj_vertex = graph_rev[current_vertex][:]
                temp_count = 0 
                for vertex in adj_vertex:
                    if visited[vertex] != 1 and visited[vertex] != 0.5:
                        visited[vertex] = 0.5
                        stack.append(vertex)
                        temp_count += 1
                if temp_count == 0:
                    time += 1
                    finishtime[time] = current_vertex
                    stack.pop()
                    
            
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