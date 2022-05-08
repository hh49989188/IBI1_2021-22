import random

Gene = {"TTT": "Phe", "TCT": "Ser", "TAT": "Tyr", "TGT": "Cys", "TTC": "Phe", "TCC": "Ser",
		"TAC": "Tyr", "TGC": "Cys", "TTA": "Leu", "TCA": "Ser", "TAA": "stop", "TGA": "stop",
		"TTG": "Leu", "TCG": "Ser", "TAG": "stop", "TGG": "Trp", "CTT": "Leu", "CCT": "Pro", "CAT": "His",
		"CGT": "Arg", "CTC": "Leu", "CCC": "Pro", "CAC": "His", "CGC": "Arg", "CTA": "Leu", "CCA": "Pro",
		"CAA": "GIn", "CGA": "Arg", "CTG": "Leu", "CCG": "Pro", "CAG": "Gln", "CGG": "Arg", "ATT": "Lle",
		"ACT": "Thr", "AAT": "Asn", "AGT": "Ser", "ATC": "lle", "ACC": "Thr", "AAC": "Asn", "AGC": "Ser",
		"ATA": "lle", "ACA": "Thr", "AAA": "Lys", "AGA": "Arg", "ATG": "Met", "ACG": "Thr", "AAG": "Lys",
		"AGG": "Arg", "GTT": "Val", "GCT": "Ala", "GAT": "Asp", "GGT": "Gly", "GTC": "Val", "GCC": "Ala",
		"GAC": "Asp", "GGC": "Gly", "GTA": "Val", "GCA": "Ala", "GAA": "Glu", "GGA": "Gly", "GTG": "Val", "GCG": "Ala",
		"GAG": "Glu", "GGG": "Gly"}  # set the dictionary of coden and corresponding amino acid sequence.
base = ["A", "C", "G", "T"]
switch = 1
Gene_to_test1 = []
while switch <= 21:
	result = random.choice(base)
	switch += 1
	Gene_to_test1.append(result)
# Produce a gene
sequences = ''.join(map(str, Gene_to_test1))
print(f"The origin sequence is AUG{sequences}TAA")
n = random.randint(0, 2)
# Give the number of random generation of mutations in range (0,2)
print(n)
i = 1
# Generate a mutation site at random
while i <= n:
	result2 = random.choice(base)
	i += 1
	i1 = random.randint(0, 20)
	Gene_to_test1[i1] = f'{result2}'
sequences2 = ''.join(map(str, Gene_to_test1))
print(f"The mutated sequence is AUG{sequences2}TAA")
# Generate the mutation gene


# FUCTION1；Design a function to compare the origin and new gene
def compare(list1, list2):
	error = []
	error_index = []
	if len(list1) == len(list2):
		for i in range(0, len(list1)):
			if list1[i] == list2[i]:
				continue
			error.append(list1[i])
			error.append(list2[i])
			error_index.append(i)
			print(f"the {error[0]} mutated to {error[1]}")
			# Point which base was mutated.
			position = ''.join(map(str, error_index))
			position = int(position)
			position = position + 3
			position = str(position)
			if len(position) < 3:
				print(f"the mutation position is {i + 4}")
			else:
				print(f"the mutation position is {i + 4}")


# Point out the mutation position

# Design a function to detect the mutated amino acid
compare(sequences, sequences2)
Amino_acid = []
Amino_acid2 = []
# Design a function for translate the coden to amino acid sequence
def aa_detector(s, Amino_acid):
	i2 = 0
	while i2 < len(s):
		first_base = s[i2:i2 + 3]
		aa = str(first_base)
		i2 += 3
		Amino_acid.append(Gene[aa])
aa_detector(sequences, Amino_acid)
print(Amino_acid)
aa_detector(sequences2, Amino_acid2)
print(Amino_acid2)
# Export the origin and mutated amino acid sequence.
def compare_aa(list1, list2):
	error = []
	error_index = []
	if len(list1) == len(list2):
		for i in range(0, len(list1)):
			if not list1[i] == list2[i]:
				error.append(list1[i])
				error.append(list2[i])
				error_index.append(i)
				print(f"the amino acid changed from {error[0]} to {error[1]}")
compare_aa(Amino_acid, Amino_acid2)

