from tkinter.ttk import *
from tkinter import *
from tkinter import messagebox
import pycep_correios
from pacotes import criarBanco
import datetime



# --------------------------------------------- cores --------------------------------------------
cor0 = '#121010'  # Preta / black
cor1 = '#feffff'  # branca / white
cor2 = '#3fb5a3'  # verde / green
cor3 = '#38576b'  # valor / value
cor4 = '#403d3d'   # letra / letters
cor5 = '#e9edf5' # sky blue
cor6 = '#ef5350' #vermelho
cor7 = '#191970' #MidnightBlue
cor8 = '#ffff40' #amarelo claro


def parcela():
    global label_cred_parcela
    total_parcel    
    lista_parcela = []
    parcelam = parcelamento.get()
    lista_parcela.append(parcelam)
    if lista_parcela == lista_parcela['1']:
        tot_parc = 1
    if lista_parcela == lista_parcela['2']:
        tot_parc = 2
    
    tot = preco_quant / tot_parc
    total_parcel = str(tot)
    
    total_parcel = f'parcelas de {tot}'

        
def se_pag_credito():
    if entre_cred_numero.get() == '' or entre_cred_cvv.get() == '' or entre_cred_cpf.get() == '' or entre_cred_vencimento.get() == '':
        messagebox.showerror('ERRO', 'Campos não estão preenchidos')
    else:
        if len(entre_cred_cpf.get()) > 11 or len(entre_cred_cpf.get()) < 11:
            messagebox.showerror('ERRO', 'CPF inválido') 
        else:
            for w in frame_topo_t2.winfo_children():
                w.destroy()

            for w in frame_baixo_t2.winfo_children():
                w.destroy()

            for w in frame_baixo_total_pagameto.winfo_children():
                w.destroy()

            for w in frame_baixo_baixo_t2.winfo_children():
                w.destroy()

            

            listra = '----------------------------------------------------------------------------------'
            #------------------- label topo ----------------------------------------------------------
            label_top_comprovante_cred = Label(frame_topo_t2, text='Comprovante de compra', font=('Arialblack 20 bold'), bg=cor3, fg=cor1)
            label_top_comprovante_cred.grid(row=0, column=0, padx=100, pady=10)

            #---------------- frame credito comprovante --------------------------------------------------
            frame_cred = Frame(frame_baixo_t2, width=450, height=270, bg=cor8, relief='flat')
            frame_cred.place(x=20, y=58)

            #------------------ labels frame credito ------------------------------------------------
            label_cred_lista_cima = Label(frame_cred, text=listra, font=('Arialblack 12 bold'), bg=cor8, fg=cor0, relief='flat')
            label_cred_lista_cima.place(x=10, y=2)

            label_cred_confe = Label(frame_cred, text='CONFERENCIA DE COMPRA', font=('Arialblack 10 bold'), bg=cor8, fg=cor0, relief='flat')
            label_cred_confe.place(x=120, y=19)
        
            label_cred_lista_baixo = Label(frame_cred, text=listra, font=('Arialblack 12 bold'), bg=cor8, fg=cor0, relief='flat')
            label_cred_lista_baixo.place(x=10, y=35)

            label_cred_nome = Label(frame_cred, text='Nome:', font=('Arialblack 10 bold'), bg=cor8, fg=cor0, relief='flat')
            label_cred_nome.place(x=15, y=60)
            
            label_cred_nom = Label(frame_cred, text=nome_var, font=('Arialblack 10 bold'), bg=cor8, fg=cor0, relief='flat')
            label_cred_nom.place(x=61, y=60)

            label_cred_cpf = Label(frame_cred, text='CPF:', font=('Arialblack 10 bold'), bg=cor8, fg=cor0, relief='flat')
            label_cred_cpf.place(x=15, y=80)

            label_cred_CPF = Label(frame_cred, text=cpf_var, font=('Arialblack 10 bold'), bg=cor8, fg=cor0, relief='flat')
            label_cred_CPF.place(x=50, y=80)

            label_cred_produt = Label(frame_cred, text='Produto:', font=('Arialblack 10 bold'), bg=cor8, fg=cor0, relief='flat')
            label_cred_produt.place(x=15, y=100)
            




            label_cred_produto = Label(frame_cred, text=produto_select, font=('Arialblack 10 bold'), bg=cor8, fg=cor0, relief='flat')
            label_cred_produto.place(x=75, y=100)

            label_cred_parcelas = Label(frame_cred, text='Parcelas de:',   font=('Arialblack 10 bold'), bg=cor8, fg=cor0, relief='flat')
            label_cred_parcelas.place(x=15, y=120)

            global label_cred_parcela
            label_cred_parcelas = Label(frame_cred, text='', command=parcela, font=('Arialblack 10 bold'), bg=cor8, fg=cor0, relief='flat')
            label_cred_parcelas.place(x=95, y=120)

            label_cred_total = Label(frame_cred, text='Total:', font=('Arialblack 10 bold'), bg=cor8, fg=cor0, relief='flat')
            label_cred_total.place(x=15, y=140)

            label_cred_tot = Label(frame_cred, text=preco_quant, font=('Arialblack 10 bold'), bg=cor8, fg=cor0, relief='flat')
            label_cred_tot.place(x=53, y=140)

            label_cred_datahora = Label(frame_cred, text='Data e hora:', font=('Arialblack 10 bold'), bg=cor8, fg=cor0, relief='flat')
            label_cred_datahora.place(x=15, y=160)

            label_cred_dataHora = Label(frame_cred, text=datetime.datetime.now(), font=('Arialblack 10 bold'), bg=cor8, fg=cor0, relief='flat')
            label_cred_dataHora.place(x=95, y=160)


            label_deb_lista_final = Label(frame_cred, text=listra, font=('Arialblack 12 bold'), bg=cor8, fg=cor0, relief='flat')
            label_deb_lista_final.place(x=10, y=180)

            #----------------------- botao voltar -------------------------------------------------------------------------------------------
            botao_voltar_cred = Button(frame_baixo_total_pagameto, text='Voltar', command=cancelar_compra, font=('Arial 12'), bg=cor2, fg=cor0, overrelief='ridge', relief='raised', height=1, width=9)
            botao_voltar_cred.place(x=320, y=10)






