

def init():
    print("************************************************")
    print("        Bem vindo ao Jogo de Advinhação!!")
    print("************************************************")

def input_de_dados():
    numero_secreto_nada_secreto = 45

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


init()


input_de_dados()

