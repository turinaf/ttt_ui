'''
This is the main logic for a tic-tac-toe game.
It simply generates random moves and checks the results of a move for a winning line.'''

import os, random
import ttt_data

def newGame():
    return list(" "*9) # return new list of 9 spaces

def saveGame(game):
    ttt_data.saveGame(game)

def restoreGame():
    try:
        game = ttt_data.restoreGame()
        if len(game) == 9:
            return game
        else:
            return newGame()
    except IOError:
        return newGame()

# _generateMove() function looks for the unused cells in the current game and then randomly selects a cell to place the computer's move.
def _generateMove(game):
    options = [i for i in range(len(game))
    if game[i] == " "] 
    return random.choice(options)

def _isWinningMove(game):
    wins = ((0,1,2), (3,4,5), (6,7,8), 
            (0,3,6), (1,4,7), (2,5,8),
            (0,4,8), (2,4,6))
    for a, b, c in wins:
        chars = game[a]+game[b]+game[c]
        if chars == 'XXX' or chars == 'OOO':
            return True
    return False

def userMove(game, cell):
    if game[cell] != ' ':
        raise ValueError('Invalid cell')
    else:
        game[cell] = 'X'
    if _isWinningMove(game):
        return 'X'
    else:
        return ''

def computerMove(game):
    cell = _generateMove(game)
    if cell == -1:
        return 'D'
    game[cell] = 'O'
    if _isWinningMove(game):
        return 'O'
    else:
        return ''

def test():
    result = ""
    game = newGame()
    while not result:
        print(game)
        try:
            result = userMove(game, _generateMove(game))
        except ValueError:
            print("Ooops, that shouldn't happen")
        if not result:
            result = computerMove(game)
        
        if not result: continue
        elif result == 'D':
            print("It's a draw")
        else:
            print("Winner is : ", result)
        print(game)

if __name__ == "__main__":
    test()