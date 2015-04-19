import numpy as np


def main():
    keys = [1, 2, 3, 4, 5, 6, 7]
    weightsArray = np.array([0,0.05, 0.4, 0.08, 0.04, 0.1, 0.1, 0.23])

    n = 7
    A = np.zeros((n+1, n+1))
    for k in range(1, n+1):
        A[k,k] = weightsArray[k]
    for s in range(1,n):
        for i in range(1,n):
            j = i + s
            if j > n:
                continue
            else:
                A[i, j],minR = minSplit(weightsArray,i,j,A)
            print i,j,minR
            # print i,j
            # print A[i,j]
    print A

def minSplit(weightsArray, i, j, A):

    baseWeight = sum(weightsArray[i:j+1])
    minWeight = 10000
    minR = 0
    for r in range(i,j+1):  # i+1 ~ j
        if r+1 > j:
            sumWeight = baseWeight + A[i,r-1] 
        elif r-1 < i:
            sumWeight = baseWeight + A[r+1, j]
        else:
            sumWeight = baseWeight + A[i,r-1] + A[r+1,j]
        # print sumWeight
        if sumWeight <= minWeight:
            minWeight = sumWeight
            minR = r
    return minWeight,minR



    



if __name__=='__main__':
    main()


