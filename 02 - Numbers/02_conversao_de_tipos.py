idade = 35

# Convertendo a variáver `idade` para o tipo string.
texto = 'Parabéns pelos seus ' + str(idade) + ' anos de idade!'
# Sem essa conversão, o código terá um erro, pois não
# é possível concatenar strings com inteiros

print(texto)

pontuacao_str = '10'
pontuacao_int = int(pontuacao_str)

print(pontuacao_int)
print(f'Tipo: {type(pontuacao_int)}')  # Verificando o tipo de dado

# A vírgula irá gerar um erro se tentarmos passar este valor para float
pontuacao_str = '5,5'
# A vírgula foi substituída pelo ponto para contornar o problema
pontuacao_float = float(pontuacao_str.replace(',', '.'))

print(pontuacao_float)
print(f'Tipo: {type(pontuacao_float)}')

# print(int('5.5'))  # Não é possível fazer essa conversão
print(int(5.5))  # Essa conversão é feita normalmente
