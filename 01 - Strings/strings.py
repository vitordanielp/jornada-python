# Essa string será utilizada para dividir os conteúdos do código
separador = '\n#######################################################\n'


""" Concatenação de strings """

nome = 'Pedro'
sobrenome = 'Sousa'

print(nome + ' ' + sobrenome)  # 'Pedro Sousa'

# Outra alternativa
nome_completo = nome + ' ' + sobrenome
print(nome_completo)  # 'Pedro Sousa'


#################
print(separador)
#################


""" Métodos básicos """

print(nome_completo.lower())  # 'pedro sousa'
print(nome_completo.upper())  # 'PEDRO SOUSA'

nome = '  Pedro  '  # Espaços adicionados
sobrenome = '  Sousa  '  # Espaços adicionados
nome_completo = nome.strip() + ' ' + sobrenome.strip()  # Removendo espaços

print(nome_completo)  # 'Pedro Sousa'


#################
print(separador)
#################


""" Quebra de linhas e tabulação """

# \n é utilizado para quebra de linhas
print('Primeira linha da minha string.\nSegunda linha da minha string.')
# \t é utilizado para inserir tabulação
print('\tUtilizei tabulação nesta linha.')
# Dica básica
print('\"Para exibir caracteres especiais do Python, utiliza-se uma barra invertida antes.\"')


#################
print(separador)
#################


""" Método format """

nome = 'Pedro'
sobrenome = 'Sousa'
idade = 35

# A variável `nome` é inserida onde está indicado com {}
print('Meu nome é {}'.format(nome))
# As variáveis `nome` e `sobrenome` são inseridas onde está indicado com {}, respectivamente
print('Meu nome completo é {} {}'.format(nome, sobrenome))
# Outro exemplo, utilizando a variável `idade`
print('Meu nome é {}, tenho {} anos.'.format(nome, idade))
# Neste caso, podemos também indicar como as variáveis serão organizadas
print('Meu nome é {primeiro_nome} {ultimo_nome}, tenho {idade} anos.'.format(
    primeiro_nome=nome, ultimo_nome=sobrenome, idade=idade))

# Também funciona com outros tipos de dados, como int e float
valor = 354.682
print('O valor é R$ {preco}'.format(preco=valor))
# Podemos definir quantas casas decimais precisamos exibir. Isso não altera a variável
print('O valor é R$ {preco:.2f}'.format(preco=valor))


#################
print(separador)
#################


""" f Strings """

titulo = 'Geladeira'
material = 'Inox'
valor = 2399.99

print(f'Produto: {titulo.upper()}\nMaterial: {material}\nPreço: R$ {valor}')
# Outra forma de exibir a mesma informação
print(
    f'Produto: {titulo.upper()}\n'
    f'Material: {material}'
    f'Preço: R$ {valor}'
)

# Prévia de formatadores especiais
print(f'Produto: {titulo.upper():*^20}')  # *****GELADEIRA******
print(f'Produto: {titulo.upper():*<20}')  # GELADEIRA***********
print(f'Produto: {titulo.upper():*>20}')  # ***********GELADEIRA
print(f'Produto: {titulo.upper():-^20}')  # -----GELADEIRA------


#################
print(separador)
#################


""" Outros métodos """

# Substitui vírgulas por nada
print('Texto, com, várias, vírgulas.'.replace(',', ''))
# Conta quantas ocorrências de 'a'
print('Texto aleatório para contagem de letra.'.count('a'))
# Centralizar texto
print('Texto posicionado no centro.'.center(40, '*'))
# Posição da primeira ocorrência de 'a'
print('Onde fica o A?.'.index('a'))
# Verifica se a string é composta apenas por números
print('10500'.isnumeric())  # true
# Retorna uma lista que separa os itens com um espaço em branco
print('Minha string bonita'.split(' '))  # ['Minha', 'string', 'bonita']
# Primeiras iniciais maiúsculas
print('Meu título princial'.title())  # 'Meu Título Principal'
# Inicial maiúscula na primeira palavra
print('um título princial'.capitalize())  # 'Um título principal'
# Preencher com zeros à esquerda
print('585'.zfill(6))  # '000585'

# Encadeamento de métodos
print('meu texto bom'.replace('bom', 'maneiro').center(40, '-').upper())
