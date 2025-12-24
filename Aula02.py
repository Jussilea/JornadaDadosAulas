'''
1. Inteiros (int)
"//" divisão inteira
"%" módulo - resto da divisão

3 + 5
3 - 5
print(5 / 4) divisão
print(5 // 4) só a parte inteira da divisão

2. Ponto Flutuante (float)

3. String (str)
"()" em Python, é uma vocação de variável 
Métodos e operações
.upper(): converte para maiúsculas
.lower(): converte para minúsculas
.strip(): remove espaços em branco no início e no final
.split(sep): divide a string em uma lista, utilizando sep como delimitador
email_aluno = jussileagf@gmail.com
print(email_aluno.split(@))
+ concatenação de strings

4. Booleanos (bool)
Operações lógicas
and: e lógico
or: ou lógico
not: não lógico
==: igualdade
!=: diferença
valor_1 = False
valor_2 = True
print (valor_1 and valor_2)

Expoente: pow(base, expoente) - para pontos flutuantes
"**" - operador

try:
except
pensar em um possível problema para que o programa não pare, caso dê algum erro
exemplo
try:
    numero1 = int(input("Inserir um número inteiro: "))
    numero2 = int(input("Inserir outro número inteiro"))
    resultado = numero1 // numero2
    print(resultado)
except ZeroDivisionError:
    print("intereger division or modulo by zero")

Exemplo que causa TyperError - fluxo de processo
try: 
    resultado = len(3)
    print(resultado)
except TyperError as e:
    print(e)
else:
    print("Tudo ocorreu bem")
finally:
    print("O importante é participar")

Exemplo isinstance if e else
numero = int(input("Insira um número: "))
if isinstance(numero, int):
    print("A variável é um inteiro")
else:
    print("A variável não é um inteiro")


'''

