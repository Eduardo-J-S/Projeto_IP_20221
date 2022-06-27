#-------------------- Criando banco de dados -----------------------------
def criar_banco():
    import mysql.connector
    global banco

    banco = mysql.connector.connect(
        host = 'localhost',
        user='root',
        passwd='',
    );

    cursor = banco.cursor()

    cursor.execute('CREATE DATABASE if not exists banco_produtos')

#-------------------- Criando tabelas -----------------------------
def criar_tabela():

    import mysql.connector

    banco = mysql.connector.connect(
        host = 'localhost',
        user='root',
        passwd='',
        database='banco_produtos'
    );

    cursor = banco.cursor()

    cursor.execute('CREATE TABLE if not exists produtos (id INT NOT NULL AUTO_INCREMENT, produto VARCHAR(50), codigo INT, preco DOUBLE, PRIMARY KEY (id))')

#-------------------- Visualizando informações da tabela -----------------------------
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