import pygame, sys
from board import Board
from cell import Cell
from sudoku_generator import *
from constants import *
pygame.init()


def start_screen(screen):         # help with start screen using geeksforgeeks.org to write on start screen
                            # https://www.youtube.com/watch?v=ZP4VOoDNuZA for help with text on start screen

    #Background color of start screen
    screen.fill(BG_COLOR)

    # This sets the font of the beginning screen words
    welcome_font = pygame.font.Font(None, 80)
    game_mode_font = pygame.font.Font(None, 65)
    difficulty_font = pygame.font.Font(None, 50)

    # Initialize texts of difficulty buttons
    easy_message = difficulty_font.render('EASY', True, BG_COLOR)
    medium_message = difficulty_font.render('MEDIUM', True, BG_COLOR)
    hard_message = difficulty_font.render('HARD', True, BG_COLOR)

    #Write "Welcome to Sudoku" on start screen
    welcome_message = welcome_font.render('Welcome to Sudoku', True, LINE_COLOR)
    welcome_message_rect = welcome_message.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 140))
    screen.blit(welcome_message, welcome_message_rect)

    #Writes "Select Game Mode:" on start screen
    game_mode_message = game_mode_font.render('Select Game Mode:', True, LINE_COLOR)
    game_mode_rect = game_mode_message.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
    screen.blit(game_mode_message, game_mode_rect)

    #Writes "Easy" "Medium" and "Hard" on start sreen
    easy_button_surface = pygame.Surface((easy_message.get_size()[0] + 20, easy_message.get_size()[1] + 20))
    easy_button_surface.fill(LINE_COLOR)
    easy_button_surface.blit(easy_message, (10, 10))

    medium_button_surface = pygame.Surface((medium_message.get_size()[0] + 20, medium_message.get_size()[1] + 20))
    medium_button_surface.fill(LINE_COLOR)
    medium_button_surface.blit(medium_message, (10, 10))

    hard_button_surface = pygame.Surface((hard_message.get_size()[0] + 20, hard_message.get_size()[1] + 20))
    hard_button_surface.fill(LINE_COLOR)
    hard_button_surface.blit(hard_message, (10, 10))

    easy_mode_rect = easy_message.get_rect(center=(WIDTH // 4, HEIGHT - 120))
    screen.blit(easy_button_surface, easy_mode_rect)

    medium_mode_rect = medium_message.get_rect(center=(WIDTH // 2, HEIGHT - 120))
    screen.blit(medium_button_surface, medium_mode_rect)

    hard_mode_rect = hard_message.get_rect(center=(WIDTH * (3/4), HEIGHT - 120))
    screen.blit(hard_button_surface, hard_mode_rect)

    # Make a click event. If clicked at certain difficulty, then it is passed into Board() with clicked difficulty.

    while True:
        # event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_mode_rect.collidepoint(event.pos):
                    # Checks if mouse is on easy button and returns easy difficulty number
                    return 30

                elif medium_mode_rect.collidepoint(event.pos):
                    # Checks if mouse is on medium button and returns medium difficulty number
                    return 40

                elif hard_mode_rect.collidepoint(event.pos):
                    # Checks if mouse is on hard button and returns hard difficulty number
                    return 50

        pygame.display.update()


def game_won_screen(screen):
    # Background color of start screen

    screen = pygame.display.set_mode((603, 703))  # this is the width and height of window.
    screen.fill(BG_COLOR)
    #sudoku_screen = Board(WIDTH, HEIGHT, screen, game_won_screen(screen))  # This initializes the sudoku screen with set difficutly

    # This sets up the font on the Game Won! screen
    game_won_font = pygame.font.Font(None, 100)
    exit_button_font = pygame.font.Font(None, 65)

    game_won_message = game_won_font.render('Game Won!', True, LINE_COLOR)
    game_won_rect = game_won_message.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 125))
    screen.blit(game_won_message, game_won_rect)

    exit_button_message = exit_button_font.render('EXIT', True, BG_COLOR)
    exit_button_rect = exit_button_message.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 100))
    screen.blit(exit_button_message, exit_button_rect)


    # initializes the exit button at bottom of sudoku screen
    exit_button_surface = pygame.Surface((exit_button_message.get_size()[0] + 20, exit_button_message.get_size()[1] + 20))
    exit_button_surface.fill(LINE_COLOR)
    exit_button_surface.blit(exit_button_message, (10, 10))

    exit_button_rect = exit_button_message.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 100))
    screen.blit(exit_button_surface, exit_button_rect)

    while True:

        # event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                    
                # pos = pygame.mouse.get_pos()
                # row_pos, col_pos = pos[0], pos[1]
                # x_y_pos = sudoku_screen.click(row_pos, col_pos)
                # if row_pos >= 0 and row_pos <= WIDTH and col_pos >= 0 and col_pos <= 600:
                #     sudoku_screen.select(x_y_pos[0], x_y_pos[1])

                if exit_button_rect.collidepoint(event.pos):
                    sys.exit()

        pygame.display.update()



