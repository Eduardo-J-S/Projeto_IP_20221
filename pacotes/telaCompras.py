from tkinter.ttk import *

from tkinter import *
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

def first_tela_compras():

    #----------------- Criando tela 1 área de compras ---------------------------------------------------
    primeiraTela_compras = Tk()
    primeiraTela_compras.title('Comprar')
    primeiraTela_compras.geometry('500x500+420+100')
    primeiraTela_compras.configure(bg=cor5)
    primeiraTela_compras.resizable(width=FALSE, height=FALSE)
    
    #----------------- Criando frame título da página -----------------------------------------------------
    frame_topo = Frame(primeiraTela_compras, width=500, height=65, bg=cor3, relief='flat')
    frame_topo.grid(row=0, column=0)
    
    frame_baixo = Frame(primeiraTela_compras, width=500, height=435, bg=cor1, relief='flat')
    frame_baixo.grid(row=1, column=0)

    #-------------- Criando labels ------------------------------------------------------------------------
    label_top_compras = Label(frame_topo, text='Faça seu pedido', font=('Arialblack 20 bold'), bg=cor3, fg=cor1)
    label_top_compras.grid(row=0, column=0, padx=140, pady=10)

    label_baixo = Label(frame_baixo, text='Escolha:', font=('Arial 12 bold'), bg=cor1, fg=cor4)
    label_baixo.place(x=15, y=50)

    label_nome_compra = Label(frame_baixo, text='Nome ', font=('Arial 10 bold'), bg=cor5, fg=cor4)
    label_nome_compra.place(x=15, y=100)

    label_telefone_compra = Label(frame_baixo, text='Telefone ', font=('Arial 10 bold'), bg=cor5, fg=cor4)
    label_telefone_compra.place(x=15, y=150)
    
    label_cidade_compra = Label(frame_baixo, text='Cidade ', font=('Arial 10 bold'), bg=cor5, fg=cor4)
    label_cidade_compra.place(x=15, y=200)

    label_bairro_compra = Label(frame_baixo, text='Bairro ', font=('Arial 10 bold'), bg=cor5, fg=cor4)
    label_bairro_compra.place(x=210, y=150)

    label_endereco_compra = Label(frame_baixo, text='Endereço ', font=('Arial 10 bold'), bg=cor5, fg=cor4)
    label_endereco_compra.place(x=210, y=200)

    label_cpf_compra = Label(frame_baixo, text='CPF ', font=('Arial 10 bold'), bg=cor5, fg=cor4)
    label_cpf_compra.place(x=15, y=250)

    label_op_pagamento = Label(frame_baixo, text='Opção de pagamento ', font=('Arial 10 bold'), bg=cor5, fg=cor4)
    label_op_pagamento.place(x=210, y=250)

    label_pagamento_total = Label(frame_baixo, text='Pagamento Total: ', font=('Arial 12 bold'), bg=cor1, fg=cor4)
    label_pagamento_total.place(x=15, y=350)


    #---------------- Criando combobox ------------------------------------------------------------------------
    comprar = Combobox(frame_baixo, width=35)
    comprar['values'] = criarBanco.visu_info()
    comprar.place(x=100, y=53)

    pagamento = Combobox(frame_baixo, width=15)
    pagamento['values'] = ('Crédito', 'Débito', 'Boleto')
    pagamento.place(x=360, y=251)

    #---------------- Criando entradas -------------------------------------------------------------------
    entre_nome_compra = Entry(frame_baixo, width=35, relief='solid')
    entre_nome_compra.place(x=65, y=101)

    entre_telefone_compra = Entry(frame_baixo, width=18, relief='solid')
    entre_telefone_compra.place(x=85, y=151)

    entre_cidade_compra = Entry(frame_baixo, width=20, relief='solid')
    entre_cidade_compra.place(x=75, y=201)

    entre_bairro_compra = Entry(frame_baixo, width=20, relief='solid')
    entre_bairro_compra.place(x=263, y=151)

    entre_endereco_compra = Entry(frame_baixo, width=20, relief='solid')
    entre_endereco_compra.place(x=283, y=201)

    entre_cep_compra = Entry(frame_baixo, width=20, relief='solid')
    entre_cep_compra.place(x=350, y=107)

    entre_cpf_compra = Entry(frame_baixo, width=20, relief='solid')
    entre_cpf_compra.place(x=60, y=251)


    #------------ Criando botão CEP -------------------------------------------------------
    botao_cep_compra = Button(frame_baixo, text='CEP ', font=('Arial 10 bold'), bg=cor2, fg=cor5, overrelief='ridge', relief='raised')
    botao_cep_compra.place(x=300, y=100)


    primeiraTela_compras.mainloop()

