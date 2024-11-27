from CONTROLLERS.AlunosController import aluno
from CONTROLLERS.ProfessoresController import professor
from MODELS import Alunos, Professores, Disciplinas, Notas

def menu():
    print("1. Alunos")
    print("2. Professores")
    print("3. Disciplinas")
    print("4. Notas")
    print("5. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        aluno()
    elif opcao == '2':
        professor()
  