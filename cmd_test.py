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
    game = Ttt_cmd().cmdloop()

if __name__=="__main__":
    main()