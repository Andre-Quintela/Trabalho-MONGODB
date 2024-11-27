from MODELS.Alunos import Alunos
from MODELS.Disciplinas import Disciplinas

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
            print("\n=== Cadastro de Aluno ===")
            id = input("ID: ")
            nome = input("Nome: ")
            idade = input("Idade: ")
            serie = input("Série: ")

            print("\nAs disciplinas disponíveis são:")
            disciplinas_obj = Disciplinas('', '', '', '')
            disciplinas_obj.listarDisciplinas()

            disciplinas = input("Informe as disciplinas do aluno separadas por vírgula: ")
            disciplinas = [disc.strip() for disc in disciplinas.split(',')]

            aluno = Alunos(id, nome, idade, disciplinas, serie)
            try:
                aluno.salvarAluno()
                print("\nAluno cadastrado com sucesso!")
            except Exception as e:
                print(f"\nErro ao cadastrar aluno: {e}")

        elif opcao == '2':
            print("\n=== Lista de Alunos ===")
            aluno = Alunos('', '', '', '', '')
            aluno.listarAlunos()

        elif opcao == '3':
            print("\n=== Buscar Aluno ===")
            id = input("Informe o ID do aluno: ")
            aluno = Alunos('', '', '', '', '')
            aluno.buscarAluno(id)

        elif opcao == '4':
            print("\n=== Atualizar Aluno ===")
            id = input("ID do aluno a ser atualizado: ")
            nome = input("Novo Nome: ")
            idade = input("Nova Idade: ")
            serie = input("Nova Série: ")

            print("\nAs disciplinas disponíveis são:")
            disciplinas_obj = Disciplinas('', '', '', '')
            disciplinas_obj.listarDisciplinas()

            disciplinas = input("Informe as novas disciplinas do aluno separadas por vírgula: ")
            disciplinas = [disc.strip() for disc in disciplinas.split(',')]

            aluno = Alunos('', '', '', '', '')
            try:
                aluno.atualizarAluno(id, nome, idade, disciplinas, serie)
                print("\nAluno atualizado com sucesso!")
            except Exception as e:
                print(f"\nErro ao atualizar aluno: {e}")

        elif opcao == '5':
            print("\n=== Deletar Aluno ===")
            id = input("Informe o ID do aluno a ser deletado: ")
            aluno = Alunos('', '', '', '', '')
            aluno.deletarAluno(id)
            print("\nAluno deletado com sucesso!")

        elif opcao == '0':
            print("\nSaindo do sistema...")
            break

        else:
            print("\nOpção inválida! Tente novamente.")
