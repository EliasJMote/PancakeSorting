# Project 2
# Created by: Elias Mote and Justin Ramos
# Date: 9/26/18


import datetime


ids_total_visited_states = 0
ids_max_stack_size = 0


def main():
	# pancakes = [3, 1, 2, 4, 5, 6, 7, 8]
	# ShufflePancakes(pancakes, 40320)

	# Get the permutation from user input
	permutation = get_input()
	#permutation = [3, 1, 2, 4, 5, 6, 7, 8] # [8,7,2,6,9,3,1,5,4]  # [4, 3, 5, 6, 1, 8, 2, 7] # get_input()

	# Call IDS
	DoIDSWork(permutation)

	# Call BFS
	BFS(permutation)

	


# def MyBFS(permutation):
# 	start = Node()
# 	start.key = permutation
# 	start.parent = []
# 	start.depth = 0
#
# 	stack = [start]
#
# 	while(len(stack) > 0):
# 		currentNode = stack.pop()
#
# 		if(IsValid(currentNode.key)):
# 			return True
#
# 		for nextKey in GenerateSuccessors(currentNode.key):
# 			if(nextKey != currentNode.parent):
# 				newNode = Node()
# 				newNode.key = nextKey
# 				newNode.parent = currentNode.key
#
# 				stack.append(newNode)
#
# 	return False


def DoIDSWork(permutation):
	MAX_DEPTH = 10
	startNode = Node()
	startNode.key = permutation
	startNode.parent = []
	startNode.depth = 1

	res, parent = IDS(startNode, MAX_DEPTH)
	if(res):
		solutionPath = []

		# The last node added to the parent array is our solution
		solution = parent[-1]
		# Following the pointers backwards until we arrive at the
		# root node, which is the only node with a parent of [].
		while(solution != []):
			solutionPath.append(solution)
			solution = solution.parent

		# Reverse the solution path.
		solutionPath = solutionPath[::-1]

		# Print out the solution path.
		for i in range(len(solutionPath)):
			print(solutionPath[i].key)

		print("visited states", ids_total_visited_states)
		print("max stack size", ids_max_stack_size)
	else:
		print("no solution found in depth", MAX_DEPTH)

# Iterative Deepening Search
# Calls DFS with a successively greater allowable depth.
# Will return the path to a solvable solution.
def IDS(pancakes, max_depth):
	for i in range(1, max_depth + 1):
		print("starting IDS depth", i)
		parent = []
		res = DFS(pancakes, parent, i)
		if(res):
			return (True, parent)
	return (False, [])


# Depth First Search
# Takes a starting key, an array of parent keys,
# and a maximum allowable depth.
def DFS(start, parent, max_depth):
	stack = [start]
	AddOneToIDSTotalVisitedStates()

	while(len(stack) > 0):
		AddOneToIDSTotalVisitedStates()
		if(len(stack) > ids_max_stack_size):
			SetIDSMaxStackSize(len(stack))

		currentNode = stack.pop()
		parent.append(currentNode)

		if(IsValid(currentNode.key)): # Is valid means current is of the form [1 2 ... n]
			return True

		if(currentNode.depth >= max_depth): # We've reached our maximum depth
			pass # We won't add any new nodes in this case
		else:
			newNodes = []

			for nextNode in GenerateSuccessors(currentNode.key):
				if(nextNode.key != currentNode.parent):
					nextNode.parent = currentNode
					nextNode.depth = currentNode.depth + 1
					newNodes.append(nextNode)

			# Append the new nodes to the start of the stack
			# because that's how DFS works.
			stack = newNodes + stack

	return False

class Node:
	key = []
	parent = None
	depth = 0


# Generates all possible swaps that can be made for a given key.
# Swap are of the form reversing a subset of entries in the key,
# always started from the top. eg reversing a key from 1 to 4
# or 1 to n, more generally.
def GenerateSuccessors(key):
	for i in range(len(key)):
		toSwap = list(key)
		SwapPancakes(toSwap, i + 1) # +1 because we want to swap 1 to n, not 0 to n-1
		newNode = Node()
		newNode.key = toSwap
		yield newNode


# Checks if a key is in the form 1, 2, 3, ... n
def IsValid(key):
	if(len(key) > 0):
		prev = key[0]
		for i in key:
			if(prev > i):
				return False
			prev = i
	return True


