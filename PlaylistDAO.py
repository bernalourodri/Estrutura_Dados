import mysql.connector
from Playlist import Playlist
from Musica import Musica


class PlaylistDAO:

    def __init__(self, conexao):
        self.conexao = conexao


    def inserir_categoria(self, Playlist):
        try:
            query1 = ("INSERT INTO playlist" "(titulo,id_playlist,musica,fk_usuarios_platlist,privacidade_privada,fk_categoria_playlist,data_de_criacao)"
                      "VALUES (%(titulo)s,%(id_playlist)s,%(musica)s,%(fk_usuarios_playlist)s,%(privacidade_privada)s,%(fk_categoria_playlist)s,%(data_de_criacao)s)")

            data1 = {
                'titulo': Playlist.titulo,
                'id_playlist': Playlist.id_playlist,
                'musica': Playlist.musica,
                'fk_usuarios_playlist': Playlist.fk_usuarios_playlist,
                'privacidade_privada': Playlist.privacidade_privada,
                'fk_categoria_playlist': Playlist.fk_categoria_playlist,
                'data_de_criacao': Playlist.data_de_criacao,
            }

            cursor = self.conexao.cursor(buffered=True)
            cursor.execute(query1, data1)

        except mysql.connector.Error as erro:
            print("Erro ao executar Insercao: {}".format())

    