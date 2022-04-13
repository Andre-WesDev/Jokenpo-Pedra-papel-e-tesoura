from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
comp = randint(0, 2)
print("""Suas opções:
  [ 0 ] PEDRA
  [ 1 ] PAPEL
  [ 2 ] TESOURA""")
jog = int(input("Qual é a sua jogada?  "))
print("\nJO")
sleep(1)
print("KEN")
sleep(1)
print("PO!!!")
sleep(1)
print('-='*11)
print('computador jogou {}'.format(itens[comp]))
print('jogador jogou {}'.format(itens[jog]))
print('-='*11)
if comp == 0:
   if jog == 0:
       print("EMPATE")
   elif jog == 1:
       print("Jogador VENCE")
   elif jog == 2:
       print("Computador VENCE")
   else:
       print("JOGADA INVÁLIDA")
elif comp == 1:
    if jog == 0:
       print("Computador VENCE")
    elif jog == 1:
       print("EMPATE")
    elif jog == 2:
       print("Jogador VENCE")
    else:
       print("JOGADA INVÁLIDA")
elif comp == 2:
    if jog == 0:
       print("JOGADOR VENCE")
    elif jog == 1:
       print("COMPUTADOR VENCE")
    elif jog == 2:
       print("EMPATE")
    else:
       print("JOGADA INVÁLIDA")
