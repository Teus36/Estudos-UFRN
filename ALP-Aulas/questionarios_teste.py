k = int(input("Digite o tamanho da sua lista:"))
idades = []

for i in range(k):
  idade = int(input("Digite a idade: "))
  idades.append(idade)

media = sum(idades) / len(idades)
amplitude = max(idades) - min(idades)

idades_ordem = idades.sort()
pos = 0

for i in range(len(idades_ordem)):
    if len(idades_ordem) % 2 == 0:
        pos1 = idades_ordem[len(idades_ordem)/2]
        pos2 = idades_ordem[len(idades_ordem)/2 + 1]
        mediana = pos1 + pos2/2
        
print(mediana)