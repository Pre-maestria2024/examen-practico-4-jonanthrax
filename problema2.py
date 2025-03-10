#@! #!/usr/bin/env
# -*- coding: utf-8 -*-
# /pract04/problema2.py

from queue import PriorityQueue
from queue import Queue

def get_max_groups(n, k, edges):
	# Caso especial: si k == 1, cada nodo forma un grupo.
	if k == 1:
		return n
	
	# Construir la lista de adyacencia (nodos 0 a n-1)
	adj = [[] for _ in range(n)]
	for u, v in edges:
		adj[u].append(v)
		adj[v].append(u)
		pass
	
	# answer[0] guardará el número de grupos formados.
	answer = [0]
	# parent: para cada nodo, su padre en el DFS.
	parent = [-1] * n

	# DFS
	def dfs(u, p, level=0):
		parent[u] = p
		# u cuenta como cadena de longitud 1 (si no está "cortado")
		dp_val = 1
		for v in adj[u]:
			if v == p:
				continue
			child_dp = dfs(v, u, level+1)
			if child_dp < 0:
				child_dp = 0  # Si el hijo retornó -1, se interpreta como 0
				pass
			dp_val = max(dp_val, child_dp + 1)
			pass
		
		if dp_val >= k:
			# Retroceder k niveles (para depuración se muestra el proceso)
			x = u
			chain = []
			for i in range(k):
				chain.append(x)
				if parent[x] == -1:
					break
				x = parent[x]
				pass
			answer[0] += 1
			return -1  # Indica que se ha "cortado" la cadena
		
		return dp_val

	dfs(0, -1)
	return answer[0]
def main():

    n, k = map(int, input().split())
    edges = []
    for i in range(n-1):
        u,v = map(int,input().split())
        edges.append((u,v),)
        pass
    max_groups = get_max_groups(n, k, edges)
    print("{}".format(max_groups))
    pass
if __name__  == '__main__':
    main()
    pass
