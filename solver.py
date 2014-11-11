#!/usr/bin/python

import math
import fileinput

board = [];

def main():
	read_in()

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

if __name__ == "__main__":
	main()



''' for reference
	board[1].remove(1);
	val = 1;
	if isinstance(val, int):
		print board, bol; '''