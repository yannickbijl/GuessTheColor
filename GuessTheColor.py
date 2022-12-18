from random import randint
import tkinter as tk

import libs.UI as UI


class GuessTheColor():
    def __init__(self):
        self.game = tk.Tk()
        self.game.attributes("-fullscreen", True)
        self.ui = UI.UI(self.game)
        self.set_bindings()
        self.setup_game()

    def set_bindings(self):
        self.game.bind("<Escape>", self.end_program)
        self.ui.quit.bind("<Button-1>", self.end_program)
        self.ui.next.bind("<Button-1>", self.setup_game)
        self.ui.check.bind("<Button-1>", self.check_rgb_color)
        self.ui.guess.bind("<Button-1>", self.guess_rgb_color)

    def end_program(self, event=None):
        self.game.quit()

    def setup_game(self, event=None):
        self.ui.result['text'] = "Total Score:"
        self.ui.score_r['text'] = "Score Red:"
        self.ui.score_g['text'] = "Score Green:"
        self.ui.score_b['text'] = "Score Blue:"
        self.set_answer_colors()
        self.ui.true_answer_color_frame['background'] = self.answer_hex
        self.ui.guess_answer_color_frame['background'] = '#f0f0ee'

    def check_rgb_color(self, event=None):
        self.get_guess_colors()
        guess_hex = self.get_hex_value(self.guess_r, self.guess_g, self.guess_b)
        self.ui.guess_answer_color_frame['background'] = guess_hex

    def guess_rgb_color(self, event=None):
        self.get_guess_colors()
        percentage_r = self.get_percentage(self.guess_r, self.answer_r)
        percentage_g = self.get_percentage(self.guess_g, self.answer_g)
        percentage_b = self.get_percentage(self.guess_b, self.answer_b)
        self.ui.result['text'] = f"Total Score: {sum((percentage_r, percentage_b, percentage_g))}"
        self.ui.score_r['text'] = f"Score Red: {percentage_r}"
        self.ui.score_g['text'] = f"Score Green: {percentage_g}"
        self.ui.score_b['text'] = f"Score Blue: {percentage_b}"

    def get_guess_colors(self):
        self.guess_r = int(self.ui.guess_r.get())
        self.guess_g = int(self.ui.guess_g.get())
        self.guess_b = int(self.ui.guess_b.get())

    def set_answer_colors(self):
        self.answer_r = randint(0, 255)
        self.answer_g = randint(0, 255)
        self.answer_b = randint(0, 255)
        self.answer_hex = self.get_hex_value(self.answer_r, self.answer_g, self.answer_b)

    def get_hex_value(self, r, g, b):
        return "#%02x%02x%02x" % (r, g, b)

    def get_percentage(self, guess, answer):
        return 100 - abs((guess/255 * 100) - (answer/255 * 100))


if __name__ == '__main__':
    app = GuessTheColor()
    app.game.mainloop()
