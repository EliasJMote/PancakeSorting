# Project 2
# Created by: Elias Mote and Justin Ramos
# Date: 9/26/18


import datetime

MAX_IDS_DEPTH = 10
ids_total_visited_states = 0
ids_max_stack_size = 0


def main():
	# pancakes = [3, 1, 2, 4, 5, 6, 7, 8]
	# ShufflePancakes(pancakes, 40320)

	# Get the permutation from user input
	permutation = [4, 3, 5, 6, 1, 8, 2, 7] # get_input()

	# Call BFS
	#BFS(permutation)
	#print(MyBFS(permutation))

	# Call IDS
	DoIDSWork(permutation)


def DoIDSWork(permutation):
	# Create our starting node.
	startNode = Node()
	startNode.key = permutation
	startNode.parent = []
	startNode.depth = 1

	# Call IDS. It will return a True/False result and
	# a parent array.
	res, parent = IDS(startNode, MAX_IDS_DEPTH)

	# Operate on the results.
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
		print("no solution found in depth", MAX_IDS_DEPTH)

# Iterative Deepening Search
# Calls DFS with a successively greater allowable depth.
# Will return the path to a solvable solution.
def IDS(start_node, max_depth):
	for i in range(1, max_depth + 1):
		print("starting IDS depth", i)
		parent = []
		res = DFS(start_node, parent, i)
		if(res):
			return (True, parent)
	return (False, [])


# Depth First Search
# Takes a starting key, an array of parent keys,
# and a maximum allowable depth.
def DFS(start_node, parent, max_depth):
	stack = [start_node]
	AddOneToIDSTotalVisitedStates()

	while(len(stack) > 0):
		# Increment our counters.
		AddOneToIDSTotalVisitedStates()
		if(len(stack) > ids_max_stack_size):
			SetIDSMaxStackSize(len(stack))

		# Get a node out of the stack and add it to the parent array.
		currentNode = stack.pop()
		parent.append(currentNode)

		if(IsValid(currentNode.key)): # Is valid means current is of the form [1 2 ... n]
			return True

		if(currentNode.depth >= max_depth): # We've reached our maximum depth
			pass # We won't add any new nodes in this case
		else:
			newNodes = []

			# Generate all the possible new nodes for our current state.
			for nextNode in GenerateSuccessors(currentNode.key):
				if(nextNode.key != currentNode.parent): # Don't create cycles of length 2.
					nextNode.parent = currentNode
					nextNode.depth = currentNode.depth + 1
					newNodes.append(nextNode)

			# Append the new nodes to the start of the stack
			# because that's how DFS works.
			stack = newNodes + stack

	# Went through the entire stack and never found a solution.
	return False


# Helper class for IDS/DFS
class Node:
	key = []
	parent = None
	depth = 0


# Generated the successors of a key and yields them to the caller.
# A successor is a key where the first 0 to n entries are reversed.
# n > 2 and n < len(key)
# What we return is a new list consisting of the reversed portion
# at the front and the regular portion at the back.
def GenerateSuccessors(key):
	for i in range(2, len(key)):
		# We want to swap only from 0 to n.
		# The slice below will make a new list consisting of
		# elements 0 to i (not including element i).
		newKeyStart = key[0:i]

		# Reverses that list.
		newKeyStart = newKeyStart[::-1]

		# Grid the elements from i to the end, where the end can
		# just be defined as the length of the key.
		newKeyEnd = key[i:len(key)]

		# Create a final list with the reversed start and normal end.
		newKey = newKeyStart + newKeyEnd

		# Create a new node with our partially reversed list as the key
		# and yield it to the caller.
		newNode = Node()
		newNode.key = newKey
		yield newNode


# Checks if a key is in the form 1, 2, 3, ... n
def IsValid(key):
	max = -1

	for i in key:
		if(max > i):
			return False
		max = i
	return True


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

		# Check if we have arrived at the correct permutation
		if(check_perm(currentNode[0])):
			print_output(pointers,currentNode[1],start,visited_states,max_queue,
				start_time)
			return

		# For each reversal length
		for l in range(len(currentNode[0]),2,-1):

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
