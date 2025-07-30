import requests as re 
import random as rd
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox


''' HANGMAN WITH GUI PROTOTYPE '''






class Hangman:
    def __init__(self, root) -> None:
        self.root = root
        self.root.title("Hangman")
        self.root.geometry("300x380")

        self.letters_guessed = []
        self.guesses  = 10
        self.get_word()


        self.header = ttk.Label(root, text="WELCOME TO HANGMAN")
        self.header.pack(padx=10, pady=10)

        self.progress_bar = ttk.Label(root, text=f"I am thinking of a word that is {len(self.secret_word)} long.", foreground="blue")
        self.progress_bar.pack(padx=10, pady=10)


        self.feedback = ttk.Label(root, text="Please guess a letter.")
        self.feedback.pack(padx=25, pady=25)


        self.entry = ttk.Entry(root, justify="center")
        self.entry.pack(padx=10, pady=10)
        self.entry.bind("<Return>", lambda event: self.game_progress())
        self.entry.bind("<Key>", lambda event: self.clear_feed())
        

        self.start = ttk.Button(root, text="Enter", command=self.game_progress)
        self.start.pack(padx=10, pady=10)






    def game_progress(self):
        self.game_logic()
        self.get_progress()
        self.entry.delete(0, tk.END)
         
        if self.has_player_won():
            self.score_calculator()
            messagebox.showinfo("🎉 Correct!",f"your score is {self.score}.")
            self.reset_game()
        elif self.guesses ==0:
            messagebox.showinfo(f"You have ran out of guesses, the sceret word was {self.secret_word}.")                  
            self.reset_game()
     

    def clear_feed(self):
        self.feedback.config(text="")
        
    def game_logic(self):
        letter = self.entry.get().strip().lower()

        if letter == "!":
            letter_revealed = self.reveal_letters()
            self.guesses -= 3
            self.letters_guessed.append(letter_revealed)
        else:
        
            if letter in self.letters_guessed:
                self.feedback.config(text="Letter already guessed")
                return

            if len(letter) > 1:
                self.feedback.config(text="PLease enter a single letter.")
                return

            if len(letter) == 1 and letter.isalpha():
                self.letters_guessed.append(letter)
            else:
                self.feedback.config(
                    text="Oops! That is not a valid letter.",
                    wraplength=150,
                    justify='left'
                    )
                return 
            
            if letter in self.secret_word:
                self.feedback.config(text="✅ Correct.")
            else:
                self.feedback.config(text="❌ Incorrect, try again.")
                self.guesses -= 1
                vowels = "aeiou"
                if letter in vowels:
                    self.guesses -= 1



        self.header.config(text=f"You have {self.guesses} guesses left.")

    def get_word(self):
        words = ["horizon", "candle", "whisper", "marble", "journey", "frost", "ember", "lantern", "grove", "ripple"]
        try:
            response = re.get("https://random-word-api.herokuapp.com/word?number=1")
            response.raise_for_status()
            self.secret_word = response.json()[0]
        except re.RequestException as e:
            self.secret_word = rd.choice(words)
        print(self.secret_word)

    def get_progress(self):
        self.progress = "".join(char if char in self.letters_guessed else "*" for char in self.secret_word)
        self.progress_bar.config(text=self.progress)

    def has_player_won(self):
        return all(char in self.letters_guessed for char in self.secret_word)
 
    def score_calculator(self):
        unique_correct = len(set(char for char in self.letters_guessed if char in self.secret_word))
        self.score = (self.guesses + 4 * unique_correct) + (3 * len(self.secret_word))    

    def reveal_letters(self):
        if self.guesses >= 3:
            self.unrevealed_letters = [char for char in self.secret_word if char not in self.letters_guessed]
            letter = rd.choice(self.unrevealed_letters)
            self.feedback.config(text=f"Letter revealed: {letter}.")
            return letter
        else:
            self.feedback.config(text="Oops! Not enough guesses left")        

    def reset_game(self):
        self.letters_guessed = []
        self.guesses = 10
        self.get_word()
        self.header.config(text="WELCOME TO HANGMAN")
        self.feedback.config(text="Please guess a letter.")
        self.progress_bar.config( text=f"I am thinking of a word that is {len(self.secret_word)} long.", foreground="blue")

        

    






def main():
    root = tk.Tk()
    Hangman(root)
    root.mainloop()



if __name__ == "__main__":
    main()
