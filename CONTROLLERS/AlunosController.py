from MODELS.Alunos import Alunos
from MODELS.Disciplinas import Disciplinas

def listar_disciplinas_disponiveis():
    """Exibe uma lista de disciplinas disponíveis no sistema."""
    disciplinas = Disciplinas('', '', '', '')  # Instanciando objeto de disciplinas
    disciplinas.listarDisciplinas()  # Chamando o método para listar as disciplinas
    print("----------------------------------------")

def aluno():
    while True:
        print('''
        ==== Menu de Alunos ====
        1 - Cadastrar Aluno
        2 - Listar Alunos
        3 - Buscar Aluno
        4 - Atualizar Aluno
        5 - Deletar Aluno
        0 - Sair
        ''')

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            print("\n--- Cadastro de Aluno ---")
            try:
                id = input("ID: ")
                nome = input("Nome: ")
                idade = input("Idade: ")
                serie = input("Série: ")

                print("\nAs disciplinas disponíveis são:")
                listar_disciplinas_disponiveis()

                disciplinas = input("Informe o nome dasdisciplinas do aluno separadas por vírgula: ")
                disciplinas = [disc.strip() for disc in disciplinas.split(',')]  # Organiza as disciplinas inseridas

                aluno = Alunos(id, nome, idade, disciplinas, serie)
                aluno.salvarAluno()  # Salva o aluno no banco de dados
                print("\nAluno cadastrado com sucesso!")
            except Exception as e:
                print(f"\nErro ao cadastrar aluno: {e}")

        elif opcao == '2':
            print("\n--- Lista de Alunos ---")
            aluno = Alunos('', '', '', '', '')
            aluno.listarAlunos()  # Lista todos os alunos cadastrados

        elif opcao == '3':
            print("\n--- Buscar Aluno ---")
            id = input("Informe o ID do aluno: ")
            aluno = Alunos('', '', '', '', '')
            aluno.buscarAluno(id)  # Busca aluno pelo ID

        elif opcao == '4':
            print("\n--- Atualizar Aluno ---")
            try:
                id = input("ID do aluno a ser atualizado: ")
                nome = input("Novo Nome: ")
                idade = input("Nova Idade: ")
                serie = input("Nova Série: ")

                print("\nAs disciplinas disponíveis são:")
                listar_disciplinas_disponiveis()

                disciplinas = input("Informe as novas disciplinas do aluno separadas por vírgula: ")
                disciplinas = [disc.strip() for disc in disciplinas.split(',')]  # Organiza as disciplinas inseridas

                aluno = Alunos('', '', '', '', '')
                aluno.atualizarAluno(id, nome, idade, disciplinas, serie)  # Atualiza as informações do aluno
                print("\nAluno atualizado com sucesso!")
            except Exception as e:
                print(f"\nErro ao atualizar aluno: {e}")

        elif opcao == '5':
            print("\n--- Deletar Aluno ---")
            try:
                id = input("Informe o ID do aluno a ser deletado: ")
                aluno = Alunos('', '', '', '', '')
                aluno.deletarAluno(id)  # Deleta o aluno pelo ID
                print("\nAluno deletado com sucesso!")
            except Exception as e:
                print(f"\nErro ao deletar aluno: {e}")

        elif opcao == '0':
            print("\nSaindo do sistema...")
            break

        else:
            print("\nOpção inválida! Tente novamente.")
