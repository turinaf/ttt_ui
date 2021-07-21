import cmd
from random import choice
import oxo_logic, oxo_ui
import argparse as ap
class Oxo_cmd(cmd.Cmd):
    intro = "Enter a command: new, resume, quit. Type 'help' or '?' for help"
    prompt = "(oxo) "
    game = ""

def do_new(self, arg):
    self.game = oxo_logic.newGame()
    oxo_ui.playGame(self.game)
   

def do_resume(self, arg):
    self.game = oxo_logic.newGame()
    oxo_ui.playGame(self.game)

def do_quit(self, arg):
    print("GOodbye...")
    raise SystemExit

def main():
    p = ap.ArgumentParser(description="Play a game of tic-tac-toe")
    grp = ap.add_mutually_exclusive_group()
    grp.add_argument("-r", "--res", "--restore", action='store_true', help="Restore old game")
    args = p.parse_args()
    if args.new:
        oxo_ui.executeChoice(1)
    elif args.res:
        oxo_ui.executeChoice(2)
    else:
        while True:
            choice = oxo_ui.getMenuChoice(oxo_ui.menu)
            oxo_ui.executeChoice(choice)
    # game = Oxo_cmd().cmdloop()

if __name__=="__main__":
    main()