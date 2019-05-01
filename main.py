from board import Board
from renderer import Renderer

board = Board()
renderer = Renderer(board)
renderer.display_in_console()

quit = False

while not quit:
    try:
        dir = int(input('Enter a number from 1-4 for a direction or a letter for exit: '))
        board.step(dir-1)
        renderer.display_in_console()
    except:
        quit = True