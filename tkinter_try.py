import tkinter 
import tkinter.messagebox as mb
tk = tkinter.Tk()
tk.withdraw() # hide the blank window behind the message box
mb.showinfo("Title", "The message goes here")

print(dir(mb))

mb.showerror("Error", "What error?")
mb.showwarning("Tile", "The warning...")
mb.askyesno("Title", "You really want to do this?")
mb.askokcancel("Prompt", "Proceed..?")
mb.askquestion("Title", "What question?")
mb.askretrycancel("Title", "Try again?")
mb.askyesnocancel("Title", "Yes, no, or cancel?")