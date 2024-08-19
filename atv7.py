## Este código calcula o valor total a ser pago por uma quantidade de melões que o usuário deseja comprar, com base no preço unitário do melão.

# Interação com o Usuário
qtdMelao = int(input('Quantos melões voce vai querer levar? '))

# Definição do custo do melao
precoMelao = 4.25

# Calculo
valorTotal = qtdMelao * precoMelao

# Exibe o Resulrado
print('O valor total a ser pago é de R${}'.format(valorTotal))