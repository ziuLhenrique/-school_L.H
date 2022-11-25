import sqlite3

from funcoes import consultar_aluno

conexao = sqlite3.connect('banco.sqlite3')
cursor = conexao.cursor()

consultar_aluno(cursor)


conexao.close()