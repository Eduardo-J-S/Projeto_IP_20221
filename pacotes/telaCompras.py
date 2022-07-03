from tkinter.ttk import *

from tkinter import *
from tkinter import messagebox
import mysql.connector
import pycep_correios
from pacotes import criarBanco


# --------------------------------------------- cores --------------------------------------------
cor0 = '#121010'  # Preta / black
cor1 = '#feffff'  # branca / white
cor2 = '#3fb5a3'  # verde / green
cor3 = '#38576b'  # valor / value
cor4 = '#403d3d'   # letra / letters
cor5 = '#e9edf5' # sky blue
cor6 = '#ef5350' #vermelho
cor7 = '#191970' #MidnightBlue



def confirmar():
    global nome_var
    global cpf_var
    global endereco_var
    global bairro_var
    global cidade_var
    global uf_var
    global telefone_var
    global preco_quant


    nome_var = entre_nome_compra.get()
    cpf_var = entre_cpf_compra.get()
    endereco_var = entre_endereco_compra.get()
    bairro_var = entre_bairro_compra.get()
    cidade_var = entre_cidade_compra.get()
    uf_var = entre_uf_compra.get()
    telefone_var = entre_telefone_compra.get()



    quantidade = spin_qnt.get()
    print(quantidade)
    produto_select = comprar.get()
    print(produto_select)

    lista_produtos = criarBanco.visu_info()
    produto = []

    for linha in lista_produtos:
        if produto_select in linha:
            produto.append(linha)
    print(produto)
    preco_quant = int(produto[0][3]) * int(quantidade)
    print(f'{int(produto[0][3]) * int(quantidade)}')
    second_tela_compras()


def cep():
    try:
        entre_cidade_compra.delete(0, 'end')
        entre_bairro_compra.delete(0, 'end')
        entre_endereco_compra.delete(0, 'end')
        entre_uf_compra.delete(0, 'end')
        cep = entre_cep_compra.get()
        dados_cep = pycep_correios.get_address_from_cep(cep)
        entre_cidade_compra.insert('end', dados_cep['cidade'])
        entre_bairro_compra.insert('end', dados_cep['bairro'])
        endereco_var = entre_endereco_compra.insert('end', dados_cep['logradouro'])
        entre_uf_compra.insert('end', dados_cep['uf'])
    except:
        messagebox.showerror('ERRO', 'CEP inexistente')




