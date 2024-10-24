import tkinter as tk
from todoGUI import *
from taskManager import TaskManager 

class Main:
    def __init__(self):
        self.telaPrincipal = tk.Tk()
        self.taskManager = TaskManager()  # Criando uma instância do TaskManager
        self.todoGUI = TodoGUI(self.telaPrincipal, self.taskManager)  # Passando a instância para todoGUI

    def run(self):
        self.telaPrincipal.mainloop()

if __name__ == "__main__":
    main = Main()
    main.run()
