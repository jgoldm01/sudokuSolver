#!/usr/bin/python
import sys
import solver

try:
    # for Python2
    from Tkinter import *
except ImportError:
    # for Python3
    from tkinter import * 
    
class App:
	def __init__(self, master):
		master.geometry("%dx%d+300+300" % (275, 340))
		master.title("Sudoku Board")
		master.configure(background='blue')
		
		frame = Frame(master, bg='blue')
		frame.grid()

		self.board = [[Entry(frame, width=2, selectborderwidth=5) for x in range(9)] for x in range(9)];
		for x in range(9):
			for y in range(9):
				self.board[x][y].insert(0, "0")
				self.board[x][y].grid(row=x+x/3+1, column=y+y/3+1, sticky=W+N)
		Label(frame, text="   ", bg="blue").grid(row=0, column=0);
		Label(frame, text="   ", bg="blue").grid(row=4, column=4);
		Label(frame, text="   ", bg="blue").grid(row=8, column=8);

		self.hi_there = Button(master, text="SOLVE!", command=self.get_board)
		self.hi_there.grid(pady=10)

		self.button = Button(master, text="QUIT", fg="red", command=frame.quit)
		self.button.grid()


	def get_board(self):
		global board 

		board = [];
		for x in range(9):
			for y in range(9):
				try:
					num = int(self.board[x][y].get())
					if num > 9 or num < 0:
						self.displayError(self.inputErrorMessage(x, y))
						return;
				except: 
					self.displayError(self.inputErrorMessage(x, y))
					return;

				if num == 0:
					board.append(range (1,10))
				else:
					board.append(num);

		retVal = solver.solve(board);
		if isinstance(retVal, str):
			self.displayError(retVal)
		else:
			self.displaySolution(retVal)

	def inputErrorMessage(self, x, y):
		return "please input a number between 1-9 in row %d, column %d" % (x+1, y+1)

	def displayError(self, message):
		top=Toplevel()
		top.title("numbers")

		msg = Message(top, text=message)
		msg.pack()
		top.geometry("%dx%d+325+400" % (200, 100))

	def displaySolution(self, board):
		for x in range(9):
			for y in range(9):
				self.board[x][y].delete(0, END)
				self.board[x][y].insert(0, board[x*9+y])



def main():
	root = Tk()
	app = App(root)
	root.mainloop()


if __name__ == '__main__':
	main()