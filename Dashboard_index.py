from tkinter import *
import DashBase
import random
from tkinter import messagebox


def Nova_senha():
    Tela_confirmacap = Tk()
    Tela_confirmacap.minsize(height=200, width=350)
    Tela_confirmacap.maxsize(height=200, width=350)
    Tela_confirmacap.title('Login')

    confirm = Label(text="Nova senha", fg="#fff", bg="#4a9",
                    width=350, height=2, font="3")
    confirm.pack()
    cod_Lab = Label(text="Crie uma senha nova")
    cod_Lab.place(x=15, y=48)
    code_reset = Entry(width=51)
    code_reset.pack(pady=25)
    conf_Lab = Label(text="Confime a senha")
    conf_Lab.place(x=15, y=90)
    conf_reset = Entry(width=51)
    conf_reset.pack()
    # ver = Label(text=Verificador)
    # ver.pack()
    Reset_btn = Button(text="Enviar", borderwidth=0,
                       background="#4a9", width=20, font="10")
    Reset_btn.pack(pady=10)
    Tela_confirmacap.mainloop


numeros = "123456789"
resetsenha = "".join(random.sample(numeros, 6))


def Reset():
    def Enviar_pass():
        email = Email_reset.get()
        nome = Nome_reset.get()
        DashBase.cursor.execute("""
        SELECT password_reset FROM pessoas
        WHERE nome = ? and email = ? """, (nome, email))
        Verificado = DashBase.cursor.fetchone()
        # print(Verificado)
        try:
            for cada in Verificado:
                print(f'seu codigo é{cada}')

                def conf():
                    numeros = "123456789"
                    resetsenha = "".join(random.sample(numeros, 6))
                    codigo = code_reset.get()
                    if (str(codigo) == str(cada)):
                        print(resetsenha)
                        DashBase.cursor.execute("""
                        UPDATE pessoas
                        SET password_reset = ?
                        WHERE password_reset = ?
                        """, (resetsenha, cada))
                        confirm.destroy()
                        cod_Lab.destroy()
                        code_reset.destroy()
                        code_btn.destroy()
                        # for vv in Verificado():
                        #     print(f'a sua pass é {vv}')

                        def New_pass():
                            print(resetsenha)
                            nova = new_reset.get()
                            confi = conf_reset.get()
                            if (nova == confi):
                                print(resetsenha)
                                DashBase.cursor.execute(
                                    "UPDATE pessoas SET senha = ? WHERE password_reset = ?", (nova, resetsenha))
                                print(
                                    f'a nova é {nova} no codigo {resetsenha}')
                                DashBase.banco.commit()
                                messagebox.showinfo(
                                    title="Senha", message="Senha atualizada")
                                Tela_recuperacao.destroy()
                                Login()
                            else:
                                messagebox.showerror(
                                    title="Erro", message="As sua senha deve ser igual a confirmação")
                        confirm_senha = Label(
                            text="Nova senha", fg="#fff", bg="#4a9", width=350, height=2, font="3")
                        confirm_senha.pack()
                        new_Lab = Label(text="Crie uma senha nova")
                        new_Lab.place(x=15, y=48)
                        new_reset = Entry(width=51)
                        new_reset.pack(pady=25)
                        conf_Lab = Label(text="Confime a senha")
                        conf_Lab.place(x=15, y=90)
                        conf_reset = Entry(width=51)
                        conf_reset.pack()
                        Reset_btn = Button(
                            text="Enviar", borderwidth=0, background="#4a9", width=20, font="10", command=New_pass)
                        Reset_btn.pack(pady=10)

                        DashBase.banco.commit()
                        print(resetsenha)
                    else:
                        print("codigo errado")
                messagebox.showinfo(title="Comfirmado",
                                    message=f"o seu codigo e: {cada}")
                print(cada)
                Email_reset.destroy()
                Nome_reset.destroy()
                Email_Lab.destroy()
                Nome_lab.destroy()
                Reset_btn.destroy()
                recupere.destroy()
                confirm = Label(text="Confirme o seu Codigo", fg="#fff",
                                bg="#4a9", width=350, height=2, font="3")
                confirm.pack()
                cod_Lab = Label(text="Ensira o seu codigo aqui")
                cod_Lab.place(x=15, y=48)
                code_reset = Entry(width=51)
                code_reset.pack(pady=25)
                # ver = Label(text=Verificador)
                # ver.pack()
                code_btn = Button(text="Enviar", borderwidth=0,
                                  background="#4a9", width=20, font="10", command=conf)
                code_btn.pack(pady=10)
        except:
            messagebox.showerror(
                title="errro", message="Os seus dados estao incorreto, verifique e volte a tentar")

    Tela_recuperacao = Tk()
    Tela_recuperacao.minsize(height=200, width=350)
    Tela_recuperacao.maxsize(height=200, width=350)
    Tela_recuperacao.title('Login')

    recupere = Label(text="Recupere a sua conta", fg="#fff",
                     bg="#4a9", width=350, height=2, font="3")
    recupere.pack()
    Email_Lab = Label(text="Ensira o seu nome aqui")
    Email_Lab.place(x=15, y=48)
    Nome_lab = Label(text="Ensira o seu email aqui")
    Nome_lab.place(x=15, y=90)
    Nome_reset = Entry(width=51)
    Nome_reset.pack(pady=25)
    Email_reset = Entry(width=51)
    Email_reset.pack()
    Reset_btn = Button(text="Enviar", borderwidth=0,
                       background="#4a9", width=20, font="10", command=Enviar_pass)
    Reset_btn.pack(pady=10)
    Tela_recuperacao.mainloop


