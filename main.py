from tkinter import *
from tkinter import messagebox
import mysql.connector
from pacotes import criarBanco, telaCompras
from tkinter import ttk
import pycep_correios


# --------------------------------------------- cores --------------------------------------------
cor0 = '#121010'  # Preta / black
cor1 = '#feffff'  # branca / white
cor2 = '#3fb5a3'  # verde / green
cor3 = '#38576b'  # valor / value
cor4 = '#403d3d'   # letra / letters
cor5 = '#e9edf5' # sky blue
cor6 = '#ef5350' #vermelho
cor7 = '#191970' #MidnightBlue


voltar = False

# ------- funçãoo deletar item da tabela ------------------------
def deletar():
    try:
        dados_topo = topo.focus()
        dici_topo = topo.item(dados_topo)
        topo_lista = dici_topo['values']

        posicao_id = topo_lista[0]

        banco = mysql.connector.connect(
            host = 'localhost',
            user='root',
            passwd='',
            database='banco_produtos'
        );
        with banco:
            cursor = banco.cursor()
            cursor.execute('DELETE FROM produtos WHERE id =' +str(posicao_id))

        quartaTela.destroy()
        nova_tela_4()
    except:
        messagebox.showerror('ERRO', 'Nenhum item selecionado')
    


#------------- botao ir tela 4 ---------------------------------------------------
def abrir_tela_4():
    voltar = True
    terceiraTela.destroy()
    if voltar:
        nova_tela_4()

# -------- Segunda tela (Seguimento login) voltando para primeira tela --------------------------
def voltar_tela_1():
    voltar = True
    segundaTela.destroy()
    if voltar:
        tela_login()

# -------- Terceira tela Seguimento login voltando para primeira tela --------------------------
def voltar_tela_1_2():
    voltar = True
    terceiraTela.destroy()
    if voltar:
        tela_login()

#-------------- tela 4 (visualizar tabela de produtos) voltando para tela 3 -----------------------------------------------
def voltar_tela_3():
    voltar = True
    quartaTela.destroy()
    if voltar:
        nova_tela_3()

#botao abrir tela compras -------------------------------------------
def abrir_tela_compras():
    voltar=True
    primeiraTela.destroy()
    if voltar:
        telaCompras.first_tela_compras()



def nova_tela_4():
    global quartaTela
    global topo

    quartaTela = Tk()
    quartaTela.title('Banco de produtos')
    quartaTela.geometry('500x500+420+100')
    quartaTela.configure(bg=cor5)
    quartaTela.resizable(width=FALSE, height=FALSE)
    #criando frame --------------------------------
    tela_4_frame = Frame(quartaTela, width=450, height=450, bg=cor3, relief='flat')
    tela_4_frame.grid(row=0, column=0)
    
    tela_4_frame_2 = Frame(quartaTela, width=500, height=300, bg=cor2, relief='flat')
    tela_4_frame_2.grid(row=1, column=0)

    # lista dos produtos da tabela
    produto = criarBanco.visu_info()
    
    # lista para topo da página. cabeçalho
    lista = ['ID', 'PRODUTOS', 'CÓDIGO', 'PREÇO']

    topo = ttk.Treeview(tela_4_frame,selectmode='extended', columns=lista, show='headings')

    #rolagem vertical horizontal -----------------------------
    rolagem_vert = ttk.Scrollbar(tela_4_frame, orient='vertical', command=topo.yview)
    rolagem_vert.grid(column=1, row=0, sticky='ns')

    rolagem_hori = ttk.Scrollbar(tela_4_frame, orient='horizontal', command=topo.yview)
    rolagem_hori.grid(column=0, row=1, sticky='ew')

    topo.configure(yscrollcommand=rolagem_vert.set, xscrollcommand=rolagem_hori.set)
    topo.grid(column=0, row=0)

    tela_4_frame.grid_rowconfigure(0, weight=12)

    posicao_cabecalho = ['center','center','center','center']
    tamanho_cabecalho = [50, 180, 150, 100]
    c=0

    for coluna in lista:
        topo.heading(coluna, text=coluna.title().upper(), anchor=CENTER)
        topo.column(coluna, width=tamanho_cabecalho[c], anchor=posicao_cabecalho[c])
        c+=1
    
    for item in produto:
        topo.insert('','end',values=item)

    #------------------------------------------botões-------------------------------------------------------
    #-------criando botao voltar página anterior ---------------------------------------------------
    botao_voltar_tela_3 = Button(tela_4_frame_2, command=voltar_tela_3, text='Voltar', font=('Arial 12 bold'), width=5, height=1, overrelief='ridge', bg=cor0, fg=cor1)
    botao_voltar_tela_3.place(x=390, y=210)

    #-------botão deletar ------------------------------------------------------------------
    botao_deletar = Button(tela_4_frame_2, command= deletar, text='Deletar', font=('Yvi 15'), width=7, height=1, overrelief='ridge', bg=cor3, fg=cor0)
    botao_deletar.place(x=40, y=30)

    quartaTela.mainloop()


