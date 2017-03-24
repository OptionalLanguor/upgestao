# encoding: utf-8

import sqlite3

class Database(object):
    dbConnect = None
    dbCursor = None

    def __init__(self,loc):
        if(loc==1):
            self.dbConnect = sqlite3.connect('GutsDados.db')
        else:
            self.dbConnect = sqlite3.connect('source/GutsDados.db')
        self.dbCursor = self.dbConnect.cursor()

        self.tables = [
            '''CREATE TABLE Categoria (
            id INTEGER PRIMARY KEY NOT NULL,
            nome varchar(500) NOT NULL,
            data_insert varchar(100) NOT NULL
        );''',
            '''CREATE TABLE Produto (
            id INTEGER PRIMARY KEY NOT NULL,
            nome varchar(500) NOT NULL,
            valor_inic varchar(100) NOT NULL,
            data_insert varchar(100) NOT NULL,
            id_categoria INTEGER NOT NULL,
            FOREIGN KEY (id_categoria) REFERENCES Categoria(id)
       );''',
            '''CREATE TABLE Cliente (
            id INTEGER PRIMARY KEY NOT NULL,
            nome_cliente varchar(500),
            data_insert varchar(100) NOT NULL,
            tem_endereco varchar(1) NOT NULL,
            tem_telefone varchar(1) NOT NULL,
            tem_email varchar(1) NOT NULL
        );''',
            '''CREATE TABLE Endereco (
            id INTEGER PRIMARY KEY NOT NULL,
            nome_endereco varchar(500) NOT NULL,
            id_cliente INTEGER NOT NULL,
            FOREIGN KEY (id_cliente) REFERENCES Cliente(id)
        );''',
            '''CREATE TABLE Telefone (
            id INTEGER PRIMARY KEY NOT NULL,
            numero varchar(500) NOT NULL,
            id_cliente INTEGER NOT NULL,
            FOREIGN KEY (id_cliente) REFERENCES Cliente(id)
        );''',
            '''CREATE TABLE Email (
            id INTEGER PRIMARY KEY NOT NULL,
            email varchar(500) NOT NULL,
            id_cliente INTEGER NOT NULL,
            FOREIGN KEY (id_cliente) REFERENCES Cliente(id)
        );''',
            '''CREATE TABLE Venda (
            id INTEGER PRIMARY KEY NOT NULL,
            id_cliente INTEGER NOT NULL,
            nome_contato varchar(500),
            tipo_festa varchar(500),
            num_pessoas varchar(500),
            endereco_nome varchar(500),
            data_evento varchar(100),
            data_insert varchar(100) NOT NULL,
            custo_local varchar(100) NOT NULL,
            custo_diversos varchar(100) NOT NULL,
            subtrair varchar(100) NOT NULL,
            valor_total varchar(100) NOT NULL
            FOREIGN KEY (id_cliente) REFERENCES Cliente(id)
        );''',
            '''CREATE TABLE Prod_Vendido (
            id INTEGER PRIMARY KEY NOT NULL,
            nome varchar(500) NOT NULL,
            valor varchar(100) NOT NULL,
            id_venda INTEGER NOT NULL,
            nome_categoria varchar(500) NOT NULL,
            FOREIGN KEY (id_venda) REFERENCES Venda(id)
        );''',
            '''CREATE TABLE ModeloPacote (
            id INTEGER PRIMARY KEY NOT NULL,
            nome varchar(500) NOT NULL,
            data_insert varchar(100) NOT NULL,
            data_modif varchar(100) NOT NULL,
            FOREIGN KEY (id_venda) REFERENCES Venda(id)
        );'''
        ]

        #Para verificar se o banco já possui suas create tables
        self.dbCursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Categoria';")
        categoriaExistence = self.dbCursor.fetchall()

        self.dbCursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Produto';")
        produtoExistence = self.dbCursor.fetchall()

        self.dbCursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Cliente';")
        clienteExistence = self.dbCursor.fetchall()

        self.dbCursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Endereco';")
        enderecoExistence = self.dbCursor.fetchall()

        self.dbCursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Telefone';")
        telefoneExistence = self.dbCursor.fetchall()

        self.dbCursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Email';")
        emailExistence = self.dbCursor.fetchall()

        self.dbCursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Venda';")
        vendaExistence = self.dbCursor.fetchall()

        self.dbCursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Prod_Vendido';")
        prodVendExistence = self.dbCursor.fetchall()

        if(not categoriaExistence):
            self.dbCursor.execute(self.tables[0])
        if(not produtoExistence):
            self.dbCursor.execute(self.tables[1])
        if(not clienteExistence):
            self.dbCursor.execute(self.tables[2])
        if(not enderecoExistence):
            self.dbCursor.execute(self.tables[3])
        if (not telefoneExistence):
            self.dbCursor.execute(self.tables[4])
        if (not emailExistence):
            self.dbCursor.execute(self.tables[5])
        if(not vendaExistence):
            self.dbCursor.execute(self.tables[6])
        if(not prodVendExistence):
            self.dbCursor.execute(self.tables[7])

