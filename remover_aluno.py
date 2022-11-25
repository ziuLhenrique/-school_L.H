import sqlite3
from funcoes import consultar_aluno

conexao = sqlite3.connect('banco.sqlite3')
cursor = conexao.cursor()


consultar_aluno(cursor)

aluno_id = input('Digite o id do luno: ')
aluno_id = int(aluno_id)

sql = 'delete from  aluno where id = ?'

cursor.execute(sql, [aluno_id])
conexao.commit()
conexao.close()