import tkinter as tk
from taskManager import *
from todoGUI import*


class Main:
    def __init__(self):
        self.telaPrincipal = tk.Tk()
        self.taskManager = TaskManager()
        self.todoGUI = todoGUI(self.telaPrincipal,self.taskManager)

    def run(self):
        self.telaPrincipal.mainloop()

if __name__ == "__main__":
    main = Main()
    main.run()
        