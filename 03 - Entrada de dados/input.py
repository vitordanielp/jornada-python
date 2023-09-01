nome = input('Digite seu nome: ')
idade = int(input('Informe sua idade: '))
# Por padrão, a função input retorna uma String

print(
    f'Nome: {nome}\n'
    f'Idade: {idade}'
)

# Entrada
numero = input('Digite um número: ')
expoente = input('Digite um expoente: ')

# Processamento
resultado = int(numero) ** int(expoente)

# Saída
print(f'O resultado de {numero} elevado è {expoente} é: {resultado}')