def se_pag_debito():
    if entre_deb_numero.get() == '' or entre_deb_cpf.get() == '' or entre_deb_vencimento.get() == '':
        messagebox.showerror('ERRO', 'Campos não estão preenchidos')
    else:
        for w in frame_topo_t2.winfo_children():
                w.destroy()

        for w in frame_baixo_t2.winfo_children():
                w.destroy()

        for w in frame_baixo_total_pagameto.winfo_children():
                w.destroy()

        for w in frame_baixo_baixo_t2.winfo_children():
                w.destroy()
        global listra
        listra = '----------------------------------------------------------------------------------'

        #------------------- label topo ----------------------------------------------------------
        label_top_comprovante_deb = Label(frame_topo_t2, text='Comprovante de compra', font=('Arialblack 20 bold'), bg=cor3, fg=cor1)
        label_top_comprovante_deb.grid(row=0, column=0, padx=100, pady=10)

        #---------------- frame debito comprovante --------------------------------------------------
        frame_deb = Frame(frame_baixo_t2, width=450, height=260, bg=cor8, relief='flat')
        frame_deb.place(x=20, y=58)

        #------------------ labels frame debcred ------------------------------------------------
        label_deb_lista_cima = Label(frame_deb, text=listra, font=('Arialblack 12 bold'), bg=cor8, fg=cor0, relief='flat')
        label_deb_lista_cima.place(x=10, y=2)

        label_deb_confe = Label(frame_deb, text='CONFERENCIA DE COMPRA', font=('Arialblack 10 bold'), bg=cor8, fg=cor0, relief='flat')
        label_deb_confe.place(x=120, y=19)

        label_deb_lista_baixo = Label(frame_deb, text=listra, font=('Arialblack 12 bold'), bg=cor8, fg=cor0, relief='flat')
        label_deb_lista_baixo.place(x=10, y=35)

        label_deb_produt = Label(frame_deb, text='Nome:', font=('Arialblack 10 bold'), bg=cor8, fg=cor0, relief='flat')
        label_deb_produt.place(x=15, y=60)
        
        label_ded_produto = Label(frame_deb, text=nome_var, font=('Arialblack 10 bold'), bg=cor8, fg=cor0, relief='flat')
        label_ded_produto.place(x=61, y=60)

        label_deb_valor = Label(frame_deb, text='CPF:', font=('Arialblack 10 bold'), bg=cor8, fg=cor0, relief='flat')
        label_deb_valor.place(x=15, y=80)

        label_deb_val = Label(frame_deb, text=cpf_var, font=('Arialblack 10 bold'), bg=cor8, fg=cor0, relief='flat')
        label_deb_val.place(x=50, y=80)

        label_deb_datahora = Label(frame_deb, text='Produto:', font=('Arialblack 10 bold'), bg=cor8, fg=cor0, relief='flat')
        label_deb_datahora.place(x=15, y=100)

        label_deb_dataHora = Label(frame_deb, text=produto_select, font=('Arialblack 10 bold'), bg=cor8, fg=cor0, relief='flat')
        label_deb_dataHora.place(x=75, y=100)

        label_deb_nome = Label(frame_deb, text='Total:', font=('Arialblack 10 bold'), bg=cor8, fg=cor0, relief='flat')
        label_deb_nome.place(x=15, y=120)

        label_deb_Nome = Label(frame_deb, text=preco_quant, font=('Arialblack 10 bold'), bg=cor8, fg=cor0, relief='flat')
        label_deb_Nome.place(x=53, y=120)

        label_deb_cpf = Label(frame_deb, text='Data e hora:', font=('Arialblack 10 bold'), bg=cor8, fg=cor0, relief='flat')
        label_deb_cpf.place(x=15, y=140)

        label_deb_CPF = Label(frame_deb, text=datetime.datetime.now(), font=('Arialblack 10 bold'), bg=cor8, fg=cor0, relief='flat')
        label_deb_CPF.place(x=95, y=140)

        label_deb_lista_final = Label(frame_deb, text=listra, font=('Arialblack 12 bold'), bg=cor8, fg=cor0, relief='flat')
        label_deb_lista_final.place(x=10, y=170)

        #----------------------- botao voltar -------------------------------------------------------------------------------------------
        botao_voltar_deb = Button(frame_baixo_total_pagameto, text='Voltar', command=cancelar_compra, font=('Arial 12'), bg=cor2, fg=cor0, overrelief='ridge', relief='raised', height=1, width=9)
        botao_voltar_deb.place(x=320, y=10)





