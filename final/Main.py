import mysql.connector
from ConexaoMySQL import *
from Autor import Autor
from Produtores import Produtores
from AutorDAO import *
from MusicaDAO import *
from CategoriaDAO import *
from UsuarioDAO import *
from PlaylistDAO import *
from ProdutoresDAO import *

conexaoMySQL = ConexaoMySQL(host="localhost", user="root", password="root", database="mydb")

# Conecta ao banco de dados
conexao = conexaoMySQL.conectar()

#Criar autor
Frank_Sinatra = Autor(0, "FrankSinatra")
Ray_Charles = Autor(1,"Ray Charles")
Ella = Autor(2,"Ella")

#Criar produtor
BillShow = Produtores(2,"Bill")
Michael = Produtores(1, "Michael")

#Criar categoria
Jazz = Categoria(1,"Jazz")

#Criar musica
New_York = Musica("New York"," New York New York","1994-02-15",10,10,1,1,[Frank_Sinatra,Ray_Charles])
Fly_me = Musica("Fly me"," Fly me to the moon","1994-02-15",10,10,2,1,[Frank_Sinatra,Ray_Charles])
Jack = Musica("Jack"," Hit the Road Jack","1994-02-15",10,10,3,1,[Ray_Charles])
Cheek = Musica("Cheek","Cheek to Cheek","1957-05-05",7,10,4,1,[Ella] )


#Criar usuario
Joao = Usuario("Joao","11111111111","2000-02-01",537)
Lucca = Usuario("Lucca","22222222222","1990-01-01",173)

#Criar Playlist
Melhores_Jazz = Playlist("Melhores Jazz",1,"11111111111",0,1,"2023-02-19")
Jazz_Feminino = Playlist("Jazz Feminino",2,"22222222222",1,1,"2020-11-15")

#Autor
ObjetoDAO = AutorDAO(conexao)
#ObjetoDAO.inserir_autor(Frank_Sinatra)
#ObjetoDAO.inserir_autor2(Ray_Charles,New_York)
#Consultar Autor
#ObjetoDAO.consulta_autor("FrankSinatra")
#Update Autor
#ObjetoDAO.update_autor(Frank_Sinatra)
#Exclusao Autor
#ObjetoDAO.exclusao_autor(Frank_Sinatra)

#Categoria
Objeto2DAO = CategoriaDAO(conexao)
#Objeto2DAO.inserir_categoria(Jazz)


#Musica
Objeto3DAO = MusicaDAO(conexao)
#Objeto3DAO.inserir_musica(Jack)
#Objeto3DAO.visualizar_musica(Jack)
#Objeto3DAO.ouvir_musica(Jack)
#Objeto3DAO.consulta_titulo("Jack")
#Objeto3DAO.musica_autor("Ray Charles")
#Objeto3DAO.musica_produtor("Bill")
#Objeto3DAO.exclusao_musica(Cheek)


#Produtor
Objeto1DAO = ProdutoresDAO(conexao)
#Objeto1DAO.inserir_produtor2(BillShow,Jack)
#Objeto1DAO.consulta_produtor("Bill")
#Objeto1DAO.update_produtor(BillShow)
#Objeto1DAO.exclusao_produtor(BillShow)



#Usuario
Objeto4DAO = UsuarioDAO(conexao)
#Objeto4DAO.inserir_usuario(Joao)
#Objeto4DAO.inserir_usuario(Lucca)
#Objeto4DAO.update_usuario(Joao)
#Objeto4DAO.exclusao_usuario(Joao)
#Objeto4DAO.consulta_usuario(Joao)

#Playlist
Objeto5DAO = PlaylistDAO(conexao)
#Objeto5DAO.inserir_categoria(Melhores_Jazz,New_York)
#Objeto5DAO.inserir_categoria(Melhores_Jazz,Jack)
#Objeto5DAO.inserir_categoria(Jazz_Feminino,Cheek)
#Objeto5DAO.ouvir_musica(1)
#Objeto5DAO.ouvir_musica(2)
#Objeto5DAO.buscar_titulo("Melhores Jazz")
#Objeto5DAO.buscar_usuario("11111111111")
#Objeto5DAO.buscar_ano("2023")
#Objeto5DAO.busca_privacidde("22222222222")
conexao.commit()

