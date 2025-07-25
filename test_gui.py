from tkinter import ttk
import tkinter as tk

# root = Tk()
# root.title("Distance Converter")

# mainframe = ttk.Frame(root, padding=20)




# from tkinter import *
# from tkinter import ttk
# 
# class FeetToMeters:

#     def __init__(self, root):

#         root.title("Feet to Meters")

#         mainframe = ttk.Frame(root, padding="3 3 12 12")
#         mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
#         root.columnconfigure(0, weight=1)
#         root.rowconfigure(0, weight=1)
       
#         self.feet = StringVar()
#         feet_entry = ttk.Entry(mainframe, width=7, textvariable=self.feet)
#         feet_entry.grid(column=2, row=1, sticky=(W, E))
#         self.meters = StringVar()

#         ttk.Label(mainframe, textvariable=self.meters).grid(column=2, row=2, sticky=(W, E))
#         ttk.Button(mainframe, text="Calculate", command=self.calculate).grid(column=3, row=3, sticky=W)

#         ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
#         ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
#         ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

#         for child in mainframe.winfo_children(): 
#             child.grid_configure(padx=5, pady=5)

#         feet_entry.focus()
#         root.bind("<Return>", self.calculate)
        
#     def calculate(self, *args):
#         try:
#             value = float(self.feet.get())
#             self.meters.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
#         except ValueError:
#             pass

# root = Tk()
# FeetToMeters(root)
# root.mainloop()






# import requests as re


# response = re.get("https://opentdb.com/api.php?amount=10&category=11&difficulty=easy")
# print(response.json())






class BasicGUI:
    def __init__(self, root) -> None:
        self.root = root
        self.root.geometry("300x200")
        self.root.title("km/h to m/s")
        
        




        self.label = tk.Label(root, text="Enter speed.")
        self.label.pack(padx=10)
# 
        self.num = tk.Entry(root, justify='center')
        self.num.pack(pady=10)
        self.num.bind("<Return>", lambda event: self.convert())
        self.num.bind("<Key>", lambda event: self.clear_text())
# 

        self.feedback = tk.Label(root, text="",fg="blue")
        self.feedback.pack(pady=10)


        self.button = tk.Button(root, text="Calculate", command=self.convert)
        self.button.pack(pady=10)

    def convert(self):
        number = float(self.num.get())
        result = number*3.6**-1
        self.feedback.config(text=f"{result:.3f} m/s")

    def clear_text(self):
        self.feedback.config(text="")
# 
# 
# 
# 
# 
root = tk.Tk()
BasicGUI(root)
root.mainloop()