def first_tela_compras():
    global entre_cidade_compra
    global entre_bairro_compra
    global entre_endereco_compra
    global entre_cep_compra
    global entre_uf_compra
    global comprar
    global spin_qnt
    global entre_nome_compra
    global entre_telefone_compra
    global entre_cpf_compra
    global pagamento
    


    #----------------- Criando tela 1 área de compras ---------------------------------------------------
    primeiraTela_compras = Tk()
    primeiraTela_compras.title('Comprar')
    primeiraTela_compras.geometry('500x500+420+100')
    primeiraTela_compras.configure(bg=cor5)
    primeiraTela_compras.resizable(width=FALSE, height=FALSE)
    
    #----------------- Criando frames da página -----------------------------------------------------
    frame_topo = Frame(primeiraTela_compras, width=500, height=65, bg=cor3, relief='flat')
    frame_topo.grid(row=0, column=0)
    
    frame_baixo = Frame(primeiraTela_compras, width=500, height=435, bg=cor1, relief='flat')
    frame_baixo.grid(row=1, column=0)

    #-------------- Criando labels ------------------------------------------------------------------------
    label_top_compras = Label(frame_topo, text='Faça seu pedido', font=('Arialblack 20 bold'), bg=cor3, fg=cor1)
    label_top_compras.grid(row=0, column=0, padx=140, pady=10)

    label_baixo = Label(frame_baixo, text='Escolha:', font=('Arial 12 bold'), bg=cor1, fg=cor4)
    label_baixo.place(x=15, y=50)

    label_baixo = Label(frame_baixo, text='Qnt.:', font=('Arial 12 bold'), bg=cor1, fg=cor4)
    label_baixo.place(x=340, y=50)

    label_nome_compra = Label(frame_baixo, text='Nome ', font=('Arial 10 bold'), bg=cor5, fg=cor4)
    label_nome_compra.place(x=15, y=100)

    label_telefone_compra = Label(frame_baixo, text='Telefone ', font=('Arial 10 bold'), bg=cor5, fg=cor4)
    label_telefone_compra.place(x=15, y=150)
    
    label_cidade_compra = Label(frame_baixo, text='Cidade ', font=('Arial 10 bold'), bg=cor5, fg=cor4)
    label_cidade_compra.place(x=15, y=200)

    label_uf_compra = Label(frame_baixo, text='UF ', font=('Arial 10 bold'), bg=cor5, fg=cor4)
    label_uf_compra.place(x=180, y=200)

    label_bairro_compra = Label(frame_baixo, text='Bairro ', font=('Arial 10 bold'), bg=cor5, fg=cor4)
    label_bairro_compra.place(x=210, y=150)

    label_endereco_compra = Label(frame_baixo, text='Endereço ', font=('Arial 10 bold'), bg=cor5, fg=cor4)
    label_endereco_compra.place(x=15, y=250)

    label_cpf_compra = Label(frame_baixo, text='CPF ', font=('Arial 10 bold'), bg=cor5, fg=cor4)
    label_cpf_compra.place(x=295, y=250)


    #---------------- Criando combobox ------------------------------------------------------------------------
    
    comprar = Combobox(frame_baixo, width=35)
    comprar['values'] = criarBanco.visu_produto()
    comprar.current(0)
    comprar.place(x=100, y=53)

    #------------------- Criando Spinbox ---------------------------------------------------------------------
    spin_qnt = Spinbox(frame_baixo, from_= 1, to=10, width=10)
    spin_qnt.place(x=382, y=52)

    #---------------- Criando entradas -------------------------------------------------------------------
    entre_nome_compra = Entry(frame_baixo, width=35, relief='solid')
    entre_nome_compra.place(x=65, y=101)

    entre_telefone_compra = Entry(frame_baixo, width=18, relief='solid')
    entre_telefone_compra.place(x=85, y=151)

    entre_cidade_compra = Entry(frame_baixo, width=15, relief='solid')
    entre_cidade_compra.place(x=75, y=201)

    entre_bairro_compra = Entry(frame_baixo, width=20, relief='solid')
    entre_bairro_compra.place(x=263, y=151)

    entre_endereco_compra = Entry(frame_baixo, width=30, relief='solid')
    entre_endereco_compra.place(x=90, y=251)

    entre_cep_compra = Entry(frame_baixo, width=20, relief='solid')
    entre_cep_compra.place(x=350, y=107)

    entre_cpf_compra = Entry(frame_baixo, width=20, relief='solid')
    entre_cpf_compra.place(x=330, y=251)

    entre_uf_compra = Entry(frame_baixo, width=3, relief='solid')
    entre_uf_compra.place(x=209, y=201)


    #------------ Criando botão CEP -------------------------------------------------------
    botao_cep_compra = Button(frame_baixo, command=cep, text='CEP ', font=('Arial 10 bold'), bg=cor2, fg=cor5, overrelief='ridge', relief='raised')
    botao_cep_compra.place(x=300, y=100)
    
    botao_confirmar_pedido = Button(frame_baixo, command=confirmar, text='Confirmar ', font=('Arial 13 bold'), bg=cor2, fg=cor0, overrelief='ridge', relief='raised', height=1)
    botao_confirmar_pedido.place(x=15, y=350)


    primeiraTela_compras.mainloop()

