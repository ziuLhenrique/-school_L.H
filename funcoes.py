

def consultar_aluno(cursor):


    termo = input('Digite o termo de busca: ')

    sql = '''
    SELECT id, nome, email, data FROM aluno WHERE nome LIKE ? OR email LIKE ?
    '''

    termo = f'%{termo}%'

    resultado = cursor.execute(sql, [termo, termo])

    for aluno in resultado:
        print("id", aluno[0], "nome", aluno[1], "email", aluno[2], "data", aluno[3])

def buscar_aluno(cursor, id):
    sql = '''
    select id, nome, email, data from aluno where id = ?
    '''
    resultado = cursor.execute(sql, [id])

    aluno = None
    for aluno in resultado:
        break
    return aluno 