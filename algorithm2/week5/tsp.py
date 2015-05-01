import sys
import numpy as np
import itertools

INF = float('inf')
def main():
    currentpath = sys.path[0]
    datapath = currentpath +'\\tsp.txt'
    distmat,vnum = load_data(datapath)
    vset = range(1,vnum) # not include first vertex 0
    A = dict()
    A[((0,), 0)] = 0
    a  = (1,3,2,4)
    b =  list(a)
    b.sort()
    print b
    for m in range(2,vnum+1):
        print m
        iterset = itertools.combinations(vset,m-1)
        for jset in iterset:
            S = (0,) + jset 
            for j in jset:
                minvalue = INF
                SnotJ = list(S)
                SnotJ.remove(j)
                SnotJ.sort()
                SnotJ = tuple(SnotJ)
                for k in S:
                    if (SnotJ,k) in A.keys():
                        dist =  A[(SnotJ,k)] + distmat[k-1,j-1] 
                        if dist<= minvalue:
                            minvalue = dist
                A[(S,j)] = minvalue
    

    allS = tuple(range(0,vnum) )       
    print A[(allS,2)]            

  
                
                    
    
    
    
    
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
        for j in range(i+1,vnum):
            x2,y2 = vinfo[j]
            dist = np.sqrt( (x1-x2)**2 + (y1-y2)**2 )
            distmat[i,j] = dist
            
    distmat += distmat.T
    return distmat,vnum
    
    
    
    
if __name__=='__main__':
    main()