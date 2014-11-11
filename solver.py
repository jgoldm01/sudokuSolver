#!/usr/bin/python

import math
import fileinput

board = [];

def main():
	read_in()
	eliminate_duplicates()
	if (isfinished()):
		print_board();
	else:
		nondeterministic_test()

def read_in():
	index = 0;
	for line in fileinput.input():
		for char in line:
			if char != ' ' and char != '\n':
				if char == '_' or char == '0':
					board.append(range (1,10))
				else:
					board.append(int(char));
				index += 1;
	print board

def eliminate_duplicates():
	isChanged = False
	for i in range(9):
		isChanged = rows(i, isChanged)
		isChanged = cols(i, isChanged)
		isChanged = blocks(i, isChanged)
	if isChanged:
		set_values()
		eliminate_duplicates()

def rows(i, isChanged):
	i *= 9
	#iterates through row, looking for integers
	for j in range (i, i+9):
		if isinstance(board[j], int):
			#iterates through row, 
			#eliminating the found number from possibility lists
			for k in range(i, i+9):
				if isinstance(board[k], list) and board[j] in board[k]:
					isChanged = True;
					board[k].remove(board[j]);
	return isChanged

def cols(i, isChanged):
	for j in range(i,81,9):
		if isinstance(board[j], int):
			for k in range(i,81,9):
				if isinstance(board[k], list) and board[j] in board[k]:
					isChanged = True;
					board[k].remove(board[j]);
	return isChanged

def blocks(i, isChanged):
	s = (i/3)*27 + (i%3)*3;
	blockArr = [s, s+1, s+2, s+9, s+10, s+11, s+18, s+19, s+20];
	for j in blockArr:
		if isinstance(board[j], int):
			#iterates through row, 
			#eliminating the found number from possibility lists
			for k in blockArr:
				if isinstance(board[k], list) and board[j] in board[k]:
					isChanged = True;
					board[k].remove(board[j]);
	return isChanged

def set_values():
	for i in xrange(81):
		if isinstance(board[i], list):
			if len(board[i]) == 1:
				board[i] = board[i][0]

def isfinished():
	return True

def nondeterministic_test():
	print "this is a hard puzzle"

def print_board():
	for i in range(9):
		print board[i*9:i*9+9]

if __name__ == "__main__":
	main()



''' for reference
	board[1].remove(1);
	val = 1;
	if isinstance(val, int):
		print board, bol; 
	if 23 in board[0]:
		board[0].remove(23)
		len(board[0])
'''