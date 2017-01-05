import sqlite3

class Database(object):
    dbConnect = None
    dbCursor = None

    def __init__(self,loc):
        if(loc==1):
            self.dbConnect = sqlite3.connect('GutsDados.db')
        else:
            self.dbConnect = sqlite3.connect('database/GutsDados.db')
        self.dbCursor = self.dbConnect.cursor()

#Funcao que cria o bd
    def createDB(self):

        self.dbCursor.execute('''CREATE TABLE Categoria (
            id INTEGER PRIMARY KEY NOT NULL,
            nome varchar(500) NOT NULL,
            data_inser INTEGER NOT NULL
        );''')

        self.dbCursor.execute('''CREATE TABLE Produto (
            id INTEGER PRIMARY KEY NOT NULL,
            nome varchar(500) NOT NULL,
            valor_inic varchar(100) NOT NULL,
            data_inser varchar(100) NOT NULL,
            Id_Categoria INTEGER NOT NULL,
            FOREIGN KEY (Id_Categoria) REFERENCES Categoria(id)
       );''')
#Insere o produto recebendo varios valores
    def insertProduto(self, id, nome, valor_inic, data_inser):
        values = [id, nome, valor_inic, data_inser]
        self.dbCursor.execute( 'INSERT INTO Produto VALUES (id, nome, valor_inic, data_inser)', values)
        self.dbConnect.commit();
#Insere o produto recebendo um objeto produto
    def insertProduto(self, prod):
        values = [prod.getId(), prod.getNome(), prod.getValor_inic(),
         prod.getData_inser(),prod.getForeign_key()]

        self.dbCursor.execute( 'INSERT INTO Produto VALUES (?, ?, ?, ?,?)',values)
        self.dbConnect.commit()
#Insere categoria recebendo varios valores
    def insertCategoria(self, id, nome, valor_inic, data_inser):
        values = [id, nome, data_inser]
        self.dbCursor.execute('INSERT INTO Categoria VALUES (?, ?, ?)', values)
        self.dbConnect.commit();
#Insere categoria recebendo um objeto
    def insertCategoria(self, categ):
        values = [categ.getId(), categ.getNome(), categ.getData_inser()]
        self.dbCursor.execute('INSERT INTO Categoria VALUES (?, ?, ?)', values)
        self.dbConnect.commit();
#Seleciona todos os produtos
    def selectProduto(self):
        self.dbCursor.execute('SELECT * FROM Produto ORDER BY id')
        x = self.dbCursor.fetchall()
        return x
#Seleciona todos os produtos da categoria doces
    def selectProdutoDoces(self):
        self.dbCursor.execute('Select * FROM Produto WHERE Id_Categoria = 1')
        return self.dbCursor.fetchall()

# Seleciona todos os produtos da categoria salgados
    def selectProdutoSalgados(self):
        self.dbCursor.execute('Select * FROM Produto WHERE Id_Categoria = 2')
        return self.dbCursor.fetchall()

# Seleciona todos os produtos da categoria massas
    def selectProdutoMassas(self):
        self.dbCursor.execute('Select * FROM Produto WHERE Id_Categoria = 3')
        return self.dbCursor.fetchall()

# Seleciona todos os produtos da categoria bebidas
    def selectProdutoBebidas(self):
        self.dbCursor.execute('Select * FROM Produto WHERE Id_Categoria = 4')
        return self.dbCursor.fetchall()

# Seleciona todos os produtos da categoria outros
    def selectProdutoOutros(self):
        self.dbCursor.execute('Select * FROM Produto WHERE Id_Categoria = 5')
        return self.dbCursor.fetchall()

#Seleciona categoria
    def selectCategoria(self):
        self.dbCursor.execute('SELECT * FROM Categoria ORDER BY id')
        print self.dbCursor.fetchone()

#conta quantos produtos tem
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

#Pega somente o nome de um id especifico
    def selectProdNameId(self,id):
        value = [id]
        self.dbCursor.execute('SELECT nome FROM Produto WHERE id = ?',value)
        x = self.dbCursor.fetchone()
        return x[0]

#Ferifica se o produto existe pelo seu id
    def ExistsProduto(self,id):
        value = [id]
        self.dbCursor.execute('SELECT id FROM Produto WHERE id = ?', value)
        data = self.dbCursor.fetchall()
        if len(data) == 0:
            return False
        else:
            return True

#Deleta o produto dado o seu id
    def deleteGivenId(self,id):
        print id
        value = [id]
        self.dbCursor.execute('DELETE FROM Produto WHERE id = ?',value)
        self.dbConnect.commit()

#Fecha a ligacao com o banco de dados
    def close(self):
        self.dbCursor.close()
