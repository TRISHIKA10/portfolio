import tkinter as tk 
from time import strftime

root = tk.Tk()
root.title("Digital Clock")
# root.geometry("1000x1000")

def time():
    string = strftime('%H:%M:%S %p \n %D')
    label.config(text=string)
    label.after(1000,time)

label = tk.Label(root, font=('Helveita', 50, 'bold'),background='#32174d',foreground='#fc0fc0')    
label.pack(anchor='center')


time()

root.mainloop()