def game_over_screen(screen):
    #Background color of start screen

    screen.fill(BG_COLOR)
    #sudoku_screen = Board(WIDTH, HEIGHT, screen, game_over_screen(screen))  # This initializes the sudoku screen with set difficutly

    # This sets up the fon on the Game Over :( screen
    game_over_font = pygame.font.Font(None, 100)
    restart_button_font = pygame.font.Font(None, 65)

    game_over_message = game_over_font.render('Game Over :(', True, LINE_COLOR)
    game_over_rect = game_over_message.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 125))
    screen.blit(game_over_message, game_over_rect)

    restart_button_message = restart_button_font.render('RESTART', True, BG_COLOR)
    restart_button_rect = restart_button_message.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
    screen.blit(restart_button_message, restart_button_rect)


    # initializes the restart button at bottom of sudoku screen
    restart_button_surface = pygame.Surface((restart_button_message.get_size()[0] + 20, restart_button_message.get_size()[1] + 20))
    restart_button_surface.fill(LINE_COLOR)
    restart_button_surface.blit(restart_button_message, (10, 10))

    restart_button_rect = restart_button_message.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
    screen.blit(restart_button_surface, restart_button_rect)


    #Draws boxes around text based on project pdf
    while True:
        # event loop
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
            if event.type == pygame.MOUSEBUTTONDOWN:
                    
                # pos = pygame.mouse.get_pos()
                # row_pos, col_pos = pos[0], pos[1]
                # x_y_pos = sudoku_screen.click(row_pos, col_pos)
                # if row_pos >= 0 and row_pos <= WIDTH and col_pos >= 0 and col_pos <= 600:
                #     sudoku_screen.select(x_y_pos[0], x_y_pos[1])
                if restart_button_rect.collidepoint(event.pos):
                    main()

        pygame.display.update()
 

def main():

    pygame.init()
    pygame.display.set_caption("Sudoku")            # This sets the name of the window at top bar of popout window
    screen = pygame.display.set_mode((603, 703))  # this is the width and height of window.
    sudoku_screen = Board(WIDTH, HEIGHT, screen, start_screen(screen))  # This initializes the sudoku screen with set difficutly

    game_on = True      
    game_won = False
    game_over = False

