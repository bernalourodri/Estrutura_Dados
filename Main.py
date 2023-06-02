import mysql.connector
from ConexaoMySQL import *
from Autor import Autor
from AutorDAO import *

conexaoMySQL = ConexaoMySQL(host="localhost", user="root", password="root", database="mydb")

# Conecta ao banco de dados
conexao = conexaoMySQL.conectar()

#Criar autor

Frank_Sinatra = Autor(1, "FrankSinatra")
print(Frank_Sinatra.nome)

#Inserir autor
insautDAO = AutorDAO(conexao)
insautDAO.inserir_autor(Frank_Sinatra)

#Consultar autor
#consautDAO = AutorDAO(conexao)
#consautDAO.consulta_autor(Frank_Sinatra)

#Criar objeto musica
#Musica1 = Musica("Sabao crucru","sabao crucru sabao crucru","1994-02-15 07:34:33",7,18,10,11,"comedia",1,"Dinho")

#Inserir nome categoria
#inomecatdao = InclusaoDAO(conexao)
#inomecatdao.inserir_nome_categoria(Musica1.id_categoria,Musica1.nome)

#Inserir musica
#idao = InclusaoDAO(conexao)
#idao.inserir(Musica1.titulo,Musica1.letra,Musica1.data_lancamento,Musica1.duracao,Musica1.censura,Musica1.id_musica,Musica1.id_categoria,Musica1.id_autor)

#Inserir autor
#iautdao = InclusaoDAO(conexao)
#iautdao.inserir_autor(Musica1.id_autor,Musica1.nome_autor,Musica1.id_musica)

#Exclusao de Musica
#edao = ExclusaoDAO(conexao)
#edao.exclusaoMusica("Sabao crucru")

conexao.commit()

