# encoding: utf-8

from Tkinter import *
from database import database as db
from database import tratamentos as tr
import tkMessageBox

class TelaMenorDel():
#Construtor
    def __init__(self):
        self.top = None
        self.cor1 = '#D32F2F'

#Fechamento da janela
    def CloseWindow(self):
        self.top.destroy()
        self.top.quit()
        self.top = None

#Janela de verificacao para a confirmacao da delecao
    def JanelaPequena(self,id,bd):
        x = bd.selectProdNameId(id)
        if tkMessageBox.askokcancel("Deletar", "Deseja mesmo deletar " + str(x) + "?"):
            bd.deleteProduto(id)

#Retorna o objeto da janela
    def GetWindow(self):
        return self.top

#Funcao que manda para tratamento para a verificacao de erros
    def SendToTR(self,id,bd):
        try:
            tr.ProdutosCheck(id,bd)
        except Exception as e:
           tkMessageBox.showerror("Erro encontrado", e.message)
        else:
            self.JanelaPequena(id,bd)
        finally:
           self.CloseWindow()

#Criacao da tela
    def FazTela(self,bd):
        if(self.top!=None):
            self.CloseWindow()
            self.FazTela()
        else:
            self.top=Toplevel()
            # criacao e posicao dos widgets
            info = Frame(self.top)
            info.grid(sticky=N+S+W+E)

            salto1 = Label(info, text="          ")
            salto1.grid(row=0, column=0)

            nome1 = Label(info, text="Id:") #comeco id
            nome1['font']=['bold']
            nome1.grid(row=1, column=1, sticky=W)

            nome2 = Entry(info)
            nome2["width"]=40
            nome2["font"] = ("Arial", "10")
            nome2.grid(row=2, column=1) #fim id

            salto2 = Label(info, text="")
            salto2.grid(row=3, column=0)

            #comeco pronto
            pronto = Button(info, text="Pronto", bg=self.cor1,command=lambda: self.SendToTR(nome2.get(),bd))
            pronto['font']=['bold']
            pronto['fg']='white'
            pronto['padx'] = 1
            pronto['pady'] = 1
            pronto.grid(row=4, column=1) #fim pronto

            salto3 = Label(info, text="          ")
            salto3.grid(row=5, column=2)
            #fim

            # barra de "status"
            status = Label(info, text="Estado: Normal", bg="white", bd=1, relief=SUNKEN, anchor=W)
            status.grid(row=6, column=0, sticky=S+W+E, columnspan=3)
            #fim

            # formatacao da janela
            self.top.title('Excluir Produto')
                #top.iconbitmap(r'c:\Python27\DLLs\icon.ico')
            self.top.resizable(width=False, height=False)
            self.top.protocol("WM_DELETE_WINDOW", lambda:self.CloseWindow())
            self.top.mainloop()
            #fim
