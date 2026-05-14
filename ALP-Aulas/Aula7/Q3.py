print("JOGO DO PEDRA, PAPEL E TESOURA")
import random
resp = "sim"
while resp.lower() == "sim":
    jogador1 = int(input("Escolha um valor entre 0 e 2, sendo 0 para pedra, 1 para papel e 2 para tesoura: "))
    jogador2 = random.randint(0,2)

    if jogador1 == 0 and jogador2 == 2:
        print(f"Parabéns você ganhou, o computador escolheu {jogador2} (tesoura)!!")
    elif jogador1 == 1 and jogador2 == 0:
        print(f"Parabéns você ganhou, o computador escolheu {jogador2} (pedra)!!")
    elif jogador1 == 2 and jogador2 == 1:
        print(f"Parabéns você ganhou, o computador escolheu {jogador2} (papel)!!")
    elif jogador1 == jogador2:
        print(f"Houve um empate, ambos escolheram {jogador1}")
    else:
        print(f"Você perdeu, o computador escolheu {jogador2}!!")

    resp = str(input("Deseja jogar novamente?: "))
