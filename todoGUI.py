import tkinter as tk
from taskManager import TaskManager
from configs import CORES

class TodoGUI:
    def __init__(self, root, taskManager):  # Recebendo taskManager como argumento
        self.tela = root
        self.taskManager = taskManager
        self.config_tela()
        self.desenharBotoes()
        self.listarTasks()

    def config_tela(self):
        self.tela.title("To-Do List")
        self.tela.configure(background=CORES['bg'])
        self.tela.geometry("400x400")
        self.tela.resizable(False, False)

    def desenharBotoes(self):
        self.entry = tk.Entry(self.tela)
        self.entry.pack(pady=20)

        self.addButton = tk.Button(self.tela, text="Adicionar Task", command=self.adicionarTask)
        self.addButton.pack(pady=10)

        self.tasksListbox = tk.Listbox(self.tela)
        self.tasksListbox.pack(pady=20)

        self.completeButton = tk.Button(self.tela, text="Concluir Task", command=self.completeTask)
        self.completeButton.pack(pady=20)

    def adicionarTask(self):
        descricaoTask = self.entry.get()
        if descricaoTask:
            self.taskManager.addTask(descricaoTask)
            self.entry.delete(0, tk.END)
            self.listarTasks()

    def completeTask(self):
        i = self.tasksListbox.curselection()
        if i:
            t = self.tasksListbox.get(i)
            tID = int(t.split(":")[0])
            print(f"Concluindo tarefa com ID: {tID}")  # Debug: Mostra o ID da tarefa

            self.taskManager.concluirTask(tID, True)

            self.listarTasks()


    def listarTasks(self):
        self.tasksListbox.delete(0, tk.END)
        tasks = self.taskManager.getTasks()
        for task in tasks:
            self.tasksListbox.insert(tk.END, f"{task[0]}: {task[1]} - {'Concluída' if task[2] else 'Pendente'}")
