#escreva um programa em python que solicite ao usuário informar um número inteiro.
# O programa deve calcular o valor do fatorial e imprimir o resultado para o usuário.
# Autor: Diego Vale do Nascimento - 07/10/2022
print('Cálculo do Fatorial')
n = int(input('Digite um número inteiro: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))