import pygame
from board import Board
from cell import Cell
from sudoku_generator import SudokuGenerator



pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("Project 4: Sudoku")

while True:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    pygame.display.update()
