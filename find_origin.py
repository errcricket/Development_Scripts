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
test = [0]

with open('201_Plasmid.fa', 'r') as inputFile:
	inputFile.readline()
	lines = inputFile.readlines()
	
	for line in lines:
		line = line.replace('\n', '')
		sequence = line

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
	outputFile.write('Count\tGC_Skew\n')
	for index, t in enumerate(test):
		outputFile.write(str(index) + '\t' + str(t) + '\n')
		
neg_pos_index = []
for index, t in enumerate(test):
	if t < 0 and test[index+1] >= 0:
		neg_pos_index.append(index)

#print(neg_pos_index, len(test))
