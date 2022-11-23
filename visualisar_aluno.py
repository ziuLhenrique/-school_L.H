import sqlite3
conexao = sqlite3.connect('banco.sqlite3')
cursor = conexao.cursor()

termo = input('Digite o termo de busca: ')

sql = '''
SELECT id, nome, email, data FROM aluno WHERE nome LIKE ? OR email LIKE ?
'''

termo = f'%{termo}%'

resultado = cursor.execute(sql, [termo, termo])

for aluno in resultado:
    print("id", aluno[0], "nome", aluno[1], "email", aluno[2], "data", aluno[3])

conexao.close()