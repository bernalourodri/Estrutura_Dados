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