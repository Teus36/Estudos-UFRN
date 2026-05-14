print("=-" * 10 + " Aula 1 " + 10 * "=-")
print("")
print("=-" * 8 + " Calcular média " + 8 * "=-")
print("")

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

soma = nota1 + nota2 + nota3
media = soma/3

print("")
print("=-" * 24)
print(f"A sua média é: {media:.2f}")