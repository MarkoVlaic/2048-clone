class Renderer:
    def __init__(self, board):
        self.board = board

    def display_in_console(self):
        for row in self.board.mat:
            print(' '.join(list(map(lambda x:str(x), row))))
        print('-'*10)