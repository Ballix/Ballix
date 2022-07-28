# Crie um programa que faça o computador jogar Jokenpô com você.
from random import choice
import time
print('Vamos jogar JOKENPÔ!')
joke = str(input('você joga pedra, papel ou tesoura? ')).strip().lower()
print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PÔ')
time.sleep(1)
# jogadas = {1:'tesoura', 2:'papel', 3:'pedra'}
sort = choice({0: 'tesoura', 1: 'papel', 2: 'pedra'})
print('O computador jogou {}.'.format(sort))
if sort == 'tesoura' and joke == 'papel':
    print('Você Perdeu!')
elif sort == 'tesoura' and joke == 'pedra':
    print('Você Ganhou!')
elif sort == 'tesoura' and joke == 'tesoura':
    print('Empate!')
elif sort == 'papel' and joke == 'tesoura':
    print('Você Ganhou')
elif sort == 'papel' and joke == 'pedra':
    print('Você Perdeu!')
elif sort == 'papel' and joke == 'papel':
    print('Empate!')
elif sort == 'pedra' and joke == 'papel':
    print('Você Ganhou!')
elif sort == 'pedra' and joke == 'tesoura':
    print('Você Perdeu!')
elif sort == 'pedra' and joke == 'pedra':
    print('Empate!')
