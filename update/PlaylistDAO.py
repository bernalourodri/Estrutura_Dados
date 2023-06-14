import mysql.connector
from Playlist import Playlist
from Musica import Musica
from Usuario import Usuario

class PlaylistDAO:

    def __init__(self, conexao):
        self.conexao = conexao


    def inserir_categoria(self, Playlist,Musica):
        try:
            query1 = ("INSERT INTO playlist" "(titulo,id_playlist,fk_usuarios_playtlist,privacidade_privada,fk_categoria_playlist,data_de_criacao)"
                      "VALUES (%(titulo)s,%(id_playlist)s,%(fk_usuarios_playlist)s,%(privacidade_privada)s,%(fk_categoria_playlist)s,%(data_de_criacao)s)")

            data1 = {
                'titulo': Playlist.titulo,
                'id_playlist': Playlist.id_playlist,
                'fk_usuarios_playlist': Playlist.fk_usuarios_playlist,
                'privacidade_privada': Playlist.privacidade_privada,
                'fk_categoria_playlist': Playlist.fk_categoria_playlist,
                'data_de_criacao': Playlist.data_de_criacao,
            }

            query2 = (
                "INSERT INTO playlist_musica" "(id_playlist,id_musica)"
                "VALUES (%(id_playlist)s,%(id_musica)s)")

            data2 = {
                'id_playlist': Playlist.id_playlist,
                'id_musica': Musica.id_musica,
            }

            cursor = self.conexao.cursor(buffered=True)
            cursor.execute(query1,data1)
            cursor.execute(query2, data2)

        except mysql.connector.Error as erro:
            print("Erro ao executar Insercao: {}".format())

    def ouvir_musica(self, id):
        try:
            query1 = (("SELECT m.letra FROM playlist_musica pm INNER JOIN playlist p ON p.id_playlist = pm.id_playlist INNER JOIN musica m ON m.id_musica = pm.id_musica WHERE pm.id_playlist = %s"))

            data1 = id

            cursor = self.conexao.cursor(buffered=True)
            cursor.execute(query1,(data1,))
            for letra in cursor:
                print("{}".format(letra))

        except mysql.connector.Error as erro:
            print("Erro ao executar Insercao: {}".format())


    def buscar_titulo(self, titulo):
        try:
            query1 = (("SELECT * FROM playlist p WHERE titulo = %s"))

            data1 = titulo

            cursor = self.conexao.cursor(buffered=True)
            cursor.execute(query1, (data1,))

            for (titulo, id_playlist,fk_usuarios_playtlist,privacidade_privada,fk_categoria_playlist,data_de_criacao) in cursor:
                print("{},{},{},{},{},{:%d %b %Y}".format(titulo, id_playlist,fk_usuarios_playtlist,privacidade_privada,fk_categoria_playlist,data_de_criacao))

        except mysql.connector.Error as erro:
            print("Erro ao executar Consulta: {}".format())


    def buscar_usuario(self, cpf):
        try:
            query1 = (("SELECT P.* FROM playlist p INNER JOIN usuarios U ON U.CPF = P.fk_usuarios_playtlist WHERE U.cpf = %s"))

            data1 = cpf

            cursor = self.conexao.cursor(buffered=True)
            cursor.execute(query1, (data1,))

            for (titulo,id_playlist,fk_usuarios_playtlist,privacidade_privada,fk_categoria_playlist,data_de_criacao) in cursor:
                print("{},{},{},{},{},{:%d %b %Y}".format(titulo, id_playlist,fk_usuarios_playtlist,privacidade_privada,fk_categoria_playlist,data_de_criacao))

        except mysql.connector.Error as erro:
            print("Erro ao executar Consulta: {}".format())

    def buscar_ano(self, ano):
        try:
            query1 = (("SELECT * FROM playlist WHERE year(data_de_criacao) = %s"))

            data1 = ano

            cursor = self.conexao.cursor(buffered=True)
            cursor.execute(query1, (data1,))

            for (titulo,id_playlist,fk_usuarios_playtlist,privacidade_privada,fk_categoria_playlist,data_de_criacao) in cursor:
                print("{},{},{},{},{},{:%d %b %Y}".format(titulo, id_playlist,fk_usuarios_playtlist,privacidade_privada,fk_categoria_playlist,data_de_criacao))

        except mysql.connector.Error as erro:
            print("Erro ao executar Consulta: {}".format())

    def busca_privacidde(self,cpf):
        try:
            query1 = (("SELECT P.titulo FROM playlist P INNER JOIN usuarios U ON U.cpf = P.FK_usuarios_playtlist WHERE privacidade_privada = TRUE AND U.CPF = %s UNION SELECT titulo FROM playlist WHERE privacidade_privada = FALSE" ))

            data1 = cpf

            cursor = self.conexao.cursor(buffered=True)
            cursor.execute(query1, (data1,))

            for titulo in cursor:
                print("{}".format(titulo))

        except mysql.connector.Error as erro:
            print("Erro ao executar Consulta: {}".format())