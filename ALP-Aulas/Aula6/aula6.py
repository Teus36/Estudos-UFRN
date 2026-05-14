print("Informe os valores a serem ordenados")
a = int(input("Valor 1: "))
b = int(input("Valor 2: "))
c = int(input("Valor 3: "))

if (a<=b) and (b<=c):
    print(f"Os valores em ordem crescente são: {a}, {b}, {c}")

elif (a<=c) and (c<=b):
    print(f"Os valores em ordem crescente são: {a}, {c}, {b}")

elif (b<=a) and (a<=c):
    print(f"Os valores em ordem crescente são: {b}, {a}, {c}")  

elif (b<=c) and (c<=a):
    print(f"Os valores em ordem crescente são: {b}, {c}, {a}")

elif (c<=a) and (a<=b):
    print(f"Os valores em ordem crescente são: {c}, {a}, {b}")

else:
    print(f"Os valores em ordem crescente são: {c}, {b}, {a}")

