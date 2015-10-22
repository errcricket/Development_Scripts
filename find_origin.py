'''
Author: 	E. Reichenberger
Date:		10.21.2015

Purpose: Quick script to find origin of replication bases on G&C nucleotides.
'''

import os
import sys
import Bio
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

sequence = ''

with open('201_Plasmid.fa', 'r') as inputFile:
	inputFile.readline()
	lines = inputFile.readlines()
	
	for line in lines:
		line = line.replace('\n', '')
		sequence = line

#sequence = 'AGTCCAGTGGC'
#sequence = 'CCCAAT'
#sequence = Seq('AGTCCAGT')

C = [0]#*len(sequence)
G = [0]#*len(sequence)
test = [0]

score = 0
for s in sequence:
	if s == 'C':
		score = score - 1
	elif s == 'G':
		score = score + 1
	else:
		score = score + 0

	test.append(score)
	
with open('GC_skew', 'w') as outputFile:
	#outputFile.write('Count\tGC_Skew\tNew_Skew\n')
	outputFile.write('Count\tGC_Skew\n')
	for index, t in enumerate(test):
		outputFile.write(str(index) + '\t' + str(t) + '\n')
		
#print(test)

neg_pos_index = []
for index, t in enumerate(test):
	if t < 0 and test[index+1] >= 0:
		neg_pos_index.append(index)

#print(neg_pos_index, len(test))
	
'''

			
S_count = 0
def GC_count(read, n_list, nucleotide):
	for index, r in enumerate(read):
		if index == 0:
			if r == nucleotide:
				n_list[0] = 1 #C[index] = 1
				S_count = 1
			else:
				n_list[0] = 0 #C[index] = 0
				S_count = 0

		else:
			if r == 'C':
				S_count = S_count - 1
			if r == 'G':
				S_count = S_count + 1
			if r == nucleotide:
				n_list.append(n_list[index-1]+1)

			if r != nucleotide:
				n_list.append(n_list[index-1])
				S_count = S_count 

			#test.append(S_count)
			
GC_count(sequence, C, 'C')


sequence = Seq(sequence)
sequence = sequence.reverse_complement()
sequence = str(sequence)
GC_count(sequence, G, 'G')

GC_skew = [G - C for G, C in zip(G, C)]
#if G is C:
#	print('match')

#print(G[-1], C[-1], GC_skew[-1])
#print(G[1:20])
#print(C[1:20]) 
#print(GC_skew[1:20])

count = 1
with open('GC_skew', 'w') as outputFile:
	outputFile.write('Count\tGC_Skew\tNew_Skew\n')
	for index, gc in enumerate(GC_skew):
		outputFile.write(str(count) + '\t' + str(gc) + '\t' + str(test[index]) + '\n')
		count+=1

origins = []
#for index, g in enumerate(GC_skew):
for index, g in enumerate(test):
	#if index !=0 and index < len(GC_skew)-1:
	if index !=0 and index < len(test)-1:
		#if g < 0 and GC_skew[index+1] > 0:
		#if g == 0 and GC_skew[index+1] > 0:
		if g == 0 and GC_skew[index+1] > 0:
			origins.append(index)
	
print(origins)
print(len(origins), len(sequence), min(GC_skew))
print(GC_skew.index(-735))
	
#print(G[1:20], C[1:20], GC_skew[1:20])
print(test)
'''