def Login():
    def Change_window():
        Tela_Login.destroy()
        Cadastro()

    def Change_senha():
        Tela_Login.destroy()
        Reset()
    Tela_Login = Tk()
    Tela_Login.minsize(height=350, width=300)
    Tela_Login.maxsize(height=350, width=300)
    Tela_Login.title('Login')

    titulo = Label(Tela_Login, text="Login", font="Bold 16",
                   height=2, foreground="#fff", width=300, bg="#4a9")
    titulo.pack()
    Lab_Nome = Label(Tela_Login, text="Nome do usuario")
    Lab_Nome.place(x=5, y=60)
    Ent_Nome = Entry(Tela_Login, width=47, justify="center")
    Ent_Nome.pack(pady=25)

    Lab_Pass = Label(Tela_Login, text="Senha")
    Lab_Pass.place(x=5, y=110)
    Ent_Pass = Entry(Tela_Login, width=47, justify="center", show="•")
    Ent_Pass.pack(pady=10)

    Reset_btn = Button(text="Esqueci a senha",
                       borderwidth=0, command=Change_senha)
    Reset_btn.place(x=200, y=160)

    def logar():
        nome = Ent_Nome.get()
        senha = Ent_Pass.get()
        DashBase.cursor.execute("""
        SELECT * FROM pessoas
        WHERE nome =? and senha = ?
        """, (nome, senha))
        Verificador = DashBase.cursor.fetchone()
        try:
            if (nome in Verificador and senha in Verificador):
                messagebox.showinfo(
                    title="ACESSOU", message="acessou como sucesso")
                Tela_Login.destroy()
                import Dashbase_croud
            else:
                pass
        except:
            messagebox.showerror(title="erro", message="algo correu errado")
    Login_btn = Button(text="Login", borderwidth=0, width=31,
                       foreground="#fff", font="BOLD 13", background="#4a9", command=logar)
    Login_btn.pack(pady=50)

    Lab_Ask = Label(text="Não tem uma conta ainda?")
    Lab_Ask.pack()

    cad_btn = Button(text="Criar conta", borderwidth=0,
                     foreground="#4a9", command=Change_window)
    cad_btn.pack()

    Tela_Login.mainloop()


def Cadastro():
    def Change_Window():
        Tela_Cadastro.destroy()
        Login()
    Tela_Cadastro = Tk()
    Tela_Cadastro.minsize(height=400, width=300)
    Tela_Cadastro.maxsize(height=400, width=300)
    Tela_Cadastro.title('Cadastro')

    titulo = Label(Tela_Cadastro, text="Cadastro", font="Bold 16",
                   height=2, foreground="#fff", width=300, bg="#4a9")
    titulo.pack()
    Lab_Nome = Label(Tela_Cadastro, text="Nome do usuario")
    Lab_Nome.place(x=5, y=60)
    Ent_Nome = Entry(Tela_Cadastro, width=47, justify="center")
    Ent_Nome.pack(pady=25)

    Lab_Email = Label(text="Email")
    Lab_Email.place(x=5, y=110)
    Ent_Email = Entry(width=47, justify="center")
    Ent_Email.pack(pady=10)

    Lab_Senha = Label(text="Senha")
    Lab_Senha.place(x=5, y=160)
    Ent_Senha = Entry(width=47, justify="center")
    Ent_Senha.pack(pady=17)

    Lab_Senhaconf = Label(text="Confirmar Senha")
    Lab_Senhaconf.place(x=5, y=210)
    Ent_Pass = Entry(width=47, justify="center")
    Ent_Pass.pack(pady=17)

    def Registar():
        numeros = "123456789"
        numeros2 = "987654321"
        resetsenha = "".join(random.sample(numeros, 6))
        numero_conta = "".join(random.sample(numeros+numeros2, 10))
        nome = Ent_Nome.get()
        email = Ent_Email.get()
        senha = Ent_Senha.get()
        confsenha = Ent_Pass.get()
        status = str(True)
        DashBase.cursor.execute("SELECT * FROM pessoas")
        verificado = DashBase.cursor.fetchall()
        if (nome == "" or email == "" or senha == "" or confsenha == ""):
            messagebox.showerror(
                title="Ocoreu um erro", message="Eroo, verifique se todos os campos estao preenchidos")
        else:
            if (nome in verificado and email in verificado and senha in verificado):
                messagebox.showerror(
                    title="Erro", message="esses dados ja existem")
            else:
                if (nome in verificado and email in verificado):
                    messagebox.showerror(
                        title='ERRO', message="O seu email e a sua senha ja estao cadastrados")
                else:
                    if (len(senha) < 5):
                        messagebox.showerror(
                            title="Erro", message="a sua senha precisa ter no minimo 6 digitos")
                    else:
                        if (senha != confsenha):
                            messagebox.showerror(
                                title="Erro", message="A sua senha precisa ser igual a confirmaçao")
                        else:
                            DashBase.cursor.execute("""
                            INSERT INTO pessoas(nome, email,senha,numero_conta,password_reset,status) VALUES(?,?,?,?,?,?)
                            """, (nome, email, senha,numero_conta, resetsenha,status))
                            DashBase.banco.commit()
                            messagebox.showinfo(
                                title="Informaçoes do cadastro", message="Registou com sucesso")
                            Tela_Cadastro.destroy()
                            Login()

    Login_btn = Button(text="Cadastrar", borderwidth=0, width=31,
                       foreground="#fff", font="BOLD 13", background="#4a9", command=Registar)
    Login_btn.pack(pady=20)

    Lab_Ask = Label(text="Ja tem uma conta?")
    Lab_Ask.pack()

    cad_btn = Button(text="Entrar", borderwidth=0,
                     foreground="#4a9", command=Change_Window)
    cad_btn.pack()

    Tela_Cadastro.mainloop()


Login()
