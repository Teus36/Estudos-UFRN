import random

palavras = ["gato", "casa", "carro"]

random.shuffle(palavras)

count = 0

while True:

    advinhar = input("Digite uma palavra: ").lower()
    indice = int(input("Digite o índice: "))

    if advinhar in palavras:

        if indice == palavras.index(advinhar):
            print("Acertou!")
            count += 1

        else:
            print("Errou o índice")

    else:
        print("Palavra não existe")

    if count == 3:
        print("Você venceu")
        break