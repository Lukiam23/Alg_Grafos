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
	return sorted(componente, key=id)

def tratar(*string):
	vetorInteiro = [] 
	aux = ""
	for i in string:
		if i != " ":
			aux += i
		else:
			vetorInteiro.append(int(aux))
			aux = ""
	vetorInteiro.append(int(aux))
	return vetorInteiro

def main():
	grafo = []
	
	n = int(input())
	for i in range(1,n+1):
		grafo.append(No(i))

	aresta = input()	
	while(aresta != ""):
		vertices = tratar(*aresta)
		grafo[vertices[0] - 1].addV(grafo[vertices[1] - 1])
		aresta = input()


	for no  in grafo:
		if not no.atingido:
			s = ""
			for i in BFS(*grafo,s=no):
				s += str(i)+" "
			print(s)
		


if __name__ == "__main__":
	main()