import tkinter as tk

class NumberInput(tk.Entry):
    def __init__(self, master=None, **kwargs):
        self.var = tk.StringVar()
        tk.Entry.__init__(self, master, textvariable=self.var, **kwargs)
        self.old_value = ''
        self.var.trace('w', self.check)
        self.get, self.set = self.var.get, self.var.set

    def check(self, *args):
        if self.get().isdigit():
            # the current value is only digits and withing range; allow this
            if int(self.get()) >= 0 and int(self.get()) <= 255:
                self.old_value = self.get()
            else:
                # the current value is out of range; reject this
                self.set(self.old_value)
        else:
            # there's non-digit characters in the input; reject this
            self.set(self.old_value)
