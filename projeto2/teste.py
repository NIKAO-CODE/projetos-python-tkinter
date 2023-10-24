import tkinter as tk
from tkinter import Entry, Button, Label

def obter_numero():
    chute_str = entrada.get()
    try:
        chute = int(chute_str)
        resultado.config(text="Você digitou: {}".format(chute))
    except ValueError:
        resultado.config(text="Por favor, insira um número válido")

janela = tk.Tk()
janela.title("Obter Número")

frame = tk.Frame(janela)
frame.pack(padx=20, pady=20)

entrada = Entry(frame)
entrada.pack()

botao = Button(frame, text="Obter Número", command=obter_numero)
botao.pack()

resultado = Label(frame, text="")
resultado.pack()

janela.mainloop()
