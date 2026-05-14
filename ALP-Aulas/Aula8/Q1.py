print("Entrevista do vinho")
total = int(input("Quantas pessoas serão entrevistadas? "))
tinto = 0
branco = 0
rose = 0
for i in range(1, total + 1):
    pessoa = input("Qual seu nome?: ")
    vinho = str(input("Entre Tinto, Branco ou Rose, de qual tipo de vinho você gosta?: "))
    print(f"{pessoa} gosta de vinho {vinho}")
    if vinho.lower() == "tinto":
        tinto += 1
    elif vinho.lower() == "branco":
        branco += 1
    elif vinho.lower() == "rose":
        rose += 1

print("-=-" * 15)
print("Resultados da entrevista:")
print(f"Total de pessoas entrevistadas: {total}")
print(f"Total de vinhos tinto: {tinto}")
print(f"Total de vinhos branco: {branco}")
print(f"Total de vinhos rose: {rose}")
print("-=-" * 15)
print("Resultado Percentual:")
print(f"Percentual de vinhos tinto: {tinto/total*100:.2f}%")
print(f"Percentual de vinhos branco: {branco/total*100:.2f}%")
print(f"Percentual de vinhos rose: {rose/total*100:.2f}%")
print("-=-" * 15)