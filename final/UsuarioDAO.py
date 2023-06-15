import mysql.connector
from Usuario import Usuario

class UsuarioDAO:
    def __init__(self, conexao):
        self.conexao = conexao

    def inserir_usuario(self,Usuario):

        try:
            query1 = ("INSERT INTO usuarios" "(nome,cpf,data_de_nascimento,numero_de_cartao)"
                      "VALUES (%(nome)s,%(cpf)s,%(data_de_nascimento)s,%(numero_de_cartao)s)")

            data1 = {
                'nome': Usuario.nome,
                'cpf': Usuario.cpf,
                'data_de_nascimento': Usuario.data_de_nascimento,
                'numero_de_cartao': Usuario.numero_de_cartao,
            }


            cursor = self.conexao.cursor(buffered=True)
            cursor.execute(query1, data1)

        except mysql.connector.Error as erro:
            print("Erro ao executar Insercao: {}".format())


    def consulta_usuario(self,Usuario):

        try:
            query1 = ("SELECT * FROM usuarios WHERE nome = %s")

            data1 = Usuario.nome

            cursor = self.conexao.cursor(buffered=True)
            cursor.execute(query1, (data1,))
            for (nome,cpf,data_de_nascimento,numero_de_cartao) in cursor:
                print("{},{},{},{}".format(
                 nome,cpf,data_de_nascimento,numero_de_cartao))

        except mysql.connector.Error as erro:
            print("Erro ao executar Consulta: {}".format())


    def update_usuario(self,Usuario):

        try:
            query1 = ("UPDATE usuarios SET numero_de_cartao = %(numero_de_cartao)s WHERE nome = %(nome)s")

            data1 = {
                'numero_de_cartao': Usuario.numero_de_cartao,
                'nome': Usuario.nome,
            }

            cursor = self.conexao.cursor(buffered=True)
            cursor.execute(query1,data1)


        except mysql.connector.Error as erro:
            print("Erro ao executar Update: {}".format())


    def exclusao_usuario(self,Usuario):

        try:
            query = ("DELETE FROM usuarios WHERE nome = %s")
            nome = Usuario.nome

            cursor = self.conexao.cursor(buffered=True)
            cursor.execute(query, (nome,))

        except mysql.connector.Error as erro:
            print("Erro ao executar Exclusao: {}".format())