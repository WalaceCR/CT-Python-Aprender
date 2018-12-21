

def init():
    print("************************************************")
    print("        Bem vindo ao Jogo de Advinhação!!")
    print("************************************************")

def input_de_dados():
    numero_secreto_nada_secreto = 45

    chute = int(input("Digite um número qualquer mongolão!!! \n"))

    if chute < numero_secreto_nada_secreto:
        print("Menor man, tente de novo")
    elif chute > numero_secreto_nada_secreto:
        print("Maior man, tente de novo")
    else:
        print("Acertou miserazi!!!!!!!!")


init()


input_de_dados()

