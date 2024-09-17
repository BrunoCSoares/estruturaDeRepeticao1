'''
Escreva um programa em Python que solicite 10 valores inteiros ao usuário e mostre quantos desses valores lidos são negativos. Para tal, utilize a estrutura de repetição “for”.
'''
negativos = 0
for cont in range(1,11):
    num = int(input("Digite um número inteiro (positivo ou negativo): "))
    if num<0:
        negativos += 1

print(f"{negativos} são negativos")