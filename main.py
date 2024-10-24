from tkinter import *

class Main:
    def __init__(self):
        self.tela = Tk()
        self.configTela()
        self.framesDeTela()

    def configTela(self):
        self.tela.title("To-Do List")
        self.tela.configure(background='#1e3743')
        self.tela.geometry("400x400")
        self.tela.resizable(False,False)
    # def framesDeTela(self):
    #     self.frame1 = Frame(self.tela,bd=4, bg="#ffffff")
    #     self.frame1.place(relx=0.02,rely=0.02,relwidth=0.96,relheight=0.46)


if __name__ == "__main__":
    main = Main()
    main.tela.mainloop()
        