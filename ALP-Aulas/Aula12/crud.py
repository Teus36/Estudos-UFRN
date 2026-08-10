lista_nomes = ['Flavius', 'Fabricio', 'Taciano', 'Karliane', 'Márcio']
lista_fones = ['99999-1111', '99999-2222', '99999-3333', '99999-4444', '99999-5555']
lista_dnasc = ['26/11/1970', '08/08/1980', '31/12/1982', '07/07/1977', '01/01/1950']
lista_email = ['flavius@ufrn.br', 'fabricio@ufrn.br', 'taciano@ufrn.br', 'karliane@ufrn.br', 'márcio@ufrn.br']

resp = ""

while resp != '0':
  print("#############################")
  print("#####  Programa Agenda  #####")
  print("#############################")
  print("##  1 - Cadastrar contato   #")
  print("##  2 - Pesquisar contato   #")
  print("##  3 - Atualizar contato   #")
  print("##  4 - Apagar contato      #")
  print("##  5 - Listar todos        #")
  print("##  0 - Sair                #")
  resp = input("##  Escolha sua opção: ")

  if resp == '1':
    print()
    print("Módulo de Cadastro")
    print()
    
    nome = str(input("Digite o seu nome: "))
    fones = str(input("Digite o seu telefone: "))
    dnasc = str(input("Digite a sua data de nascimento: "))
    email = str(input("Digite o seu email: "))
    lista_nomes += nome
    lista_fones += fones 
    lista_dnasc += dnasc
    lista_email += email
    
    print()
  elif resp == '2':
    print()
    print("Módulo de Pesquisa")
    print()

    pesquisa = str(input("Qual usuário você está procurando? "))
    achou = False
    pos = 0

    for i in range(len(lista_nomes)):
      if pesquisa == lista_nomes[i]:
          achou = True
          pos = i
      else:
          print("Este usuário não está na lista!!")

    if achou:
      print(lista_nomes[pos])
      print(lista_fones[pos])
      print(lista_dnasc[pos])
      print(lista_email[pos])
    print()
  elif resp == '3':
    print()
    print("Módulo de Atualização")
    print()

    atualizar_nome = str(input("Informe o usuário que você quer atualizar: "))
    achou = False
    pos = 0

    for i in range(len(lista_nomes)):
      if atualizar_nome == lista_nomes[i]:
        achou = True
        pos = i
      else:
        print()

    if achou:
      print(lista_nomes[pos])
      print(lista_fones[pos])
      print(lista_dnasc[pos])
      print(lista_email[pos])
      print()

      nome = str(input("Digite o seu nome: "))
      fones = str(input("Digite o seu telefone: "))
      dnasc = str(input("Digite a sua data de nascimento: "))
      email = str(input("Digite o seu email: "))

      lista_nomes[pos] = nome
      lista_fones[pos] = fones 
      lista_dnasc[pos] = dnasc
      lista_email[pos] = email

    print()
  elif resp == '4':
    print()
    print("Módulo de Exclusão")

    deletar_nome = str(input("Informe o usuário que você quer deletar: "))
    achou = True
    pos = 0

    for i in range(len(lista_nomes)):
      if deletar_nome == lista_nomes[i]:
        achou = True
        pos = i
      else:
        print()
          
    if achou:
      del lista_nomes[pos]
      del lista_fones[pos]
      del lista_dnasc[pos]
      del lista_email[pos]
    
    print()

    print()
  elif resp == '5':
    print()
    print("Módulo de Relatório")
    print()
    
    for i in range(len(lista_nomes)):

      print(lista_nomes[i])
      print(lista_fones[i])
      print(lista_dnasc[i])
      print(lista_email[i])
      print()

  elif resp == '0':
    break
  else:
    print()
    print("Opção Inválida!")
    print()

print("Fim do Programa!")



