from MODELS.Disciplinas import Disciplinas
from pymongo import MongoClient
from pymongo.errors import InvalidOperation

# Conexão com a base de dados para acessar professores
client = MongoClient('localhost', 27017)
db = client['escola']

def listar_professores_disponiveis():
    """Exibe uma lista de professores disponíveis no sistema."""
    professores = db.professores.find()
    print("\n--- Lista de Professores Disponíveis ---")
    for professor in professores:
        print(f"ID: {professor['id']}, Nome: {professor['nome']}")
    print("----------------------------------------")

def disciplina():
    while True:
        print('''
        ==== Gerenciamento de Disciplinas ====
        1 - Cadastrar Disciplina
        2 - Listar Disciplinas
        3 - Buscar Disciplina
        4 - Atualizar Disciplina
        5 - Deletar Disciplina
        0 - Voltar ao menu principal
        ''')
        opcao = input('Digite uma opção: ')

        if opcao == '1':
            print("\n--- Cadastro de Disciplina ---")
            try:
                id = input('ID da Disciplina: ')
                nome = input('Nome da Disciplina: ')
                carga_horaria = input('Carga Horária (em horas): ')

                # Exibe os professores disponíveis antes de solicitar o ID
                listar_professores_disponiveis()
                professor_id = input('Escolha o ID do Professor: ')

                disciplina = Disciplinas(id, nome, carga_horaria, professor_id)
                disciplina.salvarDisciplina()
                print("Disciplina cadastrada com sucesso!")
            except InvalidOperation as e:
                print(f"Erro: {e}")
            except Exception as e:
                print(f"Erro inesperado: {e}")
        
        elif opcao == '2':
            print("\n--- Lista de Disciplinas ---")
            disciplina = Disciplinas('', '', '', '')
            disciplina.listarDisciplinas()

        elif opcao == '3':
            print("\n--- Busca de Disciplina ---")
            id = input('ID da Disciplina: ')
            disciplina = Disciplinas('', '', '', '')
            disciplina.buscarDisciplina(id)
        
        elif opcao == '4':
            print("\n--- Atualização de Disciplina ---")
            try:
                id = input('ID da Disciplina: ')
                nome = input('Novo Nome da Disciplina: ')
                carga_horaria = input('Nova Carga Horária (em horas): ')

                # Exibe os professores disponíveis antes de solicitar o ID
                listar_professores_disponiveis()
                professor_id = input('Escolha o Novo ID do Professor: ')

                disciplina = Disciplinas('', '', '', '')
                disciplina.atualizarDisciplina(id, nome, carga_horaria, professor_id)
                print("Disciplina atualizada com sucesso!")
            except InvalidOperation as e:
                print(f"Erro: {e}")
            except Exception as e:
                print(f"Erro inesperado: {e}")

        elif opcao == '5':
            print("\n--- Exclusão de Disciplina ---")
            try:
                id = input('ID da Disciplina: ')
                disciplina = Disciplinas('', '', '', '')
                disciplina.deletarDisciplina(id)
                print("Disciplina deletada com sucesso!")
            except Exception as e:
                print(f"Erro inesperado: {e}")

        elif opcao == '0':
            print("Retornando ao menu principal...")
            break

        else:
            print("Opção inválida. Por favor, tente novamente.")
