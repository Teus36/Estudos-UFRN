
def calcular_area_retangulo():
    base = int(input("Digite o comprimento da base do retângulo: "))
    altura = int(input("Digite a altura do retângulo: "))
    area = base * altura
    print(f"A área do retângulo é: {area} m²")

def calcular_area_total():
    comprimento = int(input("Digite o comprimento da sala: "))
    largura = int(input("Digite a largura da sala: "))
    altura = int(input("Digite a altura da sala: "))

    A1 = comprimento * largura
    A2 = comprimento * altura
    A3 = largura * altura

    area_total = A1 + 2 * A2 + 2 * A3

    print(f"A área total é: {area_total} m²")

def calcular_area_triangulo():
    base = int(input("Digite o comprimento da base do triângulo: "))
    altura = int(input("Digite a altura do triângulo: "))
    area_triangulo = (base * altura) / 2
    print(f"A área do triângulo é: {area_triangulo} m²")


def calcular_quantidade_arame():
    comprimento = int(input("Digite o comprimento do terreno: "))
    largura = int(input("Digite a largura do terreno: "))
    quantidade_arame = 2 * (comprimento + largura) * 5
    print(f"A quantidade de arame necessária é: {quantidade_arame} metros")  

while True:
    print("Escolha uma opção:")
    print("1 - Calcular área do retângulo")
    print("2 - Calcular área total")
    print("3 - Calcular área do triângulo")
    print("4 - Calcular quantidade de arame")
    print("5 - Sair")

    opcao = input("Digite o número da opção desejada: ")

    if opcao == "1":
        calcular_area_retangulo()
    elif opcao == "2":
        calcular_area_total()    
    elif opcao == "3":
        calcular_area_triangulo()
    elif opcao == "4":
        calcular_quantidade_arame()
    elif opcao == "5":
        print("Encerrando o programa.")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")


