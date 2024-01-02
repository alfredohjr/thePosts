# Porque usar JOIN em uma sentença SQL 

---

creation: 2024-01-01 15:22

---

## O inicio

Quando você usa SQL dentro de um programa python, certamente você incluira uma clausula where no codigo e dentro dela certamente haverá uma condição in, é ai que entra o uso do join para te ajudar a melhorar as suas consultas, neste caso filtrando os dados diretamente no banco de dados, ao invés de fazer isso no programa.

## Uso

```python

# importe os modulos necessarios
import argparse
import sqlite3
import pandas as pd

# conecte ao banco de dados
conn = sqlite3.connect('database.db')

# adicionando opções de linha de comando
parse = argparse.ArgumentParser()
parse.add_argument('--ids', type=str, help='lista de ID para filtrar.')

args = parse.parse_args()

# verificando a string de entrada
print('string sem tratamento:',args.ids)

# tratando a string de entrada
print('string tratada:','|'.join(args.ids.split(',')))

# criando a consulta
sql = f"""select * from table where id in ({','.join(args.ids.split(','))})"""

# imprimindo a consulta
print(sql)

# executando a consulta
df = pd.read_sql(sql, conn)

# exportando o resultado para um arquivo csv
df.to_csv('output.csv', index=False)
```