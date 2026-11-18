import tkinter as tk

def mostrar_nome():
    nome = entrada.get()
    texto_resultado.config(text=f"Olá, {nome}!")

# Cria a janela principal
janela = tk.Tk()
janela.title("Minha Primeira Interface")
janela.geometry("300x200")

# Adiciona um texto, uma caixa para digitar e um botão
tk.Label(janela, text="Digite seu nome:").pack(pady=5)
entrada = tk.Entry(janela)
entrada.pack(pady=5)

tk.Button(janela, text="Enviar", command=mostrar_nome).pack(pady=10)

texto_resultado = tk.Label(janela, text="")
texto_resultado.pack(pady=5)

# Mantém a janela aberta
janela.mainloop()
