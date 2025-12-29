### Exercício 1: Verificação de Qualidade de Dados
# Você está analisando um conjunto de dados de vendas e precisa garantir 
# que todos os registros tenham valores positivos para `quantidade` e `preço`. 
# Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos 
# forem positivos ou "Dados inválidos" caso contrário.
'''quantidade = 50
preco = -30
if quantidade > 0 and preco > 0:
    print("Dados válidos.")
else:
    print("Dados inválidos.")'''


### Exercício 2: Classificação de Dados de Sensor
# Imagine que você está trabalhando com dados de sensores IoT. 
# Os dados incluem medições de temperatura. Você precisa classificar cada leitura 
# como 'Baixa', 'Normal' ou 'Alta'. Considerando que:
'''temperatura = -40
if temperatura >= 30:
    print("Temperatura alta")
elif temperatura >= 20:
    print("Temperatura normal")
else:
    print("Temperatura baixa.")'''

### Exercício 3: Filtragem de Logs por Severidade
# Você está analisando logs de uma aplicação e precisa filtrar mensagens 
# com severidade 'ERROR'. Dado um registro de log em formato de dicionário 
# como `log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}`, 
# escreva um programa que imprima a mensagem se a severidade for 'ERROR'.
'''log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}
if log['level'] == "ERROR":
    print(log['message'])
else:
    print("Sem erro")'''

### Exercício 4: Validação de Dados de Entrada
# Antes de processar os dados de usuários em um sistema de recomendação, 
# você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha 
# fornecido um email válido. Escreva um programa que valide essas condições 
# e imprima "Dados de usuário válidos" ou o erro específico encontrado.
'''from email_validator import validate_email, EmailNotValidError
def validar_email(email):
    try:
        valid = validate_email(email, check_deliverability=True)
        return True, valid.email
    except EmailNotValidError as e:
        return False, str(e)
try:
    idade_usuario = int(input("Digite sua idade: "))
except ValueError:
    print("Erro: idade deve ser somente números")
    exit()
email_usuario = input("Digite o seu e-mail: ")
is_email_valido, mensagem_email = validar_email(email_usuario)
if (18 <= idade_usuario <= 65) and is_email_valido:
    print("Dados de usuário válidos")
else:
    if not (18 <= idade_usuario <= 65):
        print("A idade deve estar entre 18 e 65 anos.")
    if not is_email_valido:
        print(f"E-mail inválido {mensagem_email}")'''
#Gabarito
'''idade = 25  # Exemplo de valor, substitua com input do usuário se necessário
email = "usuario@exemplo.com"  # Exemplo de valor, substitua com input do usuário se necessário

if not 18 <= idade <= 65:
    print("Idade fora do intervalo permitido")
elif "@" not in email or "." not in email:
    print("Email inválido")
else:
    print("Dados de usuário válidos")'''

### Exercício 5: Detecção de Anomalias em Dados de Transações
# Você está trabalhando em um sistema de detecção de fraude e precisa identificar 
# transações suspeitas. Uma transação é considerada suspeita se o valor for superior 
# a R$ 10.000 ou se ocorrer fora do horário comercial (antes das 9h ou depois das 18h). 
# Dada uma transação como `transacao = {'valor': 12000, 'hora': 20}`, verifique se ela é suspeita.
'''valor = 12000
hora = 20

if valor > 10000 and 9 < hora > 18:
    print("Transação suspeita")
else:
    print("Transação normal.")'''


### Exercício 6. Contagem de Palavras em Textos
# Objetivo:** Dado um texto, contar quantas vezes cada palavra única aparece nele.
'''texto = "hoje é a nossa terceira aula do bootcamp, bootcamp de python"
novo_texto = texto.replace(",","")
palavras = novo_texto.split()
print(palavras)
contagem_palavras = {}
for palavra in palavras:
    if palavra in contagem_palavras:
        contagem_palavras[palavra] += 1
    else:
        contagem_palavras[palavra] = 1
print(contagem_palavras)'''


### Exercício 7. Normalização de Dados
# Objetivo:** Normalizar uma lista de números para que fiquem na escala de 0 a 1.
'''numeros = [10, 20, 30, 40, 50]
minimo = min(numeros)
maximo = max(numeros)
intervalo = maximo - minimo
normalizados = []
for x in numeros:
    valor_novo = (x - minimo) / intervalo
    normalizados.append(valor_novo)
print("Original: ", numeros)
print("Normalizados: ", normalizados)'''

### Exercício 8. Filtragem de Dados Faltantes
# Objetivo:** Dada uma lista de dicionários representando dados de usuários, filtrar aqueles que têm um campo específico faltando
'''dados_usuarios = [{"nome": "Lucuiano", "email": "luciano@gmail.com"}, {"nome": "Marcelo", "email": " "},
                  {"nome": " ", "email": "alexandre@gmail.com"}]
usuarios_validos = [usuario for usuario in dados_usuarios 
                    if usuario.get("email").strip() and usuario.get("nome").strip()]
print(usuarios_validos)'''


'''Por que usar .get() e não usuario["email"]?
Segurança: Se você tentar usar usuario["email"] no usuário "Carol" (que não tem a chave), o Python vai travar com um erro (KeyError). O .get() evita isso.
Limpeza: O if usuario.get("email"): já filtra automaticamente:
Chaves que não existem (None é falso).
Campos vazios ("" string vazia é falso).
Campos nulos (None é falso).'''


