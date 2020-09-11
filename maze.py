# solucionar um labirinto utilizando DFS ou BFS

import sys

# estrutura do nó do grafo para busca de soluções (nesse caso, sem o PathCost, pois pode-se calculá-lo no final da busca)
class Node ():

	def __init__(self, state, parent, action):
		self.state = state
		self.parent = parent
		self.action = action

class StackFrontier (): # usada para DFS

	def __init__(self):
		self.frontier = [] # lista para guardar os estados a serem analizados na fronteira

	def add (self, node):
		self.frontier.append(node) # add nó no final da lista

	def containState (self, state): # testa se a fronteira contem o estado em particular
		return any(node.state == state for node in self.frontier)

	def empty (self): # testa se a fronteira não possui nenhum estado
		return len(self.frontier) == 0

	def remove (self): # remove um estado da fronteira para analisá-lo
		if self.empty():
			raise Exception("Fronteira está vazia")
		else:
			node = self.frontier[-1] # salva o ÚLTIMO node da stack
			self.frontier = self.frontier[:-1] # remove o nó da fronteira
			return node

class QueueFrontier (StackFrontier): # usada para BFS, herda metodos de StackFrontier

	def remove (self):
		if self.empty():
			raise Exception("Fronteira está vazia")
		else:
			node = self.frontier[0] # salva o PRIMEIRO node da queue
			self.frontier = self.frontier[1:] # remove o nó da fronteira
			return node

class Maze ():

	def __init__(self, filename):
		with open(filename) as r:
			contents = r.read()

		# parse file
		contents = contents.splitlines()
		self.height = len(contents)
		self.width = max(len(line) for line in contents)

		# controla as paredes
		self.walls = []
		for i in range(self.height):
			row = []
			for j in range(self.width):
				try:
					if contents[i][j] == "A":
						self.start = (i,j)
						row.append(False)
					elif contents[i][j] == "B":
						self.goal = (i, j)
						row.append(False)
					elif contents[i][j] == " ":
						row.append(False)
					else:
						row.append(True)
				except IndexError:
					row.append(False)
			self.walls.append(row)
		self.solution = None

	def printMaze (self):
		solution = self.solution[1] if self.solution is not None else None
		print()
		for i, row in enumerate(self.walls):
			for j, col in enumerate(row):
				if col:
					print("█", end="")
				elif (i, j) == self.start:
					print("A", end="")
				elif (i, j) == self.goal:
					print("B", end="")
				elif solution is not None and (i, j) in solution:
					print("*", end="")
				else:
					print(" ", end="")
			print()
		print()

	def neighbors (self, state):
		row, col = state
		candidates = [
			("up", (row - 1, col)),
			("down", (row + 1, col)),
			("left", (row, col - 1)),
			("right", (row, col + 1))
		]

		result = []
		for action, (r, c) in candidates:
			try:
				if not self.walls[r][c]:
					result.append((action, (r, c)))
			except IndexError:
				continue
		return result

	def solveProblem (self, dfs):
		self.nrVisited = 0
		# inicializa a fronteira com a posição inicial
		start = Node(state=self.start, parent=None, action=None)
		frontier = None
		if dfs:
			frontier = StackFrontier()
			print("** Utilizando DFS **")
		else:
			frontier = QueueFrontier()
			print("** Utilizando BFS **")
		frontier.add(start)

		self.visited = set() # nenhum nó visitado
		# inicio do algoritmo
		while True:
			if frontier.empty():
				raise Exception("sem solução")

			node = frontier.remove() # escolhe um estado da fronteira
			self.nrVisited += 1
			if node.state == self.goal: # verifica se é o estado final
				actions = []
				states = []
				# verifica os nós pais para encontrar a solução
				# o caminho percorrido é do fim para o início
				while node.parent is not None:
					actions.append(node.action)
					states.append(node.state)
					node = node.parent
				actions.reverse()
				states.reverse()
				self.solution = (actions, states)
				return
			# caso não seja o estado final
			self.visited.add(node.state) # marca no como visitado
			# add os vizinhos do nó na fronteira
			for action, state in self.neighbors(node.state):
				if not frontier.containState(state) and state not in self.visited:
					child = Node(state=state, parent=node, action=action)
					frontier.add(child)


maze = Maze("maze3.txt")
maze.printMaze()
print("Tentando encontrar caminho...")
maze.solveProblem(1) # 0 para BFS e 1 para DFS
print("Estados visitados:", maze.nrVisited)
print("Solução")
maze.printMaze()
