from tkinter import *
from tkinter import ttk
from tkinter import messagebox

janela = Tk()
janela.title("Projeto 1")
janela.geometry("400x480")
janela.configure(bg="#cdffba")
janela.resizable(False, False)


frame_1 = Frame(janela, width=400, height=55, bg="#589747")
frame_1.grid(column=0, row=0)


label_1 = Label(janela, text="Classificação de Números", fg="white", bg="#589747", font=("Audiowide", 20))
label_1.grid(column=0, row=0)


label_2 = Label(janela, text="Insira a sequência para ordenar,\nseparado por espaço.",
                fg="#3b732f", bg="#cdffba", font=("Audiowide", 15), pady= 9)
label_2.grid(column=0, row=1)


sequencia = Text(janela, width=40, height=5)
sequencia.grid(column=0, row=2, pady=30)

lista = []


def obter_sequencia():
    try:
        global lista
        sequencia_text = sequencia.get("1.0", "end-1c")
        lista = [int(l) for l in sequencia_text.split() if l.strip()]
        lista.sort()

        label_3 = Label(janela, text=lista, bg="white", fg="black", font=("Audiowide", 15), relief='flat', width=29, height=2)
        label_3.grid(column=0, row=5, pady=17)
    except:
        print("Ocorreu um erro, verifique se está inserindo apenas números separado por espaço.")

botao_ordenar = Button(janela,  command=obter_sequencia, text="Executar", bg="#6dac5a", fg="#ffffff", width=20, font=15, relief="flat", overrelief="solid", anchor="center")
botao_ordenar.grid(column=0, row=4)


def copiar_ordenacao():
    global lista
    info = lista
    janela.clipboard_clear()
    janela.clipboard_append(info)

    messagebox.showinfo("Sucesso", "A sequência foi copiada")


botao_ordenar = Button(janela, command=copiar_ordenacao, text="Copiar", bg="#6dac5a", fg="#ffffff", width=20, font=15, relief="flat", overrelief="solid", anchor="center")
botao_ordenar.grid(column=0, row=6, pady=10)


janela.mainloop()