def inserir():
    try:
        produto = entre_descricao.get()
        codigo = entre_codigo.get()
        preco = entre_preco.get()

        criarBanco.criar_banco()
        criarBanco.criar_tabela()


        if produto == '' or codigo == '' or preco =='':
            messagebox.showerror('Erro', 'Campos não estão preenchidos')
        else:
            messagebox.showinfo('Sucesso', 'Produto adicionado com sucesso')
            banco = mysql.connector.connect(
            host = 'localhost', #A hopedagem do seu MySQL
            user='root', #O usuario do seu MySQL
            passwd='', #A senha do seu MySQL (padrao é sem senha)
            database='banco_produtos' # Com que banco de dados a tabela conectar
            )

            cursor = banco.cursor()

            inserindo = 'INSERT INTO produtos (produto, codigo, preco) VALUES (%s, %s, %s)'
            dados = (str(produto), str(codigo), str(preco))
            cursor.execute(inserindo, dados)
            banco.commit()

            print(f'Produto: {produto}')
            print(f'Código: {codigo}')
            print(f'Preço: {preco}')

            entre_descricao.delete(0, 'end')
            entre_codigo.delete(0, 'end')
            entre_preco.delete(0, 'end')
    except:
        messagebox.showerror('ERRO', 'Algum produto digitado de forma errada')


        

def nova_tela_3():
    global terceiraTela
    global segundaTela
    global entre_descricao
    global entre_codigo
    global entre_preco
    global label_codigo

    terceiraTela = Tk()
    terceiraTela.title('Banco de dados')
    terceiraTela.geometry('500x500+420+100')
    terceiraTela.configure(bg=cor5)
    terceiraTela.resizable(width=FALSE, height=FALSE)

    
    # criando frames -------------------------------------
    primeiro_frame = Frame(terceiraTela, width=500, height=65, bg=cor3, relief='flat')
    primeiro_frame.grid(row=0, column=0)

    segundo_frame = Frame(terceiraTela, width=500, height=435, bg=cor1, relief='flat')
    segundo_frame.grid(row=1, column=0)


    # criando labels e entrys--------------------------------
    label_inserir = Label(primeiro_frame, text='Inserir Produtos', font=('Arialblack 20 bold'), bg=cor3, fg=cor1)
    label_inserir.place(x=140, y=12)

    label_descricao = Label(segundo_frame, text='Produto: *', font=('Yvi 15 bold'), bg=cor1, fg=cor4)
    label_descricao.place(x=15, y=55)
    entre_descricao = Entry(segundo_frame, width=50, relief='solid')
    entre_descricao.place(x=20, y=85)

    label_codigo = Label(segundo_frame, text='Código: *', font=('Yvi 15 bold'), bg=cor1, fg=cor4)
    label_codigo.place(x=15, y=130)
    entre_codigo = Entry(segundo_frame, width=50, relief='solid')
    entre_codigo.place(x=20, y=160)

    label_preco =  Label(segundo_frame, text='Preço *', font=('Yvi 15 bold'), bg=cor1, fg=cor4)
    label_preco.place(x=20, y=195)
    entre_preco = Entry(segundo_frame, width=50, relief='solid')
    entre_preco.place(x=20, y=224)

    #botao inserir -----------------------------------
    botao_inserir = Button(segundo_frame, text='Inserir', command=inserir, width=10, height=1, font=('Arial 10 bold'), bg=cor6, fg=cor1, relief='raised',
                    overrelief='ridge')
    botao_inserir.place(x=20, y=300)
    # botão visualizar tabela ---------------------------------------------------------
    botao_ir_tabela = Button(segundo_frame, command=abrir_tela_4, text='Visualizar Produtos', width=15, height=1, font=('Arial 10 bold'), bg=cor7, fg=cor1, relief='raised',
                    overrelief='ridge')
    botao_ir_tabela.place(x=200, y=300)
    
    botao_inicio_t3 = Button(segundo_frame, text='Início', command=voltar_tela_1_2, width=10, height=1, font=('Arial 10 bold'), bg=cor2, fg=cor1, relief='raised',
                    overrelief='ridge')
    botao_inicio_t3.place(x=20, y=390)

    terceiraTela.mainloop()



