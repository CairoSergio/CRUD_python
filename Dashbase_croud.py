from tkinter import *
from tkinter import ttk
import DashBase
from tkinter import messagebox
import random


def CORUD():
    def atualizar():
        try:
            def confirmar():
                ident = valores[2]
                print(ident)
                numeros = "123456789"
                resetsenha = "".join(random.sample(numeros,6))
                nome = nome_ent.get()
                email = Email_ent.get()
                senha = Senha_ent.get()
                confsenha = Senha_ent.get()
                DashBase.cursor.execute("SELECT * FROM pessoas")
                verificado = DashBase.cursor.fetchall()
                DashBase.cursor.execute("SELECT id FROM pessoas WHERE email = ?",[ident])
                email_verify = DashBase.cursor.fetchone()
                email_tupaado = email_verify[0]
                print(email_tupaado)
                if (nome =="" or email=="" or senha=="" or confsenha==""):
                    messagebox.showerror(title="Ocoreu um erro", message="Eroo, verifique se todos os campos estao preenchidos")
                else:
                    if(nome in verificado and email in verificado and senha in verificado):
                        messagebox.showerror(title="Erro", message="esses dados ja existem")
                    else:
                        if(nome in verificado and email in verificado):
                            messagebox.showerror(title='ERRO', message="O seu email e a sua senha ja estao cadastrados")
                        else:
                            if(len(senha)<5):
                                messagebox.showerror(title="Erro", message="a sua senha precisa ter no minimo 6 digitos")
                            else:
                                if(senha!= confsenha):
                                    messagebox.showerror(title="Erro", message="A sua senha precisa ser igual a confirmaçao")
                                else:
                                    print(nome, email, senha , resetsenha)
                                    DashBase.cursor.execute("""
                                    UPDATE pessoas SET nome = ?
                                    WHERE id = ?
                                    """,(nome,email_tupaado))
                                    DashBase.cursor.execute("""
                                    UPDATE pessoas SET email = ?
                                    WHERE id = ?
                                    """,(email,email_tupaado))
                                    DashBase.cursor.execute("""
                                    UPDATE pessoas SET senha = ?
                                    WHERE id = ?
                                    """,(senha,email_tupaado))
                                    DashBase.banco.commit()
                                    messagebox.showinfo(title="Informaçoes do cadastro", message="Atualizou as sua informaçoes com sucesso")
                                    Croud.destroy()
                                    CORUD()
            nome = nome_ent.get()
            email = Email_ent.get()
            senha = Senha_ent.get()
            tree_dados = tree.focus()
            tree_dicionario = tree.item(tree_dados)
            tree_lista = tree_dicionario['values']
            valores = tree_lista
            nome_ent.delete(0, 'end')
            Email_ent.delete(0, 'end')
            Senha_ent.delete(0, 'end')
            Pass_reset_ent.delete(0, 'end')

            nome_ent.insert(0, valores[1])
            Email_ent.insert(0, valores[2])
            Senha_ent.insert(0, valores[3])
            Pass_reset_ent.insert(0, valores[3])
            button_atualizar.destroy()
            button_confi = Button(width=38,bg='#4a9', text="CONFIRMAR",fg='#fff', command=confirmar)
            button_confi.place(x=8, y=325)
        except:
            DashBase.banco.rollback()
            messagebox.showerror('errro', 'Erro ao autualizar')
    def delete():
        def conf_delete():
            ident = str(valores[0])
            print(ident)
            try:
                DashBase.cursor.execute("DELETE FROM pessoas WHERE id = ?",(ident))
                DashBase.banco.commit()
                messagebox.showinfo('Sucesso', 'Registro excluido com sucesso!')
                Croud.destroy()
                CORUD()
            except IndexError:
                DashBase.banco.rollback()
                messagebox.showerror('Erro', 'Erro ao excluir registro!')


        nome = nome_ent.get()
        email = Email_ent.get()
        senha = Senha_ent.get()
        tree_dados = tree.focus()
        tree_dicionario = tree.item(tree_dados)
        tree_lista = tree_dicionario['values']
        valores = tree_lista
        nome_ent.delete(0, 'end')
        Email_ent.delete(0, 'end')
        Senha_ent.delete(0, 'end')
        Pass_reset_ent.delete(0, 'end')
        
        nome_ent.insert(0, valores[1])
        Email_ent.insert(0, valores[2])
        Senha_ent.insert(0, valores[3])
        Pass_reset_ent.insert(0, valores[3])
        button_delete.destroy()
        button_conf_delete = Button(width=38,bg='#4a9',text="DELETE",fg='#fff', command=conf_delete)
        button_conf_delete.place(x=8, y=360)
        print(valores)
    def Registar():
        numeros = "123456789"
        numeros2 = "987654321"
        resetsenha = "".join(random.sample(numeros,6))
        numero_conta = "".join(random.sample(numeros+numeros2, 10))
        nome = nome_ent.get()
        email = Email_ent.get()
        senha = Senha_ent.get()
        confsenha = Senha_ent.get()
        DashBase.cursor.execute("SELECT * FROM pessoas")
        verificado = DashBase.cursor.fetchall()
        if (nome =="" or email=="" or senha=="" or confsenha==""):
            messagebox.showerror(title="Ocoreu um erro", message="Eroo, verifique se todos os campos estao preenchidos")
        else:
            if(nome in verificado and email in verificado and senha in verificado):
                messagebox.showerror(title="Erro", message="esses dados ja existem")
            else:
                if(nome in verificado and email in verificado):
                    messagebox.showerror(title='ERRO', message="O seu email e a sua senha ja estao cadastrados")
                else:
                    if(len(senha)<5):
                        messagebox.showerror(title="Erro", message="a sua senha precisa ter no minimo 6 digitos")
                    else:
                        if(senha!= confsenha):
                            messagebox.showerror(title="Erro", message="A sua senha precisa ser igual a confirmaçao")
                        else:
                            DashBase.cursor.execute("""
                            INSERT INTO pessoas(nome, email,senha,numero_conta,password_reset) VALUES(?,?,?,?,?)
                            """, (nome, email, senha,numero_conta, resetsenha))
                            DashBase.banco.commit()
                            messagebox.showinfo(title="Informaçoes do cadastro", message="Registou com sucesso")
                            Croud.destroy()
                            CORUD()
    def banir():
        def conf_ban():
            ident = str(valores[0])
            print(ident)
            status = str(False)
            try:
                DashBase.cursor.execute("UPDATE pessoas SET status = ? WHERE id = ?",(status,ident))
                DashBase.banco.commit()
                messagebox.showinfo('Sucesso', 'Conta Banida com sucesso!')
                Croud.destroy()
                CORUD()
            except:
                DashBase.banco.rollback()
                messagebox.showerror('Erro', 'Erro ao excluir registro!')


        nome = nome_ent.get()
        email = Email_ent.get()
        senha = Senha_ent.get()
        tree_dados = tree.focus()
        tree_dicionario = tree.item(tree_dados)
        tree_lista = tree_dicionario['values']
        valores = tree_lista
        nome_ent.delete(0, 'end')
        Email_ent.delete(0, 'end')
        Senha_ent.delete(0, 'end')
        Pass_reset_ent.delete(0, 'end')
        
        nome_ent.insert(0, valores[1])
        Email_ent.insert(0, valores[2])
        Senha_ent.insert(0, valores[3])
        Pass_reset_ent.insert(0, valores[3])
        print(valores)
        button_banir.destroy()
        button_conf = Button(width=38,bg='#ff0000',text="BANIR",fg='#fff', command=conf_ban)
        button_conf.place(x=8, y=395)
    Croud =Tk()
    Croud.title('Formulario | CRUD')
    Croud.geometry('1310x430')
    Croud.resizable(width=False,height=False)


    frame_direita = Frame(Croud, width=600, height=300,relief='flat')
    frame_direita.grid(column=1, row=0,rowspan=2,padx=1,pady=0, sticky=NSEW)
    frame_esquerda = Frame(Croud, width=290, height=500)
    frame_esquerda.grid(column=0,row=0)
    frame_detalhes = Frame(Croud,width=280, height=500)
    frame_detalhes.grid(column=2,row=0)
    title = Label(frame_esquerda,text="Formulario CRUD", fg="#fff", bg="#4a9",width=33,height=3,anchor='center', font="3")
    title.place(x=0,  y=0)
    title = Label(frame_detalhes,text="Detalhes", fg="#fff", bg="#4a9",width=33,height=3,anchor='center', font="3")
    title.place(x=0,  y=0)
    def mostrar():
        def disban():
            tree_dados = tree.focus()
            tree_dicionario = tree.item(tree_dados)
            tree_lista = tree_dicionario['values']
            valores = tree_lista
            ident = str(valores[0])
            print(ident)
            status = state_ent.get()
            try:
                DashBase.cursor.execute("UPDATE pessoas SET status = ? WHERE id = ?",(status,ident))
                DashBase.banco.commit()
                messagebox.showinfo('Sucesso', 'Conta Banida com sucesso!')
                Croud.destroy()
                CORUD()
            except:
                DashBase.banco.rollback()
                messagebox.showerror('Erro', 'Erro ao excluir registro!')

        tree_dados = tree.focus()
        tree_dicionario = tree.item(tree_dados)
        tree_lista = tree_dicionario['values']
        valores = tree_lista
        print(valores)
        numeero_lab = Label(frame_detalhes,text=f"Nr daconta: {valores[4]}",font='14')
        numeero_lab.place(x=45,y=100)
        state = Label(frame_detalhes,text="Status:",font='12')
        state.place(x=35,y=125)
        state_ent = Entry(frame_detalhes,width=10)
        state_ent.place(x=90,y=125)
        btn_disBan = Button(frame_detalhes,text="salvar", bg="#4a9", fg="#fff", command=disban)
        btn_disBan.place(x=160,y=125)
        state_ent.insert(0,valores[6])
        operacoes = Frame(frame_detalhes,width=270,height=300, borderwidth=1,relief=RIDGE )
        operacoes.place(x=10,y=150)
        opera =[
            'levantamento',
            'deposito',
            'trasferencia',
            'Recebeu',
            'comprou'
        ]
        posi = 0
        for trans in opera:
            oo = Label(operacoes,text=trans)
            oo.place(x=10,y=posi)
            posi+=20
    detalhes = Button(frame_detalhes,text="Ver detalhes pessoais",width=40, command=mostrar,bg="#4a9", fg="#fff")
    detalhes.place(x=5, y=70)

    nome_lab = Label(text='NOME')
    nome_lab.place(x=8, y=70)

    nome_ent = Entry(width=45)
    nome_ent.place(x=8, y=95)

    Email_lab = Label(text='EMAIL')
    Email_lab.place(x=8, y=130)

    Email_ent = Entry(width=45)
    Email_ent.place(x=8, y=155)

    Senha_lab = Label(text='SENHA')
    Senha_lab.place(x=8, y=190)

    Senha_ent = Entry(width=45)
    Senha_ent.place(x=8, y=210)

    Pass_reset_lab = Label(text='Confirmar senha')
    Pass_reset_lab.place(x=8, y=238)

    Pass_reset_ent = Entry(width=45)
    Pass_reset_ent.place(x=8, y=260)

    button_insert = Button(width=38,bg='#4a9',text="INSERIR",fg='#fff', command=Registar)
    button_insert.place(x=8, y=290)

    button_atualizar = Button(width=38,bg='#4a9', text="ATUALIZAR",fg='#fff', command=atualizar)
    button_atualizar.place(x=8, y=325)

    button_delete = Button(width=38,bg='#ff0000',text="DELETAR",fg='#fff', command=delete)
    button_delete.place(x=8, y=360)

    button_banir = Button(width=38,bg='#ff0000',text="BANIR",fg='#fff', command=banir)
    button_banir.place(x=8, y=395)
    DashBase.cursor.execute('SELECT * FROM pessoas')
    ver = DashBase.cursor.fetchall()

    tabela_head=['ID', 'Nome', 'Email', 'Senha','Numero de conta','Password_reset','status']
    tree = ttk.Treeview(frame_direita, selectmode='extended', columns=tabela_head, show='headings')

    vsb = ttk.Scrollbar(frame_direita,orient='vertical',command=tree.yview)
    hsb = ttk.Scrollbar(frame_direita,orient='horizontal',command=tree.xview)
    tree.configure(yscrollcommand=vsb.set,xscrollcommand=hsb.set)
    frame_direita.grid_rowconfigure(0,weight=12)
    tree.grid(column=0,row=0,sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0,row=1, sticky='ew')
    hb=['nw','nw','nw','nw','nw', 'nw','center']
    h=[30,170,140,100,100,100,75]
    n=0
    for col in tabela_head:
        tree.heading(col, text=col, anchor=CENTER)
        tree.column(col, width=h[n], anchor=hb[n])
        n+=1

    for item in ver:
        tree.insert('', 'end', values=item)
    Croud.mainloop()

CORUD()