# FUNCTION 2: calculates how many of these mutations are synonymous and how many are nonsynonymous
syn = []
nonsyn = []
result3 = random.choice(base)
i2 = random.randint(0, 20)
Gene_to_test1[i2] = f'{result3}'
sequences3 = ''.join(map(str, Gene_to_test1))
i3 = 0
n = 0
while i3 < 7:
	slide1 = sequences2[n:n + 3]
	slide2 = sequences3[n:n + 3]
	if slide1 == slide2:
		syn.append(slide1)
	else:
		if Gene[f'{slide1}'] == Gene[f'{slide2}']:
			syn.append(f'{slide1}')
		else:
			nonsyn.append(f'{slide1},{slide2}')
	i3 = i3 + 1
	n = n + 3
print("The synonymous mutations are:", syn)
print("The nonsynonymous mutations are:", nonsyn)


# FUNCTION 3:Computes the fraction of all mutations that result in the introduction of a stop codon before the end of the sequence.
stop_codon = ['TAA', 'TAG', 'TGA']
def codon_calculator(seq):
	codon = []
	import re
	codon.append(re.findall('TA(C|T)', seq))
	codon.append(re.findall('T(C|T)A', seq))
	codon.append(re.findall('[ACG]AA', seq))
	codon.append(re.findall('[ACG]AG', seq))
	codon.append(re.findall('T[CGT]G', seq))
	codon.append(re.findall('[ACG]GA', seq))
	codon.append(re.findall('TG[CGT]', seq))
# Extract all the prematurely stopped DNA sequence.
	result4 = len(codon) / (4 ** 21)
	print(f'The introduction of a stop codon before the end of the sequence is {result4}')
codon_calculator(sequences2)


# FUNCTION 4:Transitions vs Transversions
codon_num = len(nonsyn) / 4 ** 21
def possible_compare(seq):
	n = 0
	i = 0
	counter = 0
	while n < 21:
		slide = seq[n:n + 3]
		if i == 3:
			i = 0
		if slide[i] == "A":
			slide_new = slide.replace('A', 'G', 1)
			if Gene[slide_new] == Gene[slide]:
				pass
			else:
				counter = counter + 1
		if slide[i] == "C":
			slide_new = slide.replace('C', 'T', 1)
			if Gene[slide_new] == Gene[slide]:
				pass
		if slide[i] == 'G':
			slide_new = slide.replace('G', 'A', 1)
			if Gene[slide_new] == Gene[slide]:
				pass
			else:
				counter = counter + 1
		if slide[i] == 'T':
			slide_new = slide.replace('T', 'C', 1)
			if Gene[slide_new] == Gene[slide]:
				pass
			else:
				counter = counter + 1
		i = i + 1
		if i % 3 == 0:
			n = n + 3
	print(f'the point of this seq is {counter/4**21}')
#  computes the number of amino acid changes that would results from all possible single transition mutations.
	if counter/4**21 > codon_num:
		print('The possibility of transversion mutations is smaller than amino acid changes that would results from all possible single transition mutations, and latter mutation type is more damaging to the encoded protein')
	else:
		print('The possibility of transversion mutations is bigger than amino acid changes that would results from all possible single transition mutations, and former mutation type is more damaging to the encoded protein')
# Compare transitions to the number of possible changes driven by transversion mutations, and which type of mutation are more damaging to the encoded protein
possible_compare(sequences2)