def second_tela_compras():

    #----------------- Criando tela 2 área de compras ---------------------------------------------------
    segundaTela_compras = Tk()
    segundaTela_compras.title('Comprar')
    segundaTela_compras.geometry('500x500+420+100')
    segundaTela_compras.configure(bg=cor5)
    segundaTela_compras.resizable(width=FALSE, height=FALSE)

    #----------------- Criando frames da página -----------------------------------------------------
    frame_topo_t2 = Frame(segundaTela_compras, width=500, height=65, bg=cor3, relief='flat')
    frame_topo_t2.grid(row=0, column=0)
    
    frame_baixo_t2 = Frame(segundaTela_compras, width=500, height=435, bg=cor1, relief='flat')
    frame_baixo_t2.place(x=0, y=58)

    #-------------- Criando labels ------------------------------------------------------------------------
    label_top_conf_pedido = Label(frame_topo_t2, text='Confirmação do pedido', font=('Arialblack 20 bold'), bg=cor3, fg=cor1)
    label_top_conf_pedido.grid(row=0, column=0, padx=110, pady=10)

    label_nome_conf = Label(frame_baixo_t2, text='Nome: ', font=('Arialblack 10 bold'), bg=cor1, fg=cor0)
    label_nome_conf.place(x=15, y=30)

    label_nome_var = Label(frame_baixo_t2, text= nome_var, font=('Arialblack 10 bold'), bg=cor1, fg=cor0)
    label_nome_var.place(x=60, y=30)

    label_endereco_conf = Label(frame_baixo_t2, text='Endereço: ', font=('Arialblack 10 bold'), bg=cor1, fg=cor0)
    label_endereco_conf.place(x=15, y=60)

    label_endereco_var = Label(frame_baixo_t2, text= endereco_var, font=('Arialblack 10 bold'), bg=cor1, fg=cor0)
    label_endereco_var.place(x=84, y=60)

    label_bairro_conf = Label(frame_baixo_t2, text='Bairro: ', font=('Arialblack 10 bold'), bg=cor1, fg=cor0)
    label_bairro_conf.place(x=15, y=90)

    label_bairro_var = Label(frame_baixo_t2, text= bairro_var, font=('Arialblack 10 bold'), bg=cor1, fg=cor0)
    label_bairro_var.place(x=65, y=90)

    label_cidade_conf = Label(frame_baixo_t2, text='Cidade: ', font=('Arialblack 10 bold'), bg=cor1, fg=cor0)
    label_cidade_conf.place(x=15, y=120)

    label_cidade_var = Label(frame_baixo_t2, text= cidade_var, font=('Arialblack 10 bold'), bg=cor1, fg=cor0)
    label_cidade_var.place(x=70, y=120)

    label_uf_conf = Label(frame_baixo_t2, text='UF: ', font=('Arialblack 10 bold'), bg=cor1, fg=cor0)
    label_uf_conf.place(x=250, y=120)

    label_uf_var = Label(frame_baixo_t2, text=uf_var, font=('Arialblack 10 bold'), bg=cor1, fg=cor0)
    label_uf_var.place(x=280, y=120)

    label_telefone_conf = Label(frame_baixo_t2, text='Telefone: ', font=('Arialblack 10 bold'), bg=cor1, fg=cor0)
    label_telefone_conf.place(x=15, y=150)

    label_telefone_conf = Label(frame_baixo_t2, text= telefone_var, font=('Arialblack 9 bold'), bg=cor1, fg=cor0)
    label_telefone_conf.place(x=84, y=150)

    label_cpf_conf = Label(frame_baixo_t2, text='CPF: ', font=('Arialblack 10 bold'), bg=cor1, fg=cor0)
    label_cpf_conf.place(x=15, y=180)

    label_cpf_var = Label(frame_baixo_t2, text=cpf_var, font=('Arialblack 9 bold'), bg=cor1, fg=cor0)
    label_cpf_var.place(x=49, y=180)

    label_opc_pagamento = Label(frame_baixo_t2, text='Opção de pagamento: ', font=('Arialblack 11 bold'), bg=cor1, fg=cor0)
    label_opc_pagamento.place(x=15, y=230)

    label_total_pagamento = Label(frame_baixo_t2, text='Pegamento total: ', font=('Arialblack 11 bold'), bg=cor1, fg=cor0)
    label_total_pagamento.place(x=15, y=400)
    
    label_total = Label(frame_baixo_t2, text=preco_quant, font=('Arialblack 11 bold'), bg=cor1, fg=cor0)
    label_total.place(x=139, y=400)

    #------------------ criando combobox ---------------------------------
    pagamento = Combobox(frame_baixo_t2, width=15)
    pagamento['values'] = ('Crédito', 'Débito', 'Boleto')
    pagamento.current(0)
    pagamento.place(x=185, y=232)

    def selecionar():
        pagamento_cred = pagamento.get()
        print(pagamento_cred)

    #------------------- criando botao opc comprar --------------------------------------------
    botao_selcionar_opc = Button(frame_baixo_t2, command=selecionar, text='Selecionar ', font=('Arial 13 bold'), bg=cor2, fg=cor0, overrelief='ridge', relief='raised', height=1, width=10)
    botao_selcionar_opc.place(x=320, y=227)


    segundaTela_compras.mainloop()