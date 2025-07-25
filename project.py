


# def main():










from tkinter import ttk
# from tkinter import *
from tkinter import messagebox
import tkinter as tk
import random

# class GuessingGame:
    # def __init__(self, root):
        # self.root = root
        # self.root.title("Guess the Number (0-100)")
# 
        # Generate random number
        # self.secret_number = random.randint(0, 100)
        # self.attempts = 0
# 
        # GUI elements
        # self.label = tk.Label(root, text="I'm thinking of a number between 0 and 100")
        # self.label.pack(pady=10)
# 
        # self.entry = tk.Entry(root, justify="center")
        # self.entry.pack(pady=5)
# 
        # self.feedback_label = tk.Label(root, text="hey", fg="blue")
        # self.feedback_label.pack(pady=5)
# 
        # self.guess_button = tk.Button(root, text="Guess", command=self.check_guess)
        # self.guess_button.pack(pady=5)
# 
        # self.reset_button = tk.Button(root, text="Restart Game", command=self.reset_game)
        # self.reset_button.pack(pady=5)
# 
    # def check_guess(self):
        # guess = self.entry.get().strip()
# 
        # if not guess.isdigit():
            # self.feedback_label.config(text="❌ Please enter a valid number!")
            # return
# 
        # guess = int(guess)
        # self.attempts += 1
# 
        # if guess < self.secret_number:
            # self.feedback_label.config(text="🔽 Too low! Try again.")
        # elif guess > self.secret_number:
            # self.feedback_label.config(text="🔼 Too high! Try again.")
        # else:
            # messagebox.showinfo("🎉 Correct!", f"You guessed it in {self.attempts} attempts!")
            # self.reset_game()
# 
    # def reset_game(self):
        # self.secret_number = random.randint(0, 100)
        # self.attempts = 0
        # self.entry.delete(0, tk.END)
        # self.feedback_label.config(text="✅ New number generated! Guess again.")
# 
# Run the game
# if __name__ == "__main__":
    # root = tk.Tk()
    # game = GuessingGame(root)
    # root.mainloop()


"""

"""


# import tkinter as tk
# from tkinter import messagebox
# import random

class GuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Guess the Number (0-100)")

        # Generate random number
        self.secret_number = random.randint(0, 100)
        self.attempts = 0

        # GUI elements
        self.label = tk.Label(root, text="I'm thinking of a number between 0 and 100")
        self.label.pack(pady=10)

        self.entry = tk.Entry(root, justify="center")
        self.entry.pack(pady=5)
        self.entry.bind("<Return>", lambda event: self.check_guess())  # Enter key submits
        self.entry.bind("<Key>", lambda event: self.clear_feedback()) # typing clears feedback

        self.feedback_label = tk.Label(root, text="", fg="blue")
        self.feedback_label.pack(pady=5)

        self.guess_button = tk.Button(root, text="Guess", command=self.check_guess)
        self.guess_button.pack(pady=5)

        self.reset_button = tk.Button(root, text="Restart Game", command=self.reset_game)
        self.reset_button.pack(pady=5)

    def check_guess(self):
        guess = self.entry.get().strip()

        if not guess.isdigit():
            self.feedback_label.config(text="❌ Please enter a valid number!")
            return

        guess = int(guess)
        self.attempts += 1

        if guess < self.secret_number:
            self.feedback_label.config(text="🔽 Too low! Try again.")
        elif guess > self.secret_number:
            self.feedback_label.config(text="🔼 Too high! Try again.")
        else:
            messagebox.showinfo("🎉 Correct!", f"You guessed it in {self.attempts} attempts!")
            self.reset_game()

    def clear_feedback(self):
        """Clear feedback text when typing a new guess"""
        self.feedback_label.config(text="")

    def reset_game(self):
        self.secret_number = random.randint(0, 100)
        self.attempts = 0
        self.entry.delete(0, tk.END)
        self.feedback_label.config(text="✅ New number generated! Guess again.")

# Run the game
if __name__ == "__main__":
    root = tk.Tk()
    game = GuessingGame(root)
    root.mainloop()



"""

"""


# class FeetToMeters:
# # 
#     def __init__(self, root):
# # 
#         root.title("Feet to Meters")
# # 
#         mainframe = ttk.Frame(root, padding="3 3 12 12")
#         mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
#         root.columnconfigure(0, weight=1)
#         root.rowconfigure(0, weight=1)
#     #    
#         self.feet = StringVar()
#         feet_entry = ttk.Entry(mainframe, width=7, textvariable=self.feet)
#         feet_entry.grid(column=2, row=1, sticky=(W, E))
#         self.meters = StringVar()
# # 
#         ttk.Label(mainframe, textvariable=self.meters).grid(column=2, row=2, sticky=(W, E))
#         ttk.Button(mainframe, text="Calculate", command=self.calculate).grid(column=3, row=3, sticky=W)
# # 
#         ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
#         ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
#         ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)
# # 
#         for child in mainframe.winfo_children(): 
#             child.grid_configure(padx=5, pady=5)
# # 
#         feet_entry.focus()
#         root.bind("<Return>", self.calculate)
#         # 
#     def calculate(self, *args):
#         try:
#             value = float(self.feet.get())
#             self.meters.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
#         except ValueError:
#             pass
# # 
# root = Tk()
# FeetToMeters(root)
# root.mainloop()