def se_pag_pix():
    for w in frame_topo_t2.winfo_children():
            w.destroy()

    for w in frame_baixo_t2.winfo_children():
            w.destroy()

    for w in frame_baixo_total_pagameto.winfo_children():
            w.destroy()

    for w in frame_baixo_baixo_t2.winfo_children():
            w.destroy()

    pix_cop_cola = '''00020126580014br.gov.bcb.pix0136f02eb187-570d-44b5-b4
    ba-0f99e5a44b505204000053039865802BR5921
    Eduardo Jose Da Silva6009Sao Paulo62070503***630470A7'''


    #------------------- label topo ----------------------------------------------------------
    label_top_comprovante = Label(frame_topo_t2, text='Comprovante de compra', font=('Arialblack 20 bold'), bg=cor3, fg=cor1)
    label_top_comprovante.grid(row=0, column=0, padx=100, pady=10)


    #---------------- frame pix comprovante --------------------------------------------------
    frame_pix = Frame(frame_baixo_t2, width=450, height=260, bg=cor8, relief='flat')
    frame_pix.place(x=20, y=58)

    label_pix_chave = Label(frame_pix, text=pix_cop_cola, font=('Arialblack 10 bold'), bg=cor1, fg=cor0, relief='solid')
    label_pix_chave.place(x=30, y=30)
    
    def copiar():
        copiando = pix_cop_cola
        frame_pix.clipboard_clear()
        frame_pix.clipboard_append(copiando)
        messagebox.showinfo('Copiado', 'Chave copiada com sucesso')

    #----------------------- botao copiar -------------------------------------------
    botao_pix = Button(frame_pix, text='Copiar', command=copiar, font=('Arial 12'), bg=cor2, fg=cor0, overrelief='ridge', relief='raised', height=1, width=9)
    botao_pix.place(x=170, y=100)

    #----------------------- botao voltar -------------------------------------------------------------------------------------------
    botao_voltar_pix = Button(frame_baixo_total_pagameto, text='Voltar', command=cancelar_compra, font=('Arial 12'), bg=cor2, fg=cor0, overrelief='ridge', relief='raised', height=1, width=9)
    botao_voltar_pix.place(x=320, y=10)


