import tkinter

class Renderer:
    def __init__(self, board):
        self.board = board
        self.board_widgets = []

        
        self.init_window()
        self.init_grid()
        self.display_board()

        self.window.mainloop()
        

    def init_window(self):
        self.window = tkinter.Tk()
        self.window.title('2048')

        self.WIDTH = 640
        self.HEIGHT = 480

        self.window.geometry('{}x{}'.format(self.WIDTH, self.HEIGHT))

        self.window.bind('<KeyPress>', self.handle_input)
    
    def init_grid(self):
        for row in range(3):
            self.window.rowconfigure(row, weight=1)
            self.window.columnconfigure(row, weight=1)

    def display_board(self):
        #self.window.grid
        self.clear_board()
        for row in range(3):
            for col in range(3):
                value = self.board.mat[row][col]
                if not value:
                    value = ''
                #[width, height] = list(map(lambda x: int(x)//3, self.window.geometry().split('x')))
                w = int(0.5*self.WIDTH//3)
                h = int(0.5*self.HEIGHT//3)
                tkinter.Label(self.window, text=str(value), bd=5, width=w, height=h, bg='white', font=("Courier", 40), borderwidth=2, relief="solid").grid(row=row, column=col)
                #self.board_widgets.append(label)

    def clear_board(self):
        for label in self.window.grid_slaves():
            label.grid_forget()

    def handle_input(self, e):
        print(e.keycode)
        if e.keycode == 111:
            self.board.step(0)
        elif e.keycode == 116:
            self.board.step(1)
        elif e.keycode == 113:
            self.board.step(2)
        elif e.keycode == 114:
            self.board.step(3)
        else:
            return

        self.display_board()
        self.display_in_console()
    def display_in_console(self):
        '''
        template = '{0:4} {0:4} {0:4}'

        for row in self.board.mat:
            print(template.format(*row))
        '''

        for row in self.board.mat:
            print(' '.join(list(map(lambda x:str(x), row))))
        print('-'*10)

'''
for row in self.board.mat:
            print(' '.join(list(map(lambda x:str(x), row))))
        print('-'*10)
'''