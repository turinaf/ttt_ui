import os.path
game_file = ".tttgame.dat"

def _getPath():
    '''getPath() -> string
    returns a valid path for data file.. Tries to use the users home folder
    defualt cwd'''

    try:
        game_path = os.environ['HOMEPATH'] or os.environ['HOME']
        if not os.path.exists(game_path):
            game_path = os.getcwd()
    except (KeyError, TypeError):
        game_path = os.getcwd()
    
    return game_path

def saveGame(game):
    '''saveGame(game) -> None
    saves a game object in the data file in the users home folder. no checking is done on the input'''
    path = os.path.join(_getPath(), game_file)
    with open(path, 'w') as gf:
        gamestr = ''.join(game)
        gf.write(gamestr)

def restoreGame():
    '''restoreGame() -> game
    Restores a game from the data file. The game object is a list of characters'''
    path = os.path.join(_getPath(), game_file)
    with open(path) as gf:
        gamestr = gf.read()
        return list(gamestr)

def test():
    print("Path = ", _getPath())
    saveGame(list("XO XO OX"))
    print(restoreGame())

if __name__== "__main__": test()