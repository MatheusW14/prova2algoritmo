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


def classificar_quadrados(lista_numeros):
    """
    Classifica uma lista de números em quadrados perfeitos e não quadrados.
    Args:
        lista_numeros (list): Lista de números inteiros a serem classificados.
    Returns:
        dict: Um dicionário com duas chaves:
            - "quadrados_perfeitos" (list): Lista de números que são quadrados perfeitos.
            - "nao_quadrados" (list): Lista de números que não são quadrados perfeitos.
    """

    quadrados_perfeitos = []
    nao_quadrados = []

    for numero in lista_numeros:
        if numero < 0:
            continue
        raiz = int(numero**0.5)
        if raiz * raiz == numero:
            quadrados_perfeitos.append(numero)
        else:
            nao_quadrados.append(numero)

    return {"quadrados_perfeitos": quadrados_perfeitos, "nao_quadrados": nao_quadrados}


entrada_usuario = input(
    "Digite uma lista de numeros inteiros separados por uma virgula: "
)

lista_numeros = list(map(int, entrada_usuario.split(",")))

resultado = classificar_quadrados(lista_numeros)
print(resultado)
