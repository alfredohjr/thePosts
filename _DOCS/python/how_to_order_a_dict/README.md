# Como ordenar um dicionario através de uma key?

---

criado em: 2024-01-01 15:21

---

## Introdução

Se você trabalha com python e lista de dicionarios, provavelmente já se deparou com a necessidade de ordenar um dicionario através de uma key. Neste artigo iremos ver como fazer isso.

Claro, importar o pandas, transformar em dataframe e ordenar é uma opção, mas vamos manter a simplicidade e fazer isso sem pandas.

## Exemplos

```python
# Criando uma lista com 100 dicionarios de forma aleatoria
import random
import string

lista = []
for i in range(100):
    lista.append({
        'nome': f'nome_{i}',
        'idade': random.randint(1, 100)
    })

# Ordenando a lista de dicionarios pela key 'idade'
lista_ordenada = sorted(lista, key=lambda k: k['idade'])

# Imprimindo a lista ordenada
for i in lista_ordenada:
    print(i.get('nome')) # Imprime o nome de cada dicionario
    print(i.get('idade')) # Imprime a idade de cada dicionario

```

você também pode ordenar de forma reversa, basta adicionar o parametro `reverse=True` no `sorted()`

