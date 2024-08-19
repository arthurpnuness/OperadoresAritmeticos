## Este código calcula o preço de venda de um produto, adicionando uma margem de lucro de 65% ao preço de custo informado pelo usuário. 

## Interação com o usuário
custo = int(input('Digite o preço de custo do produto:'))

## Calculo
venda = custo + ( custo * 0.65)

# Exibe o Resultado
print('O preço final de venda do produto é de R${}'.format(venda))