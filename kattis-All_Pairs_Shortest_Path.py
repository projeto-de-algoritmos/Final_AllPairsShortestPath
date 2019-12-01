# Python program for Bellman-Ford's single source 
# shortest path algorithm. 

from collections import defaultdict 

# Class to represent a graph 
class Graph: 

	def __init__(self, vertices): 
		self.V = vertices # No. of vertices 
		self.graph = [] # default dictionary to store graph 

	# function to add an edge to graph 
	def addEdge(self, u, v, w): 
		self.graph.append([u, v, w]) 
	
	# The main function that finds shortest distances from src to 
	# all other vertices using Bellman-Ford algorithm. The function 
	# also detects negative weight cycle 
	def BellmanFord(self, src, pont): 

		# Step 1: Initialize distances from src to all other vertices 
		# as INFINITE 
		dist = [float("Inf")] * self.V 
		dist[src] = 0


		# Step 2: Relax all edges |V| - 1 times. A simple shortest 
		# path from src to any other vertex can have at-most |V| - 1 
		# edges 
		for i in range(self.V - 1): 
			# Update dist value and parent index of the adjacent vertices of 
			# the picked vertex. Consider only those vertices which are still in 
			# queue 
			for u, v, w in self.graph: 
				if dist[u] != float("Inf") and dist[u] + w < dist[v]: 
					dist[v] = dist[u] + w 
		# Step 3: check for negative-weight cycles. The above step 
		# guarantees shortest distances if graph doesn't contain 
		# negative weight cycle. If we get a shorter path, then there 
		# is a cycle.
		for u, v, w in self.graph: 
			if dist[u] != float("Inf") and dist[u] + w < dist[v]: 
					print("Impossible")
  
		if dist[pont] == float("Inf") :
				print("Impossible")
		else:
				print(dist[pont])

n = 1
m = 1
q = 1

while(n != 0 and m != 0 and q != 0):
	n = int(input())
	m = int(input())
	q = int(input())
	g = Graph(n) 
	i = 0
	if(n == 0 and m == 0 and q == 0):
		break
	else:
		while(i<m):
			u = int(input())
			v = int(input())
			w = int(input())
			g.addEdge(u,v,w)
			i+=1
		j=0
		while(j<q):
			a = int(input())
			b = int(input())
			g.BellmanFord(a,b)
			j+=1
		print("\n")

# This code is contributed by Neelam Yadav 
