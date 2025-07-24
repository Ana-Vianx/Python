from datetime import datetime

print("""====================
ALISTAMENTO MILITAR
====================""")
ano=int(input('Digite o ano de nascimento: '))
idade=datetime.now().year - ano

if idade < 18:
    print("Você ainda vai se alistar daqui a {} anos".format(18-idade))
elif idade == 18:
    print('Está na hora de se alistar')
else:
    print('Você já passou do tempo de alistamento há {} anos'.format(idade-18))