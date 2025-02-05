"""
Exercício 1 – Identificando Quadrados Perfeitos

Objetivo:
Crie uma função chamada `classificar_quadrados` que receba uma lista de números inteiros e retorne um dicionário com duas chaves:
    - 'quadrados_perfeitos': contendo os números que são quadrados perfeitos (por exemplo, 1, 4, 9, 16, …);
    - 'nao_quadrados': contendo os demais números.

Requisitos:
- Utilize laços de repetição para percorrer a lista.
- Adicione uma docstring explicando o funcionamento da função.

Exemplo de chamada:
    resultado = classificar_quadrados([1, 2, 3, 4, 8, 9, 15])
    print(resultado)
    # Saída esperada: {'quadrados_perfeitos': [1, 4, 9], 'nao_quadrados': [2, 3, 8, 15]}
    
Importante:
- Não se preocupe com números negativos.
"""
# Sua solução aqui

def quadrados_perfeitos():
    ''' definição para retornar os numeros que são quadrados perfeitos, e os que não são
    dentro de uma lista de numeros inseridos pelo usuário. '''
    numeros = []

    entrada = input("Digite uma sequencia de numeros separados por vírgula:")

    numeros = list(map(int, entrada.split(",")))
    
    if numeros_quadrados = map(lambda x: x % x == 1 or x % 1 == x ,numeros)
        return numeros_quadrados()
    else:
        return nao_quadrados()

resultado = ["Quadrados Perfeitos": numero_quadrados, "Não Quadrados": nao_quadrados]
resultado = quadrados_perfeitos()
print(f'{resultado}')