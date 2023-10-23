from tkinter import *
from tkinter import ttk
from adivinhacao import jogar_adivinhacao
from forca import jogar_forca

janela = Tk()
janela.title("Game Collection")
janela.geometry("1000x480")
janela.configure(bg="#cdffba")
janela.resizable(False, False)


frame_1 = Frame(janela, width=250, height=480, bg="#347d28")
frame_1.grid(column=0, row=0, rowspan=2)

label_1 = Label(janela, text="Game\nCollection", bg="#347d28", fg="#ffffff", font=("Arial", 20))
label_1.grid(column=0, row=0, rowspan=2)

# Acessar os jogos -----------------------------------

# Jogo da adivinhação --------------------------------------
def jogar_adivinhacao_chamada():
    for widget in janela.winfo_children():
        widget.destroy()
        
    jogar_adivinhacao()


label_2 = Label(janela, text="Jogo da Advinhação", bg="#cdffba", fg="#000000", font=("Arial", 20))
label_2.grid(column=1, row=0, padx=70)

botao_1 = Button(janela, command=jogar_adivinhacao_chamada, text="Jogar", width=20, relief="flat", overrelief="solid", bg="#347d28", fg="#ffffff", font=("Arial", 15))
botao_1.grid(column=1, row=1)


# Jogo da forca --------------------------------------
def jogar_forca_chamada():
    jogar_forca()


label_3 = Label(janela, text="Jogo da Forca", bg="#cdffba", fg="#000000", font=("Arial", 20))
label_3.grid(column=2, row=0, padx=70)

botao_2 = Button(janela, command=jogar_forca_chamada, text="Jogar", width=20, relief="flat", overrelief="solid", bg="#347d28", fg="#ffffff", font=("Arial", 15))
botao_2.grid(column=2, row=1)


janela.mainloop()