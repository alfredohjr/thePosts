# Sobre o uso do if

## Introdução

Use o condição `if` para executar um bloco de código se uma condição for verdadeira.

## Sintaxe

A sintaxe do comando `if` é a seguinte:

```python
if <condição>:
    <bloco de código 1>
else:
    <bloco de código 2>
```

Onde:

- `<condição>` é uma expressão que pode ser avaliada como verdadeira ou falsa.
- `<bloco de código 1>` é um conjunto de comandos que serão executados se a condição for verdadeira.
- `<bloco de código 2>` é um conjunto de comandos que serão executados se a condição for falsa.

## Exemplos práticos

### Exemplo 1

Usando valores booleanos:

```python
condicao = True
if condicao == True:
    print("A condição é verdadeira")
```	

### Exemplo 2

Usando valores numéricos:

```python
valor = 10
if valor > 5:
    print("O valor é maior que 5")
```

### Exemplo 3

Usando valores de texto:

```python
valor = "texto"
if valor == "texto":
    print("O valor é texto")
```

## Avançando um pouco mais

Você também pode usar o comando `if` com operadores lógicos:

Os operadores lógicos são:

- `and` (e)
    ```python
    valor = 10
    if valor > 5 and valor < 15:
        print("O valor está entre 5 e 15")
    ```

- `or` (ou)
    ```python
    valor = 10
    if valor < 5 or valor > 15:
        print("O valor não está entre 5 e 15")
    ```

- `not` (não)
    ```python
    valor = 10
    if not valor == 5:
        print("O valor não é 5")
    ```

- `in` (está em)
    ```python
    valor = 10
    if valor in [5, 10, 15]:
        print("O valor está na lista")
    ```

- `not in` (não está em)
    ```python
    valor = 10
    if valor not in [5, 10, 15]:
        print("O valor não está na lista")
    ```

- `is` (é)
    ```python
    valor = 10
    if valor is 10:
        print("O valor é 10")
    ```

- `is not` (não é)
    ```python
    valor = 10
    if valor is not 5:
        print("O valor não é 5")
    ```

- `==` (igual)
    ```python
    valor = 10
    if valor == 10:
        print("O valor é 10")
    ```

- `!=` (diferente)
    ```python
    valor = 10
    if valor != 5:
        print("O valor não é 5")
    ```

- `>` (maior)
    ```python
    valor = 10
    if valor > 5:
        print("O valor é maior que 5")
    ```

- `>=` (maior ou igual)
    ```python
    valor = 10
    if valor >= 5:
        print("O valor é maior ou igual a 5")
    ```

- `<` (menor)
    ```python
    valor = 10
    if valor < 15:
        print("O valor é menor que 15")
    ```

- `<=` (menor ou igual)
    ```python
    valor = 10
    if valor <= 15:
        print("O valor é menor ou igual a 15")
    ```

- `isinstance()` (é instância de)
    ```python
    valor = 10
    if isinstance(valor, int):
        print("O valor é um inteiro")
    ```

- `not isinstance()` (não é instância de)
    ```python
    valor = 10
    if not isinstance(valor, str):
        print("O valor não é uma string")
    ```

- `issubclass()` (é subclasse de)
    ```python
    class ClassePai:
        pass

    class ClasseFilha(ClassePai):
        pass

    if issubclass(ClasseFilha, ClassePai):
        print("A classe filha é subclasse da classe pai")
    ```

- `not issubclass()` (não é subclasse de)
    ```python
    class ClassePai:
        pass

    class ClasseFilha:
        pass

    if not issubclass(ClasseFilha, ClassePai):
        print("A classe filha não é subclasse da classe pai")
    ```

### if ternário

Você também pode usar o comando `if` numa linha, sem toda a estrutura de bloco. Isso é chamado de `if ternário`.

em particular, eu aprendi sobre if ternário com Javascript e depois fui ver se o python tinha algo parecido, e tinha! um ótimo uso dele é no arquivo de settings do Django, quando você carrega um arquivo .env nele, avaliar um valor numa linha só abre várias possibilidades.

```python
valor = 10
valor if valor > 5 else 0
print(valor)
```