#main event loop
    while True:

        while game_on and not game_won and not game_over:
            sudoku_screen.draw()

            bottom_game_font = pygame.font.Font(None, 50)               # sets up the fonts of RESET, RESTART and EXIT buttons on the screen, while game_on

            # This sets text at bottom of sudoku screen
            reset_message = bottom_game_font.render('RESET', True, BG_COLOR)
            restart_message = bottom_game_font.render('RESTART', True, BG_COLOR)
            exit_message = bottom_game_font.render('EXIT', True, BG_COLOR)

            # initializes the reset button at bottom of sudoku screen
            reset_button_surface = pygame.Surface((reset_message.get_size()[0] + 20, reset_message.get_size()[1] + 20))
            reset_button_surface.fill(LINE_COLOR)
            reset_button_surface.blit(reset_message, (10, 10))

            # initializes the restart button at bottom of sudoku screen
            restart_button_surface = pygame.Surface((restart_message.get_size()[0] + 20, restart_message.get_size()[1] + 20))
            restart_button_surface.fill(LINE_COLOR)
            restart_button_surface.blit(restart_message, (10, 10))

            # initializes the exit button at bottom of sudoku screen
            exit_button_surface = pygame.Surface((exit_message.get_size()[0] + 20, exit_message.get_size()[1] + 20))
            exit_button_surface.fill(LINE_COLOR)
            exit_button_surface.blit(exit_message, (10, 10))

            # These draw the rectangle around text
            reset_button_rect = reset_message.get_rect(center=(((WIDTH / 9) * 1.5) - 10, HEIGHT + 40))    #(center=(WIDTH // 4 - 30, HEIGHT))
            screen.blit(reset_button_surface, reset_button_rect)

            restart_button_rect = restart_message.get_rect(center=((WIDTH / 2) - 10, HEIGHT + 40))
            screen.blit(restart_button_surface, restart_button_rect)

            exit_button_rect = exit_message.get_rect(center=(((WIDTH / 9) * 7) + 10, HEIGHT + 40))     #(center=(WIDTH * (3 / 4) + 30, HEIGHT))
            screen.blit(exit_button_surface, exit_button_rect)


            # event loop
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    game_on = False
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    row_pos, col_pos = pos[0], pos[1]
                    x_y_pos = sudoku_screen.click(row_pos, col_pos)
                    if row_pos >= 0 and row_pos <= WIDTH and col_pos >= 0 and col_pos <= 600:
                        sudoku_screen.select(x_y_pos[0], x_y_pos[1])

                    if exit_button_rect.collidepoint(event.pos):
                        sys.exit()

                    if reset_button_rect.collidepoint(event.pos):
                        sudoku_screen.reset_to_original()

                    if restart_button_rect.collidepoint(event.pos):
                        main()
                   

                if event.type == pygame.KEYDOWN: #or event.type == pygame.KEYUP
                    if event.key == pygame.K_1 or event.key == pygame.K_KP1:
                        number_to_place = 1
                        sudoku_screen.sketch(1)


                    if event.key == pygame.K_2 or event.key == pygame.K_KP2:
                        number_to_place = 2
                        sudoku_screen.sketch(2)


                    if event.key == pygame.K_3 or event.key == pygame.K_KP3:
                        number_to_place = 3
                        sudoku_screen.sketch(3)


                    if event.key == pygame.K_4 or event.key == pygame.K_KP4:
                        number_to_place = 4
                        sudoku_screen.sketch(4)


                    if event.key == pygame.K_5 or event.key == pygame.K_KP5:
                        number_to_place = 5
                        sudoku_screen.sketch(5)
                      

                    if event.key == pygame.K_6 or event.key == pygame.K_KP6:
                        number_to_place = 6
                        sudoku_screen.sketch(6)
                    

                    if event.key == pygame.K_7 or event.key == pygame.K_KP7:
                        number_to_place = 7
                        sudoku_screen.sketch(7)                  


                    if event.key == pygame.K_8 or event.key == pygame.K_KP8:
                        number_to_place = 8
                        sudoku_screen.sketch(8)
                     

                    if event.key == pygame.K_9 or event.key == pygame.K_KP9:
                        number_to_place = 9
                        sudoku_screen.sketch(9)

                    if event.key == pygame.K_UP:
                        if x_y_pos[1] == 0: #check if on top row
                            x_y_pos[1] = 8      #if on top row, move to bottom row
                        else:
                            x_y_pos[1] -= 1 #move up one row
                        sudoku_screen.select(x_y_pos[0] , x_y_pos[1])

                        # x_y_pos[1] -= 1
                        # if x_y_pos[1] == -1:
                        #     x_y_pos[1] = 8
                        # else:
                        #     continue

                    if event.key == pygame.K_DOWN:
                        if x_y_pos[1] == 8:     #check if on bottom row
                            x_y_pos[1] = 0          #if on bottom row move to top row
                        else:
                            x_y_pos[1] += 1         #move down one row

                        sudoku_screen.select(x_y_pos[0] , x_y_pos[1])
                        # x_y_pos[1] += 1
                        # if x_y_pos[1] == 9:             # This part here gets error if past bottom row.
                        #     x_y_pos[1] = 0              # this part needs work
                        # else:
                        #     continue

                    if event.key == pygame.K_LEFT:
                        if x_y_pos [0] == 0:        #check if on leftmost column
                            x_y_pos[0] = 8          #if so, move to rightmost column
                        else:
                            x_y_pos[0] -= 1         #move one column to the left
                        sudoku_screen.select(x_y_pos[0] , x_y_pos[1])
                        # x_y_pos[0] -= 1
                        # if x_y_pos[0] == -1:
                        #     x_y_pos[0] = 8
                        # else:
                        #     continue

                    if event.key == pygame.K_RIGHT:
                        if x_y_pos[0] == 8:         #check if on rightmost column
                            x_y_pos[0] = 0          #if on rightmost colum, move to leftmost column
                        else:
                            x_y_pos[0] += 1         #move one column to the right
                        sudoku_screen.select(x_y_pos[0] , x_y_pos[1])
                        # x_y_pos[0] += 1
                        # if x_y_pos[0] == -1:
                        #     x_y_pos[0] = 0
                        # else:
                        #     continue
                       
                    if event.key == pygame.K_DELETE or event.key == pygame.K_BACKSPACE:
                        sudoku_screen.clear()

                    if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                        sudoku_screen.place_number(number_to_place)

                        if sudoku_screen.is_full():       #check if the board is full 

                            if sudoku_screen.check_board():
                                game_on = False
                                game_won = True
                                return game_won_screen(screen)

                            else:
                                game_on = False
                                game_over = True
                                return game_over_screen(screen)

            pygame.display.update()

if __name__ == '__main__':
    main()
    
    
    
