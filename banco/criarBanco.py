def criar_banco():
    import mysql.connector

    banco = mysql.connector.connect(
        host = 'localhost', #A hopedagem do seu MySQL
        user='root', #O usuario do seu MySQL
        passwd='', #A senha do seu MySQL (padrao e sem senha)
    );

    cursor = banco.cursor()

    cursor.execute('CREATE DATABASE if not exists banco_produtos')

def criar_tabela():
    import mysql.connector

    banco = mysql.connector.connect(
        host = 'localhost', #A hopedagem do seu MySQL
        user='root', #O usuario do seu MySQL
        passwd='', #A senha do seu MySQL (padrao e sem senha)
        database='banco_produtos' # Com que banco de dados a tabela conectar
    );

    cursor = banco.cursor()

    cursor.execute('CREATE TABLE if not exists produtos (id INT NOT NULL AUTO_INCREMENT, produto VARCHAR(50), codigo INT, preco DOUBLE, PRIMARY KEY (id))')