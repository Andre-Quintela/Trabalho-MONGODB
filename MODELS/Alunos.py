from pymongo import MongoClient

class Alunos:
    def __init__(self, id, nome, idade, disciplinas, serie):
        self.id = id
        self.nome = nome
        self.idade = idade
        self.disciplinas = disciplinas
        self.serie = serie

    def __str__(self):
        return f'Nome: {self.nome} - Idade: {self.idade}'   
    
    client = MongoClient('localhost', 27017)
    db = client['alunos']

    def salvarAluno(self):
        alunos = self.db.alunos
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
