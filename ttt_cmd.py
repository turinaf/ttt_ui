import cmd
import ttt_ui, ttt_logic
import argparse as ap
class Ttt_cmd(cmd.Cmd):
    intro = "Enter a command: new, resume, quit. Type 'help' or '?' for help"
    prompt = "(ttt) "
    game = ""

def do_new(self, arg):
    self.game = ttt_logic.newGame()
    ttt_ui.playGame(self.game)
   

def do_resume(self, arg):
    self.game = ttt_logic.restoreGame()
    ttt_ui.playGame(self.game)

def do_quit(self, arg):
    print("GOodbye...")
    raise SystemExit

def main():
    p = ap.ArgumentParser(description="Play a game of tic-tac-toe")
    # grp = ap.add_mutually_exclusive_group()
    p.add_argument("-n", "--new", action='store_true', help="Start new game")
    p.add_argument("-r", "--res", "--restore", action='store_true', help="Restore old game")
    args = p.parse_args()
    if args.new:
        ttt_ui.executeChoice(1)
    elif args.res:
        ttt_ui.executeChoice(2)
    else:
        while True:
            choice = ttt_ui.getMenuChoice(ttt_ui.menu)
            ttt_ui.executeChoice(choice)
    

if __name__=="__main__":
    main()