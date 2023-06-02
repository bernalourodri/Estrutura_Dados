import mysql.connector
from Autor import Autor
from Musica import Musica

class AutorDAO:
    def __init__(self, conexao):
        self.conexao = conexao

    def inserir_autor(self,Autor):

        try:
            query1 = ("INSERT INTO autor" "(id_autor,nome)"
                      "VALUES (%(id_autor)s,%(nome)s)")

            data1 = {
                'id_autor': Autor.id_autor,
                'nome': Autor.nome,
            }


            cursor = self.conexao.cursor(buffered=True)
            cursor.execute(query1, data1)

        except mysql.connector.Error as erro:
            print("Erro ao executar Insercao: {}".format())

    def inserir_autor2(self,Autor, Musica):

        try:
            query1 = ("INSERT INTO autor" "(id_autor,nome)"
                      "VALUES (%(id_autor)s,%(nome)s)")

            data1 = {
                'id_autor': Autor.id_autor,
                'nome': Autor.nome,
            }

            query2 = ("INSERT INTO musica_autor" "(id_musica,id_autor)"
                      "VALUES (%(id_musica)s,%(id_autor)s)")

            data2 = {
                'id_musica': Musica.id_musica,
                'id_autor': Autor.id_autor,
            }

            cursor = self.conexao.cursor(buffered=True)
            cursor.execute(query1, data1)
            cursor.execute(query2, data2)

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