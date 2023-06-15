import mysql.connector
from Musica import Musica
from Autor import Autor
from AutorDAO import *

class MusicaDAO:
    def __init__(self, conexao):
        self.conexao = conexao

    def inserir_musica(self,Musica):

        try:
            query1 = ("INSERT INTO musica" "(titulo,letra,data_de_lançamento,duracao,censura,id_musica,id_categoria)"
                      "VALUES (%(titulo)s,%(letra)s,%(data_lancamento)s,%(duracao)s,%(censura)s,%(id_musica)s,%(id_categoria)s)")

            data1 = {
                'titulo' : Musica.titulo,
                'letra' : Musica.letra,
                'data_lancamento' : Musica.data_lancamento,
                'duracao' : Musica.duracao,
                'censura' : Musica.censura,
                'id_musica' : Musica.id_musica,
                'id_categoria' : Musica.id_categoria

            }

            cursor = self.conexao.cursor(buffered=True)
            cursor.execute(query1, data1)

            for i in range (len(Musica.Autor)):
                AutorDAO.inserir_autor2(self,Musica.Autor[i],Musica)




        except mysql.connector.Error as erro:
            print("Erro ao executar Insercao: {}".format())


    def visualizar_musica(self,Musica):

        try:
            query1 = ("SELECT titulo,data_de_lançamento,duracao,censura,id_musica,id_categoria FROM musica WHERE titulo = %s")

            data1 = Musica.titulo

            cursor = self.conexao.cursor(buffered=True)
            cursor.execute(query1, (data1,))
            for (titulo, data_de_lançamento, duracao,censura,id_musica,id_categoria) in cursor:
                print("{},{:%d %b %Y},{},{},{},{}".format(
                    titulo, data_de_lançamento, duracao,censura,id_musica,id_categoria))

        except mysql.connector.Error as erro:
            print("Erro ao executar Consulta: {}".format())

    def ouvir_musica(self, Musica):

        try:
            query1 = (
                "SELECT letra FROM musica WHERE titulo = %s")

            data1 = Musica.titulo

            cursor = self.conexao.cursor(buffered=True)
            cursor.execute(query1, (data1,))
            for (letra) in cursor:
                print("{}".format(
                    letra))

        except mysql.connector.Error as erro:
            print("Erro ao executar Consulta: {}".format())

    def consulta_titulo(self,titulo):

        try:
            query1 = ("SELECT * FROM musica WHERE titulo = %s")

            data1 = titulo

            cursor = self.conexao.cursor(buffered=True)
            cursor.execute(query1, (data1,))
            for (titulo,letra,data_de_lançamento,duracao,censura,id_musica,id_categoria) in cursor:
                print("{},{},{:%d %b %Y},{},{},{},{}".format(
                    titulo,letra,data_de_lançamento,duracao,censura,id_musica,id_categoria))

        except mysql.connector.Error as erro:
            print("Erro ao executar Consulta: {}".format())


    def musica_autor(self,autor):
        try:
            query1 =("SELECT M.titulo, M.letra, M.data_de_lançamento, M.duracao, M.censura, M.id_musica, M.id_categoria FROM musica M INNER JOIN musica_autor MA ON M.id_musica = MA.id_Musica INNER JOIN autor A ON MA.id_autor = A.id_autor WHERE A.nome = %s")

            data1 = autor
            cursor = self.conexao.cursor(buffered=True)
            cursor.execute(query1, (data1,))
            for (titulo, letra, data_de_lançamento, duracao, censura, id_musica,id_categoria) in cursor:
                print("{},{},{:%d %b %Y},{},{},{},{}".format(
                    titulo, letra, data_de_lançamento, duracao, censura, id_musica,id_categoria))
        except mysql.connector.Error as erro:
            print("Erro ao executar Consulta: {}".format())


    def musica_produtor(self,produtor):
        try:
            query1 =("SELECT M.titulo FROM musica M INNER JOIN produtores_musica MP ON M.id_musica = MP. id_Musica INNER JOIN produtores P ON MP.id_produtores = P.id_produtores WHERE P.nome = %s")

            data1 = produtor
            cursor = self.conexao.cursor(buffered=True)
            cursor.execute(query1, (data1,))
            for (titulo) in cursor:
                print("{}".format(
                    titulo))
        except mysql.connector.Error as erro:
            print("Erro ao executar Consulta: {}".format())


    def exclusao_musica(self,Musica):

        try:
            query = ("DELETE FROM musica WHERE id_musica = %s")
            nome = Musica.id_musica

            cursor = self.conexao.cursor(buffered=True)
            cursor.execute(query, (nome,))

        except mysql.connector.Error as erro:
            print("Erro ao executar Exclusao: {}".format())