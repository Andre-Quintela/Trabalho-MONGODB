from pymongo import MongoClient

class Notas:
    def __init__(self, id, id_aluno, id_disciplina, nota):
        self.id = id
        self.id_aluno = id_aluno
        self.id_disciplina = id_disciplina
        self.nota = nota

    def __str__(self):
        return f'ID: {self.id} - ID Aluno: {self.id_aluno} - ID Disciplina: {self.id_disciplina} - Nota: {self.nota}'   
     
    client = MongoClient('localhost', 27017)
    db = client['notas']

    def salvarNota(self):
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
            print(nota)

    def buscarNota(self, id):
        notas = self.db.notas
        nota = notas.find_one({'id': id})
        print(nota)

    def atualizarNota(self, id, id_aluno, id_disciplina, nota):
        notas = self.db.notas
        notas.update_one({'id': id}, {'$set': {'id_aluno': id_aluno, 'id_disciplina': id_disciplina, 'nota': nota}})  
    
    def deletarNota(self, id):
        notas = self.db.notas
        notas.delete_one({'id': id})