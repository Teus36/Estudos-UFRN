print("=-" * 40)
print("=-" * 8 + " COMO ESTÃO SUAS PRÁTICAS DE EXERCÍCIOS FÍSICOS " + 8 * "=-")
print("=-" * 40)

print("")

print("1. Com que frequência você pratica atividades físicas ?")
print("Digite a pontuação de sua resposta: ")

print("")

print("3 - Todos os dias ")
print("2 - Regularmente")
print("1 - Raramente")
print("0 - Nunca")

print("")

p1 = int(input("Pontos: "))

print("")
print("=-" * 40)

print("2. Você gosta de praticar atividades físicas ?")
print("Digite a pontuação de sua resposta: ")

print("")

print("3 - Amo")
print("2 - Gosto")
print("1 - Nem gosto nem acho ruim")
print("0 - Odeio")


print("")

p2 = int(input("Pontos: "))

print("")
print("=-" * 40)


print("3. Com que frequência as pessoas a sua volta te incentivam à praticar \natividades físicas ?")
print("Digite a pontuação de sua resposta: ")

print("")

print("3 - Todos os dias")
print("2 - Regularmente")
print("1 - Raramente")
print("0 - Nunca")


print("")

p3 = int(input("Pontos: "))

print("")

soma = p1 + p2 + p3

print("=-" * 15 + " CLASSIFICAÇÃO FINAL " + 15 * "=-")
print("8 a 9 pontos → Totalmente em dia com as atividades físicas")
print("4 a 7 pontos → Parcialmente em dia, mas pode melhorar a frequência")
print("0 a 3 pontos → Sedentário ou muito abaixo do recomendado")
print("=-" * 40)

print("")
print(f"Sua pontuação é: {soma}")

