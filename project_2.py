# Project 2
# Created by: Elias Mote and Justin Ramos
# Date: 9/15/18

import datetime

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
	permutation = raw_input("Please enter input permutation: ")

	# Remove the braces and split the elements up
	#permutation = permutation.replace("[", "").replace("]", "").split(',')
	permutation = permutation.split(' ')

	# Convert the strings of the permutation to integers
	for i in range(0,len(permutation)):
		permutation[i] = int(permutation[i])

	# Perform BFS
	BFS(permutation)