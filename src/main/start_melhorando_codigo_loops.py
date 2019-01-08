import random


def init():
    print("************************************************")
    print("        Bem vindo ao Jogo de Advinhação!!")
    print("************************************************")


def input_de_dados():
    numero_secreto_nada_secreto = round(random.randrange(1, 101))
    numero_de_tentativas = 1
    tentativas_do_nivel = 0

    print("************************************************//************************************************")
    nivel = int(input("Digite um nível mongolão entre 1(Easy), 2(Medium) e 3(Hard)!!! \n"))
    if nivel == 1:
        tentativas_do_nivel = 20
    elif nivel == 2:
        tentativas_do_nivel = 10
    else:
        tentativas_do_nivel = 5


    print("************************************************//************************************************")
    print("                                    Vocẽ terá trẽs tentativas!!!")
    print("************************************************//************************************************")
    while numero_de_tentativas <= tentativas_do_nivel:
        print("Vocẽ está na tentativa: ", numero_de_tentativas)
        chute = int(input("Digite um número qualquer mongolão!!! \n"))

        menor = chute < numero_secreto_nada_secreto
        maior = chute > numero_secreto_nada_secreto
        igual = chute == numero_secreto_nada_secreto

        if menor:
            print("Menor man, tente de novo")
        elif maior:
            print("Maior man, tente de novo")
        elif igual:
            print("Acertou miserazi!!!!!!!!")

        numero_de_tentativas += 1

    print("Fim de jogo mongolão")
    print("O número secreto era ", numero_secreto_nada_secreto)


init()


input_de_dados()

