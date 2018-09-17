# Project 2
# Created by: Elias Mote and Justin Ramos
# Date: 9/15/18

def rev_block(perm, start, length):
	if(start >= length):
		return perm
	first = perm[0:start]
	rev = (perm[start:(start+length)])[::-1]
	last = perm[(start+length):len(perm)]
	return first + rev + last

def check_perm(perm):
	max_num = -999999999
	for i in perm:
		if(i > max_num):
			max_num = i
		else:
			return False
	return True

# Breadth First Search algorithm
# In this algo, we apply reversals of length 3 to permutation length
def BFS(perm, cost):
	# For each reversal length
	for j in range(1,len(perm)-1):

		# For each initial position we are reversing
		for pos in range(0,j):
			if(check_perm(rev_block(perm, pos, len(perm)-j+1))):
				return cost + 1

	return -999999

# Ask the user for an input permutation P
permutation = raw_input("Please enter input permutation: ")

# Remove the braces and split the elements up
permutation = permutation.replace("[", "").replace("]", "").split(',')

# Convert the strings of the permutation to integers
for i in range(0,len(permutation)):
	permutation[i] = int(permutation[i])


print(BFS(permutation, 0))

# [1,2,3,4,5,6,7,8]