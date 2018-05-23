import math
class Vertice:
	
	def __init__(self,id):
		self.id = id
		self.vizinhos = []

	def addV(self,no):
		self.vizinhos.append(no)
		no.vizinhos.append(self)
	
	def getV(self):
		return self.vizinhos
	
	def __str__(self):
		return str(self.id)

class Aresta:
		def __init__(self,origem,peso,destino):
			self.origem = origem
			self.peso = peso
			self.destino = destino

class Heap:
	def __init__(self):
		self.heap = []
		self.size = 0 

	def minHeapfy(self,i):
		l = self.left(i)
		r = self.right(i)
		
		if l < self.size and self.heap[l].peso < self.heap[i].peso:
			smallest = l
		else:
			smallest = i

		if r < self.size and self.heap[r].peso < self.heap[smallest].peso:
			smallest = r
		if smallest != i:
			aux = self.heap[i]
			self.heap[i] = self.heap[smallest] 
			self.heap[smallest]  = aux

	def build(self, *array):
		self.heap += list(array)
		self.size = len(self.heap)
		for k in range(math.floor(self.size/2),-1,-1):
			self.minHeapfy(k)

	def heapExtract(self):
		if not self.heap:
			return "Underflow"
		max = self.heap.pop(0)
		self.size -= 1
		self.minHeapfy(0)
		return max

	def parent(self,i):
		return math.floor(i/2)

	def right(self,i):
		return 2*i+1

	def left(self,i):
		return 2*i

def main():
	input()
	input()
	n = int(input().split('=')[1])
	input()
	hashTable = {}
	grafo = []
	for i in range(1,n+1):
		grafo.append(Vertice(i))
		hashTable[i] = grafo[i-1]
	heap = Heap()
	while(aresta != ""):
		origem,destino,peso = aresta.split()
		heap.build(Aresta(origem,peso,destino))

		try:
			aresta = input()
		except:
			break
	
if __name__ == "__main__":
	main()