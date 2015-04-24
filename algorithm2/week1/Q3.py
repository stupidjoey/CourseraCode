import sys
import random
import pdb


def main():
	currentPath = sys.path[0]
	dataPath = currentPath + '/edgess.txt'
	nodeNum,edgeNum,graph = loadData(dataPath)
	nodeSet = set(range(1,nodeNum+1))
	
	
	# ......... prim's algorithm for MST ..............
	
	rndStartNode = random.randint(1,nodeNum)
	X = set([rndStartNode])
	leftNodeSet = nodeSet - X
	

	# ......... init the heap ................... 

	myheap = Heap()
	adjacentNode = graph[rndStartNode][0][:]
	adjacentCost = graph[rndStartNode][1][:]

	for pair in zip(adjacentNode,adjacentCost):
		node = pair[0]
		cost = pair[1]
		myheap.insertData(node,cost)

	for node in (leftNodeSet - set(adjacentNode) ):
		cost = 9999999
		myheap.insertData(node,cost)


	T = []
	while len(X) != nodeNum:
		data = myheap.extractMinData()
		node = data[0]
		cost = data[1]
		T.append([node,cost])
		X.add(node)
		for inNode,inIdx in myheap.nodeIdxMap.iteritems():
			curCost = myheap.arrayList[inIdx][1]
			minCost = curCost
			for outNode in X:
				adjNode = graph[outNode][0][:]
				adjCost = graph[outNode][1][:]
				if inNode in adjNode:
					theIdx = adjNode.index(inNode)
					theCost = adjCost[theIdx]
					if theCost<minCost:
						minCost = theCost
			if minCost <= curCost:
				myheap.deleteData(inIdx)
				myheap.insertData(inNode,minCost)
	# print X
	sumCost = 0
	for edge in T:
		cost = int(edge[1])
		sumCost += cost

	print sumCost

class Heap:
	""" this is the heap data structure """
	def __init__(self):
		self.arrayList = []
		self.nodeIdxMap = dict()
	
	def insertData(self,node,cost):
		self.arrayList.append([node,cost])
		idx = len(self.arrayList)-1
		self.bubbleUp(idx)
		
	def deleteData(self,idx):
		endIdx = len(self.arrayList)-1
		node = self.arrayList[idx][0]
		if idx == endIdx:
			del self.nodeIdxMap[node] 
			self.arrayList.pop(idx)
		else:
			endNode = self.arrayList[endIdx][0]
			self.swap(idx,endIdx)
			del self.nodeIdxMap[node] 
			self.arrayList.pop(endIdx)
			self.nodeIdxMap[endNode] = idx
			self.bubbleDown(idx)

	def extractMinData(self):
		minData = self.arrayList[0][:]
		node = minData[0]
		if len(self.arrayList) == 1:
			del self.nodeIdxMap[node] 
			self.arrayList.pop(0)
		else:
			endIdx = len(self.arrayList)-1
			endNode = self.arrayList[endIdx][0]
			self.swap(0,endIdx)
			del self.nodeIdxMap[node] 
			self.arrayList.pop(endIdx)
			self.nodeIdxMap[endNode] = 0
			self.bubbleDown(0)
		
		return minData
	
	def bubbleDown(self,idx):
		endIdx = len(self.arrayList)-1
		flag = True
		while flag == True:

			cost = self.arrayList[idx][1]
			node = self.arrayList[idx][0]
			leftIdx = 2 * idx +1
			rightIdx = (2 * idx) + 2
			
			if rightIdx > endIdx and leftIdx > endIdx:
				flag = False  
				self.nodeIdxMap[node] = idx
			
			elif rightIdx > endIdx and leftIdx <= endIdx:
				leftCost = self.arrayList[leftIdx][1]
				if cost > leftCost:
					self.swap(idx,leftIdx)
					idx = leftIdx
					flag = False
					self.nodeIdxMap[node] = idx
				else:
					flag = False
					self.nodeIdxMap[node] = idx
			
			elif rightIdx <= endIdx and leftIdx <= endIdx:
				leftCost = self.arrayList[leftIdx][1]
				rightCost = self.arrayList[rightIdx][1]
				if cost > leftCost or cost > rightCost:
					if leftCost <= rightCost:
						self.swap(idx,leftIdx)
						idx = leftIdx
					else:
						self.swap(idx,rightIdx)
						idx = rightIdx
				
				else:
					flag = False
					self.nodeIdxMap[node] = idx
				

	def bubbleUp(self,idx):
		flag = True
		while flag == True:
			node = self.arrayList[idx][0]
			if idx == 0:
				self.nodeIdxMap[node] = idx
				break
			cost = self.arrayList[idx][1]
			if idx % 2 == 0:
				parIdx = idx/2 - 1
			else:
				parIdx = idx/2
			parCost = self.arrayList[parIdx][1]
			if parCost > cost:
				self.swap(idx,parIdx)
				idx = parIdx
			else:
				flag = False
				self.nodeIdxMap[node] = idx
	
	def swap(self,idx1,idx2):
		data1 = self.arrayList[idx1][:]
		data2 = self.arrayList[idx2][:]

		node1 = data1[0]
		node2 = data2[0]
		self.nodeIdxMap[node1] = idx2
		self.nodeIdxMap[node2] = idx1

		self.arrayList[idx1] = data2
		self.arrayList[idx2] = data1
		
		
	
def loadData(dataPath):
	f = open(dataPath)
	dataSet = f.readlines()
	f.close()
	basicInfoStr = dataSet[0]
	basicInfo = basicInfoStr[:-1].split(' ')
	nodeNum = int(basicInfo[0])
	edgeNum = int(basicInfo[1])
	dataSet = dataSet[1:]
	
	graph = [[[],[]]] * (nodeNum+1)  # first list won't store any thing

	for dataStr in dataSet:
		data = dataStr[:-1].split(' ')
		node1 = int(data[0])
		node2 = int(data[1])
		cost = int(data[2])

		node1List = graph[node1][:]
		node1Set = node1List[0][:]
		cost1Set = node1List[1][:]
		node1Set.append(node2)
		cost1Set.append(cost)
		node1List = [node1Set,cost1Set]
		graph[node1] = node1List

		node2List = graph[node2][:]
		node2Set = node2List[0][:]
		cost2Set = node2List[1][:]
		node2Set.append(node1)
		cost2Set.append(cost)
		node2List = [node2Set,cost2Set]
		graph[node2] = node2List

	

	return nodeNum,edgeNum,graph

	



	
	
if __name__=='__main__':
	main()