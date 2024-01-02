import argparse

parse = argparse.ArgumentParser()
parse.add_argument('--ids', type=str, help='lista de ID para filtrar.')

args = parse.parse_args()

print('string sem tratamento:',args.ids)
print('string tratada:','|'.join(args.ids.split(',')))

sql = f"""select * from table where id in ({','.join(args.ids.split(','))})"""
print(sql)