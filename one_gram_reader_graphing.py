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


def read_wfile(word, year_range, wfile, tfile): 
	year, vol = zip(*list(reader(open('datafiles3/'+tfile))))[0:2]
	year_range_array = range(year_range[0], year_range[1]+1)

	#initialize a dictionary
	mydata = {}
	for r in reader(open('datafiles3/'+wfile),delimiter='\t'):
		#Num times the word appears/Total number of words from all texts
		f = float(r[2]) / float(vol[year.index(r[1])])

		#If the term is already in my dictionary, append another value to the key
		#Else create a new key
		if r[0] in mydata and r[0] in word and int(r[1]) in year_range_array:
			mydata[r[0]].append((int(r[1]), f))
		elif r[0] not in mydata and r[0] in word and int(r[1]) in year_range_array:
			mydata[r[0]] = [(int(r[1]), f)]
	
	#Dictionary has word as a key and a list of tuples as the value.
	#This removes the list from the key/value pair
	mydata_list = [mydata[x] for x in word]
	print mydata_list
	print mydata

	#This takes the list of tuples and plots it
	for x in mydata_list:
		print x
		#print zip(*x)
		plt.plot(*zip(*x))
	plt.xlabel("Year")
	plt.ylabel("Relative frequency")
	plt.grid()
	plt.legend(word)
	plt.show()


#read_wfile(['horse', 'computer'], [1800, 2007], 'all_words.csv', 'total_counts.csv')
read_wfile(['wandered'], [2000, 2010], 'very_short.csv', 'total_counts.csv')




