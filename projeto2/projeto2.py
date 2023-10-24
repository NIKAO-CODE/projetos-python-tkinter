from tkinter import *
from tkinter import ttk
import random


janela = Tk()
janela.title("Game Collection")
janela.geometry("1000x480")
janela.configure(bg="#cdffba")
janela.resizable(False, False)

pontos = 1000


frame_1 = Frame(janela, width=1000, height=75, bg="#347d28")
frame_1.grid(column=0, row=0, columnspan=2) 

label_1 = Label(janela, text="Game Collection", bg="#347d28", fg="#ffffff", font=("Arial", 20))
label_1.grid(column=0, row=0, columnspan=2)
# Acessar os jogos -----------------------------------

# Jogo da adivinhação --------------------------------------
def jogar_adivinhacao_chamada():
    for widget in janela.winfo_children():
        widget.destroy()

    frame_1_adv = Frame(janela, width=1000, height=75, bg="#347d28")
    frame_1_adv.grid(column=0, row=0, columnspan=3)

    label_1_adv = Label(janela, text="Bem-vindo ao jogo de Advinhação", bg="#347d28", fg="#ffffff", font=("Arial", 20))
    label_1_adv.grid(column=0, row=0, columnspan=3)


    numero_secreto = random.randint(1, 10)

    def obter():
        global pontos
        nivel = selecionado.get()
        if(nivel == 1):
            total_de_tentativas = 20
        elif(nivel == 2):
            total_de_tentativas = 10
        else:
            total_de_tentativas = 5

        return total_de_tentativas

    selecionado = IntVar()
    
    label_2_adv = Label(janela, text="Escolha a dificuldade", bg="#cdffba", fg="#000000", font=("Arial", 20))
    label_2_adv.grid(column=0, row=1, columnspan=3, pady=50)

    rad_1 = Radiobutton(janela, text="Fácil", bg="#cdffba", fg="#000000", font=("Arial", 20), value=1, var=selecionado, command=obter)
    rad_1.grid(column=0, row=2)

    rad_2 = Radiobutton(janela, text="Médio", bg="#cdffba", fg="#000000", font=("Arial", 20), value=2, var=selecionado, command=obter)
    rad_2.grid(column=1, row=2)

    rad_3 = Radiobutton(janela, text="Difícil", bg="#cdffba", fg="#000000", font=("Arial", 20), value=3, var=selecionado, command=obter)
    rad_3.grid(column=2, row=2)

    selecionado.set(1)

    total_de_tentativas = obter()

    def reconstruir_janela():
        global pontos
        for widget in janela.winfo_children():
            widget.destroy()

        frame_1_adv = Frame(janela, width=1000, height=75, bg="#347d28")
        frame_1_adv.grid(column=0, row=0, columnspan=3)

        label_1_adv = Label(janela, text="Bem-vindo ao jogo de Advinhação", bg="#347d28", fg="#ffffff", font=("Arial", 20))
        label_1_adv.grid(column=0, row=0, columnspan=3)

        for rodada in range(1, total_de_tentativas + 1):
            texto = "Tentativa {} de {}".format(rodada, total_de_tentativas)
            
            label_3_adv = Label(janela, text=texto, bg="#cdffba", fg="#000000", font=("Arial", 20))
            label_3_adv.grid(column=0, row=1, columnspan=3, pady=30)
            
            label_4_adv = Label(janela, text="Digite um número entre 1 e 10: ", bg="#cdffba", fg="#000000", font=("Arial", 15))
            label_4_adv.grid(column=0, row=2, columnspan=3, pady=30)

            entrada = Entry(janela)
            entrada.grid(column=0, row=3, columnspan=3)

            
            chute_str = entrada.get()
            chute = int(chute_str)

            
            print("Você digitou {}".format(chute_str))
            chute = int(chute_str)

            if(chute < 1 or chute > 10):
                print("Você deve digitar um número entre 1 e 10.")
                continue

            acertou = chute == numero_secreto
            maior   = chute > numero_secreto
            menor   = chute < numero_secreto

            if(acertou):
                print("Parabéns! Você acertou e fez {} pontos!".format(pontos))
                break
            else:
                if(maior):
                    print("Você errou! O número secreto é menor.")
                elif(menor):
                    print("Você errou! O número secreto é maior.")

                pontos_perdidos = abs(numero_secreto - chute)
                pontos -= pontos_perdidos


    botao_1_adv = Button(janela, command=reconstruir_janela, text="Jogar", width=20, relief="flat", overrelief="solid", bg="#347d28", fg="#ffffff", font=("Arial", 15))
    botao_1_adv.grid(column=1, row=3, pady= 30)


label_2 = Label(janela, text="Jogo da Advinhação", anchor="n", bg="#cdffba", fg="#000000", font=("Arial", 20))
label_2.grid(column=0, row=1, pady=70)

botao_1 = Button(janela, command=jogar_adivinhacao_chamada, text="Jogar", width=20, relief="flat", overrelief="solid", bg="#347d28", fg="#ffffff", font=("Arial", 15))
botao_1.grid(column=0, row=2)





# Jogo da forca --------------------------------------
def jogar_forca_chamada():
    pass


label_3 = Label(janela, text="Jogo da Forca", bg="#cdffba", fg="#000000", font=("Arial", 20))
label_3.grid(column=1, row=1, pady=70)

botao_2 = Button(janela, command=jogar_forca_chamada, text="Jogar", width=20, relief="flat", overrelief="solid", bg="#347d28", fg="#ffffff", font=("Arial", 15))
botao_2.grid(column=1, row=2)


janela.mainloop()