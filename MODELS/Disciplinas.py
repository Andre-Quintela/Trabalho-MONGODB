from pymongo import MongoClient

class Disciplinas:
    def __init__(self, id, nome, carga_horaria, professor):
        self.id = id
        self.nome = nome
        self.carga_horaria = carga_horaria
        self.professor = professor

    def __str__(self):
        return f'Nome: {self.nome} - Carga Horária: {self.carga_horaria} - Professor: {self.professor}'   
     
    client = MongoClient('localhost', 27017)
    db = client['disciplinas']

    def salvarDisciplina(self):
        disciplinas = self.db.disciplinas
        disciplina = {
            'id': self.id,
            'nome': self.nome,
            'carga_horaria': self.carga_horaria,
            'professor': self.professor
        }
        disciplinas.insert_one(disciplina)

    def listarDisciplinas(self):
        disciplinas = self.db.disciplinas
        for disciplina in disciplinas.find():
            print(disciplina)

    def buscarDisciplina(self, id):
        disciplinas = self.db.disciplinas
        disciplina = disciplinas.find_one({'id': id})
        print(disciplina)

    def atualizarDisciplina(self, id, nome, carga_horaria, professor):
        disciplinas = self.db.disciplinas
        disciplinas.update_one({'id': id}, {'$set': {'nome': nome, 'carga_horaria': carga_horaria, 'professor': professor}})  
        
    def deletarDisciplina(self, id):
        disciplinas = self.db.disciplinas
        disciplinas.delete_one({'id': id})