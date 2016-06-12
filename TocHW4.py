# -*- coding: utf-8 -*-
import sys
import re
import operator

top = int(sys.argv[1])
path = sys.argv[2]

hashtable = {}

dataset = file(path, 'r')

for line in dataset:
	line = line.rstrip('\n')
	s_line = line.split('\t')
	if(hashtable.has_key(s_line[0])):
		hashtable[s_line[0]] += 1
	else:
		insertdata = {s_line[0]:1}
		hashtable.update(insertdata)
	
	if(hashtable.has_key(s_line[2])):
		hashtable[s_line[2]] += 1
	else:
		insertdata = {s_line[2]:1}
		hashtable.update(insertdata)

#to sort

sorted_hash = sorted(hashtable.items(), key=operator.itemgetter(1), reverse=True)

for i in range(0, top):
	print sorted_hash[i][0] + ',' + str(sorted_hash[i][1])

#to print same rank
for i in range(top, len(sorted_hash)):
	if(sorted_hash[i][1] == sorted_hash[top-1][1]):
		print sorted_hash[i][0] + ',' + str(sorted_hash[i][1])
