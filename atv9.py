## Este código calcula o custo total para trocar as ferraduras de todos os cavalos em uma fazenda, considerando que o preço de troca de ferradura é fixo por cavalo. 

# Interação com o usuario
cavalos = int(input('Quantos cavalos tem na fazenda? '))

# Calculo
nFerraduras = cavalos * 4
preco = 80
valorTotal = nFerraduras * preco

# Exibe o resultado
print('O valor total para trocar as ferraduras do(s) cavalos(s) é de R${}'.format(valorTotal))