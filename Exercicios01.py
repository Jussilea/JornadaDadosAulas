# Exercício 01: Crie um programa que o usuário digita o seu nome e retorna o número de caracteres

# print(len(input ("Digite o seu nome: "))) # len conta caracteres

# Exercício 02: Crie um programa onde o usuário digitre dois valores e apareça a soma
# Minha resolução
'''x = input ("Digite um valor: ")
x = float(x)
y = input ("Digite outro valor: ")
y = float(y)
print (x+y)'''
# Resolução do curso
#print(int((input("Digite um número: "))) + int(input("Digite outro número:")))

# Exercício 03: Refatore o exercício 01 atribuindo variáveis
#nome = input("Digite o seu nome: ")
#quantidade_de_caractere = len(nome)
#print (quantidade_de_caractere)

# DESAFIO
# Um programa em Python que solicita oao usuário para digitar seu nome, o valor do seu salário mensal e o valor do bônus que recebeu.
# O programa deve, então, imprimir uma mensagem saudando o usuário pelo nome informado, o valor do salário em comparação com o bônus
# recebido
''' Minha resolução
print ("Oi, usuário.")
nome = input ("Digite o seu nome: ")
salario = float (input ("Digite o seu salário mensal: "))
bonus = float (input ("Digite o valor do seu bônus: "))
calculo_bonus = float (1000 + salario * bonus)
print ("Oi,", nome, "Seu bônus foi de: ", calculo_bonus) '''

# Gabarito
CONSTANTE_BONUS_2024 = 1000
nome_usuario = input("Digite o seu nome: ")
salario_usuario = float(input("Digite o seu salário: "))
bonus_usuario = float(input("Digite o seu bônus: "))
valor_do_bonus = CONSTANTE_BONUS_2024 + salario_usuario * bonus_usuario
print(f"O usuário {nome_usuario} possui o bônus de {valor_do_bonus}")
