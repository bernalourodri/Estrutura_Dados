import mysql.connector
from ConexaoMySQL import *
from Autor import Autor
from AutorDAO import *
from MusicaDAO import *

conexaoMySQL = ConexaoMySQL(host="localhost", user="root", password="root", database="mydb")

# Conecta ao banco de dados
conexao = conexaoMySQL.conectar()

#Criar autor

Frank_Sinatra = Autor(0, "FrankSinatra")
Ray_Charles = Autor(1,"Ray Charles")

#Criar musica
New_York = Musica("New York"," New York New York","1994-02-15",10,10,1,10,[Frank_Sinatra,Ray_Charles])
#print(New_York.Autor[0].id_autor)


#ObjetoDAO = AutorDAO(conexao)
#Inserir Autor
#ObjetoDAO.inserir_autor(Frank_Sinatra)
#ObjetoDAO.inserir_autor2(Ray_Charles,New_York)
#Consultar Autor
#ObjetoDAO.consulta_autor(Frank_Sinatra)
#Update Autor
#ObjetoDAO.update_autor(Frank_Sinatra)
#Exclusao Autor
#ObjetoDAO.exclusao_autor(Frank_Sinatra)


#Incluir Musica
Objeto2DAO = MusicaDAO(conexao)
Objeto2DAO.inserir_musica(New_York)






conexao.commit()

