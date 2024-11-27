from MODELS.Notas import Notas
from pymongo import MongoClient

# Conexão com a base de dados para acessar alunos e disciplinas
client = MongoClient('localhost', 27017)
db = client['escola']

def listar_alunos_disponiveis():
    """Exibe uma lista de alunos disponíveis no sistema."""
    alunos = db.alunos.find()
    print("\n--- Lista de Alunos Disponíveis ---")
    for aluno in alunos:
        print(f"ID: {aluno['id']}, Nome: {aluno['nome']}")
    print("-----------------------------------")

def listar_disciplinas_disponiveis():
    """Exibe uma lista de disciplinas disponíveis no sistema."""
    disciplinas = db.disciplinas.find()
    print("\n--- Lista de Disciplinas Disponíveis ---")
    for disciplina in disciplinas:
        print(f"ID: {disciplina['id']}, Nome: {disciplina['nome']}")
    print("----------------------------------------")

def nota():
    while True:
        print('''
        ==== Gerenciamento de Notas ====
        1 - Cadastrar Nota
        2 - Listar Notas
        3 - Buscar Nota
        4 - Atualizar Nota
        5 - Deletar Nota
        0 - Voltar ao menu principal
        ''')
        opcao = input('Digite uma opção: ')

        if opcao == '1':
            print("\n--- Cadastro de Nota ---")
            try:
                id = input('ID da Nota: ')

                # Exibe os alunos disponíveis
                listar_alunos_disponiveis()
                id_aluno = input('Escolha o ID do Aluno: ')

                # Exibe as disciplinas disponíveis
                listar_disciplinas_disponiveis()
                id_disciplina = input('Escolha o ID da Disciplina: ')

                nota_valor = input('Nota: ')

                nota = Notas(id, id_aluno, id_disciplina, nota_valor)
                nota.salvarNota()
                print("Nota cadastrada com sucesso!")
            except Exception as e:
                print(f"Erro inesperado: {e}")

        elif opcao == '2':
            print("\n--- Lista de Notas ---")
            nota = Notas('', '', '', '')
            nota.listarNotas()

        elif opcao == '3':
            print("\n--- Busca de Nota ---")
            id = input('ID da Nota: ')
            nota = Notas('', '', '', '')
            nota.buscarNota(id)

        elif opcao == '4':
            print("\n--- Atualização de Nota ---")
            try:
                id = input('ID da Nota: ')

                # Exibe os alunos disponíveis
                listar_alunos_disponiveis()
                id_aluno = input('Escolha o Novo ID do Aluno: ')

                # Exibe as disciplinas disponíveis
                listar_disciplinas_disponiveis()
                id_disciplina = input('Escolha o Novo ID da Disciplina: ')

                nota_valor = input('Nova Nota: ')

                nota = Notas('', '', '', '')
                nota.atualizarNota(id, id_aluno, id_disciplina, nota_valor)
                print("Nota atualizada com sucesso!")
            except Exception as e:
                print(f"Erro inesperado: {e}")

        elif opcao == '5':
            print("\n--- Exclusão de Nota ---")
            try:
                id = input('ID da Nota: ')
                nota = Notas('', '', '', '')
                nota.deletarNota(id)
                print("Nota deletada com sucesso!")
            except Exception as e:
                print(f"Erro inesperado: {e}")

        elif opcao == '0':
            print("Retornando ao menu principal...")
            break

        else:
            print("Opção inválida. Por favor, tente novamente.")
