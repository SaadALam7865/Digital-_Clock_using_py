
import tkinter as tk
from time import strftime

root = tk.Tk()  # ✅ Corrected
root.title("Digital Clock")

def time():
    string = strftime('%H:%M:%S %p \n %D')  # ✅ Formatted time and date
    label.config(text=string)  # ✅ Update label
    label.after(1000, time)  # ✅ Update every 1 second

label = tk.Label(root, font=('calibri', 50, 'bold'), background='yellow', foreground='black')
label.pack(anchor='center')

time()  # ✅ Start updating time
root.mainloop()  # ✅ Run the application
