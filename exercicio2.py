"""
Exercício 2 – Agrupando Argumentos por Tipo

Objetivo:
Crie uma função chamada `separar_tipos` que receba um número arbitrário de argumentos posicionais e retorne um dicionário com duas chaves:
    - 'numeros': contendo uma lista com todos os argumentos que são do tipo int ou float;
    - 'strings': contendo uma lista com todos os argumentos que são do tipo str.
    
Observação:
- Argumentos de outros tipos devem ser ignorados.

Exemplo de chamada:
    resultado = separar_tipos(10, 'Python', 3.14, True, 'Teste', 42)
    print(resultado)
    # Saída esperada: {'numeros': [10, 3.14, 42], 'strings': ['Python', 'Teste']}
    
Requisitos:
- Use estruturas condicionais e funções built-in (como isinstance) para classificar os argumentos.
"""


# Sua solução aqui
def separar_tipos(*args):
    """
    Separa os argumentos fornecidos em listas de números e strings.
    Args:
        *args: Uma lista de argumentos que podem ser de qualquer tipo.
    Returns:
        dict: Um dicionário com duas chaves:
            - "Numeros": uma lista contendo todos os argumentos que são int ou float.
            - "Stings": uma lista contendo todos os argumentos que são strings.
    """

    numeros = []
    strings = []

    for arg in args:
        if isinstance(arg, (int, float)):  # Verifica se é int ou float.
            numeros.append(arg)
        elif isinstance(arg, str):  # Verifica se é string
            strings.append(arg)

    return {"Numeros": numeros, "Stings": strings}


resultado = separar_tipos(10, "Python", 3.14, True, "Teste", 42)
print(f"{resultado}")
