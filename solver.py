#!/usr/bin/python

import math
import fileinput

global board

#macro control flow of the program, 
#at least until the nondeterministic function is called
def main():
	read_in()
	eliminate_duplicates()
	if not isCorrect():
		print "error: board not solveable"
		exit()
	if isFinished():
		print_board()
	else:
		if nondeterministic_test():
			print_board()
		else:
			print "error: board not solveable"

#reads in the board from a text file
def read_in():
	global board 
	board = []
	index = 0
	for line in fileinput.input():
		for char in line:
			if char != ' ' and char != '\n':
				if char == '_' or char == '0':
					board.append(range (1,10))
				else:
					board.append(int(char));
				index += 1;

#eliminates duplicates from the sudoku board through simple rcb checks
#rcb - row, column, block
def eliminate_duplicates():
	isChanged = False
	for i in range(9):
		isChanged = rcb_elimination(i, isChanged, rowArr)
		isChanged = rcb_elimination(i, isChanged, colArr)
		isChanged = rcb_elimination(i, isChanged, blockArr)
	if isChanged:
		set_values()
		eliminate_duplicates()

#returns the indicies of the i'th row
def rowArr(i):
	return range(i*9, (i*9)+9);

#returns the indicies of the i'th column
def colArr(i):
	return range(i,81,9);

#returns the indicies of the i'th block
def blockArr(i):
	s = (i/3)*27 + (i%3)*3;
	return [s, s+1, s+2, s+9, s+10, s+11, s+18, s+19, s+20];

#goes through by row, column, or block and eliminates possible values 
#if the number is found in the rcb
def rcb_elimination(i, isChanged, rcb_func):
	global board
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

#after board is changed
#sets possibility lists of only one element to certain integers
def set_values():
	global board
	for i in range(81):
		if isinstance(board[i], list):
			if len(board[i]) == 1:
				board[i] = board[i][0]

#returns whether the board adheres to the rules of sudoku
def isCorrect():
	correct = True
	for i in range(9):
		correct = rcb_check(i, correct, rowArr)
		correct = rcb_check(i, correct, colArr)
		correct = rcb_check(i, correct, blockArr)
		if not correct:
			return False
	return True

#checks that the row, column, or block does not contain any duplicate numbers
def rcb_check(i, correct, rcb_func):
	rcbRange = rcb_func(i)
	for j in rcbRange:
		if isinstance(board[j], int):
			#iterates through row, 
			#eliminating the found number from possibility lists
			for k in rcbRange:
				if k != j and board[k] == board[j]:
					return False
		elif board[j] == []:
			return False
	return correct

#returns true if all elements in the board are determined
def isFinished():
	for i in range(81):
		if isinstance(board[i], list):
			return False
	return True

#selects potential values for the board, from those squares with only possible ones
#recursively tests these and other values if necessary
def nondeterministic_test():
	global board
	oldBoard = [];
	oldBoard = deepCopy(oldBoard, board)

	#find first element that is a list
	for i in range(81):
		if isinstance(board[i], list):
			index = i
			break

	#test that element's possible numbers
	for i in range(len(oldBoard[index])):
		board[index] = oldBoard[index][i]
		eliminate_duplicates()

		if isCorrect():
			if isFinished():
				return True
			else:
				#continue on to the next list 
				if nondeterministic_test():
					return True

		board = deepCopy(board, oldBoard)

	#no solution is possible with this current iteration of the board
	return False

#makes a deep copy of the original board. In python, lists are not copied but
#pointed to, this is true of lists within lists as well.
def deepCopy(copy, orig):
	copy = [];
	for i in range(81):
		if isinstance(orig[i], list):
			copy.append([])
			for j in range(len(orig[i])):
				copy[i].append(orig[i][j])
		else:
			copy.append(orig[i])
	return copy


#prints the board with block delimiters
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
	print "\n"

#lets get this party started!
if __name__ == "__main__":
	main()


