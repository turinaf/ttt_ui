import tkinter as tk

# create the top level window/Frame
top = tk.Tk()
top.title("GUI Demo")
# set geomenty - initial size of the window
top.geometry("600x250")
top.eval('tk::PlaceWindow . center') # placing the window at the center of pc screen
F = tk.Frame(top)
F.pack(fill="both")

# The frame with text entry
fEntry = tk.Frame(F, border=1)
eHello = tk.Entry(fEntry)
eHello.pack(side="left")
lHistory = tk.Label(fEntry, text="   ", foreground="steelblue")
lHistory.pack(side="bottom", fill='x')
fEntry.pack(side='top')

# Create the event handler to clear the text
def evClear():
    lHistory['text'] = eHello.get()
    eHello.delete(0, tk.END)

# Frame with buttons
fButtons = tk.Frame(F, relief="sunken", border=2)
bClear = tk.Button(fButtons, text="Clear Text", command=evClear)
bClear.pack(side="left", padx=5, pady=2)
bQuit = tk.Button(fButtons, text="Quit", command=F.quit)
bQuit.pack(side="left", fill="x")
fButtons.pack(side="bottom", fill='x')

# Running the event loop
F.mainloop()