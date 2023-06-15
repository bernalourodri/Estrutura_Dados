import mysql.connector
from Categoria import Categoria

class CategoriaDAO:
    def __init__(self, conexao):
        self.conexao = conexao

    def inserir_categoria(self,Categoria):

        try:
            query1 = ("INSERT INTO categoria" "(id_categoria,nome)"
                      "VALUES (%(id_categoria)s,%(nome)s)")

            data1 = {
                'id_categoria': Categoria.id_categoria,
                'nome': Categoria.nome,
            }


            cursor = self.conexao.cursor(buffered=True)
            cursor.execute(query1, data1)

        except mysql.connector.Error as erro:
            print("Erro ao executar Insercao: {}".format())


    def exclusao_Categoria(self,Categoria):

        try:
            query = ("DELETE FROM autor WHERE id_categoria = %s")
            nome = Categoria.id_categoria

            cursor = self.conexao.cursor(buffered=True)
            cursor.execute(query, (nome,))

        except mysql.connector.Error as erro:
            print("Erro ao executar Exclusao: {}".format())