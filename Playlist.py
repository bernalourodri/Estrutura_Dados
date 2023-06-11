class Playlist:
    def __init__(self,titulo,id_playlist,musica,fk_usuarios_playlist,privacidade_privada,fk_categoria_playlist,data_de_criacao ):
        self.titulo = titulo
        self.id_playlist = id_playlist
        self.musica = musica
        self.fk_usuarios_playlist = fk_usuarios_playlist
        self.privacidade_privada = privacidade_privada
        self.fk_categoria_playlist = fk_categoria_playlist
        self.data_de_criacao = data_de_criacao

