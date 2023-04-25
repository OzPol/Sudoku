import pygame, sys
from constants import *

class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.cell_sketched_value = 0
        self.clicked = False
        self.width = WIDTH
        self.height = HEIGHT
        self.editable = False
        self.cell_filled = True
        if value == 0:
            self.cell_filled = False


    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        self.cell_sketched_value = value

    def draw(self):
        # This sets the font of the numbers
        number_font = pygame.font.Font(None, 70)
        small_font = pygame.font.Font(None, 35)
        number_surf = number_font.render(str(self.value), 0, LINE_COLOR)
        sketched_surf = small_font.render(str(self.cell_sketched_value), 0, LINE_COLOR)
        empty_surf = number_font.render('', 0, LINE_COLOR)

        if self.value != 0:
            number_rect = number_surf.get_rect(center=(SQUARE_SIZE // 2 + SQUARE_SIZE * self.row, SQUARE_SIZE // 2 + SQUARE_SIZE * self.col))
            self.screen.blit(number_surf, number_rect)

        else:
            if self.cell_sketched_value == 0:
                number_rect = empty_surf.get_rect(center=(SQUARE_SIZE // 2 + SQUARE_SIZE * self.row, SQUARE_SIZE // 2 + SQUARE_SIZE * self.col))
                self.screen.blit(empty_surf, number_rect)

            else:
                sketched_rect = sketched_surf.get_rect(center=(SQUARE_SIZE * self.row + 10, SQUARE_SIZE * self.col + 15))
                self.screen.blit(sketched_surf, sketched_rect)


        if self.clicked:
            pygame.draw.rect(self.screen, RED, pygame.Rect(self.row * SQUARE_SIZE - 1, self.col * SQUARE_SIZE - 1, SQUARE_SIZE + 3, SQUARE_SIZE + 3), CLICKED_OUTLINE_WIDTH)
            

