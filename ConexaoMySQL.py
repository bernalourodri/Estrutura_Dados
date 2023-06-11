import mysql.connector


class ConexaoMySQL:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.conexao = None
        self.cursor = None

    def conectar(self):
        try:
            self.conexao = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            self.cursor = self.conexao.cursor(buffered=True)
            print("Conexão estabelecida com sucesso!")
            return self.conexao
        except mysql.connector.Error as erro:
            print("Erro ao conectar ao banco de dados: {erro}")


    def desconectar(self):
        if self.conexao:
            self.cursor.close()
            self.conexao.close()
            print("Conexão encerrada.")