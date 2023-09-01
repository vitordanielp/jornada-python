numero_1 = input('Digite o primeiro número: ')
numero_2 = input('Digite o segundo número: ')

operacao = input(
    'Digite a operação desejada:\n'
    '\t+ para ADIÇÃO\n'
    '\t- para SUBTRAÇÃO\n'
    '\t* para MULTIPLICAÇÃO\n'
    '\t/ para DIVISÃO\n'
)

equacao = f'{numero_1}{operacao}{numero_2}'  # String com os dados de entrada
resultado = eval(equacao)

print(f'Resultado: {resultado}')
