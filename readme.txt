This program finds a solution to a sudoku puzzle of any difficulty. 

It reads in a text file specified on the command line. 
call with: python solver.py board.txt

An example body of board.txt would be:

_ _ 2 _ _ 7 5 8 _  <- blanks signify unknown spaces, 0 does as well
9 4 _ 8 _ _ 7 1 _  
1 _ _ 9 3 _ 6 4 _ 
_ _ 9 _ _ _ _ _ _ 
4 _ 3 5 _ _ 8 _ _ 
_ 7 1 6 _ 3 2 9 _  
2 _ 4 | _ 9 6 | 1 5 _ <- the user can choose to separate blocks with | 
5 _ _ | 2 _ 1 | _ 3 _ 	 for organization
_ _ _ | _ _ 4 | _ _ _ 

the solution will be pushed to standard ouptput. 

Enjoy!
