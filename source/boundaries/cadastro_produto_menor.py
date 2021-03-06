# encoding: utf-8

import tkMessageBox
from Tkinter import *

from source.entities import tratamentos as tr


class TelaMenor():
#Construtor
    def __init__(self):
        self.top = None
        self.OPTIONS = []
        self.cor1 = '#D32F2F'

#Funcao de fechamento da janela
    def CloseWindow(self):
        self.top.destroy()
        self.top.quit()
        self.top = None

#Retorna o valor objeto da janela
    def GetWindow(self):
        return self.top

#Verificacao de tratamento para possiveis erros antes de inserir
    def SendToTR(self, id, nome, valor, tipo, bd):
        try:
            if(not bd.ExistsProduto(id)):
                p1 = tr.ProdutosReceive(id, nome, valor, tipo, bd)
            else:
                raise tr.ErroEntrada(id, "O ID digitado (" + id + ") já existe no atual banco de dados. Escolha outro Id")
        except tr.ErroEntrada as e:
            tkMessageBox.showerror("Erro encontrado", e.message)
        else:
            bd.insertProduto(p1)
        finally:
            self.CloseWindow()

#Criacao da tela
    def FazTela(self,bd):
        if(self.top!=None):
            self.CloseWindow()
            self.FazTela()
        else:
            self.top=Toplevel()
            # opcoes do droplist
            self.OPTIONS = [
                "Tipo de produto",
                "Doce",
                "Salgado",
                "Massa",
                "Bebida",
                "Outro"
                ]
            #fim

            # criacao e posicao dos widgets
            info = Frame(self.top)
            info.grid(sticky=N+S+W+E)

            salto1 = Label(info, text="        ")
            salto1.grid(row=0, column=0)

            id1 = Label(info, text="Id:") #comeco id
            id1['font'] = ['bold']
            id1.grid(row=1, column=1, sticky=W)

            id2 = Entry(info)
            id2["width"] = 40
            id2["font"] = ("Arial", "10")
            id2.grid(row=2, column=1) #fim id

            salto2 = Label(info, text="")
            salto2.grid(row=3, column=2)

            nome1 = Label(info, text="Nome:") #começo nome
            nome1['font']=['bold']
            nome1.grid(row=4, column=1, sticky=W)

            nome2 = Entry(info)
            nome2["width"]=40
            nome2["font"] = ("Arial", "10")
            nome2.grid(row=5, column=1) #fim nome

            salto3 = Label(info, text="")
            salto3.grid(row=6, column=0)

            valor1 = Label(info, text="Valor:") #comeco valor
            valor1['font']=['bold']
            valor1.grid(row=7, column=1, sticky=W)

            valor2 = Entry(info)
            valor2["width"]=40
            valor2["font"] = ("Arial", "10")
            valor2.grid(row=8, column=1) #fim valor

            salto4 = Label(info, text="")
            salto4.grid(row=9, column=0)

            variable = StringVar(info) #começo opcoes
            variable.set(self.OPTIONS[0])

            droplist = apply(OptionMenu, (info, variable) + tuple(self.OPTIONS))
            droplist.grid(row=10, column=1) #fim opcoes

            salto5 = Label(info, text="")
            salto5.grid(row=11, column=0)

            #comeco botao
            pronto = Button(info, text="Pronto", bg=self.cor1, command=lambda: self.SendToTR(id2.get(),nome2.get(),valor2.get(),variable.get(),bd))
            pronto['font']=['bold']
            pronto['fg']='white'
            pronto['padx'] = 1
            pronto['pady'] = 1
            pronto.grid(row=12, column=1) #fim botao

            salto6 = Label(info, text="        ")
            salto6.grid(row=13, column=2)

            # barra de "status"
            status = Label(info, text="Estado: Normal", bg="white", bd=1, relief=SUNKEN, anchor=W)
            status.grid(row= 14, column=0, sticky=S+W+E, columnspan=3)
            #fim

            # formatacao da janela
            self.top.title('Cadastro do Produto')
                #top.iconbitmap(r'c:\Python27\DLLs\icon.ico')
            self.top.resizable(width=False, height=False)
            self.top.protocol("WM_DELETE_WINDOW", lambda:self.CloseWindow())
            self.top.mainloop()
            #fim
