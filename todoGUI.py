import tkinter as tk
from taskManager import *

class todoGUI:

    def __init__(self,root,taskManager):
        self.tela = root
        self.taskManager = taskManager
        self.configTela()
        todoGUI.desenharBotao(self)

    def configTela(self):
        self.tela.title("To-Do List")
        self.tela.configure(background='#1e3743')
        self.tela.geometry("400x400")
        self.tela.resizable(False,False)


    def desenharBotao(self):
        b = tk.Button(self.tela, text="Clique aqui!", command=TaskManager.clicado)
        b.pack(pady=20)