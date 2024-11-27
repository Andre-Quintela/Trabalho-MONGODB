from pymongo import MongoClient

class Professores:
    def __init__(self, id, nome, idade, disciplinas):
        self.id = id
        self.nome = nome
        self.idade = idade
        self.disciplinas = disciplinas

    def __str__(self):
        return f'Nome: {self.nome} - Idade: {self.idade}'   
    
    client = MongoClient('localhost', 27017)
    db = client['professores']

    def salvarProfessor(self):
        professores = self.db.professores
        professor = {
            'id': self.id,
            'nome': self.nome,
            'idade': self.idade,
            'disciplinas': self.disciplinas
        }
        professores.insert_one(professor)

    def listarProfessores(self):
        professores = self.db.professores
        for professor in professores.find():
            print(professor)

    def buscarProfessor(self, id):
        professores = self.db.professores
        professor = professores.find_one({'id': id})
        print(professor)

    def atualizarProfessor(self, id, nome, idade, disciplinas):
        professores = self.db.professores
        professores.update_one({'id': id}, {'$set': {'nome': nome, 'idade': idade, 'disciplinas': disciplinas}})  
    
    def deletarProfessor(self, id):
        professores = self.db.professores
        professores.delete_one({'id': id})