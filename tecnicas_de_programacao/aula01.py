def atividade_01():
  x = int(input("Adicione o valor do lado x? "))
  y = int(input("Adicione o valor do lado y? "))

  calc = x * y
  print(f'A área do quadrado é {calc}')


def atividade_02():
  print("A lampada está ligada? 1 para sim e 2 para não")
  state = input()

  if state == 1:
    print('A lampada esta a ligada')
    state == 0
  else:
    print('A lampada esta desligada')
    state == 1


def atividade_03():
  print("Coloque a nota do aluno: ")
  nota = int(input())
  letter = ""

  if nota > 10 or nota < 0:
    print("O valor deve estar entre 0 e 10")
    return

  if nota >= 9:
    letter = "A"
  elif nota >= 8:
    letter = "B"
  elif nota >= 7:
    letter = "C"
  elif nota >= 6:
    letter = "D"
  elif nota < 6:
    letter = "E"
  else:
    print("valor incorreto")

  return print(f"A nota do aluno é {letter}")


if __name__ == '__main__':
  atividade_03()
