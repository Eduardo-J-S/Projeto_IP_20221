def criar_banco():
    import mysql.connector

    banco = mysql.connector.connect(
        host = 'localhost', #A hopedagem do seu MySQL
        user='root', #O usuario do seu MySQL
        passwd='', #A senha do seu MySQL (padrao é sem senha)
    );

    cursor = banco.cursor()

    cursor.execute('CREATE DATABASE if not exists banco_produtos')

def criar_tabela():
    import mysql.connector

    banco = mysql.connector.connect(
        host = 'localhost', #A hopedagem do seu MySQL
        user='root', #O usuario do seu MySQL
        passwd='', #A senha do seu MySQL (padrao é sem senha)
        database='banco_produtos' # Com que banco de dados a tabela conectar
    );

    cursor = banco.cursor()

    cursor.execute('CREATE TABLE if not exists produtos (id INT NOT NULL AUTO_INCREMENT, produto VARCHAR(50), codigo INT, preco DOUBLE, PRIMARY KEY (id))')

def visu_info():
    import mysql.connector
    banco = mysql.connector.connect(
        host = 'localhost',
        user='root',
        passwd='',
        database='banco_produtos'
    );
    lista=[]
            
    cursor = banco.cursor()
    mostrar = 'SELECT * FROM produtos'
    cursor.execute(mostrar)
    dados = cursor.fetchall()
    for i in dados:
        lista.append(i)
    return lista