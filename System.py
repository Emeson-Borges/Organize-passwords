#Criando Sistema com Tkinter
import tkinter
from tkinter import *
from tkinter import messagebox
import os

#Criando caminho onde salvar os arquivos
caminho = os.path.dirname(__file__)
nomeArquivo = caminho+"\\senhas.txt"

#Criando a Aplicação
System = Tk()

#Tabela de Cores em Hexadecimal para usar no Sistema
azul_escuro     = '#00BFFF'
azul_claro      = '#00BFFF'
preto           = '#000000'
branco          = '#F0F8FF'
verde           = '#00FA9A'
vermelho        = '#FF0000'
rosa            = '#FF1493'
LightSkyBlue    = '#87CEFA'
SkyBlue         = '#87CEEB'

#Configurações da Tela
System.title("Organize Passwords")
System.geometry("600x400")
System.configure(background=SkyBlue)

#Definindo um título para o meu sistema
lblTitulo = Label(System, text="ORGANIZADOR DE SENHAS", background=azul_claro, foreground=preto, font=("Arial", 10))
lblTitulo.pack(ipadx=150, ipady=30, padx=30, pady=60, side="top", fill=X, expand=True) #expandir, lado, preencher, valores de preenchimento
lblTitulo.place(x=10, y=2, width=600, height=20) #posição e o tamanho
#lblTitulo.grid(número da linha, número da coluna, rowsapn, columnpan, valores de preenchimento)

#Dados de entrada
lblConta = Label(System, text="Conta", bg=SkyBlue, fg=preto)
lblConta.pack(side="left")
lblConta.place(x=20, y=30)
lblEmail = Label(System, text="Email", bg=SkyBlue, fg=preto)
lblEmail.pack(side="left")
lblEmail.place(x=20, y=75)
lblSenha = Label(System, text="Senha", bg=SkyBlue, fg=preto)
lblSenha.pack(side="left")
lblSenha.place(x=20, y=120)
lblLinkLogin = Label(System, text="Link do Login", bg=SkyBlue, fg=preto)
lblLinkLogin.pack(side="left")
lblLinkLogin.place(x=20, y=165)
lblObs = Label(System, text="Observação", bg=SkyBlue, fg=preto)
lblObs.pack(side="left")
lblObs.place(x=20, y=210)

#Pegando o valor do campo nome
vConta = Entry(System)
vConta.pack(side="left")
vConta.place(x=20, y=50, width=200, height=20)

#Pegando o valor do Campo Telefone
vEmail = Entry(System)
vEmail.pack(side="left")
vEmail.place(x=20, y=95, width=200, height=20)

#Pegando o valor do Apelido
vSenha = Entry(System)
vSenha.pack(side="left")
vSenha.place(x=20, y=140, width=200, height=20)

#Pegando o valor do Link de Login
vLinkLogin = Entry(System)
vLinkLogin.pack(side="left")
vLinkLogin.place(x=20, y=185, width=200, height=20)

#Pegando o valor da Observação
vObs = Text(System)
vObs.pack(side="left")
vObs.place(x=20, y=235, width=350, height=85)

#Criando a função dos botões
#Botão Salvar Arquivo em txt
def salvar_arquivo():
    if vConta.get() == "" or vEmail.get() == "" or vSenha.get() == "":
        msg = "Campos obrigatórios não preenchidos"
        messagebox.showwarning("Aviso", msg)
    else:
        arquivo = open(nomeArquivo, "a")
        arquivo.write("Conta      : %s"% vConta.get())
        arquivo.write("\nEmail      : %s"% vEmail.get())
        arquivo.write("\nSenha      : %s"% vSenha.get())
        arquivo.write("\nLink       : %s" % vLinkLogin.get())
        arquivo.write("\nObservação : %s"% vObs.get("1.0", END))
        arquivo.write("\n\n")
        arquivo.close()
        msgSucess = "Dados salvos com sucesso"
        messagebox.showinfo("Sucesso", msgSucess)


#Criando panel de botões
'''
btncadastrar = tkinter.Button(System, text="Cadastrar", command=cad_pessoa, width=10, height=2, bg=azul_claro, fg=preto).place(x=115, y=350)
btnsalvar = tkinter.Button(System, text="Salvar", width=10, height=2, bg=azul_claro, fg=preto).place(x=215, y=350)
btneditar = tkinter.Button(System, text="Editar", width=10, height=2, bg=azul_claro, fg=preto).place(x=315, y=350)
btnexcluir = tkinter.Button(System, text="Excluir", width=10, height=2, bg=azul_claro, fg=preto).place(x=415, y=350)
'''
btnsalvar_arquivo = tkinter.Button(System, text="Salvar Arquivo", width=15, height=2,
                                   bg=azul_claro, fg=preto, font=("Arial", 10), command=salvar_arquivo).place(x=220, y=350)

#Chamando o Sistema
System.mainloop()