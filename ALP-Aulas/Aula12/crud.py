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
    nome  = str(input("Nome  : "))
    fone  = str(input("Fone  : "))
    email = str(input("E-mail: "))
    dnasc = str(input("Nasc  : "))
    lista_nomes += [nome]
    lista_fones += [fone]
    lista_dnasc += [dnasc]
    lista_email += [email]
    print()
  elif resp == '2':
    print()
    print("Módulo de Pesquisa")
    print()
    nome = str(input("Qual o nome do contato? "))
    tam = len(lista_nomes)
    pos = 0
    achou = False
    while (pos < tam) and (not achou):
      if nome == lista_nomes[pos]:
        achou = True
      else:
        pos += 1
    if achou:
      print("Nome : ", lista_nomes[pos])
      print("Fone : ", lista_fones[pos])
      print("Nasc : ", lista_dnasc[pos])
      print("Email: ", lista_email[pos])
    else:
      print("%s não é um contato da agenda"%nome)

    print()
  elif resp == '3':
    print()
    print("Módulo de Atualização")
    print()

    update_nome = str(input("Qual o nome do contato? "))
    tam = len(lista_nomes)
    pos = 0

    achou = False
    while (pos < tam) and (not achou):
      if update_nome == lista_nomes[pos]:
        achou = True
      else:
        pos += 1
      
    if achou:
      print("Nome : ", lista_nomes[pos])
      print("Fone : ", lista_fones[pos])
      print("Nasc : ", lista_dnasc[pos])
      print("Email: ", lista_email[pos])

      print("Qual informação deseja atualizar?")
      print("1 - Nome")
      print("2 - Fone")
      print("3 - Nasc")
      print("4 - Email")
      opcao = input("Escolha sua opção: ")

      if opcao == '1':
        lista_nomes[pos] = str(input("Novo nome: "))
      elif opcao == '2':
        lista_fones[pos] = str(input("Novo fone: "))
      elif opcao == '3':
        lista_dnasc[pos] = str(input("Nova data de nascimento: "))
      elif opcao == '4':
        lista_email[pos] = str(input("Novo email: "))

    print()
  elif resp == '4':
    print()
    print("Módulo de Exclusão")
    print()

    delete_nome = str(input("Qual o nome do contato? "))
    tam = len(lista_nomes)
    pos = 0
    achou = False
    while (pos < tam) and (not achou):
      if delete_nome == lista_nomes[pos]:
        achou = True
      else:
        pos += 1

    if achou:
      del lista_nomes[pos]
      del lista_fones[pos]
      del lista_dnasc[pos]
      del lista_email[pos]
      print("%s foi excluído da agenda"%delete_nome)
    else:
      print("%s não é um contato da agenda"%delete_nome)

    print()
  elif resp == '5':
    print()
    print("Módulo de Relatório")
    print()
    tam = len(lista_nomes)
    for i in range(tam):
      print("Nome : ", lista_nomes[i])
      print("Fone : ", lista_fones[i])
      print("Nasc : ", lista_dnasc[i])
      print("Email: ", lista_email[i])
      print()
    print()

  elif resp == '0':
    break
  else:
    print()
    print("Opção Inválida!")
    print()

print("Fim do Programa!")



