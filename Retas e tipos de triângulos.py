r1=float(input('Digite a primeira reta do triângulo: '))
r2=float(input('Digite a segunda reta do triângulo: '))
r3=float(input('Digite a terceira reta do triângulo: '))
if r1+r2>r3 and r1+r3>r2 and r2+r3>r1:
    print('\033[1;36mAs retas formam um triângulo')
    if r1==r2==r3:
        print('É um triângulo equilátero')
    elif r1==r2 or r1==r3 or r2==r3:
        print('É um triângulo isóceles')
    else:
        print('É um triângulo escaleno')
else:
    print('\033[1;31mAs retas não formam um triângulo')
