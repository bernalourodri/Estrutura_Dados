import mysql.connector
from Autor import Autor

class ProdutoresDAO:
    def __init__(self, conexao):
        self.conexao = conexao

    def inserir_produtores(self,Produtores):

        try:
            query1 = ("INSERT INTO produtores" "(id_produtores,nome)"
                      "VALUES (%(id_produtores)s,%(nome)s)")

            data1 = {
                'id_autor': Produtores.id_produtores[0],
                'nome': Produtores.nome,
            }


            cursor = self.conexao.cursor(buffered=True)
            cursor.execute(query1, data1)

        except mysql.connector.Error as erro:
            print("Erro ao executar Insercao: {}".format())


    def inserir_produtores2(self,Produtores):

        try:
            query1 = "INSERT INTO produtores (id_produtores,nome) VALUES (%s,%s)"

            data1 =(Produtores.id_produtores,Produtores.nome)


            cursor = self.conexao.cursor(buffered=True)
            cursor.execute(query1, data1)

        except mysql.connector.Error as erro:
            print("Erro ao executar Insercao: {}".format())


    def consulta_produtores(self,Produtores):

        try:
            query1 = ("SELECT * FROM produtores WHERE id = %s")

            data1 = Produtores.id_produtores

            cursor = self.conexao.cursor(buffered=True)
            cursor.execute(query1, (data1))

        except mysql.connector.Error as erro:
            print("Erro ao executar Consulta: {}".format())

    def update_produtores(self,Produtores):

        try:
            query1 = ("UPDATE produtores SET id_produtores = %(id_produtores)s, nome = %(nome)s WHERE nome = %(nome)s")

            data1 = {
                'id_produtores': Produtores.id_produtores[0],
                'nome': Produtores.nome,
            }

            cursor = self.conexao.cursor(buffered=True)
            cursor.execute(query1,data1)

        except mysql.connector.Error as erro:
            print("Erro ao executar Update: {}".format())


    def exclusao_produtores(self,Produtores):

        try:
            query = ("DELETE FROM produtores WHERE nome = %s")
            nome = Produtores.nome

            cursor = self.conexao.cursor(buffered=True)
            cursor.execute(query, (nome,))

        except mysql.connector.Error as erro:
            print("Erro ao executar Exclusao: {}".format())