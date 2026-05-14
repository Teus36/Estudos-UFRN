import random 

contador = 0
num_aleatorio = random.randint(1, 9)


advinha1 = int(input("Tente adivinhar o número entre 1 e 9: "))

if advinha1 == num_aleatorio and contador == 0: 
    print("PARABÉNS VC É MUITO SORTUDO SEU FDP, ACERTOU DE PRIMEIRA")
else:
    if advinha1 < num_aleatorio:
        print("NÃO FOI DESSA VEZ, DIGITE UM NÚMERO MAIOR") 
    else:
        print("NÃO FOI DESSA VEZ, DIGITE UM NÚMERO MENOR")
    contador += 1

advinha2 = int(input("Tente adivinhar o número entre 1 e 9: "))

if advinha2 == num_aleatorio and contador == 1:
    print("VOCÊ JOGA BEM, MAS AINDA CONTOU SORTE")
else:
    if advinha2 < num_aleatorio:
        print("NÃO FOI DESSA VEZ, DIGITE UM NÚMERO MAIOR") 
    else:
        print("NÃO FOI DESSA VEZ, DIGITE UM NÚMERO MENOR")
    contador += 1

advinha3 = int(input("Tente adivinhar o número entre 1 e 9: "))

if advinha3 == num_aleatorio and contador == 2:
    print("VOCÊ É UM EXCELENTE ESTRATEGISTA")
else:
    print("ANALIZE MELHOR SUA ESTRATÉGIA ANTES DE JOGAR NOVAMENTE")
