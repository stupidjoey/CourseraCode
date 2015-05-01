import matplotlib.pyplot as plt
import sys


def main():
    currentpath = sys.path[0]
    datapath = currentpath +'\\tsp.txt'
    distmat,vx,vy,vnum = load_data(datapath)
    plt.scatter(vx,vy)
    plt.plot()
 


def load_data(datapath):
    f = open(datapath)
    dataset = f.readlines()
    f.close()
    vnum = int(dataset[0][:-1])
    vinfo = []
    vx = []
    vy = []
    for line in dataset[1:]:
        x,y = map(float,line[:-1].split(' '))
        vinfo.append([x,y])
        vx.append(x)
        vy.append(y)

    distmat = np.zeros((vnum,vnum))
    for i in range(0,vnum):
        x1,y1 = vinfo[i]
        for j in range(i+1,vnum):
            x2,y2 = vinfo[j]
            dist = np.sqrt( (x1-x2)**2 + (y1-y2)**2 )
            distmat[i,j] = dist
            
    distmat += distmat.T
    return distmat,vx,vy,vnum





if __name__=='__main__':
    main()
