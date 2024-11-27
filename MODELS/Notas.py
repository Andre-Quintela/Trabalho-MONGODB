from pymongo import MongoClient
from pymongo.errors import InvalidOperation

class Notas:
    client = MongoClient('localhost', 27017)
    db = client['escola']  # Usar uma única base de dados para todas as coleções

    def __init__(self, id, id_aluno, id_disciplina, nota):
        self.id = id
        self.id_aluno = id_aluno
        self.id_disciplina = id_disciplina
        self.nota = nota

    def __str__(self):
        return f'ID: {self.id} - Aluno: {self.id_aluno} - Disciplina: {self.id_disciplina} - Nota: {self.nota}'

    def verificar_aluno(self, id_aluno):
        alunos = self.db.alunos
        return alunos.find_one({'id': id_aluno}) is not None

    def verificar_disciplina(self, id_disciplina):
        disciplinas = self.db.disciplinas
        return disciplinas.find_one({'id': id_disciplina}) is not None

    def salvarNota(self):
        if not self.verificar_aluno(self.id_aluno):
            raise InvalidOperation(f"O aluno com ID '{self.id_aluno}' não existe.")
        if not self.verificar_disciplina(self.id_disciplina):
            raise InvalidOperation(f"A disciplina com ID '{self.id_disciplina}' não existe.")

        notas = self.db.notas
        nota = {
            'id': self.id,
            'id_aluno': self.id_aluno,
            'id_disciplina': self.id_disciplina,
            'nota': self.nota
        }
        notas.insert_one(nota)

    def listarNotas(self):
        notas = self.db.notas
        for nota in notas.find():
            aluno = self.db.alunos.find_one({'id': nota['id_aluno']})
            disciplina = self.db.disciplinas.find_one({'id': nota['id_disciplina']})
            print(f"Nota ID: {nota['id']}, Aluno: {aluno['nome'] if aluno else 'Não encontrado'}, "
                  f"Disciplina: {disciplina['nome'] if disciplina else 'Não encontrada'}, Nota: {nota['nota']}")

    def buscarNota(self, id):
        notas = self.db.notas
        nota = notas.find_one({'id': id})
        if nota:
            aluno = self.db.alunos.find_one({'id': nota['id_aluno']})
            disciplina = self.db.disciplinas.find_one({'id': nota['id_disciplina']})
            print(f"Nota ID: {nota['id']}, Aluno: {aluno['nome'] if aluno else 'Não encontrado'}, "
                  f"Disciplina: {disciplina['nome'] if disciplina else 'Não encontrada'}, Nota: {nota['nota']}")
        else:
            print(f"Nota com ID '{id}' não encontrada.")

    def atualizarNota(self, id, id_aluno, id_disciplina, nota):
        if not self.verificar_aluno(id_aluno):
            raise InvalidOperation(f"O aluno com ID '{id_aluno}' não existe.")
        if not self.verificar_disciplina(id_disciplina):
            raise InvalidOperation(f"A disciplina com ID '{id_disciplina}' não existe.")

        notas = self.db.notas
        result = notas.update_one({'id': id}, {'$set': {
            'id_aluno': id_aluno,
            'id_disciplina': id_disciplina,
            'nota': nota
        }})
        if result.matched_count > 0:
            print(f"Nota com ID '{id}' atualizada com sucesso.")
        else:
            print(f"Nota com ID '{id}' não encontrada para atualização.")

    def deletarNota(self, id):
        notas = self.db.notas
        result = notas.delete_one({'id': id})
        if result.deleted_count > 0:
            print(f"Nota com ID '{id}' deletada com sucesso.")
        else:
            print(f"Nota com ID '{id}' não encontrada para exclusão.")
