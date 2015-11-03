'''
Author:	E. Reichenberger
Date:		11.3.2015

Purpose: Easy way for me to keep track of my hours.
'''

import time
import os.path
import sys

arguments = sys.argv
f_name = arguments[1]
f_nameII = arguments[2]

Time = time.strftime("%H:%M:%S")
Date = time.strftime("%m/%d/%Y")
string = Date + '\t' + Time

if os.path.isfile(f_name) == False:
	with open(f_name, 'w') as outputFile:
		outputFile.write('Date\tStart Time\tEnd Time\n')
		outputFile.write(string + '\n')

if os.path.isfile(f_name) == True:
	with open(f_nameII, 'w+') as outputFile:
		with open(f_name, 'r+') as inputFile:
			lastLine = ''
			lines = inputFile.readlines()
			for line in lines:
				lastLine = line
				if len(line.split('\t')) == 3:
					outputFile.write(line)

			if len(lastLine.split('\t')) == 3:
				outputFile.write(string + '\n') #will this write the last line twice?
				
			elif len(line.split('\t')) == 2:
				lastLine = line.replace('\n', '')
				lastLine = lastLine + '\t' + Time + '\n'
				outputFile.write(lastLine)


os.rename(f_nameII, f_name)
