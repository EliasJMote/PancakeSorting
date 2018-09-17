# Project 2
# Created by: Elias Mote and Justin Ramos
# Date: 9/15/18

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

# Check that a permutation is in ascending order
def check_perm(perm):
	max_num = -999999999
	for i in perm:
		if(i > max_num):
			max_num = i
		else:
			return False
	return True

# Breadth First Search algorithm
# In this algo, we apply reversals from the length of the permutation
# down to length 3
def BFS(perm, cost):
	# For each reversal length
	for l in range(len(perm),2,-1):

		# For each initial position we are reversing
		for pos in range(0,l):
			if(check_perm(rev_block(perm, pos, len(perm)-l+1))):
				return cost + 1

	# If we get here, the BFS did not find a solution
	return -999999

# Ask the user for an input permutation P
permutation = raw_input("Please enter input permutation: ")

# Remove the braces and split the elements up
permutation = permutation.replace("[", "").replace("]", "").split(',')

# Convert the strings of the permutation to integers
for i in range(0,len(permutation)):
	permutation[i] = int(permutation[i])

# Print the cost of the BFS
print("Cost = " + BFS(permutation, 0))