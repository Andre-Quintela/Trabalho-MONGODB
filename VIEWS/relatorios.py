from pymongo import MongoClient

def relatorio_numero_de_alunos_por_disciplina():
    client = MongoClient('localhost', 27017)
    db = client['escola']

    disciplinas = db.disciplinas
    notas = db.notas

    for disciplina in disciplinas.find():
        qtd_alunos = notas.count_documents({'id_disciplina': disciplina['id']})
        print(f"Disciplina: {disciplina['nome']} - Número de alunos: {qtd_alunos}")
    


def relatorio_media_de_notas_dos_alunos_por_disciplina():
    client = MongoClient('localhost', 27017)
    db = client['escola']

    disciplinas = db.disciplinas
    notas = db.notas

    for disciplina in disciplinas.find():
        notas_disciplina = notas.find({'id_disciplina': disciplina['id']})
        qtd_alunos = notas.count_documents({'id_disciplina': disciplina['id']})
        
        # Converter as notas para float, se necessário
        soma_notas = sum([float(nota['nota']) for nota in notas_disciplina if nota.get('nota') is not None])
        
        media = soma_notas / qtd_alunos if qtd_alunos > 0 else 0
        print(f"Disciplina: {disciplina['nome']} - Média de notas: {media:.2f}")
  