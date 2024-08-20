# Desenvolva um programa que crie uma lista de compras, de a opção de adicionar, remover ou finalizar
# Em adicionar, adicione o item que o usuarioquer ao final da lista
# Em remover, de a opção do usuário remover o item que ele quer
# Ao finalizar, encerre o programa

import os

def getAllProducts(listOfItems):
  if not listOfItems:
    print("A lista está vazia.")
    return
  print("Seus itens são:")
  for idx, item in enumerate(listOfItems, start=1):
    print(f"{idx}: {item}")

def clear_screen():
  print("-" * 100)

if __name__ == '__main__':
  option = 0
  listOfItems = []
  while True:
    clear_screen()
    print("Lista de compras - Selecione a opção desejada")
    print("1. Adicionar item ao carrinho")
    print("2. Remover item")
    print("3. Listar os items")
    print("4. Encerrar programa")
    option = int(input("Digite a opção: "))

    if option == 1:
      item = input(print("Digite seu item: "))
      listOfItems.append(item)
      print(f"{item} adicionado \n")

    elif option == 2:
      getAllProducts(listOfItems)
      var = int(input(print("Digite o numero do item que deseja remover: "))) - 1
      print(f"{listOfItems[var]} removido \n")
      listOfItems.pop(var)

    elif option == 3:
      getAllProducts(listOfItems)

    elif option == 4:
      break

    else:
      print("Comando errado")

