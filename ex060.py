"""from math import factorial
n = int(input('Digite um numero para calcular o fatorial:'))
f = factorial(n)
print('O fatorial de {} é {}'.format(n,f))"""



numero = int(input("Digite um número:"))
c = numero
fatorial = 1
print('Calculando o fatorial de {}'.format(numero))

while c > 0:
    print ('{}'.format(c), end='') 
    print('x'if c>1 else '=', end='')
    fatorial *=c
    c-=1
print(fatorial)
    

