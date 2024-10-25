import tkinter as tk
from sys import exit

class Application:

    def __init__(self, terminal):
        self.root = tk.Tk()
        self.root.title("Враженко Даниил Олегович")
        self.root.geometry("800x600")
        self.root.resizable(False, False)
        self.root.configure(bg="#3e3e3e")
        frame = tk.Frame(self.root)
        frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=(10, 0))
        self.output = tk.Text(frame, wrap=tk.WORD, bg="#2b2b2b", fg="#ffffff", font=("Courier New", 10), state=tk.DISABLED)
        self.output.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.output.tag_configure("input", foreground="#ffffff")
        self.output.tag_configure("command", foreground="#ffffff")
        self.output.tag_configure("error", foreground="#ef5858")
        self.input = tk.Entry(self.root, bg="#2b2b2b", fg="#ffffff", font=("Courier New", 10))
        self.input.pack(fill=tk.X, side=tk.BOTTOM, padx=10, pady=10)
        self.input.bind("<Return>", self.read)
        self.terminal = terminal
        self.terminal.link(self)

    def read(self, event):
        line = self.input.get().strip()
        self.input.delete(0, tk.END)
        if line:
            self.print(' ' + line, "input")
            self.terminal.command_dispatcher(line)
        else:
            self.print("", "input")

    def print(self, text, type):
        color_tag = "input" if type == "input" else "command" if type == "command" else "error"
        self.output.config(state=tk.NORMAL)
        if type == "input":
            self.output.insert(tk.END, f"{self.terminal.username}:~{self.terminal.path}${text}\n", color_tag)
        else:
            self.output.insert(tk.END, f"{text}\n", color_tag)
        self.output.config(state=tk.DISABLED)
        self.output.see(tk.END)

    def run(self):
        self.root.mainloop()

    def exit(self):
        self.root.destroy()
        exit()