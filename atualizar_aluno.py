import sqlite3
from funcoes import consultar_aluno, buscar_aluno

conexao = sqlite3.connect('banco.sqlite3')
cursor = conexao.cursor()


consultar_aluno(cursor)

aluno_id = input('Digite o id do luno: ')
aluno_id = int(aluno_id)
aluno = buscar_aluno(cursor, aluno_id)

nome = input('Digite o novo nome (deixe em branco para atualizar): ')

if not nome:
    nome = aluno[1]

email = input('Digite o novo e-mail (deixe em branco para não atualizar): ')

if not email:
    email = aluno[2]

sql = 'update aluno set nome = ?, email = ? where id = ?'
cursor.execute(sql, [nome, email, aluno_id])
conexao.commit()
conexao.close()
