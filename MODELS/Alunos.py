from decimal import InvalidOperation
from pymongo import MongoClient

class Alunos:
    def __init__(self, id, nome, idade, disciplinas, serie):
        self.id = id
        self.nome = nome
        self.idade = idade
        self.disciplinas = disciplinas if isinstance(disciplinas, list) else [disciplinas]
        self.serie = serie

    def __str__(self):
        return f'Nome: {self.nome} - Idade: {self.idade}'   
    
    client = MongoClient('localhost', 27017)
    db = client['escola']

    def salvarAluno(self):
        alunos = self.db.alunos
        disciplinas_collection = self.db.disciplinas

        # Validar disciplinas
        disciplinas_existentes = [d['nome'] for d in disciplinas_collection.find()]
        for disciplina in self.disciplinas:
            if disciplina not in disciplinas_existentes:
                raise InvalidOperation(f"A disciplina '{disciplina}' não existe na coleção de disciplinas.")

        # Inserir aluno após validação
        aluno = {
            'id': self.id,
            'nome': self.nome,
            'idade': self.idade,
            'disciplinas': self.disciplinas,
            'serie': self.serie
        }
        alunos.insert_one(aluno)

    def listarAlunos(self):
        alunos = self.db.alunos
        for aluno in alunos.find():
            print(aluno)

    def buscarAluno(self, id):
        alunos = self.db.alunos
        aluno = alunos.find_one({'id': id})
        print(aluno)

    def atualizarAluno(self, id, nome, idade, disciplinas, serie):
        alunos = self.db.alunos
        alunos.update_one({'id': id}, {'$set': {'nome': nome, 'idade': idade, 'disciplinas': disciplinas, 'serie': serie}})  
        
    def deletarAluno(self, id):
        alunos = self.db.alunos
        alunos.delete_one({'id': id})
