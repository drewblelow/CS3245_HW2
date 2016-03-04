#A0110649J
import re
import nltk
import sys
import os
import getopt
import math
from collections import Counter
from os.path import basename
from os import listdir
from os.path import isfile, join

#use message
def usage():
	print "usage: " + sys.argv[0] + " -d dictionary-file -p postings-file -q file-of-queries -o output-file-of-results"

#default settings
dictionary_file = "dictionary.txt"
postings_file = "postings.txt"
query_file = "query.txt"
output_file = "out.txt"

#variables
DICTIONARY = {}
LEFT_ASSOC = 0
RIGHT_ASSOC = 1
#representation of boolean operators are symbols + * -
OPERATORS = { 
	#OR REPRESENTATION
	'+' : (0, LEFT_ASSOC),
	#AND REPRESENTATION
    '*' : (5, LEFT_ASSOC),
	#NOT REPRESENTATION
    '-' : (10, RIGHT_ASSOC)
}

#specified settings
try:
	opts, args = getopt.getopt(sys.argv[1:], 'd:p:q:o')
except getopt.GetoptError, err:
	usage()
	sys.exit(2)
for o, a in opts:
	if o == '-d':
		dictionary_file = a
	elif o == '-p':
		postings_file = a
	elif o == '-q':
		query_file = a
	elif o == '-o':
		output_file = a
	else:
		assert False, "unhandled option"

#filepath handling for specified options			
if dictionary_file == None or postings_file == None or query_file == None or output_file == None:
    usage()
    sys.exit(2)
	
#load dictionary into memory
def load_dic():
	print("loading dictionary into memory..."),
	dic = open(dictionary_file, 'r').readline()
	entries = dic.split()
	for entry in entries:
		item = entry.split('^')
		word = item[0]
		index = item[1]
		DICTIONARY[word] = index
	print("[DONE]")

#wrapper method reads all queries in the file
def read_queries():
	print("reading and searching queries..."),
	query_lines = open(query_file).readlines()
	for query in query_lines:
		line = parse(query)
		evaluate(line)
	print("[DONE]")
	
#parses the query 	
def parse(string):
	tokenised = string.split()
	output = toRPN(tokenised)
	return output

#evaluates the parsed query
def evaluate(string):
	print("TODO: evaluate search")
	
	out_writer = open(output_file, 'w')

#changes the format of query, infix to rpn
def toRPN(query):
	output = []
	stack = []
	for token in query:
		if isOperator(token):
			while len(stack) != 0 and isOperator(token)
				if (isAssoc(token, LEFT_ASSOC) and precedence(token, stack[-1]) <= 0) or (isAssoc(token, RIGHT_ASSOC) and precedence(token, stack[-1]) < 0):
					out.append(stack.pop())
					continue
				break
			stack.append(token)
		elif token == '(':
			stack.append(token)
		elif token == ')':
			while len(stack) != 0 and stack[-1] != '(':
				out.append(stack.pop())
			stack.pop()
		else:
			out.append(token)
	while len(stack) != 0
		out.append(stack.pop())
	return out
		
#shunting yard helpers
#check if operator
def isOperator(token):
	return token in OPERATORS

#check associativity
def isAssoc(token, assoc):
	return OPERATORS[token][1] == assoc

#compare precedence
	return OPERATORS[t1][0] - OPERATORS[t2][0]
def precedence(t1, t2):

#run the methods declared above
load_dic()
read_queries()