def cancelar_compra():
    segundaTela_compras.destroy()
    first_tela_compras()


def selecionar():
    opcao_de_pagamento = pagamento.get()
    print(opcao_de_pagamento)

    opc_pagar = ['Crédito', 'Débito', 'PIX']

    if opcao_de_pagamento == opc_pagar[0]:
        for w in frame_baixo_baixo_t2.winfo_children():
            w.destroy()
        #---------------- labels do cartao de credito --------------------------------------------
        label_cred_numero = Label(frame_baixo_baixo_t2, text='Número do cartão: ', font=('Arialblack 11 bold'), bg=cor1, fg=cor0)
        label_cred_numero.place(x=15, y=5)
        
        label_cred_cvv = Label(frame_baixo_baixo_t2, text='CVV: ', font=('Arialblack 11 bold'), bg=cor1, fg=cor0)
        label_cred_cvv.place(x=15, y=35)

        label_cred_cpf = Label(frame_baixo_baixo_t2, text='CPF titular: ', font=('Arialblack 11 bold'), bg=cor1, fg=cor0)
        label_cred_cpf.place(x=200, y=35)

        label_cred_vencimento = Label(frame_baixo_baixo_t2, text='Vencimento do cartão: ', font=('Arialblack 11 bold'), bg=cor1, fg=cor0)
        label_cred_vencimento.place(x=15, y=65)

        #------------------------- criando as entradas do cartao de credito ----------------------------------------------
        global entre_cred_numero 
        global entre_cred_cvv
        global entre_cred_cpf
        global entre_cred_vencimento

        entre_cred_numero = Entry(frame_baixo_baixo_t2, width=20, relief='solid')
        entre_cred_numero.place(x=157, y=7)

        entre_cred_cvv = Entry(frame_baixo_baixo_t2, width=15, relief='solid')
        entre_cred_cvv.place(x=59, y=38)

        entre_cred_cpf = Entry(frame_baixo_baixo_t2, width=15, relief='solid')
        entre_cred_cpf.place(x=292, y=38)

        entre_cred_vencimento = Entry(frame_baixo_baixo_t2, width=15, relief='solid')
        entre_cred_vencimento.place(x=184, y=68)

        #--------------------- criando combobox do cartao de credito ---------------------------------------------
        global parcelamento
        parcelamento = Combobox(frame_baixo_baixo_t2, width=15)
        parcelamento['values'] = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12')
        parcelamento.current(0)
        parcelamento.place(x=15, y=95)

        #-------------------- criando botao confirmar comprar -------------------------------------------------------
        botao_selcionar_opc = Button(frame_baixo_baixo_t2, command=se_pag_credito + parcela, text='Confirmar compra ', font=('Arial 13 bold'), bg=cor2, fg=cor0, overrelief='ridge', relief='raised', height=1, width=15)
        botao_selcionar_opc.place(x=320, y=95)


    if opcao_de_pagamento == opc_pagar[1]:
        for w in frame_baixo_baixo_t2.winfo_children():
            w.destroy()


        #---------------- labels do cartao de debito --------------------------------------------
        label_deb_numero = Label(frame_baixo_baixo_t2, text='Número do cartão: ', font=('Arialblack 11 bold'), bg=cor1, fg=cor0)
        label_deb_numero.place(x=15, y=5)

        label_deb_cpf = Label(frame_baixo_baixo_t2, text='CPF titular: ', font=('Arialblack 11 bold'), bg=cor1, fg=cor0)
        label_deb_cpf.place(x=15, y=35)

        label_deb_vencimento = Label(frame_baixo_baixo_t2, text='Vencimento do cartão: ', font=('Arialblack 11 bold'), bg=cor1, fg=cor0)
        label_deb_vencimento.place(x=15, y=65)

        #------------------ criando entradas para o cartao de debito --------------------------------
        global entre_deb_numero
        global entre_deb_cpf
        global entre_deb_vencimento

        entre_deb_numero = Entry(frame_baixo_baixo_t2, width=20, relief='solid')
        entre_deb_numero.place(x=157, y=7)

        entre_deb_cpf = Entry(frame_baixo_baixo_t2, width=15, relief='solid')
        entre_deb_cpf.place(x=108, y=38)

        entre_deb_vencimento = Entry(frame_baixo_baixo_t2, width=15, relief='solid')
        entre_deb_vencimento.place(x=184, y=68)

        #-------------------- criando botao confirmar comprar -------------------------------------------------------
        botao_selcionar_opc = Button(frame_baixo_baixo_t2, command=se_pag_debito, text='Confirmar compra ', font=('Arial 13 bold'), bg=cor2, fg=cor0, overrelief='ridge', relief='raised', height=1, width=15)
        botao_selcionar_opc.place(x=320, y=95)

    if opcao_de_pagamento == opc_pagar[2]:
        for w in frame_baixo_baixo_t2.winfo_children():
            w.destroy()
        texto = '''Clique no botão confirmar compra para ser
        gerado um pix copia e cola e efetuar o pagamento!'''
        label_mensagem_pix = Label(frame_baixo_baixo_t2, text=texto, font=('Arialblack 10 bold'), bg=cor1, fg=cor0)
        label_mensagem_pix.place(x=10, y=35)

        #-------------------- criando botao confirmar comprar -------------------------------------------------------
        botao_selcionar_opc = Button(frame_baixo_baixo_t2, command=se_pag_pix, text='Confirmar compra ', font=('Arial 13 bold'), bg=cor2, fg=cor0, overrelief='ridge', relief='raised', height=1, width=15)
        botao_selcionar_opc.place(x=320, y=95)
        



