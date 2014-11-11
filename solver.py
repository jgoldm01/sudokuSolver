#!/usr/bin/python

import math
import fileinput

board = [];

def main():
	read_in()
	eliminate_duplicates()
	if not isCorrect():
		print "error: board not solveable"
		exit()
	if isFinished():
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

def eliminate_duplicates():
	isChanged = False
	for i in range(9):
		isChanged = rcb_elimination(i, isChanged, rowArr)
		isChanged = rcb_elimination(i, isChanged, colArr)
		isChanged = rcb_elimination(i, isChanged, blockArr)
	if isChanged:
		set_values()
		eliminate_duplicates()

def rowArr(i):
	return range(i*9, (i*9)+9);

def colArr(i):
	return range(i,81,9);

def blockArr(i):
	s = (i/3)*27 + (i%3)*3;
	return [s, s+1, s+2, s+9, s+10, s+11, s+18, s+19, s+20];

def rcb_elimination(i, isChanged, rcb_func):
	rcbRange = rcb_func(i);
	for j in rcbRange:
		if isinstance(board[j], int):
			#iterates through row, 
			#eliminating the found number from possibility lists
			for k in rcbRange:
				if isinstance(board[k], list) and board[j] in board[k]:
					isChanged = True;
					board[k].remove(board[j]);
	return isChanged

def set_values():
	for i in range(81):
		if isinstance(board[i], list):
			if len(board[i]) == 1:
				board[i] = board[i][0]

#returns whether the board adheres to the rules of sudoku
def isCorrect():
	correct = True
	for i in range(9):
		correct = rcb_check(i, rowArr)
		correct = rcb_check(i, colArr)
		correct = rcb_check(i, blockArr)
		if not correct:
			return False
	return True

def rcb_check(i, rcb_func):
	rcbRange = rcb_func(i)
	for j in rcbRange:
		if isinstance(board[j], int):
			#iterates through row, 
			#eliminating the found number from possibility lists
			for k in rcbRange:
				if k != j and board[k] == board[j]:
					return False
	return True

def isFinished():
	for i in range(81):
		if isinstance(board[i], list):
			return False
	return True

def nondeterministic_test():
	print "this is a hard puzzle"

def print_board():
	index = 0;
	for i in range(81):
			print board[i],
			if index%9 == 2 or index%9 == 5:
				print "|",
			elif index%9 == 8:
				print "\n",
			if index%27 == 26:
				print "_ _ _ _ _ _ _ _ _ _ _ "
			index += 1;

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