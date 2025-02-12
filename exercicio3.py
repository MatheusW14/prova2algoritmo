"""
Exercício 3 – Processamento de Nomes com Tuplas

Objetivo:
1. Solicite ao usuário uma entrada contendo uma sequência de nomes separados por vírgula.
2. Converta essa entrada em uma lista de strings, garantindo a remoção de espaços desnecessários e a conversão para minúsculas.
3. Crie uma função chamada `nome_e_tamanho` que receba um nome (string) e retorne uma tupla contendo:
    - O próprio nome.
    - O tamanho (número de caracteres) do nome.
4. Utilize essa função para transformar cada nome da lista em uma tupla (nome, tamanho) e armazene essas tuplas em uma nova lista.
5. Percorra a nova lista e, para cada tupla, imprima uma mensagem informando se o nome possui mais de 5 caracteres ou não.

Exemplo de mensagem:
    "O nome 'Carlos' tem 6 caracteres e é considerado longo." 
    ou 
    "O nome 'Ana' tem 3 caracteres e é considerado curto."

Requisitos:
- Faça uso de laços de repetição e estruturas condicionais.
- Garanta o tratamento adequado da entrada do usuário.
"""

# Sua solução aqui


def nome_e_tamanho(nome):
    """
    Returns a tuple containing the given name and its length.
    Parameters:
    nome (str): The name to be evaluated.
    Returns:
    tuple: A tuple where the first element is the name (str) and the second element is the length of the name (int).
    """

    return (nome, len(nome))


entrada = input("Digite uma lista de nomes separados por vírgula:")

nomes = [nome.strip().lower for nome in entrada.split(",")]

tuplas_nomes = [nome_e_tamanho(nome) for nome in nomes]

for nome, tamanho in tuplas_nomes:
    if tamanho > 5:
        print(f"O nome '{nome}' tem {tamanho} caracteres e é considerado longo.")
    else:
        print(f"O nome '{nome}' tem {tamanho} caracteres e é considerado curto.")
