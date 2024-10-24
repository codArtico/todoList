import mysql.connector
from dotenv import load_dotenv
import os

class BDManager:
    def __init__(self):
        load_dotenv()
        self.db_user = os.getenv('DB_USER')
        self.db_pass = os.getenv('DB_PASS')
        self.db_name = os.getenv('DB_NAME')
        self.connection = None
        self.cursor = None
    
    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host='localhost',
                user=self.db_user,
                password=self.db_pass,
                database=self.db_name
            )
            self.cursor = self.connection.cursor()
            print("Conexão com o banco de dados estabelecida com sucesso.")
        except mysql.connector.Error as err:
            print("Erro ao conectar ao banco de dados. Verifique suas credenciais e a configuração do banco de dados.")