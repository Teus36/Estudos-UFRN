tabuleiro = [
    ["0", "1", "2"],
    ["3", "4", "5"],
    ["6", "7", "8"]
]

print('=='* 8 + " JOGO DA VELHA " + '=='* 8)

print("MODO DE JOGAR: ESCOLHA UM NÚMERO CORRESPONDENTE\nA ONDE VOCÊ QUER MARCAR")

print("==" * 24)

jogador1 = str(input("Informe o nome do jogador 1: "))
jogador2 = str(input("Informe o nome do jogador 2: "))

for i in range(len(tabuleiro)):
    for j in range(len(tabuleiro[i])):
        while True:
            jogar1 = int(input("Jogador 1, escolha um número de 0 a 8: "))

            linha1 = jogar1 // 3
            coluna1 = jogar1 % 3

            if tabuleiro[linha1][coluna1] == "X" or tabuleiro[linha1][coluna1] == "O":
                print("Essa posição já está ocupada. Tente novamente.")
            else:
                tabuleiro[linha1][coluna1] = "X"
                break
        
        while True:
            jogar2 = int(input("Jogador 2, escolha um número de 0 a 8: "))
            print()

            linha2 = jogar2 // 3
            coluna2 = jogar2 % 3

            if tabuleiro[linha2][coluna2] == "X" or tabuleiro[linha2][coluna2] == "O":
                print("Essa posição já está ocupada. Tente novamente.")
            else:
                tabuleiro[linha2][coluna2] = "O"
                break

       
        for i in range(len(tabuleiro)):
            print(tabuleiro[i][0], "|", tabuleiro[i][1], "|", tabuleiro[i][2])
            if i < 2:
                print("-" * 10)

        if (tabuleiro[0][0] == "X" and tabuleiro[0][1] == "X" and tabuleiro[0][2] == "X") or \
           (tabuleiro[1][0] == "X" and tabuleiro[1][1] == "X" and tabuleiro[1][2] == "X") or \
           (tabuleiro[2][0] == "X" and tabuleiro[2][1] == "X" and tabuleiro[2][2] == "X") or \
           (tabuleiro[0][0] == "X" and tabuleiro[1][0] == "X" and tabuleiro[2][0] == "X") or \
           (tabuleiro[0][1] == "X" and tabuleiro[1][1] == "X" and tabuleiro[2][1] == "X") or \
           (tabuleiro[0][2] == "X" and tabuleiro[1][2] == "X" and tabuleiro[2][2] == "X") or \
           (tabuleiro[0][0] == "X" and tabuleiro[1][1] == "X" and tabuleiro[2][2] == "X") or \
           (tabuleiro[0][2] == "X" and tabuleiro[1][1] == "X" and tabuleiro[2][0] == "X"):
            print("==" * 24)
            print(f"{jogador1} venceu!")
            break

        elif (tabuleiro[0][0] == "O" and tabuleiro[0][1] == "O" and tabuleiro[0][2] == "O") or \
             (tabuleiro[1][0] == "O" and tabuleiro[1][1] == "O" and tabuleiro[1][2] == "O") or \
             (tabuleiro[2][0] == "O" and tabuleiro[2][1] == "O" and tabuleiro[2][2] == "O") or \
             (tabuleiro[0][0] == "O" and tabuleiro[1][0] == "O" and tabuleiro[2][0] == "O") or \
             (tabuleiro[0][1] == "O" and tabuleiro[1][1] == "O" and tabuleiro[2][1] == "O") or \
             (tabuleiro[0][2] == "O" and tabuleiro[1][2] == "O" and tabuleiro[2][2] == "O") or \
             (tabuleiro[0][0] == "O" and tabuleiro[1][1] == "O" and tabuleiro[2][2] == "O") or \
             (tabuleiro[0][2] == "O" and tabuleiro[1][1] == "O" and tabuleiro[2][0] == "O"):
            print("==" * 24)
            print(f"{jogador2} venceu!")
            break
        