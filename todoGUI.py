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
        self.tela.geometry("600x600")
        self.tela.resizable(False, False)

    def desenharBotoes(self):
        # Criar um frame para os botões
        bFrame = tk.Frame(self.tela)
        bFrame.pack(pady=10, padx=10, fill=tk.X)  # Adiciona o frame à tela

        # Botão para adicionar a tarefa
        self.addButton = tk.Button(bFrame, text="Adicionar Task", command=self.adicionarTask)
        self.addButton.pack(side=tk.LEFT, padx=5)  # Adiciona o botão à esquerda do frame

        # Botão para concluir a tarefa
        self.completeButton = tk.Button(bFrame, text="Concluir Task", command=self.completeTask)
        self.completeButton.pack(side=tk.LEFT, padx=5)  # Adiciona o botão à esquerda do frame

        self.delButton = tk.Button(bFrame, text="Deletar Task", command=self.deleteTask)
        self.delButton.pack(side=tk.LEFT, padx=5)

        self.entry = tk.Entry(self.tela)
        self.entry.pack(pady=10, padx=10, fill=tk.X)
        self.entry.insert(0, "Digite a nova tarefa...")  # Texto de placeholder
        self.entry.bind("<FocusIn>", self.limparPlaceholder)
        self.entry.bind("<FocusOut>", self.addPlaceholder)

        # Lista de tarefas
        self.tasksListbox = tk.Listbox(self.tela)
        self.tasksListbox.pack(pady=20, padx=10, fill=tk.BOTH, expand=True)  # Centraliza a Listbox


    def limparPlaceholder(self, event):
        if self.entry.get() == "Digite a nova tarefa...":
            self.entry.delete(0, tk.END)

    def addPlaceholder(self, event):
        if not self.entry.get():
            self.entry.insert(0, "Digite a nova tarefa...")

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

            self.taskManager.concluirTask(tID,True)

            self.listarTasks()

    def deleteTask(self):
        i = self.tasksListbox.curselection()
        if i:
            t = self.tasksListbox.get(i)
            tID = int(t.split(":")[0])
            print(f"Concluindo tarefa com ID: {tID}")  # Debug: Mostra o ID da tarefa

            self.taskManager.deleteTask(tID)

            self.listarTasks()

    def listarTasks(self):
        self.tasksListbox.delete(0, tk.END)
        tasks = self.taskManager.getTasks()
        for task in tasks:
            self.tasksListbox.insert(tk.END, f"{task[0]}: {task[1]} - {'Concluída' if task[2] else 'Pendente'}")