# Additional function: Double sequence global alignment of amino acids by BLOSUM62
global S
global E
global MIN
global amino # Introduction to amino acid arrays
global blosum # Introduction to BLOSUM62
S = -11   #gap opening penalty  The M state transitions to a non-M state
E = -1    #gap extending penalty    X or Y converts to its own penalty score
MIN = -float("inf") # Edge value initialization
amino = ['A', 'R', 'N', 'D', 'C', 'Q', 'E', 'G', 'H', 'I', 'L', 'K', 'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'V', 'B', 'Z', 'X', '*']
blosum = [
[ 4, -1, -2, -2,  0, -1, -1,  0, -2, -1, -1, -1, -1, -2, -1,  1,  0, -3, -2,  0, -2, -1,  0, -4],
[-1,  5,  0, -2, -3,  1,  0, -2,  0, -3, -2,  2, -1, -3, -2, -1, -1, -3, -2, -3, -1,  0, -1, -4],
[-2,  0,  6,  1, -3,  0,  0,  0,  1, -3, -3,  0, -2, -3, -2,  1,  0, -4, -2, -3,  3,  0, -1, -4],
[-2, -2,  1,  6, -3,  0,  2, -1, -1, -3, -4, -1, -3, -3, -1,  0, -1, -4, -3, -3,  4,  1, -1, -4],
[ 0, -3, -3, -3,  9, -3, -4, -3, -3, -1, -1, -3, -1, -2, -3, -1, -1, -2, -2, -1, -3, -3, -2, -4],
[-1,  1,  0,  0, -3,  5,  2, -2,  0, -3, -2,  1,  0, -3, -1,  0, -1, -2, -1, -2,  0,  3, -1, -4],
[-1,  0,  0,  2, -4,  2,  5, -2,  0, -3, -3,  1, -2, -3, -1,  0, -1, -3, -2, -2,  1,  4, -1, -4],
[ 0, -2,  0, -1, -3, -2, -2,  6, -2, -4, -4, -2, -3, -3, -2,  0, -2, -2, -3, -3, -1, -2, -1, -4],
[-2,  0,  1, -1, -3,  0,  0, -2,  8, -3, -3, -1, -2, -1, -2, -1, -2, -2,  2, -3,  0,  0, -1, -4],
[-1, -3, -3, -3, -1, -3, -3, -4, -3,  4,  2, -3,  1,  0, -3, -2, -1, -3, -1,  3, -3, -3, -1, -4],
[-1, -2, -3, -4, -1, -2, -3, -4, -3,  2,  4, -2,  2,  0, -3, -2, -1, -2, -1,  1, -4, -3, -1, -4],
[-1,  2,  0, -1, -3,  1,  1, -2, -1, -3, -2,  5, -1, -3, -1,  0, -1, -3, -2, -2,  0,  1, -1, -4],
[-1, -1, -2, -3, -1,  0, -2, -3, -2,  1,  2, -1,  5,  0, -2, -1, -1, -1, -1,  1, -3, -1, -1, -4],
[-2, -3, -3, -3, -2, -3, -3, -3, -1,  0,  0, -3,  0,  6, -4, -2, -2,  1,  3, -1, -3, -3, -1, -4],
[-1, -2, -2, -1, -3, -1, -1, -2, -2, -3, -3, -1, -2, -4,  7, -1, -1, -4, -3, -2, -2, -1, -2, -4],
[ 1, -1,  1,  0, -1,  0,  0,  0, -1, -2, -2,  0, -1, -2, -1,  4,  1, -3, -2, -2,  0,  0,  0, -4],
[ 0, -1,  0, -1, -1, -1, -1, -2, -2, -1, -1, -1, -1, -2, -1,  1,  5, -2, -2,  0, -1, -1,  0, -4],
[-3, -3, -4, -4, -2, -2, -3, -2, -2, -3, -2, -3, -1,  1, -4, -3, -2, 11,  2, -3, -4, -3, -2, -4],
[-2, -2, -2, -3, -2, -1, -2, -3,  2, -1, -1, -2, -1,  3, -3, -2, -2,  2,  7, -1, -3, -2, -1, -4],
[ 0, -3, -3, -3, -1, -2, -2, -3, -3,  3,  1, -2,  1, -1, -2, -2,  0, -3, -1,  4, -3, -2, -1, -4],
[-2, -1,  3,  4, -3,  0,  1, -1,  0, -3, -4,  0, -3, -3, -2,  0, -1, -4, -3, -3,  4,  1, -1, -4],
[-1,  0,  0,  1, -3,  3,  4, -2,  0, -3, -3,  1, -1, -3, -1,  0, -1, -3, -2, -2,  1,  4, -1, -4],
[ 0, -1, -1, -1, -2, -1, -1, -1, -1, -1, -1, -1, -1, -1, -2,  0,  0, -2, -1, -1, -1, -1, -1, -4],
[-4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4,  1],
]

# This function is used to score match or mismatch of different amino acids in the double sequence S and T (return match or mismatch score)
def _match(s, t, i, j): 
    index1 = amino.index(t[i-1])
    # Reads the order value of the t[i-1] string in the t string for the amino acid
    index2 = amino.index(s[j-1])
    # Reads the order value of the s[j-1] string in the s string for the amino acid
    return blosum[index1][index2]

# Initialization in X-state cases，gap extending = d+e*(n-1) 
def _init_x(i, j):
    if i > 0 and j == 0:
        return MIN
    else:
        if j > 0:
            return S + E * j
        else:
            return 0
# Initialization in the case of Y state，gap extending = d+e*(n-1)  
def _init_y(i, j):
    if j > 0 and i == 0:
        return MIN
    else:
        if i > 0:
            return S + E * i
        else:
            return 0
# # Initialization in the case of M state
def _init_m(i, j):
    if j == 0 and i == 0:
        return 0
    else:
        if j == 0 or i == 0:
            return MIN
        else:
            return 0
# Generate a distance matrix
def distance_matrix(s, t):
    dim_i = len(t) + 1
    dim_j = len(s) + 1
# Utilize  comprehensions of list to create matrices
# Because there is no transition between the same states (X cannot turn to Y), X has two cases. The X stands for vertical case
# The first is X to X, i.e. X[i][j] = X[i][j-1] + e
# The second is M-state steering, where X[x][j-1] = M[i][j-1] + S+E
# Create a three-dimensional space by creating X, Y, M matrices
    X = [[_init_x(i, j) for j in range(0, dim_j)] for i in range(0, dim_i)]
# print(X)
    Y = [[_init_y(i, j) for j in range(0, dim_j)] for i in range(0, dim_i)]
# print(Y)
    M = [[_init_m(i, j) for j in range(0, dim_j)] for i in range(0, dim_i)]
# print(M)
    for j in range(1, dim_j):
        for i in range(1, dim_i):
            
            X[i][j] = max((S + E + M[i][j-1]), (E + X[i][j-1]))
# in fact, X and Y are the same state. Except that Y[i][j] is the case of another plane. Y stands for horizontal condition
            Y[i][j] = max((S + E + M[i-1][j]), (E + Y[i - 1][j]))
# There are three cases for the M state
# One is the conversion of itself, that is, the M state to the M state, which is the conversion of the diagonal line at this time. Plus mismatch or match points above
# The second and third are transitions to X and Y states. This conversion can only occur when X and Y are edges, that is, M itself
            M[i][j] = max(_match(s, t, i, j) + M[i - 1][j - 1], X[i][j],
                          Y[i][j])
    return [X, Y, M]

# Backtracking, to get a string that matches a double sequence
def backtrace(s, t, X, Y, M):
    sequ1 = ''
    sequ2 = ''
    i = len(t)
    j = len(s)
    while (i>0 or j>0):
# When i, j is not 0, it means not on the boundary. And the M state is a direct transition to the M state. Describes the diagonal conversion.
        if (i>0 and j>0 and M[i][j] == M[i-1][j-1] + _match(s, t, i, j)):
            sequ1 += s[j-1]
            sequ2 += t[i-1]
            i -= 1
            j -= 1
# When j = 0 and i is not 0, only horizontal transfer can be performed, indicating that it is empty in the vertical state
        elif (i>0 and M[i][j] == Y[i][j]):
# When i > 0 and j = 0, we subtract only i. The scoring matrix is consistent with the value of the Y matrix, indicating the presence of a vacancy
            sequ1 += '_'
            sequ2 += t[i-1]
            i -= 1
# When i = 0 and j is not 0, the instruction can only be transferred vertically, indicating that it is empty in the horizontal state.
        elif (j>0 and M[i][j] == X[i][j]):
# When j>0 and i = 0, we only subtract from j, and the score matrix matches the value of the X matrix, indicating that there is a vacancy
            sequ1 += s[j - 1]
            sequ2 += '_'
            j -= 1
# After going backtrack, reverse order output
    sequ1r = ' '.join([sequ1[j] for j in range(-1, -(len(sequ1)+1), -1)])
    sequ2r = ' '.join([sequ2[j] for j in range(-1, -(len(sequ2)+1), -1)])
    return [sequ1r, sequ2r]

seq1 = input("Please input long sequence:")
seq2 = input("Please input short sequence:")
# The input string needs to be converted to 3 states
[X, Y, M] = distance_matrix(seq1, seq2)
# print(X)
# print(M)
[str1, str2] = backtrace(seq1, seq2, X, Y, M)

score = M[len(seq2)][len(seq1)]
print("Alignment Score:"+ str(score))
print(str1)
print(str2)
