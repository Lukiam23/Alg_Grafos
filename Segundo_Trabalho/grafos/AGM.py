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
		def __str__(self):
			return str("{"+str(self.origem.id)+","+str(self.peso)+","+str(self.destino.id)+"}")

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
			self.minHeapfy(smallest)

	def build(self, *array):
		self.heap += list(array)
		self.size = len(self.heap)
		for k in range(math.floor(self.size/2),-1,-1):
			self.minHeapfy(k)

	def heapExtract(self):
		if self.size == 0:
			return "Underflow"
		min = self.heap[0]
		self.heap[0] = self.heap[self.size-1]
		self.size -= 1
		self.minHeapfy(0)
		return min

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
		hashTable[grafo[i-1]] = [grafo[i-1]] 
	heap = Heap()

	e = input()
	while(e != ""):
		o,d,p = e.split()
		heap.build( Aresta(grafo[int(o)-1],float(p),grafo[int(d)-1]) )
		try:
			e = input()
		except:
			break
	resultado = 0
	m = 0
	while m < n-1:
		edge = heap.pop(0)
		if edge!="Underflow" and hashTable[edge.origem] != hashTable[edge.destino]:
			print(edge)
			resultado += edge.peso
			if len(hashTable[edge.origem]) >= len(hashTable[edge.destino]):
				hashTable[edge.origem] += hashTable[edge.destino]
				hashTable[edge.destino] = hashTable[edge.origem]
			else:
				hashTable[edge.destino] += hashTable[edge.origem]
				hashTable[edge.origem] = hashTable[edge.destino]

			m += 1
	print(resultado)

if __name__ == "__main__":
	main()