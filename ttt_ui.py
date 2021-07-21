from random import choice
import ttt_logic

menu  = [ "Start new game", 
            "Resume saved game",
            "Display Help",
            "Quit"]
def getMenuChoice(aMenu):
    ''' getMenuChoice(aMenu) -> int
    takes a list of strings as input
    displays as numbered menu and looops until user selects a valid number'''

    if not aMenu:
        raise ValueError('NO MENU CONTECT')

    while True:
        print("\n\n")
        for index, item in enumerate (aMenu, start=1):
            print(index,"\t", item)
        try:
            choice = int(input("\nChoose a menu option: "))
            if 1<= choice <= len(aMenu):
                return choice
            else: print("Choose a number between 1 and ", len(aMenu))
        except ValueError:
             print("Choose the number of a menu option")

def startGame():
    return ttt_logic.newGame()

def resumeGame():
    return ttt_logic.restoreGame()

def displayHelp():
    print('''
    Start new game: starts new game of tic-tac-toe 
    Resume saved game: restores the last saved game and commences play 
    Display help: shows help 
    Quit: quits the application
    '''
    )
def quit():
    print("Goodbye")
    raise SystemExit

def executeChoice(choice):
    '''Execute whichever option the user selected.
    If the choice produces a valid game then play hte game until it completes.'''
    dispatch = [startGame, resumeGame, displayHelp, quit]
    option = dispatch[choice-1]
    game = ""
    if option == dispatch[0]:
        # play game here
        game = startGame()
        playGame(game)
    elif option == dispatch[1]:
        game = resumeGame()
        playGame(game)
    elif option == dispatch[2]:
        displayHelp()
    elif option == dispatch[3]:
        quit()
    else:
        print("Please enter appropriate option")

def printGame(game):
    display = '''
      1 | 2 | 3     {} | {} | {}
     -----------   ------------
      4 | 5 | 6     {} | {} | {}
     -----------   ------------
      7 | 8 | 9     {} | {} | {}
    '''
    print(display.format(*game))

def playGame(game):
    result = ""
    while not result:
        printGame(game)
        choice = input("Cell [1-9 or q to quit]: " )
        if choice.lower()[0] == 'q':
            save = input("Save game before quitting? [y/n]: ")
            if save.lower()[0] == 'y':
                ttt_logic.saveGame(game)
                quit()
            else:
                quit()
        else:
            try:
                cell = int(choice)-1
                if not (0 <= cell <= 8):
                    raise ValueError
            except ValueError:
                print("Choose a number between 1-9 or q to quit: ")
                continue
            try:
                result = ttt_logic.userMove(game, cell)
            except ValueError:
                print("Choose an empty cell")
                continue
            if not result:
                result = ttt_logic.computerMove(game)
            if not result:
                continue
            elif result == 'D':
                printGame(game)
                print("It is a draw")
            else: 
                printGame(game)
                print("Winner is: ", result, "\n")
def main():
    # while True:
    #     choice = getMenuChoice(menu)
    #     executeChoice(choice)
    choice = getMenuChoice(menu)
    executeChoice(choice)
    
    
if __name__=="__main__":
    main()