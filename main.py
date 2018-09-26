from random import choice


def main():
	pancakes = [3, 1, 2, 4, 5, 6, 7, 8]
	ShufflePancakes(pancakes, 40320)

	# print(IDS(pancakes, 10))

	res, parent = IDS(pancakes, 100)
	for i in parent:
		print str(i) + " --> ",




def IDS(pancakes, max_depth):
	for i in range(1, max_depth + 1):
		parent = []
		res = DFS(pancakes, parent, i)
		if(res):
			return (True, parent)
	return (False, [])



# start is a node
# parent is a key
# depth is an int
def DFS(start, parent, depth):
	stack = [start]
	parent.append(start)
	while(len(stack) > 0):
		current = stack.pop()
		if(IsValid(current)): # Is valid means current is of the form [1 2 ... n]
			return True
		if(depth == 0): # We've reached our maximum depth
			return False
		for nextNode in GenerateSuccessors(current):
			if(nextNode != parent[-1]):
				res = DFS(nextNode, parent, depth - 1)
				if(res):
					return True
				del parent[-1]


	return False



def GenerateSuccessors(key):
	for i in range(len(key)):
		toSwap = list(key)
		SwapPancakes(toSwap, i + 1) # +1 because we want to swap 1 to n, not 0 to n-1
		yield toSwap



def IsValid(key):
	if(len(key) > 0):
		prev = key[0]
		for i in key:
			if(prev > i):
				return False
			prev = i
	return True






def ShufflePancakes(pancakes, num_shuffles):
	for i in CoolRange(num_shuffles):
		rand = choice(range(1, len(pancakes) + 1))
		SwapPancakes(pancakes, rand)





def SwapPancakes(pancakes, num_to_swap):
	for i in range(num_to_swap / 2):
		pancakes[i], pancakes[(num_to_swap - 1) - i] = pancakes[(num_to_swap - 1) - i], pancakes[i]







def CoolRange(n):
	i = 0
	while(i < n):
		yield i
		i += 1








# class Node():
# 	def __init__(self, key):
# 		self.key = key













main()