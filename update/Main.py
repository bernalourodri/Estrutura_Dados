import mysql.connector
from ConexaoMySQL import *
from Autor import Autor
from AutorDAO import *
from MusicaDAO import *
from CategoriaDAO import *
from UsuarioDAO import *
from PlaylistDAO import *

conexaoMySQL = ConexaoMySQL(host="localhost", user="root", password="root", database="mydb")

# Conecta ao banco de dados
conexao = conexaoMySQL.conectar()

#Criar autor
Frank_Sinatra = Autor(0, "FrankSinatra")
Ray_Charles = Autor(1,"Ray Charles")

#Criar categoria
Jazz = Categoria(1,"Jazz")

#Criar musica
New_York = Musica("New York"," New York New York","1994-02-15",10,10,1,1,[Frank_Sinatra,Ray_Charles])
Fly_me = Musica("Fly me"," Fly me to the moon","1994-02-15",10,10,2,1,[Frank_Sinatra,Ray_Charles])
Jack = Musica("Jack"," Hit the Road Jack","1994-02-15",10,10,3,1,[Ray_Charles])
#print(New_York.Autor[0].id_autor)

#Criar usuario
Joao = Usuario("Joao","11111111111","2000-02-01",567)

#Criar Playlist

Melhores_Jazz = Playlist("Melhores Jazz",1,"11111111111",0,1,"2023-02-19")


ObjetoDAO = AutorDAO(conexao)
#Autor
#ObjetoDAO.inserir_autor(Frank_Sinatra)
#ObjetoDAO.inserir_autor2(Ray_Charles,New_York)
#Consultar Autor
#ObjetoDAO.consulta_autor(Frank_Sinatra)
#Update Autor
#ObjetoDAO.update_autor(Frank_Sinatra)
#Exclusao Autor
#ObjetoDAO.exclusao_autor(Frank_Sinatra)

#Categoria

#Objeto2DAO = CategoriaDAO(conexao)
#Objeto2DAO.inserir_categoria(Jazz)

#Musica
Objeto3DAO = MusicaDAO(conexao)
#Objeto3DAO.inserir_musica(Jack)
#Objeto3DAO.consulta_musica(New_York)
#Objeto3DAO.exclusao_musica(New_York)

#Usuario
Objeto4DAO = UsuarioDAO(conexao)
#Objeto4DAO.inserir_usuario(Joao)
#Objeto4DAO.update_usuario(Joao)
#Objeto4DAO.exclusao_usuario(Joao)
#Objeto4DAO.consulta_usuario(Joao)

#Playlist
Objeto5DAO = PlaylistDAO(conexao)
#Objeto5DAO.inserir_categoria(Melhores_Jazz,New_York)
#Objeto5DAO.inserir_categoria(Melhores_Jazz,Jack)
#Objeto5DAO.ouvir_musica(Melhores_Jazz)
#Objeto5DAO.buscar_titulo("Melhores Jazz")
conexao.commit()

