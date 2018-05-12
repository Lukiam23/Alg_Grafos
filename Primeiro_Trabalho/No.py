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
	return sorted(componente, key=id)

def main():
	
	input()
	input()
	n = int(input().split('=')[1])
	input()
	
	grafo = []
	for i in range(1,n+1):
		grafo.append(No(i))

	aresta = input()	
	while(aresta != ""):
		vertices = aresta.split()
		grafo[int(vertices[0]) - 1].addV(grafo[int(vertices[1]) - 1])
		try:
			aresta = input()
		except:
			break

	s = ""
	for no  in grafo:
		if not no.atingido:
			for i in BFS(*grafo,s=no):
				s += str(i)+" "
			s += "\n"
	print(s)
		


if __name__ == "__main__":
	main()