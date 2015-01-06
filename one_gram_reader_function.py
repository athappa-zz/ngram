#!/usr/bin/env python

'''
Google n-gram viewer
Source: http://joshh.ug/SRPC/assignments/assignment3.html
To get data: Run 'wget http://joshh.ug/SRPC/assignments/datafiles3.zip' in shell
'''

import csv as csv
import numpy as np
from datetime import datetime as dt
import matplotlib.pyplot as plt
from csv import reader
import operator

#Returns the counts and years for the word
#Inputs: word, year_range, wfile
#Outputs: years, counts

#Total_Counts: 0) Year, 1) Total # of words from all texts, 2) Total # of pages, 3)Total # Sources
#Very_Short: 0) Word, 1) Year, 2) # Times the word appeared, 3) # distinct sources containing that word


#Return the counts and years 
def read_entire_wfile(wfile):

	count_data = {}
	for r in reader(open('datafiles3/'+wfile), delimiter = '\t'):
		year = r[1]
		counts = r[2]

		if r[0] in count_data:
			count_data[r[0]].append((int(year), int(counts)))
		elif r[0] not in count_data:
			count_data[r[0]] = [(int(year), int(counts))]
	return count_data

#word_data = read_entire_wfile("Very_Short.csv")
#print word_data
#print("---------------------")
#print(word_data["request"])


