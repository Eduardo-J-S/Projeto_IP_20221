from tkinter import *
from tkinter import messagebox

# --------------------------------------------- cores --------------------------------------------
co0 = "#121010"  # Preta / black
co1 = "#feffff"  # branca / white
co2 = "#3fb5a3"  # verde / green
co3 = "#38576b"  # valor / value
co4 = "#403d3d"   # letra / letters


voltar = False

def voltar_tela_1():
    global voltar
    voltar = True
    segundaTela.destroy()
    if voltar:
        tela_login()
        

def nova_tela_3():
    global segundaTela
    segundaTela.destroy()

    terceiraTela = Tk()
    terceiraTela.title('Banco de dados')
    terceiraTela.geometry('500x500')
    terceiraTela.configure(bg=co1)
    terceiraTela.resizable(width=FALSE, height=FALSE)
    
    terceiraTela.mainloop()



def login_tela_3():
    nome = entre_nome.get()
    senha = entre_senha.get()
    if nome == 'adm' and senha == 'adm':
        messagebox.showinfo('Login', 'Seja bem vindo')
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
    segundaTela.geometry('500x500')
    segundaTela.configure(bg=co1)
    segundaTela.resizable(width=FALSE, height=FALSE)
    label_nome = Label(segundaTela, text='Usuário *', font=('Arial 12'), bg=co1, fg=co0)
    label_nome.place(x=100, y=160)
    entre_nome = Entry(segundaTela, width=25, justify='left', font=('', 15), highlightthickness=1, relief='solid')
    entre_nome.place(x=100, y=180)

    label_senha = Label(segundaTela, text='Senha *', font=('Arial 12'), bg=co1, fg=co0)
    label_senha.place(x=100, y=250)
    entre_senha = Entry(segundaTela, width=25, justify='left', font=('', 15), highlightthickness=1, relief='solid', show='*')
    entre_senha.place(x=100, y=270)


    #--------- botao segunda tela voltar -----------------------------------
    botao_voltar = Button(segundaTela, command= voltar_tela_1, text='Voltar', font=('Arial 12 bold'), width=15, height=1,
                        overrelief='ridge', bg=co1, fg=co0)
    botao_voltar.place(x=30, y=30)

    # -------- botão segunda tela entrar banco de dados ------------------------------
    login_segunda_tela = Button(segundaTela, text='Login', command=login_tela_3,  font=('Arial 12 bold'), width=15, height=1,
                        overrelief='ridge', bg=co3, fg=co1)
    login_segunda_tela.place(x=100, y=325)
    nome_senha_erro = Label(segundaTela, text='', font=('Arial 8'), bg=co1, fg=co0)
    nome_senha_erro.place(x=100, y=303)

    segundaTela.mainloop()
    


def tela_login():
    global primeiraTela
    global segundaTela
    primeiraTela = Tk()
    primeiraTela.title('Login/Compra')
    primeiraTela.geometry('500x500')
    primeiraTela.configure(bg=co1)
    primeiraTela.resizable(width=FALSE, height=FALSE)
        

    #----------------------------------- dividindo a tela principal ----------------------------------
    frame_esquerda = Frame(primeiraTela, width=250, height=500, bg=co1, relief='flat')
    frame_esquerda.place(x=0, y=0)

    frame_direita = Frame(primeiraTela, width=250, height=500, bg=co1, relief='flat')
    frame_direita.place(x=250, y=0)

    #----------------------------------- configurando frame esque ----------------------------------
    label_nome = Label(frame_esquerda, text='Entrar', font=('Arialblack 20 bold'),bg=co2, fg=co0)
    label_nome.place(x=30, y=150)
    label_descricao = Label(frame_esquerda, text='Área de login para funcionários', 
                            font=('Ivy 10 italic'),bg=co2, fg=co0)
    label_descricao.place(x=30, y=190)

    #criar linha 
    label_linha = Label(frame_esquerda, text= '', height=160, width=0, anchor=NW, font=('Ivy 1'), bg=co0, fg=co4)
    label_linha.place(x=248, y=60)

    #------------------------------------ Criando botao login --------------------------------------------------------
    botao_login = Button(frame_esquerda, command=nova_tela_login, text='Login', font=('Arial 12 bold'), width=15, height=1,
                        overrelief='ridge', bg=co3, fg=co1)
    botao_login.place(x=30, y=230)


    #----------------------------------- configurando frame direit ----------------------------------
    label_nome2 = Label(frame_direita, text='Comprar', font=('Arialblack 20 bold'),bg=co3, fg=co0)
    label_nome2.place(x=30, y=150)
    label_descricao2 = Label(frame_direita, text='Área de pedidos de compras', 
                            font=('Ivy 10 italic'),bg=co3, fg=co0)
    label_descricao2.place(x=30, y=190)

    #-------------------------------- Criando botao comprar ------------------------------------------------------
    botao_login = Button(frame_direita, text='Comprar', font=('Arial 12 bold'), width=15, height=1,
                        overrelief='ridge', bg=co2, fg=co1)
    botao_login.place(x=30, y=230)


    primeiraTela.mainloop()

tela_login()