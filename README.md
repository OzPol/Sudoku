# Sudoku
Sudoku_generator program in Python
UF - COP3502 - Group Project4



'''
Below instructions were provided to the students who initiated the contents of this repository 
as part of a group assignment in COP3502 class at the University of Florida, under the guidance of Pr. Lisha Zhou.

P4: Sudoku 

Overview 
In this project, students will work in groups of 4 to create a simplified version of the Sudoku game. Students 
will implement random board generation, state checking, and visuals using PyGame. The project is designed to 
be a playful and practical opportunity to practice the programming skills we have learned this semester, as well 
as working with external libraries. 

Getting Started
The provided code and instructions for working with Replit are available at the following GitHub link: 
https://github.com/zhoulisha/Sudoku-Project 

To get started, it is recommended for students to fork the repository (this can be done by clicking “fork” in the 
upper-right corner).

Rules of the Road 
Note: The phrase ‘single-digit numbers’ will be used throughout this project to refer to numbers 1-9, inclusive. 
For the purposes of this project, we will not consider 0 a single-digit number. 
A Sudoku is a puzzle consisting of a 9x9 grid which is partially filled with single-digit numbers. The objective is 
to fill in the rest of the grid with single-digit numbers so that certain rules are satisfied: 
1. In each of the nine rows of the board, no digit is repeated (and each digit occurs once). 
2. In each of the nine columns of the board, no digit is repeated (and each digit occurs once). 
3. In each of the nine 3x3 outlined ‘boxes’ of the board, no digit is repeated (and each digit occurs 
once). 


Example Sudoku boards. When the board satisfies the above rules and each cell is filled, it is solved

Image reference: https://sandiway.arizona.edu/sudoku/examples.html 


    Your task for this project is split into two main parts: 
    1. Generate a random solvable Sudoku board. 
    2. Create visuals for your program using PyGame. 



When the program starts, it should display a Game Start screen.
This will have buttons for the user to choose a difficulty between easy, medium, or hard. 
Once the user clicks a button to select a difficulty, you will generate a Sudoku board.
The difficulty level will determine how many squares on the board are initially empty: 

    Difficulty Number of empty cells 
    easy 30 
    medium 40 
    hard 50 

Once a difficulty is chosen, your program should generate a Sudoku board, make the appropriate number of cells 
empty, and display the partially filled board as shown in the image below. 
 
 
 
 
Game Start screen 
Game-In-Progress Screen 

Note: 1 and 3 in the top-left squares are sketched in 
by a user as input to the game. 

Sudoku successfully completedscreen
Sudoku unsuccessfully completed screen 

Once the player has chosen a difficulty, a partially filled Sudoku board is shown.
There are a few different operations the user can use to interact with the game: 

            • The user can select a cell by clicking on it. Please note that the user can select any cell; however, 
            the user can only edit the cells that are not randomly generated. 

            • Once a cell is selected, the user can type a single-digit number to ‘sketch’ it in the cell (see the 
            game-in-progress screenshot for an example). 

            • If the selected cell has a sketched value, the user can press the return (enter) key to submit their guess. 

            • The user can select a different cell by clicking on it, or by using the arrow keys.

            If the board is full and solved completely correctly, the game win screen is displayed. If the board is full but not 
            solved correctly, the game over screen should be displayed. 

During the game, there are three buttons below the board: 
                                  • The Reset button will reset the board to its initial state. 
                                  • The Restart button will take the user back to the Game Start screen. 
                                  • The Exit button will end the program. 


    Class Structure 
Students should have the following classes in their code. Class methods/attributes other than those listed may be 
added as necessary. 

        SudokuGenerator (Required)
        This class generates a Sudoku – the puzzle as well as the solution. 
        __init__(self, row_length, removed_cells) 
        Constructor for the SudokuGenerator class. 

        For the purposes of this project, row_length is always 9. 
        removed_cells could vary depending on the difficulty level chosen (see “UI Requirements”). 
        

        get_board(self) 
        Returns a 2D python list of numbers, which represents the board 

        print_board(self) 
        Displays the board to the console. 
        This is not strictly required, but it may be useful for debugging purposes. 


        valid_in_row(self, row, num) 
        Returns a Boolean value. 
        Determines if num is contained in the given row of the board. 


        valid_in_col(self, col, num) 
        Returns a Boolean value. 
        Determines if num is contained in the given column of the board. 


        valid_in_box(self, row_start, col_start, num) 
        Returns a Boolean value. 
        Determines if num is contained in the 3x3 box from (row_start, col_start) to (row_start+2, col_start+2) 


        is_valid(self, row, col, num) 
        Returns if it is valid to enter num at (row, col) in the board. 
        This is done by checking the appropriate row, column, and box. 


        fill_box(self, row_start, col_start)
        Randomly fills in values in the 3x3 box from (row_start, col_start) to (row_start+2, col_start+2) 
        Uses unused_in_box to ensure no value occurs in the box more than once. 


        fill_diagonal(self) 
        Fills the three boxes along the main diagonal of the board. 
        This is the first major step in generating a Sudoku. 
        See the Step 1 picture in Sudoku Generation for further explanation. 


        fill_remaining(self, row, col) 
        This method is provided for students. 
        It is the second major step in generating a Sudoku. 
        This will return a completely filled board (the Sudoku solution). 



        fill_values(self) 
        This method is provided for students. 
        It constructs a solution by calling fill_diagonal and fill_remaining. 




        remove_cells(self) 
        This method removes the appropriate number of cells from the board. 
        It does so by randomly generating (row, col) coordinates of the board and setting the value to 0. 
        Note: Be careful not to remove the same cell multiple times. A cell can only be removed once. 
        This method should be called after generating the Sudoku solution. 


        generate_sudoku(size, removed) 
        Note: This is a function outside of the SudokuGenerator class. 
        This function should also be implemented in sudoku_generator.py as it interacts with the class. 
        Given size and removed, this function generates and returns a size-by-size sudoku board. 
        The board has cleared removed number of cells. 
        This function should just call the constructor and appropriate methods from the SudokuGenerator class. 



                                      Cell (Recommended)
                                      This class represents a single cell in the Sudoku board. There are 81 Cells in a Board. 
                                      __init__(self, value, row, col, screen) 
                                      Constructor for the Cell class 

                                      set_cell_value(self, value) 
                                      Setter for this cell’s value

                                      set_sketched_value(self, value) 
                                      Setter for this cell’s sketched value 

                                      draw(self) 
                                      Draws this cell, along with the value inside it. 
                                      If this cell has a nonzero value, that value is displayed. 
                                      Otherwise, no value is displayed in the cell. 
                                      The cell is outlined red if it is currently selected. 
 


                  Board (Recommended)
                  This class represents an entire Sudoku board. A Board object has 81 Cell objects. 
                  __init__(self, width, height, screen, difficulty) 
                  Constructor for the Board class. 
                  screen is a window from PyGame. 

                  difficulty is a variable to indicate if the user chose easy, medium, or hard. 
                  draw(self) 
                  Draws an outline of the Sudoku grid, with bold lines to delineate the 3x3 boxes. 
                  Draws every cell on this board.


                  select(self, row, col) 
                  Marks the cell at (row, col) in the board as the current selected cell. 
                  Once a cell has been selected, the user can edit its value or sketched value. 


                  click(self, x, y) 
                  If a tuple of (x, y) coordinates is within the displayed board,
                  this function returns a tuple of the (row, col) 
                  of the cell which was clicked. Otherwise, this function returns None. 


                  clear(self) 
                  Clears the value cell. Note that the user can only remove
                  the cell values and sketched value that are 
                  filled by themselves. 

                  sketch(self, value) 
                  Sets the sketched value of the current selected cell equal to user entered value. 
                  It will be displayed at the top left corner of the cell using the draw() function. 


                  place_number(self, value) 
                  Sets the value of the current selected cell equal to user entered value. 
                  Called when the user presses the Enter key. 


                  reset_to_original(self) 
                  Reset all cells in the board to their original values
                  (0 if cleared, otherwise the corresponding digit). 


                  is_full(self) 
                  Returns a Boolean value indicating whether the board is full or not.


                  update_board(self) 
                  Updates the underlying 2D board with the values in all cells. 


                  find_empty(self) 
                  Finds an empty cell and returns its row and col as a tuple (x, y). 


                  check_board(self) 
                  Check whether the Sudoku board is solved correctly. 
 
 
 
 
 
 
 
 
 
 
Main (Required)
In addition to the above classes, students will have a sudoku.py file, where the main function will be run. This 
file will contain code to create the different screens of the project (game start, game over, and game in 
progress), and will form a cohesive project together with the rest of the code. 
Sudoku Generation 
Generating a Sudoku board involves a process known as backtracking, which is beyond the scope of this class. 
Students will implement some of the functions necessary to generate a Sudoku board, and the rest of the 
backtracking algorithm will be provided. 

The overall process of generating a Sudoku board follows 3 main steps: 
1. Generate values along boxes on the diagonal 
2. Fill in the remaining values using backtracking 
3. Make some of the cells blank 

A Sudoku board after steps 1, 2, and 3 of generating the board. ‘0’ digits represent empty spaces. 
Notice that the board is filled after step 2 is completed.
This is the solution to the Sudoku, so it should be stored 
in your program to verify if the solver’s guess is correct or incorrect for a certain cell.
'''
