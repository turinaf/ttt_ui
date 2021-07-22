import tkinter as tk
import tkinter.messagebox as mb
import ttt_logic

top = tk.Tk()
top.title("Tic-tac-toe game") # title of the top-level Window
top.geometry("400x450")
top.eval('tk::PlaceWindow . center') # Places the window at the center of pc screen

def buildMenu(parent):
    menus = (
           ("File", (("New", evNew),
                      ("Resume", evResume), 
                      ("Save", evSave), 
                      ("Exit", evExit))),

            ("Help", (("Help", evHelp), 
                      ("About", evAbout)))
            )
    ''' for menu in menus:
        print(menu, "\n")
        The menu in menus looks like this, nested tuples. we use indexes
        to access corresponding labels and commands.
        
        ('File', (('New', 'evNew'), ('Resume', 'evResume'), ('Save', 'evSave'), ('Exit', 'evExit'))) 

        ('Help', (('Help', 'evHelp'), ('About', 'evAbout'))) '''

    menubar = tk.Menu(parent)
    for menu in menus:
        m = tk.Menu(parent)
        for item in menu[1]:
            m.add_command(label=item[0], command=item[1])
            # print(item[0], "  ", item[1])
        menubar.add_cascade(label=menu[0], menu=m)
    return menubar

# def dummy():
#     mb.showinfo("Dummy", "Event to be done")
# evNew = dummy
# evResume = dummy
# evSave = dummy
# evExit = top.quit
# evHelp = dummy
# evAbout = dummy

def evNew():
    global gameover
    gameover = False
    status['text'] = "PLAYING GAME"
    game2cells(ttt_logic.newGame())

def evResume():
    global gameover
    gameover =False
    status['text'] = "PLAYING GAME"
    game2cells(ttt_logic.restoreGame())

def evSave():
    game = cells2game()
    ttt_logic.saveGame(game)

def evExit():
    if status['text'] == "PLAYING GAME":
        if mb.askyesno("Quitting", "Do you want to save the game before quitting?"):
            evSave()
    top.quit()

def evHelp():
    mb.showinfo("Help", '''
     File->New: starts new game 
     File->Resume: resumes the last saved game
     File->Save: Saves current game.
     File->Exit: Exits the game, prompts to save current active game
     Help->Help: Shows this page
     Help->About: Shows information about the program.
    ''')
def evAbout():
    mb.showinfo("About", "Tic-tac-toe game gui")
gameover = False
def evClick(row, col):
    global gameover
    if gameover:
        mb.showerror("Game over", "Game over!")
        return
    game = cells2game()
    index = (3*row)+col
    result = ttt_logic.userMove(game, index)
    game2cells(game)

    if not result:
        result = ttt_logic.computerMove(game=game)
        game2cells(game)
    if result == 'D':
        mb.showinfo("Result", "It's a draw")
        gameover = True
        status['text'] = "GAME OVER"
    else:
        if result == 'X' or result == 'O':
            mb.showinfo("Result", "The winner is: {}".format(result))
            gameover = True
            status['text'] = "GAME OVER"
    # mb.showinfo("CEll clicked", "row:{}, col:{}".format(row, col))

def game2cells(game):
    table = board.pack_slaves()[0]
    for row in range(3):
        for col in range(3):
            table.grid_slaves(row=row, column=col)[0]['text'] = game[3*row+col]

def cells2game():
    values = []
    table = board.pack_slaves()[0]
    for row in range(3):
        for col in range(3):
            values.append(table.grid_slaves(row=row, column=col)[0]['text'])
    return values
def buildBoard(parent):
    outer = tk.Frame(parent, border=0, relief="sunken", pady='50')
    inner = tk.Frame(outer)
    inner.pack(pady='5', padx='5')

    for row in range(3):
        for col in range(3):
            cell = tk.Button(inner, text=" ", width='5', height='3', command=lambda r=row, c=col: evClick(r, c))
            cell.grid(row=row, column=col)
    return outer

mbar = buildMenu(top)
top['menu'] = mbar

board = buildBoard(top)
board.pack()

status = tk.Label(top, text="PLAYING GAME", border=0, background='blue', foreground='white' , pady='5')
status.pack(anchor='s', fill='x', expand=True)
tk.mainloop()