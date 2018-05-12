class Graph(object):
	def __init__(self, n):
	    self.n = n
    	self.vertices = [i for i in range(n)]
    	self.adjacent_list = [None] * n
	
	for i in range(n):
        self.adjacent_list[i] = []
	
	def add_edge(self, u, v):
	    self.adjacent_list[u].append(v)
	    self.adjacent_list[v].append(u)
	
	def find_component(self, o):
    	component = []
    	knowns = [False] * self.n
    	A = set()
    	P = set()
    	knowns[o] = True
    	component.append(o)
    	A = A | {o}
    	while len(A) != 0:
            u = A.pop()
            for v in self.adjacent_list[u]:
                if not knowns[v]:
                    knowns[v] = True
                    component.append(v)
                    P = P | {v}
            
            if len(A) == 0:
                aux = P
                P = A
                A = aux
    	
	return component
	
	def find_components(self):
    	components = []
    	vertices = set(self.vertices)
	
	    while len(vertices) > 0:
            u = vertices.pop()
            this_component = self.find_component(u)
            components.append(this_component)
            vertices = vertices - set(this_component)
	
	return components def main():
    input()
    input()
    n = int(input().split("=")[1])
    input()
    
    my_graph = Graph(n)
    
    cur_edge = input()
    while cur_edge != "":
        my_graph.add_edge(*[int(e)-1 for e in cur_edge.split(" ")[:2]])
        cur_edge = input()
    
    def sort_and_join(lst):
        lst.sort()
        return " ".join(
          list(
            map(
              lambda x: str(x + 1),
              lst
            )
          )
        )
    print(
    "\n".join(
      map(
        sort_and_join,
        my_graph.find_components()
      )
    )
    )
main()
