# Interação com o usuário 
fahrenheit = float(input("Digite a temperatura em graus Fahrenheit: "))

# Fórmula de conversão para Celsius
celsius = (fahrenheit - 32) * 5 / 9

#  Exibe  o resultado
print('{} graus Fahrenheit é igual a {} graus Celsius'.format(fahrenheit,round(celsius, 2))) 

##A função round(celsius, 2) é usada para arredondar o valor de celsius para duas casas decimais.
