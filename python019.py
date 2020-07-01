import random

a = input('Digite o nome do primeiro aluno: ')
b = input('Digite o nome do segundo: ')
c = input('Digite o nome do terceiro: ')
d = input('Digite o nome do quarto: ')

names = [a, b, c, d]

print('O aluno escolhido foi: {}'.format(random.choice(names)))
