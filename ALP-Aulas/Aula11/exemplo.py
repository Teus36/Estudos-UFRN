linhas = int(input("Informe o número de linhas da matriz: "))
colunas = int(input("Informe o número de colunas da matriz: "))

matriz = []

for i in range(linhas):
    matriz.append([])
    for k in range(colunas):
        elemento = int(input("Informe o valor de [%d][%d]" %(i+1, k+1)))
        matriz[i].append(elemento)

print()
for linha in matriz:
    print(linha)