'''
Desenvolva um programa que receba:
- taxa de abatimento em porcentagem;
- número de prestações;
- valor da primeira prestação.
Seu programa deverá exibir na tela os valores das prestações na forma decrescente, dado que a cada mês o valor da prestação diminui do valor da prestação do mês anterior (utilize a taxa de abatimento fornecida pelo usuário para realizar esse cálculo). OBS: utilize o “for”
'''

taxaAbat = float(input("Insira a taxa de abatimento: "))
numPrest = int(input("Insira o número de prestações: "))
prest = int(input("Insira o valor da primeira prestação: "))
taxaAbat = taxaAbat / 100

for cont in range(1,numPrest+1):
    print(f"prestação {cont} R${prest:.2f}")
    prest -= prest*taxaAbat