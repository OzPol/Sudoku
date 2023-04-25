import pygame, sys
from constants import *
from cell import Cell
from sudoku_generator import *

class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.rows = 9
        self.cols = 9
        self.board = generate_sudoku(9, difficulty)
        self.cells = [[Cell(self.board[row][col], row, col, self.screen) for col in range(9)] for row in range(9)]
        self.unused_cells = []

    def draw(self):
        # Draws an outline of hte Sudoku grid, the bold lines to delineate the 3x3 boxes.
        # Draws every cell on this board

        # Background color of start screen
        self.screen.fill(BG_COLOR)

        # this loop draws thicker horizontal lines dividing screen into 9 equal boxes
        for i in range(0, BOARD_ROWS + 1):
            pygame.draw.line(
                self.screen,  # first argument 'screen'
                LINE_COLOR,  # second argument 'color'
                (0, i * SQUARE_SIZE * 3),  # third argument, 'starting point' of line
                (WIDTH, i * SQUARE_SIZE * 3),  # fourth argument, 'ending point' of line
                LINE_WIDTH  # fifth argument, 'line width' of line
            )

        # this loop draw thicker vertical lines
        for i in range(0, BOARD_COLS + 1):
            pygame.draw.line(
                self.screen,
                LINE_COLOR,
                (i * SQUARE_SIZE * 3, 0),
                (i * SQUARE_SIZE * 3, HEIGHT),
                LINE_WIDTH
            )

        # this loop makes the smaller horizontal lines within each bigger box.
        for i in range(0, SMALL_LINE_ROWS + 1):
            pygame.draw.line(
                self.screen,
                LINE_COLOR,
                (0, i * SQUARE_SIZE),
                (WIDTH, i * SQUARE_SIZE),
                SMALL_LINE_WIDTH
            )

        # This loop makes the smaller vertical line within each bigger box.
        for i in range(1, SMALL_LINE_COLS):
            pygame.draw.line(
                self.screen,
                LINE_COLOR,
                (i * SQUARE_SIZE, 0),
                (i * SQUARE_SIZE, WIDTH),
                SMALL_LINE_WIDTH
            )

        # This draws the cells value
        for list_cells in self.cells:
            for cell in list_cells:
                cell.draw()

    def select(self, row, col):
        # Marks the cell at (row, col) in the board as the current selected cell.
        # once a cell has been selected, the user can edit its value or sketched value
        # Reset the clicked status of all cells to False to remove outlines from other cells

        for i in range(9):
            for j in range(9):
                self.cells[i][j].clicked = False
        self.cells[row][col].clicked = True
        self.click(row, col)





    def click(self, x, y):

        # If a tuple of (x, y) coordinates is within the displayed board,
        # this function returns a tuple of the clicked cell's (row, col)
        # Otherwise returns None
        clicked_row = x // SQUARE_SIZE
        clicked_col = y // SQUARE_SIZE
        if clicked_row in range(9) and clicked_col in range(9):
            print([clicked_row, clicked_col])
            return [clicked_row, clicked_col]
        else:
            return None

    def clear(self):
        # Clears the. Note that the user can only remove the cell value
        # and sketched value that are filled by themselves
        # K_BACKSPACE
        for cell_list in range(9):  # for cell_list in self.cells:
            for cell in range(9):  # for cell in cell_list:
                if self.cells[cell_list][cell].clicked:
                    if self.cells[cell_list][cell].cell_filled == False:
                        self.cells[cell_list][cell].value = 0
                        self.cells[cell_list][cell].cell_sketched_value = 0
                    # Wherever we are generating the cells, we need to mark whether is cell is editable or not

    def sketch(self, value):
        # Sets the sketched value of the current selected cell equal to user entered value.
        # It will be displayed at the top left corner of the cell using the draw() function

        for cell_list in self.cells:
            for cell in cell_list:
                if cell.clicked:
                    cell.set_sketched_value(value)


    def place_number(self, value):
        # Sets the value of the current selected cell equal to user entered value.
        # Called when the user presses the Enter key
        self.find_empty()

        for cell_list in range(9):            #for cell_list in self.cells:
            for cell in range(9):              #for cell in cell_list:
                if self.cells[cell_list][cell].clicked:            # if cell.clicked:
                    if (cell_list, cell) in self.unused_cells:

                        if self.cells[cell_list][cell].cell_sketched_value == 0:
                            self.cells[cell_list][cell].set_cell_value(0)
                        else:
                            self.cells[cell_list][cell].set_cell_value(value)
                    #cell.clicked = False

    def reset_to_original(self):
        #Reset all cells in the board to their original values (0 if cleared, otherwise the corresponding digit).

        for row in range(9):
            for col in range(9):
                if (row, col) in self.unused_cells:
                    self.cells[row][col].set_cell_value(0)
                    self.cells[row][col].set_sketched_value(0)
                    self.cells[row][col].clicked = False

    def is_full(self):
        #Returns a Boolean value indicating whether the board is full or not.
        for row in range(9):
            for col in range(9):
                if self.cells[row][col].value == 0:
                    return False
        return True

    def update_board(self):
        #Updates the underlying 2D board with the values in all cells.

        for row in range(9):
            for col in range(9):
                self.board[row][col] = self.cells[row][col].value

    def find_empty(self):
        #Finds an empty cell and returns its row and col as a tuple (x, y).
        for row in range(9):
            for col in range(9):
                if self.cells[row][col].value == 0:
                    pos_cell = (row, col)
                    self.unused_cells.append(pos_cell)

        return self.unused_cells

    def check_board(self):
        #Check whether the Sudoku board is solved correctly.

        #check each row for duplicates, return false if found any, and add the number to the row set, if it's not a duplicate
        for row in range(9):
            row_list = set()
            for col in range(9):
                num = self.cells[row][col].value
                if num in row_list:
                    return False
                row_list.add(num)
                
        #check each col for duplicates, return false if found any, and add the number to the col set, if it's not a duplicate
        for col in range(9):
            col_list = set()
            for row in range(9):
                num = self.cells[row][col].value
                if num in col_list:
                    return False
                col_list.add(num)

        #check each 3x3 box for duplicates,
        for col in range(0, 9, 3):
            for row in range(0, 9, 3):
                small_box = set()
                for i in range (3):
                    for j in range(3):
                        num = self.cells[i + col][j + row].value           
                        if num in small_box:
                            return False
                        small_box.add(num)        
        return True

