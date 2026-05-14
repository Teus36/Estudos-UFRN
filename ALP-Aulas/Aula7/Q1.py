import random

while True: 
    print("=-" * 30)
    jogar = str(input("Deseja jogar o jogo de dados 7 ou 11 ?: "))
    if jogar.lower() == "sim" or jogar.lower() == "s":
        dado1 = random.randint(0,9)
        dado2 = random.randint(0,9)
        soma = dado1 + dado2
        print(f"ROLAGEM FEITA!! OS VALORES ADQUIRIDOS FORAM {dado1} e {dado2}")
        if soma == 7 or soma == 11:
            print(f"Parabéns você me venceu pois a soma dos valores é: {soma}")
        else:
            print(f"Que pena, você perdeu, a soma dos valores foi {soma} :(")
            jogar = str(input("Deseja tentar novamente?: "))
            if jogar.lower() == "não" or jogar.lower() == "n":
                break
    else:
        break

    