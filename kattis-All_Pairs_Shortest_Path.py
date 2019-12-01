from collections import defaultdict 

# classe que representa o grafo
class Graph: 

	def __init__(self, vertices):
		# numero de vertices 
		self.V = vertices
		# grafo vazio
		self.graph = []

	# adicionar uma aresta ao grafo
	def addEdge(self, u, v, w): 
		self.graph.append([u, v, w]) 

	def BellmanFord(self, src, pont): 

		# inicialize distancias de src para todos os outros vertices como INFINITO
		dist = [float("Infinity")] * self.V 
		dist[src] = 0

		# as vertice pode so pode ter no maximo V - 1 arestas
		for i in range(self.V - 1):
			# Atualiza a distancia das vertices adjacentes do vertice selecionado, 
			# garantindo a distacia mais curta
			for u, v, w in self.graph: 
				if dist[u] != float("Infinity") and dist[u] + w < dist[v]: 
					dist[v] = dist[u] + w 

		# verifica os ciclos de peso negativo
		for u, v, w in self.graph: 
			if dist[u] != float("Infinity") and dist[u] + w < dist[v]: 
					print("Impossible")
  
		if dist[pont] == float("Infinity") :
				print("Impossible")
		else:
				print(dist[pont])

n = 1
m = 1
q = 1

while(n != 0 and m != 0 and q != 0):
	n, m, q = map(int, input().split())
	g = Graph(n) 
	i = 0
	if(n == m == q == 0):
		break
	else:
		while(i < m):
			u, v, w = map(int, input().split())
			g.addEdge(u, v, w)
			i+=1
		j=0
		while(j<q):
			a, b = map(int, input().split())
			g.BellmanFord(a, b)
			j+=1
		print("\n")
