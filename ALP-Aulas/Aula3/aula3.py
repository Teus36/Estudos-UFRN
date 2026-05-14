a = int(input("Digite um valor inteiro para A: "))
b = int(input("Digite um valor inteiro para B: "))

print("Invertendo os valores...")

a = a + b
b = a - b
a = a - b

print("Novo valor de A: ", a)
print("Novo valor de B: ", b)   
print("Fim do programa.")

