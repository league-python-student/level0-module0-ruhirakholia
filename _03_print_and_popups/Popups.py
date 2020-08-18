from tkinter import messagebox, simpledialog, Tk

window = Tk()
window.withdraw()

input = simpledialog.askstring("Title goes here", "Enter your name")
messagebox.showinfo("Super Tetris", input)
messagebox.showinfo("Title", "Hi!")



window.mainloop()