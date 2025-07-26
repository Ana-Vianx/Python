import random

print("""==============================
JOGUINHO PEDRA PAPEL E TESOURA
==============================""")
escolhaUsuario = int(input('1 - PEDRA\n2 - PAPEL\n3 - TESOURA\nEscolha uma opção:'))
escolhaOponente = random.choice(('PEDRA', 'PAPEL', 'TESOURA'))
print('JOGANDO...')

if escolhaUsuario == 1 and escolhaOponente == 'PAPEL' or escolhaUsuario == 2 and escolhaOponente == 'TESOURA' or escolhaUsuario == 3 and escolhaOponente == 'PEDRA':
   print('VOCÊ PERDEU! EU ESCOLHI {}'.format(escolhaOponente))
elif escolhaUsuario == 3 and escolhaOponente == 'PAPEL' or escolhaUsuario == 2 and escolhaOponente == 'PEDRA' or escolhaUsuario == 1 and escolhaOponente == 'PAPEL':
    print('VOCÊ GANHOU, PARABÉNS! EU ESCOLHI {}'.format(escolhaOponente))
else:
    print('JOGAMOS A MESMA MÃO! EU ESCOLHI {}'.format(escolhaOponente))
print('FIM DO JOGO!')