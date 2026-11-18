import tkinter as tk
from tkinter import messagebox, simpledialog

# Dados originais da conta
USUARIO_CORRETO = 'Ravi1020'
SENHA_CORRETA = 1234
SENHA_TRANSACAO = 2011
saldo = 200.0


def verificar_login():
    usuario_digitado = entry_usuario.get()
    senha_digitada = entry_senha.get()

    if not senha_digitada.isdigit():
        messagebox.showerror('Erro', 'A senha deve conter apenas números.')
        return

    senha_num = int(senha_digitada)

    if usuario_digitado == USUARIO_CORRETO and senha_num == SENHA_CORRETA:
        # Esconde a tela de login e mostra o menu do caixa
        frame_login.pack_forget()
        atualizar_texto_saldo()
        frame_menu.pack(pady=20)
    elif usuario_digitado != USUARIO_CORRETO:
        messagebox.showerror('Erro', 'Nome de usuário inválido.')
    else:
        messagebox.showerror('Erro', 'Senha inválida.')


def atualizar_texto_saldo():
    label_saldo.config(text=f'Saldo disponível: R$ {saldo:.2f}')


def validar_senha_transacao():
    tentativas = 0
    while tentativas < 3:
        senha_t = simpledialog.askstring(
            'Segurança',
            f'Digite sua senha de transferência (Tentativa {tentativas + 1}/3):',
            show='*',
        )

        # Se o usuário clicar em Cancelar
        if senha_t is None:
            return False

        tentativas += 1

        if senha_t.isdigit() and int(senha_t) == SENHA_TRANSACAO:
            messagebox.showinfo('Sucesso', 'SENHA CORRETA')
            return True
        else:
            messagebox.showwarning('Atenção', 'SENHA INCORRETA')

    # Se errar 3 vezes, encerra o programa igual ao seu código original
    messagebox.showerror(
        'Bloqueado',
        'LIMITE DE TENTATIVAS EXCEDIDO.\nCaixa eletrônico encerrado.',
    )
    janela.destroy()
    return False


def depositar():
    global saldo
    valor = simpledialog.askfloat(
        'Depositar', 'Qual valor você deseja depositar?'
    )

    if valor is None:
        return

    if valor > 0:
        if validar_senha_transacao():
            saldo += valor
            atualizar_texto_saldo()
            messagebox.showinfo(
                'Depósito Concluído',
                f'Seu saldo disponível agora é R$ {saldo:.2f}',
            )
    else:
        messagebox.showwarning(
            'Valor Inválido', 'O valor do depósito deve ser maior que zero.'
        )


def sacar():
    global saldo
    valor = simpledialog.askfloat('Sacar', 'Quanto você deseja sacar?')

    if valor is None:
        return

    if valor <= 0:
        messagebox.showwarning(
            'Valor Inválido', 'O valor do saque deve ser maior que zero.'
        )
    elif valor > saldo:
        messagebox.showerror('Erro', 'Saldo insuficiente.')
    else:
        if validar_senha_transacao():
            saldo -= valor
            atualizar_texto_saldo()
            messagebox.showinfo(
                'Saque Concluído',
                f'Seu saldo disponível agora é R$ {saldo:.2f}',
            )


def ver_saldo():
    messagebox.showinfo('Saldo Atual', f'Seu saldo é R$ {saldo:.2f}')


def sair():
    messagebox.showinfo('Encerrando', 'Saindo...\nCaixa eletrônico encerrado.')
    janela.destroy()


# --- Configuração da Janela Principal ---
janela = tk.Tk()
janela.title('Caixa Do Banco do São Pedro')
janela.geometry('1920x1080')
janela.resizable(False, False)

# --- TELA 1: LOGIN ---
frame_login = tk.Frame(janela)
frame_login.pack(pady=90)

tk.Label(
    frame_login,
    text='Seja bem-vindo ao caixa eletrônico do Banco do São Pedro',
    font=('Arial', 12, 'bold'),
).pack(pady=10)

tk.Label(frame_login, text='NOME DE USUÁRIO').pack()
entry_usuario = tk.Entry(frame_login, width=25)
entry_usuario.pack(pady=5)

tk.Label(frame_login, text='SENHA').pack()
entry_senha = tk.Entry(frame_login, width=25, show='*')
entry_senha.pack(pady=5)

tk.Button(
    frame_login,
    text='Entrar',
    width=15,
    bg='#4CAF50',
    fg='white',
    command=verificar_login,
).pack(pady=15)

# --- TELA 2: MENU DO CAIXA (Começa oculta) ---
frame_menu = tk.Frame(janela)

tk.Label(
    frame_menu,
    text='Escolha qual ação deseja executar',
    font=('Arial', 11, 'bold'),
).pack(pady=5)

label_saldo = tk.Label(
    frame_menu,
    text=f'Saldo disponível: R$ {saldo:.2f}',
    font=('Arial', 10),
    fg='blue',
)
label_saldo.pack(pady=5)

tk.Button(
    frame_menu, text='1. Depositar', width=20, height=2, command=depositar
).pack(pady=4)
tk.Button(
    frame_menu, text='2. Sacar', width=20, height=2, command=sacar
).pack(pady=4)
tk.Button(
    frame_menu, text='3. Ver Saldo', width=20, height=2, command=ver_saldo
).pack(pady=4)
tk.Button(
    frame_menu,
    text='0. Sair',
    width=20,
    height=2,
    bg='#f44336',
    fg='white',
    command=sair,
).pack(pady=4)

janela.mainloop()
