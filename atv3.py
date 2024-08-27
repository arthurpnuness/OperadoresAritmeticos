## Este código calcula a área de um círculo com base no raio fornecido pelo usuário. 

#interação com o usuário
raio = float(input("Digite o raio do círculo: ")) 

#Calculo
pi = 3.14159 # Valor aproximado de (pi)

area = pi * raio ** 2 # Calcula a área usando a fórmula - OUtra observação válida é os dois asteriscos(**), eles elevam o valor do raio ao quadrado

# Exibe o resultado
print('A área do círculo com raio {} é: {}'.format(raio, area)) 

