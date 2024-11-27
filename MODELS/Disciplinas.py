from pymongo import MongoClient
from pymongo.errors import InvalidOperation

class Disciplinas:
    def __init__(self, id, nome, carga_horaria, professor_id):
        self.id = id
        self.nome = nome
        self.carga_horaria = carga_horaria
        self.professor_id = professor_id

    def __str__(self):
        return f'Nome: {self.nome} - Carga Horária: {self.carga_horaria} - Professor ID: {self.professor_id}'   
     
    client = MongoClient('localhost', 27017)
    db = client['escola']

    def salvarDisciplina(self):
        disciplinas = self.db.disciplinas
        professores = self.db.professores

        # Validar se o professor existe
        professor = professores.find_one({'id': self.professor_id})
        if not professor:
            raise InvalidOperation(f"O professor com ID '{self.professor_id}' não existe.")

        # Inserir disciplina após validação
        disciplina = {
            'id': self.id,
            'nome': self.nome,
            'carga_horaria': self.carga_horaria,
            'professor_id': self.professor_id
        }
        disciplinas.insert_one(disciplina)

    def listarDisciplinas(self):
        disciplinas = self.db.disciplinas
        professores = self.db.professores

        for disciplina in disciplinas.find():
            professor = professores.find_one({'id': disciplina['professor_id']})
            professor_nome = professor['nome'] if professor else 'Não encontrado'
            print(f"ID: {disciplina['id']} - Nome: {disciplina['nome']} - "
                  f"Carga Horária: {disciplina['carga_horaria']} - Professor: {professor_nome}")

    def buscarDisciplina(self, id):
        disciplinas = self.db.disciplinas
        professores = self.db.professores

        disciplina = disciplinas.find_one({'id': id})
        if disciplina:
            professor = professores.find_one({'id': disciplina['professor_id']})
            professor_nome = professor['nome'] if professor else 'Não encontrado'
            print(f"ID: {disciplina['id']} - Nome: {disciplina['nome']} - "
                  f"Carga Horária: {disciplina['carga_horaria']} - Professor: {professor_nome}")
        else:
            print("Disciplina não encontrada.")

    def atualizarDisciplina(self, id, nome, carga_horaria, professor_id):
        disciplinas = self.db.disciplinas
        professores = self.db.professores

        # Validar se o novo professor existe
        professor = professores.find_one({'id': professor_id})
        if not professor:
            raise InvalidOperation(f"O professor com ID '{professor_id}' não existe.")

        # Atualizar disciplina
        disciplinas.update_one(
            {'id': id},
            {'$set': {'nome': nome, 'carga_horaria': carga_horaria, 'professor_id': professor_id}}
        )

    def deletarDisciplina(self, id):
        disciplinas = self.db.disciplinas
        disciplinas.delete_one({'id': id})
