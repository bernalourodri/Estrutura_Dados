import mysql.connector
from Autor import Autor

class UsuariosDAO:
    def __init__(self, conexao):
        self.conexao = conexao

    def inserir_usuarios(self,Usuarios):

        try:
            query1 = ("INSERT INTO usuarios" "(cpf,nome,data_de_nascimento,numero_de_cartao)"
                      "VALUES (%(cpf)s,%(nome)s),%(data_de_nascimento)s),%(numero_de_cartao)s)")

            data1 = {
                'cpf': Usuarios.cpf[0],
                'nome': Usuarios.nome,
                'data_de_nascimento':Usuarios.data_de_nascimento,
                'numero_de_cartao':Usuarios.numero_de_cartao[0],
            }


            cursor = self.conexao.cursor(buffered=True)
            cursor.execute(query1, data1)

        except mysql.connector.Error as erro:
            print("Erro ao executar Insercao: {}".format())


    def inserir_usuarios2(self,Usuarios):

        try:
            query1 = "INSERT INTO usuarios (cpf,nome,data_de_nascimento,numero_de_cartao) VALUES (%s,%s,%s,%s)"

            data1 =(Usuarios.cpf,Usuarios.nome,Usuarios.data_de_nascimento,Usuarios.numero_de_cartao)


            cursor = self.conexao.cursor(buffered=True)
            cursor.execute(query1, data1)

        except mysql.connector.Error as erro:
            print("Erro ao executar Insercao: {}".format())


    def consulta_produtores(self,Usuarios):

        try:
            query1 = ("SELECT * FROM usuarios WHERE cpf = %s")

            data1 = Usuarios.cpf

            cursor = self.conexao.cursor(buffered=True)
            cursor.execute(query1, (data1))

        except mysql.connector.Error as erro:
            print("Erro ao executar Consulta: {}".format())

    def update_usuarios(self,Usuarios):

        try:
            query1 = ("UPDATE usuarios SET cpf = %(cpf)s, nome = %(nome)s , data_de_nasciemnto = %(data_de_nascimento)s, numero_de_cartao = %(numero_de_cartao)s WHERE nome = %(nome)s")

            data1 = {
                'id_produtores': Usuarios.cpf[0],
                'nome': Usuarios.nome,
                'data_de_nascimento': Usuarios.data_de_nascimento,
                'numero_de_cartao': Usuarios.numero_de_cartao[0],

            }

            cursor = self.conexao.cursor(buffered=True)
            cursor.execute(query1,data1)

        except mysql.connector.Error as erro:
            print("Erro ao executar Update: {}".format())


    def exclusao_produtores(self,Usuarios):

        try:
            query = ("DELETE FROM usuarios WHERE nome = %s")
            nome = Usuarios.nome

            cursor = self.conexao.cursor(buffered=True)
            cursor.execute(query, (nome,))

        except mysql.connector.Error as erro:
            print("Erro ao executar Exclusao: {}".format())