### Exercício 9. Extração de Subconjuntos de Dados
# Objetivo:** Dada uma lista de números, extrair apenas aqueles que são pares.
'''num = [[], []] # uma lista foi atribuída a num, sendo que dentro dessa lista possui outras duas, uma sendo par e a outra ímpar
valor = 0
for c in range (1, 8): #  vão ser inseridos 7 valores que precisam ser analisados, c vai ser o contandor, range desconsidera o último valor, por isso 8
    valor = int(input(f"Digite o {c}º valor inteiro: "))
    if valor % 2 ==0:
        num [0].append(valor)
    else:
        num[1].append(valor)
print(f"Todos os valores: {num}")
num[0].sort() #sort organiza os valores em ordem
num[1].sort()
print(f"Os valores pares são: {num[0]} e os valores ímpares são: {num[1]}")
print(f"Os valores pares são: {num[0], len(num[0])} e os valores ímpares são: {num[1], len(num[0])}")'''

### Exercício 10. Agregação de Dados por Categoria
# Objetivo:** Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.
'''vendas = [
    {"categoria": "eletrônicos", "valor": 1200},
    {"categoria": "livros", "valor": 200},
    {"categoria": "eletrônicos", "valor": 800},
    {"categoria": "livros", "valor": 300},
    {"categoria": "beleza", "valor": 500}
]

total_por_categoria = {}
for venda in vendas:
    categoria = venda["categoria"]
    valor = venda["valor"]
    if categoria in total_por_categoria:
        total_por_categoria[categoria] += valor
    else:
        total_por_categoria[categoria] = valor

print(total_por_categoria)'''


### Exercícios com WHILE

### Exercício 11. Leitura de Dados até Flag
# Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida.
'''dados = []
entrada = ""
while entrada.lower () != "sair":
    entrada = input("Digite uma palavra (ou 'sair' para terminar):")
    if entrada.lower() != "sair":
        dados.append(entrada)
print (dados)'''

### Exercício 12. Validação de Entrada
# Solicitar ao usuário um número dentro de um intervalo específico até que a entrada seja válida.
'''numero = int(input("Digite um número inteiro entre 1 e 10: "))
while numero < 1 or numero > 10:
    print("Número fora do intervalo")
    numero = int(input("Digite um número inteiro entre 1 e 10: "))
print("Número válido.")'''


### Exercício 13. Consumo de API Simulado
# Simular o consumo de uma API paginada, onde cada "página" de dados é processada em loop até que não haja mais páginas.
'''pagina_atual = 1
paginas_totais = 5
while pagina_atual <= paginas_totais:
    print(f"Processando paginas {pagina_atual} de {paginas_totais}")
    pagina_atual += 1
print("Todas as páginas foram processadas.")'''

### Exercício 14. Tentativas de Conexão
# Simular tentativas de reconexão a um serviço com um limite máximo de tentativas.
'''tentativas_maximas = 5
tentativa = 1

while tentativa <= tentativas_maximas:
    print(f"Tentativa {tentativa} de {tentativas_maximas}")
    # Simulação de uma tentativa de conexão
    # Aqui iria o código para tentar conectar
    if True:  # Suponha que a conexão foi bem-sucedida
        print("Conexão bem-sucedida!")
        break
    tentativa += 1
else:
    print("Falha ao conectar após várias tentativas.")'''

### Exercício 15. Processamento de Dados com Condição de Parada
# Processar itens de uma lista até encontrar um valor específico que indica a parada.
itens = [1, 2, 3, "parar", 4, 5]

i = 0
while i < len(itens):
    if itens[i] == "parar":
        print("Parada encontrada, encerrando o processamento.")
        break
    # Processa o item
    print(f"Processando item: {itens[i]}")
    i += 1

# Desafio
'''nome_valido = False
salario_valido = False
bonus_valido = False
 
CONSTANTE_BONUS_2024 = 1000
while nome_valido is not True:
    try:
        nome_usuario = input("Digite o seu nome: ")
        #if nome_usuario.isdigit():
        if any(char.isdigit() for char in nome_usuario):
            raise ValueError ("O nome deve conter somente letras.")
        elif len(nome_usuario) == 0:
            raise ValueError ("Você não digitou nada.")
        elif nome_usuario.isspace():
            raise ValueError("Você digitou só espaço.")
        else:
            nome_valido = True
            print ("Nome válido:", nome_usuario)
    except ValueError as e:
        print(e)
while salario_valido is not True:  
    try:
        salario_usuario = float(input("Digite o seu salário: "))
        if salario_usuario <= 0:
            print("Erro: Salário não pode ser menor ou igual a zero.")
        else:
            salario_valido = True
    except ValueError:
        print("Erro: Salário devem ser apenas números.")
while bonus_valido is not True:
    try:
        bonus_usuario = float(input("Digite o seu bônus: "))
   
        if bonus_usuario <= 0:
            print("Erro: Bônus não pode ser menor ou igual a zero.")
        else:
            bonus_valido = True
    except ValueError:
        print("Erro: Bônus devem ser apenas números.")
valor_do_bonus = CONSTANTE_BONUS_2024 + salario_usuario * bonus_usuario
print(f"O usuário {nome_usuario} possui o bônus de {valor_do_bonus}")'''