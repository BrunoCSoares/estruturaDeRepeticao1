'''
Escreva um algoritmo para ler 10 números. Todos os números lidos com valor inferior a 40 devem ser somados. Escreva o valor final da soma efetuada.
'''

soma = 0

for cont in range(1,11):
    num = float(input("Insira um número: "))
    if num < 40:
        soma += num

print(soma)