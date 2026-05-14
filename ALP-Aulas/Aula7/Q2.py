import random
resp = "sim"

while resp.lower() == "sim":
    print("JOGO ZERINHO OU UM")
    jogador1 = int(input("Escolha um valor entre 0 e 1: "))
    jogador2 = random.randint(0,1)
    jogador3 = random.randint(0,1)

    if jogador1 != jogador2 and jogador1 != jogador3:
        print(f"Parabéns você ganhou, os demais escolheram {jogador2}!!")
    elif jogador1 == jogador2 == jogador3:
        print(f"Houve um empate, todos escolheram {jogador1}")
    elif jogador2 != jogador1 and jogador2 != jogador3:
        print("Você perdeu, o vencedor foi o jogador 2!!")
    else:
        print(f"Você perdeu, o vencedor foi  o jogador 3!!")

    resp = str(input("Deseja jogar novamente?: "))

