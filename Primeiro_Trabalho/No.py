#_*_ coding: utf8 _*_
class No:
	
	def __init__(self,id):
		self.id = id
		self.vizinhos = []
		self.atingido = False
	
	def addV(self,no):
		self.vizinhos.append(no)
		no.vizinhos.append(self)
	
	def getV(self):
		return self.vizinhos
	
	def isIn(self,no):
		return (no in self.vizinhos)
	
	def atingir(self):
		self.atingido = True
	
	def __str__(self):
		return str(self.id)


def BFS(*grafo,s):
	componente = []
	fila = []
	fila.append(s)
	while len(fila)>0:
		u = fila.pop(0)
		componente.append(u)
		for v in u.getV():
			if not v.atingido:
				v.atingir()
				fila.append(v)
		u.atingir()
	return componente

def main():
	vetorNos = []
	for i in range(0,10):
		vetorNos.append(No(i))
	no1 = No(1)
	no1.addV(vetorNos[3])
	no1.addV(vetorNos[4])
	no1.addV(vetorNos[5])
	no1.addV(vetorNos[6])
		

	for i in BFS(*vetorNos,s=no1):
		print(i, end = '')


if __name__ == "__main__":
	main()