#Seleciona todas as categorias
    def selectCategoria(self):
        self.dbCursor.execute('SELECT * FROM Categoria ORDER BY id')
        aux = self.dbCursor.fetchall()
        return aux

# Seleciona todos os produtos
    def selectProduto(self):
        self.dbCursor.execute('SELECT * FROM Produto ORDER BY id')
        aux = self.dbCursor.fetchall()
        return aux

#Seleciona todos os clientes
    def selectCliente(self):
        self.dbCursor.execute('SELECT * FROM Cliente ORDER BY id')
        aux = self.dbCursor.fetchall()
        return aux

#Seleciona todos os enderecos
    def selectEndereco(self):
        self.dbCursor.execute('SELECT * FROM Endereco ORDER BY id')
        aux = self.dbCursor.fetchall()
        return aux

# Seleciona todos os telefones
    def selectTelefone(self):
        self.dbCursor.execute('SELECT * FROM Telefone ORDER BY id')
        aux = self.dbCursor.fetchall()
        return aux

# Seleciona todos os emails
    def selectEmail(self):
        self.dbCursor.execute('SELECT * FROM Email ORDER BY id')
        aux = self.dbCursor.fetchall()
        return aux

#Seleciona todas as vendas
    def selectVenda(self):
        self.dbCursor.execute('SELECT * FROM Venda ORDER BY id')
        aux = self.dbCursor.fetchall()
        return aux

#Seleciona todos os produtos vendidos
    def selectProdVendido(self):
        self.dbCursor.execute('SELECT * FROM Prod_Vendido ORDER BY id')
        aux = self.dbCursor.fetchall()
        return aux


#Insere o produto recebendo um objeto produto
    def insertProduto(self, prod):
        values = [prod.getId(), prod.getNome(), prod.getValor_inic(),
                  prod.getData_insert(), prod.getForeign_key()]

        self.dbCursor.execute( 'INSERT INTO Produto VALUES (?, ?, ?, ?, ?)', values)
        self.dbConnect.commit()

#Insere categoria recebendo um objeto
    def insertCategoria(self, categ):
        values = [categ.getId(), categ.getNome(), categ.getData_insert()]
        self.dbCursor.execute('INSERT INTO Categoria VALUES (?, ?, ?)', values)
        self.dbConnect.commit()

#Seleciona todos os produtos da categoria doces
    def selectProdutoDoces(self):
        self.dbCursor.execute('Select * FROM Produto WHERE Id_Categoria = 1')
        return self.dbCursor.fetchall()

#Seleciona todos os produtos da categoria salgados
    def selectProdutoSalgados(self):
        self.dbCursor.execute('Select * FROM Produto WHERE Id_Categoria = 2')
        return self.dbCursor.fetchall()

#Seleciona todos os produtos da categoria massas
    def selectProdutoMassas(self):
        self.dbCursor.execute('Select * FROM Produto WHERE Id_Categoria = 3')
        return self.dbCursor.fetchall()

#Seleciona todos os produtos da categoria bebidas
    def selectProdutoBebidas(self):
        self.dbCursor.execute('Select * FROM Produto WHERE Id_Categoria = 4')
        return self.dbCursor.fetchall()

#Seleciona todos os produtos da categoria outros
    def selectProdutoOutros(self):
        self.dbCursor.execute('Select * FROM Produto WHERE Id_Categoria = 5')
        return self.dbCursor.fetchall()

#Conta quantos produtos tem
    def ContadorProduto(self):
        self.dbCursor.execute('SELECT * FROM Produto ORDER BY id')
        x = self.dbCursor.fetchall()
        return int((len(x)+1))

#Seleciona um produto especifico pelo seu id
    def selectProdutoId(self, id):
        value = [id]
        self.dbCursor.execute('SELECT * FROM Produto WHERE id = ?', value)
        return self.dbCursor.fetchone()

    def selectProdutoIdAll(self, id):
        value = [id]
        self.dbCursor.execute('SELECT * FROM Produto WHERE id = ?', value)
        return self.dbCursor.fetchall()

#Pega o id de todos os produtos
    def selectProdutoOnlyId(self):
        self.dbCursor.execute('SELECT id FROM Produto ORDER BY id')
        return self.dbCursor.fetchall()

#Pega somente o nome de um produto especifico
    def selectProdNameId(self,id):
        value = [id]
        self.dbCursor.execute('SELECT nome FROM Produto WHERE id = ?', value)
        x = self.dbCursor.fetchone()
        return x[0]

#Verifica se o produto existe pelo seu id
    def ExistsProduto(self,id):
        value = [id]
        self.dbCursor.execute('SELECT id FROM Produto WHERE id = ?', value)
        data = self.dbCursor.fetchall()
        if len(data) == 0:
            return False
        else:
            return True

#Deleta o produto dado seu id
    def deleteProduto(self, id):
        value = [id]
        self.dbCursor.execute('DELETE FROM Produto WHERE id = ?', value)
        self.dbConnect.commit()

#Deleta a categoria dado seu id         O CERTO É VERIFICAR SE ALGUM PRODUTO ESTÁ ATRELADA A CATEGORIA!!!!
    def deleteCategoria(self, id):
        value = [id]
        self.dbCursor.execute('DELETE FROM Categoria WHERE id = ?', value)
        self.dbConnect.commit()