def login_tela_3():
    nome = entre_nome.get()
    senha = entre_senha.get()
    if nome == 'adm' and senha == '123':
        messagebox.showinfo('Login', 'Seja bem vindo')
        segundaTela.destroy()
        nova_tela_3()
    else:
        nome_senha_erro['text'] = 'Usuário ou senha incorretos'
        

def nova_tela_login():
    global entre_nome
    global entre_senha
    global nome_senha_erro
    global segundaTela
    global primeiraTela
    global botao_voltar

    primeiraTela.destroy()
    segundaTela = Tk()
    segundaTela.title('Login')
    segundaTela.geometry('500x500+420+100')
    segundaTela.configure(bg=cor1)
    segundaTela.resizable(width=FALSE, height=FALSE)
    label_nome = Label(segundaTela, text='Usuário *', font=('Arial 12'), bg=cor1, fg=cor0)
    label_nome.place(x=100, y=160)
    entre_nome = Entry(segundaTela, width=25, justify='left', font=('', 15), highlightthickness=1, relief='solid')
    entre_nome.place(x=100, y=180)


    label_senha = Label(segundaTela, text='Senha *', font=('Arial 12'), bg=cor1, fg=cor0)
    label_senha.place(x=100, y=250)
    entre_senha = Entry(segundaTela, width=25, justify='left', font=('', 15), highlightthickness=1, relief='solid', show='*')
    entre_senha.place(x=100, y=270)


    #--------- botao segunda tela voltar -----------------------------------
    botao_voltar = Button(segundaTela, command= voltar_tela_1, text='Voltar', font=('Arial 12 bold'), width=15, height=1,
                        overrelief='ridge', bg=cor1, fg=cor0)
    botao_voltar.place(x=30, y=30)

    # -------- botão segunda tela entrar banco de dados ------------------------------
    login_segunda_tela = Button(segundaTela, text='Login', command=login_tela_3,  font=('Arial 12 bold'), width=15, height=1,
                        overrelief='ridge', bg=cor3, fg=cor1)
    login_segunda_tela.place(x=100, y=325)
    nome_senha_erro = Label(segundaTela, text='', font=('Arial 8'), bg=cor1, fg=cor0)
    nome_senha_erro.place(x=100, y=303)

    segundaTela.mainloop()
    


def tela_login():
    global primeiraTela
    global segundaTela
    primeiraTela = Tk()
    primeiraTela.title('Login/Compra')
    primeiraTela.geometry('500x500+420+100')
    primeiraTela.configure(bg=cor1)
    primeiraTela.resizable(width=FALSE, height=FALSE)
        

    #----------------------------------- dividindo a tela principal ----------------------------------
    frame_esquerda = Frame(primeiraTela, width=250, height=500, bg=cor1, relief='flat')
    frame_esquerda.place(x=0, y=0)

    frame_direita = Frame(primeiraTela, width=250, height=500, bg=cor1, relief='flat')
    frame_direita.place(x=250, y=0)

    #----------------------------------- configurando frame esque ----------------------------------
    label_nome = Label(frame_esquerda, text='Entrar', font=('Arialblack 20 bold'),bg=cor2, fg=cor0)
    label_nome.place(x=30, y=150)
    label_descricao = Label(frame_esquerda, text='Área de login para funcionários', 
                            font=('Ivy 10 italic'),bg=cor2, fg=cor0)
    label_descricao.place(x=30, y=190)

    #criar linha 
    label_linha = Label(frame_esquerda, text= '', height=160, width=0, anchor=NW, font=('Ivy 1'), bg=cor0, fg=cor4)
    label_linha.place(x=248, y=60)

    #------------------------------------ Criando botao login --------------------------------------------------------
    botao_login = Button(frame_esquerda, command=nova_tela_login, text='Login', font=('Arial 12 bold'), width=15, height=1,
                        overrelief='ridge', bg=cor3, fg=cor1)
    botao_login.place(x=30, y=230)


    #----------------------------------- configurando frame direit ----------------------------------
    label_nome2 = Label(frame_direita, text='Comprar', font=('Arialblack 20 bold'),bg=cor3, fg=cor0)
    label_nome2.place(x=30, y=150)
    label_descricao2 = Label(frame_direita, text='Área de pedidos de compras', 
                            font=('Ivy 10 italic'),bg=cor3, fg=cor0)
    label_descricao2.place(x=30, y=190)

    #-------------------------------- Criando botao comprar ------------------------------------------------------
    botao_login = Button(frame_direita, command=abrir_tela_compras, text='Comprar', font=('Arial 12 bold'), width=15, height=1,
                        overrelief='ridge', bg=cor2, fg=cor1)
    botao_login.place(x=30, y=230)


    primeiraTela.mainloop()

tela_login()
