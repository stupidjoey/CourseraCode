import sys
import numpy as np

INF = float('inf')
def main():
    currentpath = sys.path[0]
    datapath = currentpath +'\\tsp.txt'
    distmat,vnum = load_data(datapath)
    vset = range(0,vnum)
    A = np.ones((vnum,vnum)) * INF
    A[0,0] = 0
    for m in range(2, vnum):
        S = vset[0:m]
        for j in S[1:]:
            copyS = S.copy()
            copyS[j] = []
            A[copyS,:]
                
                    
    
    
    
    
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