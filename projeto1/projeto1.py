from tkinter import *
from tkinter import ttk
import algoritmo_quicksort

janela = Tk()
janela.title("Projeto 1")
janela.geometry("500x500")


frame_1 = Frame(janela, width=500, height=75, bg="black")
frame_1.grid(column=0, row=0)


label_1 = Label(janela, text="Ordenação", fg="white", bg="black", font=("Audiowide", 20))
label_1.grid(column=0, row=0)


label_2 = Label(janela, text="Insira a sequência para ordenar\nSeparado por espaço",
                fg="black", font=("Audiowide", 15), pady= 9)
label_2.grid(column=0, row=1)


sequencia = Text(janela, width=50, height=5)
sequencia.grid(column=0, row=2, pady=30)


def obter_sequencia():
    sequencia_text = sequencia.get("1.0", "end-1c")
    sequencia_ajustada = sequencia_text.replace(" ", ", ")
    lista = sequencia_ajustada.split(", ")

    lista.sort()
    print(lista)

    sequencia_ordenada = ", ".join(lista)

    label_3 = Label(janela, text= sequencia_ordenada, fg="black", font=("Audiowide", 15), relief='solid',
                    width=36, height=2)
    label_3.grid(column=0, row=3)


botao_ordenar = Button(janela, text="Executar", bg="gray", fg="black", width=20, font=15, command=obter_sequencia,)
botao_ordenar.grid(column=0, row=4)


janela.mainloop()