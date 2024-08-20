import os

# Exercicio 1
# Peça ao usuário para digitar um número.
# Utilize um laço while para contar de 0 até o número digitado.

# if __name__ == '__main__':
#   limit = int(input("Digite um numero: "))
#   text = input("Digite um Texto: ")
#   count = 0
#   while count != limit:
#     print(f"{text}")
#     count = count + 1

# Exercicio 2
# Peça ao usuário para digitar um número.
# Utilize um laço while para imprimir a tabuada desse número até o 10.

# if __name__ == '__main__':
#   number = int(input("Digite um numero: "))
#
#   for i in range(0, 11):
#       print(f"{ number * i }")

# 3 Soma de números:
# Inicialize uma variável soma com 0.
# Utilize um laço while para pedir ao usuário que digite números.
# A cada número digitado, adicione-o à variável soma.
# O laço para quando o usuário digitar 0.
# Ao final, imprima a soma total.

if __name__ == '__main__':
    number = 0
    result = 0

    while True:
      number = int(input("Digite um numero: para ser somado: "))
      if number == 0:
        break
      else:
        result += number
        print(result)
