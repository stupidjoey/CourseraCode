import sys
import numpy as np
import random

''' using ant algorithm to solve the tsp problem'''

INF = float('inf')

def main():
    currentpath = sys.path[0]
    datapath = currentpath +'//tsp.txt'
    distmat,etamat,vnum = load_data(datapath)
    C = 1.0
    taomat = np.ones((vnum,vnum)) * C
    NCmax = 3000
    antnum = vnum
    rou = 0.9
    alpha = 1
    beta = 2
    Q = 1000
    answer = INF
    for k in range(NCmax):    
        visit_path = ant(etamat,taomat,alpha,beta,antnum,vnum)
        taomat,min_path_length = update(visit_path,taomat,distmat,Q,rou,antnum,vnum)
        print min_path_length
        if min_path_length <= answer:
            answer = min_path_length
    print 'answer is %f' % answer


def update(visit_path,taomat,distmat,Q,rou,antnum,vnum):
    min_path_length  = INF
    for i in range(vnum):
        for j in range(vnum):
            taomat[i,j] = taomat[i,j] * rou

    for ant_id in range(antnum):
        thepathset = visit_path[ant_id]
        circle_length = 0
        first_node = thepathset[0][0]
        last_node = thepathset[-1][1]
        back_length = distmat[first_node,last_node]
        for path in thepathset:
            i = path[0]
            j = path[1]
            circle_length += distmat[i,j]

        circle_length += back_length
        for path in thepathset:
            i = path[0]
            j = path[1]
            taomat[i,j] += Q/circle_length
            taomat[j,i] += Q/circle_length

        if circle_length <= min_path_length:
            min_path_length = circle_length

    # taomat += taomat.T
    return taomat,min_path_length



def ant(etamat,taomat,alpha,beta,antnum,vnum):
    visit_path = {}.fromkeys(range(0,antnum),[])
    for ant_id in range(antnum):
        tabu = [random.randint(0,vnum-1)]  
        while len(tabu)!= vnum:
            current_node = tabu[-1]
            left_nodes = list(set(range(vnum)) - set(tabu))
            probmat = np.zeros((1,len(left_nodes)))
            for idx,lnode in enumerate(left_nodes):
                probmat[0,idx] = (taomat[current_node,lnode]**alpha) * (etamat[current_node,lnode]**beta)
            totalprob = np.sum(probmat) 
            probmat = probmat/totalprob
            # roulette wheel selection 
            randprob = random.uniform(0,1)
            for idx,lnode in enumerate(left_nodes):
                randprob -= probmat[0,idx]
                if randprob < 0:
                    next_node = lnode
                    break
            tabu.append(next_node)
            thepathset = visit_path[ant_id][:]
            thepathset.append([current_node,next_node])
            visit_path[ant_id] = thepathset

    return visit_path



def load_data(datapath):
    f = open(datapath)
    dataset = f.readlines()
    f.close()
    vnum = int(dataset[0][:-1])
    vinfo = []
    for line in dataset[1:]:
        x,y = map(float,line[:-1].split(' '))
        vinfo.append([x,y])

    distmat = np.zeros((vnum,vnum))
    for i in range(0,vnum):
        x1,y1 = vinfo[i]
        distmat[i,i] = 1
        for j in range(i+1,vnum):
            x2,y2 = vinfo[j]
            dist = np.sqrt( (x1-x2)**2 + (y1-y2)**2 )
            distmat[i,j] = dist
           
    distmat += distmat.T
    etamat = 1.0/distmat
    return distmat,etamat,vnum







if __name__=='__main__':
    main()