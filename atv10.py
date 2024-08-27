## Este código calcula e exibe o preço final de um produto, bem como seu dobro e metade, considerando um acréscimo de 30% ao preço de custo. 

## Aqui foi feito dois exercicios em um

# Interação com o usuário
custo = int(input('Digite o preço de custo do produto:'))

# Calculos
acrescimo = custo * 0.30
venda = custo + acrescimo
dobro = venda * 2
metade = venda / 2

# Exibe o resultado
print('O valor final do produto é de R${} - O dobro é R${} e a metade é R${}'.format(venda, dobro, metade))
