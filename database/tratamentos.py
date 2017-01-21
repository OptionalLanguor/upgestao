# encoding: utf-8

import database as db
import produto as pr
from datetime import datetime

#Classes criadas para caracterizar os erros do programa

class Erro(Exception):
    def __init__(self, expression='null', message='null'):
        self.expression = expression
        self.message = message

class ErroEntrada(Erro):
   def __init__(self, expression='null', message='null'):
        self.expression = expression
        self.message = message

class ErroIntegridade(Erro):
   def __init__(self, expression='null', message='null'):
       self.expression = expression
       self.message = message

#Tratamento de dados
def ProdutosReceive(id, nome, valor, tipo,bd):
    try:
        VerificaDigit(id)
        VerificaAlpha(nome)
        VerificaComma(valor)
        VerificaTipo(tipo)
    except Erro as e:
        raise e             #Apenas repassando os possiveis erros para o nivel superior
    else:
        nome = TrataStr(nome)
        valor = TrataValor(valor)
        agora = datetime.now().strftime('%H:%M:%S')
        if (tipo == "Doce"): tipo = 1
        if (tipo == "Salgado"): tipo = 2
        if (tipo == "Massa"): tipo = 3
        if (tipo == "Bebida"): tipo = 4
        if (tipo == "Outro"): tipo = 5
        p1 = pr.Produto(id, nome, valor, agora, tipo)
        return p1
#fim

#Recebe um id, faz a consulta no bd cria um objeto com as info do produto.
def ObjetivaProduto(id, bd):
    x = bd.selectProdutoId(id)
    p1 = pr.Produto(x[0],x[1],x[2],x[3],x[4])
    return p1

#Checa se existe um produto com o id
def ProdutosCheck(valor,bd):
    VerificaDigit(valor)
    if (not bd.ExistsProduto(valor)):
        raise ErroIntegridade(valor, "O ID digitado: \"" + str(valor) + "\" nao existe no atual banco de dados. Por favor, digite novamente.")

#Tratamento do valor
def VerificaComma(valor):
    for i in range(len(valor)):
        if (not valor[i].isdigit()):
            if (valor[i] != ","):
                raise ErroEntrada(valor, "O valor deve apresentar apenas números e vírgula(s).")
    return True

#Verifica se a string eh um numero
def VerificaDigit(valor):
    if (valor.isdigit()):
        return True
    else:
        raise ErroEntrada(valor, "O texto deve apenas ser composto por numeros.")

#Verifica se a string tem somente letras
def VerificaAlpha(nome):
    if (nome.isalpha()):
        return True
    else:
        raise ErroEntrada(nome, "O texto deve apenas ser composto por letras.")

#Verifica se o produto eh de uma categoria valida
def VerificaTipo(tipo):
    if (tipo == "Tipo de produto"):
        raise ErroEntrada(tipo, "O produto digitado nao possui uma categoria valida. Por favor, escolha uma categoria.")
    else:
        return True

#Faz o tramento, deixando todas as letras minusculas e colocando a primeira letra maiuscula
def TrataStr(nome):
    nome = nome.lower()
    nome = nome.capitalize()
    return nome

#Faz um tratamento do valor
def TrataValor(valor):
    if (valor.isdigit()):
        valor = valor + ",00"
    return valor