# Reverses a subset of a key, always starting at 1 and going to
# n, where n is the number of keys to reverse. n = 5 would reverse
# the keys from 1 to 5.
def SwapPancakes(pancakes, num_to_swap):
	for i in range(num_to_swap // 2):
		pancakes[i], pancakes[(num_to_swap - 1) - i] = pancakes[(num_to_swap - 1) - i], pancakes[i]


def AddOneToIDSTotalVisitedStates():
	global ids_total_visited_states
	ids_total_visited_states += 1


def SetIDSMaxStackSize(size):
	global ids_max_stack_size
	ids_max_stack_size = size


# Reverse a block with a given index start and length
def rev_block(perm, start, length):

	# If we accidentally start at the length or greater,
	# return the init permutation
	if(start >= length):
		return perm

	# Get the first part of the permutation
	first = perm[0:start]

	# Reverse the middle part of the permutation
	rev = (perm[start:(start+length)])[::-1]

	# Get the last part of the permutation
	last = perm[(start+length):len(perm)]

	# Combine the permutation pieces
	return first + rev + last

# Check that a permutation is in ascending order (sorted)
def check_perm(perm):

	# Initialize the max number to a dummy value
	max_num = -999999999

	# Check each value in the permutation, using the current max value to
	# make sure each following value is larger
	for i in perm:
		if(i > max_num):
			max_num = i

		# If the permutation is unsorted, return false
		else:
			return False

	# If the permutation is sorted, return true
	return True

# Print the results
def print_output(pointers,indx,start,visited_states,max_queue,start_time):

	# Get end time
	end_time = datetime.datetime.now()

	# Temp variable used for printing successive states in reverse order
	p = []

	# While we haven't reached the parent node
	while(indx != -1):
		p.append(pointers[indx][0])
		indx = pointers[indx][1]

	# Reverse the list of successive states
	p = p[::-1]

	# Print the contents of the reversed successive states
	print("Successive states:")
	for i in p:
		print(i)

	# Print cpu time
	cpu_time = end_time-start_time
	print("CPU time: " + str(cpu_time.seconds) + " second(s) and "
		+ str(cpu_time.microseconds) + " microseconds")

	# Print how many states we have visited
	print("Total number of visited states = " + str(visited_states))

	# Print max queue size
	print("Max queue size = " + str(max_queue))

"""
Breadth-First Search algorithm
In this algorithm, reversals are applied from the length of the permutation
down to length 3. Each reversal is inserted into a queue. If the current
node's reversals are exhausted and a sorted permutation isn't found, the first
node in the queue is used to spawn more reversed child nodes in the same fasion.
This is repeated until the sorted permutation is found, at which point the
results are reported.
"""
def BFS(start):
	# Get start time
	start_time = datetime.datetime.now()

	# Initialize the pointer and queue lists, as well as number of visited
	# states and max queue size
	pointers = []
	queue = []
	visited_states = 0
	max_queue = 0

	# Push the root parent node onto the pointer stack
	pointers.append([start, -1])

	# Insert the root parent node onto the queue
	queue.append([start, len(pointers) - 1])

	# Increment the visited state count and max queue size
	visited_states += 1
	max_queue = len(queue)

	# While the queue is not empty
	while(len(queue) > 0):

		# Remove the first element from the queue and set it to the
		# current node
		currentNode = queue[0]
		del queue[0]

		# For each reversal length
		for l in range(len(currentNode[0]),1,-1):

			# For each initial position we are reversing
			for pos in range(0,l):

				# The successive node is the reversal we are performing
				succ = rev_block(currentNode[0], pos, l)

				# Push the successive node onto the pointer stack
				pointers.append([succ,currentNode[1]])

				# Insert the successive node onto the end of the queue
				queue.append([succ,len(pointers)-1])

				# Increment the visited state count
				visited_states += 1

				# Check if the max queue size has been increased and update
				if(len(queue) > max_queue):
					max_queue = len(queue)

				# Check if we have arrived at the correct permutation
				if(check_perm(succ)):
					print_output(pointers,len(pointers)-1,start,visited_states,max_queue,
						start_time)
					return

# Get the permutation input from the user
def get_input():

	# Ask the user for an input permutation P
	permutation = input("Please enter input permutation: ")

	# Split the elements up
	permutation = permutation.split(' ')

	# Convert the strings of the permutation to integers
	for i in range(0,len(permutation)):
		permutation[i] = int(permutation[i])

	# Return the permutation
	return permutation








main()
