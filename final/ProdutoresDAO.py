import mysql.connector
from Produtores import Produtores
from Musica import Musica

class ProdutoresDAO:
    def __init__(self, conexao):
        self.conexao = conexao

    def inserir_produtor(self,Produtores):

        try:


            query1 = ("INSERT INTO produtores" "(id_produtores,nome)"
                      "VALUES (%(id_produtores)s,%(nome)s)")

            data1 = {
                'id_produtores': Produtores.id_produtores,
                'nome': Produtores.nome,
            }


            cursor = self.conexao.cursor(buffered=True)
            cursor.execute(query1, data1)

        except mysql.connector.Error as erro:
            print("Erro ao executar Insercao: {}".format())

    def inserir_produtor2(self,Produtores, Musica):

        try:

            query_condicional = "SELECT * FROM produtores WHERE id_produtores = %s"

            data_condicional = Produtores.id_produtores

            cursor = self.conexao.cursor(buffered=True)
            cursor.execute(query_condicional, (data_condicional,))
            resultado = cursor.fetchall()

        except mysql.connector.Error as erro:
            print("Erro ao executar Insercao: {}".format())


        try:
            query1 = ("INSERT INTO produtores" "(id_produtores,nome)"
                      "VALUES (%(id_produtores)s,%(nome)s)")

            data1 = {
                'id_produtores': Produtores.id_produtores,
                'nome': Produtores.nome,
            }

            query2 = ("INSERT INTO produtores_musica" "(id_produtores,id_musica)"
                      "VALUES (%(id_produtores)s,%(id_musica)s)")

            data2 = {
                'id_produtores': Produtores.id_produtores,
                'id_musica': Musica.id_musica,
            }

            cursor = self.conexao.cursor(buffered=True)
            cursor.execute(query1, data1)
            cursor.execute(query2, data2)


        except mysql.connector.Error as erro:
            print("Erro ao executar Insercao: {}".format())
            '''
            else:
                try:

                    query2 = ("INSERT INTO musica_autor" "(id_musica,id_autor)"
                              "VALUES (%(id_musica)s,%(id_autor)s)")

                    data2 = {
                        'id_musica': Musica.id_musica,
                        'id_autor': Autor.id_autor,
                    }

                    cursor = self.conexao.cursor(buffered=True)
                    cursor.execute(query2, data2)

                except mysql.connector.Error as erro:
                    print("Erro ao executar Insercao: {}".format())
            '''


    def consulta_produtor(self,nome):

        try:
            query1 = ("SELECT * FROM produtores WHERE nome = %s")

            data1 = nome

            cursor = self.conexao.cursor(buffered=True)
            cursor.execute(query1, (data1,))
            for (id_produtores, nome) in cursor:
                print("{},{}".format(
                    id_produtores, nome))

        except mysql.connector.Error as erro:
            print("Erro ao executar Consulta: {}".format())

    def update_produtor(self,Produtores):

        try:
            query1 = ("UPDATE produtores SET nome = %(nome)s WHERE id_produtores = %(id_produtores)s")

            data1 = {
                'id_produtores': Produtores.id_produtores,
                'nome': Produtores.nome,
            }

            cursor = self.conexao.cursor(buffered=True)
            cursor.execute(query1,data1)

        except mysql.connector.Error as erro:
            print("Erro ao executar Update: {}".format())


    def exclusao_produtor(self,Produtores):

        try:
            query = ("DELETE FROM produtores WHERE nome = %s")
            nome = Produtores.nome

            cursor = self.conexao.cursor(buffered=True)
            cursor.execute(query, (nome,))

        except mysql.connector.Error as erro:
            print("Erro ao executar Exclusao: {}".format())