#Fecha a ligacao com o banco de dados
    def close(self):
        self.dbCursor.close()


#Funções de salvar e ler códigos de backup em sql

    # Método que salva os dados atuais do sistema em um arquivo com código SQL
    def exportSQL(self, fileName='dados.sql'):

        buffer = ''

        # Insert Categoria
        dadosCategoria = self.selectCategoria()
        sizeCategoria = len(dadosCategoria)
        for i in range(0, sizeCategoria):
            buffer = buffer + 'INSERT INTO Categoria VALUES ((' + str(dadosCategoria[i][0]) + '), (\'' \
                    + dadosCategoria[i][1] + '\'), (' + str(dadosCategoria[i][2]) + '));' + '\n'

        # Insert Produto
        dadosProduto = self.selectProduto()
        sizeProduto = len(dadosProduto)
        for i in range(0, sizeProduto):
            buffer = buffer + 'INSERT INTO Produto VALUES ((' + str(dadosProduto[i][0]) + '), ' \
                    + '(\'' + dadosProduto[i][1] + '\'), (\'' + str(dadosProduto[i][2]) +'\'), (\'' \
                    + str(dadosProduto[i][3]) + '\'), (' + str(dadosProduto[i][4]) + '));' + '\n'

        # Insert Cliente
        dadosCliente = self.selectCliente()
        sizeCliente = len(dadosCliente)
        for i in range(0, sizeCliente):
            buffer = buffer + 'INSERT INTO Cliente VALUES ((' + str(dadosCliente[i][0]) + '), (\'' \
                    + dadosCliente[i][1] + '\'), (\'' + str(dadosCliente[i][2]) + '\'), (\'' \
                    + dadosCliente[i][3] + '\'), (\'' + dadosCliente[i][4] + '\'), (\'' \
                    + dadosCliente[i][5] + '\'));' + '\n'

        # Insert Endereco
        dadosEndereco = self.selectEndereco()
        sizeEndereco = len(dadosEndereco)
        for i in range(0, sizeEndereco):
            buffer = buffer + 'INSERT INTO Endereco VALUES ((' + str(dadosEndereco[i][0]) + '), (\'' \
                    + dadosEndereco[i][1] + '\'), (' + str(dadosEndereco[i][2]) + '));' + '\n'

        # Insert Telefone
        dadosTelefone = self.selectTelefone()
        sizeTelefone = len(dadosTelefone)
        for i in range(0, sizeTelefone):
            buffer = buffer + 'INSERT INTO Telefone VALUES ((' + str(dadosTelefone[i][0]) + '), (\'' \
                    + dadosTelefone[i][1] + '\'), (' + str(dadosTelefone[i][2]) + '));' + '\n'

        # Insert Email
        dadosEmail = self.selectEmail()
        sizeEmail = len(dadosEmail)
        for i in range(0, sizeEmail):
            buffer = buffer + 'INSERT INTO Email VALUES ((' + str(dadosEmail[i][0]) + '), (\'' \
                    + dadosEmail[i][1] + '\'), (' + str(dadosEmail[i][2]) + '));' + '\n'

        # Insert Venda
        dadosVenda = self.selectVenda()
        sizeVenda = len(dadosVenda)
        for i in range(0, sizeVenda):
            buffer = buffer + 'INSERT INTO Venda VALUES ((' + str(dadosVenda[i][0]) + '), (\'' \
                    + str(dadosVenda[i][1]) + '\'), (\'' + dadosVenda[i][2] + '\'), (\'' \
                    + dadosVenda[i][3] + '\'), (\'' + str(dadosVenda[i][4]) + '\'), (\'' \
                    + dadosVenda[i][5] + '\'), (\'' + str(dadosVenda[i][6]) + '\'), (\'' \
                    + str(dadosVenda[i][7]) + '\'), (\'' + str(dadosVenda[i][8]) + '\'), (\'' \
                    + str(dadosVenda[i][9]) + '\'), (\'' + str(dadosVenda[i][10]) + '\'), (\'' \
                    + str(dadosVenda[i][11]) + '\'));' + '\n'

        # Insert Prod_Vendido
        dadosProdVend = self.selectProdVendido()
        sizeProdVend = len(dadosProdVend)
        for i in range(0, sizeProdVend):
            buffer = buffer + 'INSERT INTO Venda VALUES ((' + str(dadosProdVend[i][0]) + '), ' \
                     + '(\'' + dadosProdVend[i][1] + '\'), (\'' + str(dadosProdVend[i][2]) + '\'), (' \
                     + str(dadosProdVend[i][3]) + '), (\'' + dadosProdVend[i][4] + '\'));' + '\n'

        # Escrita da string criada "buffer" no arquivo
        file = open(fileName, 'w')
        file.write(buffer)
        file.close()

    # Método que insere dados ao sistema ao ler um arquivo com código SQL
    def importSQL(self, fileName='dados.sql'):
        file = open(fileName, 'r')
        script = file.read()
        file.close()
        self.dbCursor.executescript(script)