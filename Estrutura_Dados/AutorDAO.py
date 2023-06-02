import mysql.connector
from Autor import Autor

class AutorDAO:
    def __init__(self, conexao):
        self.conexao = conexao

    def inserir_autor(self,Autor):

        try:
            query1 = ("INSERT INTO autor" "(id_autor,nome)"
                      "VALUES (%(id_autor)s,%(nome)s)")

            data1 = {
                'id_autor': Autor.id_autor[0],
                'nome': Autor.nome,
            }


            cursor = self.conexao.cursor(buffered=True)
            cursor.execute(query1, data1)

        except mysql.connector.Error as erro:
            print("Erro ao executar Insercao: {}".format())


    def inserir_autor2(self,Autor):

        try:
            query1 = "INSERT INTO autor (id_autor,nome) VALUES (%s,%s)"

            data1 =(Autor.id_autor,Autor.nome)


            cursor = self.conexao.cursor(buffered=True)
            cursor.execute(query1, data1)

        except mysql.connector.Error as erro:
            print("Erro ao executar Insercao: {}".format())


    def consulta_autor(self,Autor):

        try:
            query1 = ("SELECT * FROM autor WHERE id = %s")

            data1 = Autor.id_autor

            cursor = self.conexao.cursor(buffered=True)
            cursor.execute(query1, (data1))

        except mysql.connector.Error as erro:
            print("Erro ao executar Consulta: {}".format())

    def update_autor(self,Autor):

        try:
            query1 = ("UPDATE autor SET id_autor = %(id_autor)s, nome = %(nome)s WHERE nome = %(nome)s")

            data1 = {
                'id_autor': Autor.id_autor[0],
                'nome': Autor.nome,
            }

            cursor = self.conexao.cursor(buffered=True)
            cursor.execute(query1,data1)

        except mysql.connector.Error as erro:
            print("Erro ao executar Update: {}".format())


    def exclusao_autor(self,Autor):

        try:
            query = ("DELETE FROM autor WHERE nome = %s")
            nome = Autor.nome

            cursor = self.conexao.cursor(buffered=True)
            cursor.execute(query, (nome,))

        except mysql.connector.Error as erro:
            print("Erro ao executar Exclusao: {}".format())