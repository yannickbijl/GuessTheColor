import tkinter as tk
import libs.NumberInput as NI

class UI:
    def __init__(self, game):
        self.game_window = tk.Frame(game)
        self.title_frame = self.get_title_frame()
        self.true_answer_color_frame = self.get_color_frame()
        self.gameplay_frame = self.get_gameplay_frame()
        self.guess_answer_color_frame = self.get_color_frame()
        self.title_frame.pack(side="top", fill="x", expand=False)
        self.true_answer_color_frame.pack(side="left", fill="both", expand=True)
        self.gameplay_frame.pack(side="left", fill="both", expand=False)
        self.guess_answer_color_frame.pack(side="left", fill="both", expand=True)
        self.game_window.pack(fill="both", expand=True)

    def get_title_frame(self):
        title_frame = tk.Frame(self.game_window, height = 1)
        title = tk.Label(title_frame, text="Guess The Color", font=("Arial", 35))
        title.pack(fill="both", expand=True)
        return title_frame

    def get_color_frame(self):
        color_frame = tk.Frame(self.game_window, height = 5)
        return color_frame

    def get_gameplay_frame(self):
        gameplay_frame = tk.Frame(self.game_window, height = 5)
        guess_frame = self.get_gameplay_guess_frame(gameplay_frame)
        answer_frame = self.get_gameplay_answer_frame(gameplay_frame)
        guess_frame.pack(side="top", fill="both", expand=True)
        answer_frame.pack(side="top", fill="both", expand=True)
        return gameplay_frame

    def get_gameplay_guess_frame(self, main_window):
        gameplay_guess_frame = tk.Frame(main_window)
        top_frame = self.get_guess_frame_top(gameplay_guess_frame)
        mid_frame = self.get_guess_frame_mid(gameplay_guess_frame)
        bot_frame = self.get_guess_frame_bot(gameplay_guess_frame)
        top_frame.pack(side="top", fill="both", expand=False)
        mid_frame.pack(side="top", fill="both", expand=True)
        bot_frame.pack(side="top", fill="both", expand=True)
        return gameplay_guess_frame

    def get_guess_frame_top(self, main_window):
        top_frame = tk.Frame(main_window)
        explain1 = tk.Label(top_frame, text="Guess the Red, Green, and Blue of the color on the left.", font=("Arial", 20))
        explain2 = tk.Label(top_frame, text="Use the button check to view your color on the right.", font=("Arial", 20))
        explain3 = tk.Label(top_frame, text="Use the button guess when you made your decision.", font=("Arial", 20))
        explain1.pack(fill="x", expand=True)
        explain2.pack(fill="x", expand=True)
        explain3.pack(fill="x", expand=True)
        return top_frame

    def get_guess_frame_mid(self, main_window):
        mid_frame = tk.Frame(main_window)
        rgb_label = tk.Label(mid_frame, text="RGB:", font=("Arial", 15))
        self.guess_r = NI.NumberInput(mid_frame)
        self.guess_g = NI.NumberInput(mid_frame)
        self.guess_b = NI.NumberInput(mid_frame)
        rgb_label.pack(side="left", fill="both", expand=True)
        self.guess_r.pack(side="left", fill="x", expand=True)
        self.guess_g.pack(side="left", fill="x", expand=True)
        self.guess_b.pack(side="left", fill="x", expand=True)
        return mid_frame

    def get_guess_frame_bot(self, main_window):
        bot_frame = tk.Frame(main_window,)
        self.guess = tk.Button(bot_frame, text="Guess")
        self.check = tk.Button(bot_frame, text="Check")
        self.guess.pack(side="left", fill="both", expand=True)
        self.check.pack(side="left", fill="both", expand=True)
        return bot_frame

    def get_gameplay_answer_frame(self, main_window):
        gameplay_answer_frame = tk.Frame(main_window)
        top_frame = self.get_answer_frame_top(gameplay_answer_frame)
        mid_frame = self.get_answer_frame_mid(gameplay_answer_frame)
        bot_frame = self.get_answer_frame_bot(gameplay_answer_frame)
        top_frame.pack(side="top", fill="both", expand=False)
        mid_frame.pack(side="top", fill="both", expand=True)
        bot_frame.pack(side="top", fill="both", expand=True)
        return gameplay_answer_frame

    def get_answer_frame_top(self, main_window):
        top_frame = tk.Frame(main_window)
        explain1 = tk.Label(top_frame, text="Total score is sum of individual scores (max = 300)", font=("Arial", 20))
        explain2 = tk.Label(top_frame, text="Each individual score is the percentage of\nhow close the guess is to the true value.", font=("Arial", 20))
        explain1.pack(fill="x", expand=True)
        explain2.pack(fill="x", expand=True)
        return top_frame

    def get_answer_frame_mid(self, main_window):
        mid_frame = tk.Frame(main_window)
        self.result = tk.Label(mid_frame, text="Total Score:", font=("Arial", 15))
        self.score_r = tk.Label(mid_frame, text="Score Red:", font=("Arial", 15))
        self.score_g = tk.Label(mid_frame, text="Score Green:", font=("Arial", 15))
        self.score_b = tk.Label(mid_frame, text="Score Blue:", font=("Arial", 15))
        self.result.pack(side="top", fill="both", expand=True)
        self.score_r.pack(side="top", fill="both", expand=True)
        self.score_g.pack(side="top", fill="both", expand=True)
        self.score_b.pack(side="top", fill="both", expand=True)
        return mid_frame

    def get_answer_frame_bot(self, main_window):
        bot_frame = tk.Frame(main_window,)
        self.quit = tk.Button(bot_frame, text="Quit")
        self.next = tk.Button(bot_frame, text="Next")
        self.quit.pack(side="left", fill="both", expand=True)
        self.next.pack(side="left", fill="both", expand=True)
        return bot_frame
