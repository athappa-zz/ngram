#!/usr/bin/env python

import one_gram_reader_function

word_data = one_gram_reader_function.read_entire_wfile("very_short.csv")
print word_data
#print total_count_list

'''
word = ["wandered"]
for element in word:
	if element not in total_count_list:
		return 0
	else:
'''

'''
def total_occurrences(word_data, word):
	
	for element in word:
		if element not in word_data:
			return 0

	else:
		total_count_list = [word_data[x] for x in word]
		#print total_count_list

		for element_list in total_count_list:
			sum_occurrences = sum([pair[1] for pair in element_list])
			return sum_occurrences
					

print total_occurrences(word_data, ["wandered", 'airport'])
'''




def count_letters(word_data):
	#Input: word_data

	total_count_list = [word_data[x] for x in word_data]
	#print total_count_list

	sum_occurrences_list = []
	sum_occurrences_dict = {}

	#for item in word_data.values():
	#sum_occurrences_dict[item] = 
	#print tuple_list

	for key in word_data:
		for tuples in word_data[key]:
			if key not in sum_occurrences_dict:
				sum_occurrences_dict[key] = tuples[1]
			else:
				sum_occurrences_dict[key] = sum_occurrences_dict[key] + tuples[1]
	print sum_occurrences_dict

	'''
	#Not necessary
	#find the total number of times each word appeared in a given year
	for element_list in total_count_list:
		sum_occurrences = sum([pair[1] for pair in element_list])
		sum_occurrences_list.append(sum_occurrences)
		#print sum_occurrences_list
	'''	

	#create dictionary to hold the letter counts
	letter_count = {}
	a_to_z = list(map(chr,range(ord('a'),ord('z')+1)))

	#initialize the counts of all letters to 0
	for letter in a_to_z:
		letter_count[letter] = 0


	for key in sum_occurrences_dict:
		print key
		print sum_occurrences_dict[key]
		for letter in key:
			print letter
			letter_count[letter] = (letter_count[letter] + 1) * sum_occurrences_dict[key]	
	return letter_count	

	'''	
	for key in word_data:
		#print key	
		for letter in key:
			#print letter
			letter_count[letter] = letter_count[letter] + 1	
	return letter_count
	'''			
		
print count_letters(word_data)

'''	
if letter not in letter_count:
letter_count[letter] = 1
else:
letter_count[letter] = letter_count[letter] + 1
'''


#str.count('string')





#Output: letter_counts: A list of length 26 where the 0th element is the 
#percentage of letters that are a, the 1st element is the percentage of 
#letters that are b, and so forth.





#make a dictionary with the keys as the letters of the alphabet
#values of the dictionary is the # of times each letter occurs















