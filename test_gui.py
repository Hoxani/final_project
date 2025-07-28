import requests as re 
import random as rd
from tkinter import ttk
import tkinter as tk

# # root = Tk()
# # root.title("Distance Converter")

# # mainframe = ttk.Frame(root, padding=20)




# # from tkinter import *
# # from tkinter import ttk
# # 
# # class FeetToMeters:

# #     def __init__(self, root):

# #         root.title("Feet to Meters")

# #         mainframe = ttk.Frame(root, padding="3 3 12 12")
# #         mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
# #         root.columnconfigure(0, weight=1)
# #         root.rowconfigure(0, weight=1)
       
# #         self.feet = StringVar()
# #         feet_entry = ttk.Entry(mainframe, width=7, textvariable=self.feet)
# #         feet_entry.grid(column=2, row=1, sticky=(W, E))
# #         self.meters = StringVar()

# #         ttk.Label(mainframe, textvariable=self.meters).grid(column=2, row=2, sticky=(W, E))
# #         ttk.Button(mainframe, text="Calculate", command=self.calculate).grid(column=3, row=3, sticky=W)

# #         ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
# #         ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
# #         ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

# #         for child in mainframe.winfo_children(): 
# #             child.grid_configure(padx=5, pady=5)

# #         feet_entry.focus()
# #         root.bind("<Return>", self.calculate)
        
# #     def calculate(self, *args):
# #         try:
# #             value = float(self.feet.get())
# #             self.meters.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
# #         except ValueError:
# #             pass

# # root = Tk()
# # FeetToMeters(root)
# # root.mainloop()






# # import requests as re


# # response = re.get("https://opentdb.com/api.php?amount=10&category=11&difficulty=easy")
# # print(response.json())






# # class BasicGUI:
# #     def __init__(self, root) -> None:
# #         self.root = root
# #         self.root.geometry("300x200")
# #         self.root.title("km/h to m/s")
        
        




# #         self.label = tk.Label(root, text="Enter speed.")
# #         self.label.pack(padx=10)
# # # 
# #         self.num = tk.Entry(root, justify='center')
# #         self.num.pack(pady=10)
# #         self.num.bind("<Return>", lambda event: self.convert())
# #         self.num.bind("<Key>", lambda event: self.clear_text())
# # # 

# #         self.feedback = tk.Label(root, text="",fg="blue")
# #         self.feedback.pack(pady=10)


# #         self.button = tk.Button(root, text="Calculate", command=self.convert)
# #         self.button.pack(pady=10)

# #     def convert(self):
# #         number = float(self.num.get())
# #         result = number*3.6**-1
# #         self.feedback.config(text=f"{result:.3f} m/s")

# #     def clear_text(self):
# #         self.feedback.config(text="")
# # # 
# # # 
# # # 
# # # 
# # # 
# # root = tk.Tk()
# # BasicGUI(root)
# # root.mainloop()


# # https://random-word-api.herokuapp.com/word?number=1



# # get("https://random-word-api.herokuapp.com/word?number=1")



# ''' HANGMAN WITH GUI PROTOTYPE '''






class Hangman:
    def __init__(self, root) -> None:
        self.root = root
        self.root.title("Hangman")
        self.root.geometry("300x380")

        self.start_game_wrapper()



        self.letters_guessed = []
        self.attempts  = 10


        self.header = ttk.Label(root, text="WELCOME TO HANGMAN")
        self.header.pack(padx=10, pady=10)

        self.progress_bar = ttk.Label(root, text="", foreground="blue")
        self.progress_bar.pack(padx=10, pady=10)


        self.feedback = ttk.Label(root, text=f"Guess  a letter for the secret word, the word is {len(self.secret_word)} letters long.")
        self.feedback.pack(padx=25, pady=25)


        self.entry = ttk.Entry(root, justify="center")
        self.entry.pack(padx=10, pady=10)
        self.entry.bind("<Return>", lambda event: self.game_progress())
        

        self.start = ttk.Button(root, text="Enter", command=self.game_progress)
        self.start.pack(padx=10, pady=10)










    def start_game_wrapper(self):
        self.get_word()


    def game_progress(self):
        self.letter_guess()
        self.get_progress()
        self.entry.delete(0, tk.END)
        self.feedback.config(text="")
        # self.check_guess()
        # self.reveal_letters()





 
  
    def letter_guess(self):
        letter = self.entry.get().strip().lower()

        if letter == "!":
            self.reveal_letters()
            return

        if letter in self.letters_guessed:
            self.feedback.config(text="Letter already guessed")
            return
            
        if len(letter) > 1:
            self.feedback.config(text="PLease enter a single letter.")
            return
        
        if len(letter) == 1 and letter.isalpha():
            self.letters_guessed.append(letter)
            self.feedback.config(text="".join(self.letters_guessed))
        else:
            self.feedback.config(text="Invalid input")

    def get_word(self):
        words = ["horizon", "candle", "whisper", "marble", "journey", "frost", "ember", "lantern", "grove", "ripple"]
        try:
            response = re.get("https://random-word-api.herokuapp.com/word?number=1")
            response.raise_for_status()
            self.secret_word = response.json()[0]
        except re.RequestException as e:
            self.secret_word = rd.choice(words)

    def get_progress(self):
        self.progress = "".join(char if char in self.letters_guessed else "*" for char in self.secret_word)
        self.progress_bar.config(text=self.progress)
  
    def check_guess(self):
        pass


    def reveal_letters(self):
        pass
        

        

    







root = tk.Tk()
Hangman(root)
root.mainloop()
