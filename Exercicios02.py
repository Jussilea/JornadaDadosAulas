# #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
'''x = int(input("Digite um número inteiro: "))
y = int(input("Digite um número inteiro: "))
soma = (x + y)
print(f"A soma dos dois números é: {soma}")'''

# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
'''x = int(input("Digite um número: "))
CONSTANTE_RESTO = 5
resultado = x % CONSTANTE_RESTO
print (f"O resto da divisão é: {resultado}")'''

# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
'''x = int(input("Digite um número inteiro: "))
y = int(input("Digite outro número inteiro: "))
multiplicacao = (x * y)
print(f"O resultado da multipĺicação é: {multiplicacao}")'''

# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
'''x = int(input("Digite um número inteiro: "))
y = int(input("Digite outro número inteiro: "))
divisao_inteira = (x // y)
print(f"A parte inteira da divisão é: {divisao_inteira}")'''

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
'''base = int(input("Digite um número inteiro: "))
expoente = 2
resultado = pow(base, expoente)
print(f"O quadrado do número digitado é: {resultado}")'''

# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
'''x = float(input("Digite um número: "))
y = float(input("Digite outro número: "))
soma = (x + y)
print(f"A soma dos dois números é: {soma: .4f}")'''

# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
'''x = float(input("Digite um número: "))
y = float(input("Digite outro número: "))
soma = x + y
media = (soma / 2)
print(f"A média dos números é: {media}")'''

# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
'''base = float(input("Digite o número da base para o cálculo da potenciação: "))
expoente = float(input("Digite o expoente: "))
resultado = pow(base, expoente)
print(f"O resultado da operação é {resultado}")'''

# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
'''temperatura_celsius = float(input("Digite a temperatura em Celsius: "))
temperatura_fahrenheit = (temperatura_celsius * 1.8) + 32
print(f"A temperatura em Fahrenheit é: {temperatura_fahrenheit}")'''

# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
'''import math
raio = float(input("Digite o raio do círculo: "))
area_circulo = math.pi * raio ** 2
print(f"A área do círculo é: {area_circulo}")'''

# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
'''palavra = input("Digite uma palavra: ")
palavra_maiscula = palavra.upper()
print(palavra_maiscula)'''

# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
'''nome = input("Digite o seu nome completo: ")
nome_maiusculo = nome.upper()
print(nome_maiusculo)'''

# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
'''frase = (input("Digite uma frase: "))
frase_sem_espaco = frase.strip()
print(frase_sem_espaco)'''

# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
'''data = input("Digite uma data no formato dd/mm/aaaa: ")
print(data.split("/"))'''
# Gabarito curso, considerando a lista 
'''data = input("Digite uma data no formato dd/mm/aaaa: ")
lista_data = data.split("/")
print(f"O dia é: {lista_data[0]}")
print(f"O mẽs é: {lista_data[1]}")
print(f"O ano é: {lista_data[2]}") '''

# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.
'''palavra1 = input ("Digite uma palavra: ")
palavra2 = input ("Digite outra palavra: ")
print (palavra1 + " " + palavra2)'''


# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
'''expressao1 = input("Digite true ou false: ").lower() == "true"
expressao2 = input("Digite true ou false: ").lower() == "true"
resultado = expressao1 and expressao2
print(resultado)'''

# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
'''expressao1 = input("Digite true ou false: ").lower() == "true"
expressao2 = input("Digite true ou false: ").lower() == "true"
resultado = expressao1 or expressao2
print(resultado)'''

# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
'''expressao1 = input("Digite true ou false: ").strip().lower() == "true"
resultado = not expressao1
print(resultado)'''

# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
'''numero1 = float(input("Digite um número: "))
numero2  = float(input("Digite outro número: "))
if numero1 == numero2:
    print("Os números são iguais")
else: print("Os números são diferentes")'''


# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
'''numero1 = float(input("Digite um número: "))
numero2  = float(input("Digite outro número: "))
if numero1 != numero2:
    print("Os números são diferentes")
else: print("Os números são iguais")'''

# #### try-except e if

# 21: Conversor de Temperatura
'''try:
    temperatura_celsius = float(input("Digite a temperatura em Celsius: "))
    temperatura_fahrenheit = (temperatura_celsius * 1.8) + 32
    print(f"A temperatura em Fahrenheit é: {temperatura_fahrenheit}")
except ValueError:
    print("Digite um número válido")'''

# 22: Verificador de Palíndromo
'''entrada = input("Digite uma palavra ou frase: ")
if isinstance(entrada, str):
    formatado = entrada.replace(" ", "").lower()
    if formatado == formatado[::-1]:
        print("É um palíndromo.")
    else:
        print("Não é um palíndromo.")
else:
    print("Entrada inválida. Por favor, digite uma palavra ou frase.")'''

# 23: Calculadora Simples
'''try:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    operador = input("Digite o operador (+, -, *, /): ")
    if operador == '+':
        resultado = num1 + num2
    elif operador == '-':
        resultado = num1 - num2
    elif operador == '*':
        resultado = num1 * num2
    elif operador == '/' and num2 != 0:
        resultado = num1 / num2
    else:
        print("Operador inválido ou divisão por zero.")
    print("Resultado:", resultado)
except ValueError:
    print("Erro: Entrada inválida. Certifique-se de inserir números.")'''

# 24: Classificador de Números
'''try:
    numero = int(input("Digite um número: "))
    if numero > 0:
        print("Positivo")
    elif numero < 0:
        print("Negativo")
    else:
        print("Zero")
    if numero % 2 == 0:
        print("Par")
    else:
        print("Ímpar")
except ValueError:
    print("Por favor, digite um número inteiro válido.")'''

# 25: Conversão de Tipo com Validação
'''entrada_lista = input("Digite uma lista de números separados por vírgula: ")
numeros_str = entrada_lista.split(",")
numeros_int = []
try:
    for num in numeros_str:
        numeros_int.append(int(num.strip()))
    print("Lista de inteiros:", numeros_int)
except ValueError:
    print("Erro: certifique-se de que todos os elementos são números inteiros válidos.")'''

# Desafio
CONSTANTE_BONUS_2024 = 1000
nome_usuario = input("Digite o seu nome: ")
if any(char.isdigit() for char in nome_usuario):
    print("O nome deve conter somente letras.")
    exit()
elif len(nome_usuario) == 0:
    print("Você não digitou nada.")
    exit()
elif nome_usuario.isspace():
    print("Você digitou só espaço.")
    exit()
try:
    salario_usuario = float(input("Digite o seu salário: "))
    bonus_usuario = float(input("Digite o seu bônus: "))
except ValueError:
    print("Erro: Salário e bônus devem ser apenas números.")
    exit()
if salario_usuario <= 0 or bonus_usuario < 0:
    print("Erro: Salário não pode ser menor ou igual a zero ou bônus não pode ser negativo.")
    exit()
valor_do_bonus = CONSTANTE_BONUS_2024 + salario_usuario * bonus_usuario
print(f"O usuário {nome_usuario} possui o bônus de {valor_do_bonus}")