def confirmar():
    global nome_var
    global cpf_var
    global endereco_var
    global bairro_var
    global cidade_var
    global uf_var
    global telefone_var
    global preco_quant
    global produto_select

    try:

        nome_var = entre_nome_compra.get().strip()
        cpf_var = entre_cpf_compra.get().strip()
        endereco_var = entre_endereco_compra.get().strip()
        bairro_var = entre_bairro_compra.get().strip()
        cidade_var = entre_cidade_compra.get().strip()
        uf_var = entre_uf_compra.get().strip()
        telefone_var = entre_telefone_compra.get().strip()


        quantidade = spin_qnt.get()
        print(quantidade)
        produto_select = comprar.get()
        print(produto_select)
        
         
        if nome_var == '' or cpf_var == '' or endereco_var == '' or bairro_var == '' or cidade_var == '' or uf_var == '' or telefone_var == '':
            messagebox.showerror('ERRO', 'Campos não estão preenchidos') 
        else:
            if len(cpf_var) > 11 or len(cpf_var) < 11:
                messagebox.showerror('ERRO', 'CPF inválido') 

            else:

                lista_produtos = criarBanco.visu_info()
                produto = []

                for linha in lista_produtos:
                    if produto_select in linha:
                        produto.append(linha)
                print(produto)
                preco_quant = int(produto[0][3]) * int(quantidade)
                print(f'{int(produto[0][3]) * int(quantidade)}')

                primeiraTela_compras.destroy()
                second_tela_compras()

    except:
        messagebox.showerror('ERRO', 'Algum campo não foi preenchido corretamente!')    


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
        entre_endereco_compra.insert('end', dados_cep['logradouro'])
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
    global primeiraTela_compras
    


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
    
    #-------------- criando botao confirmar -------------------------------------------
    botao_confirmar_pedido = Button(frame_baixo, command=confirmar, text='Confirmar ', font=('Arial 13 bold'), bg=cor2, fg=cor0, overrelief='ridge', relief='raised', height=1)
    botao_confirmar_pedido.place(x=15, y=350)


    primeiraTela_compras.mainloop()

def second_tela_compras():
    global frame_baixo_baixo_t2
    global segundaTela_compras
    global frame_topo_t2
    global frame_baixo_t2
    global frame_baixo_total_pagameto

    #----------------- Criando tela 2 área de compras ---------------------------------------------------
    segundaTela_compras = Tk()
    segundaTela_compras.title('Comprar')
    segundaTela_compras.geometry('500x500+420+100')
    segundaTela_compras.configure(bg=cor5)
    segundaTela_compras.resizable(width=FALSE, height=FALSE)

    #----------------- Criando frames da página -----------------------------------------------------
    frame_topo_t2 = Frame(segundaTela_compras, width=500, height=65, bg=cor3, relief='flat')
    frame_topo_t2.grid(row=0, column=0)
    
    frame_baixo_t2 = Frame(segundaTela_compras, width=500, height=260, bg=cor1, relief='flat')
    frame_baixo_t2.place(x=0, y=58)

    frame_baixo_baixo_t2 = Frame(segundaTela_compras, width=500, height=130, bg=cor1, relief='flat')
    frame_baixo_baixo_t2.place(x=0, y=318)

    frame_baixo_total_pagameto = Frame(segundaTela_compras, width=500, height=54, bg=cor1, relief='flat')
    frame_baixo_total_pagameto.place(x=0, y=448)

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

    label_total_pagamento = Label(frame_baixo_total_pagameto, text='Pegamento total: ', font=('Arialblack 11 bold'), bg=cor1, fg=cor0)
    label_total_pagamento.place(x=15, y=10)
    
    label_total = Label(frame_baixo_total_pagameto, text=preco_quant, font=('Arialblack 11 bold'), bg=cor1, fg=cor0)
    label_total.place(x=139, y=10)

    #------------------ criando combobox ---------------------------------
    global pagamento
    pagamento = Combobox(frame_baixo_t2, width=15)
    pagamento['values'] = ('Crédito', 'Débito', 'PIX')
    pagamento.current(0)
    pagamento.place(x=185, y=232)


    #------------------- criando botao opc comprar --------------------------------------------
    botao_selcionar_opc = Button(frame_baixo_t2, command=selecionar, text='Selecionar ', font=('Arial 13 bold'), bg=cor2, fg=cor0, overrelief='ridge', relief='raised', height=1, width=10)
    botao_selcionar_opc.place(x=320, y=225)

    #-------------------- criando botao cancelar comprar -------------------------------------------------------
    botao_selcionar_opc = Button(frame_baixo_total_pagameto, command=cancelar_compra, text='Cancelar compra ', font=('Arial 13 bold'), bg=cor6, fg=cor0, overrelief='ridge', relief='raised', height=1, width=15)
    botao_selcionar_opc.place(x=320, y=10)

    segundaTela_compras.mainloop()