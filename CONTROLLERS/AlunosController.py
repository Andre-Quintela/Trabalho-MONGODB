from MODELS.Alunos import Alunos


def aluno():
    while True:
        print('''
        1 - Cadastrar Aluno
        2 - Listar Alunos
        3 - Buscar Aluno
        4 - Atualizar Aluno
        5 - Deletar Aluno
        0 - Sair
        ''')
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            id = input("ID: ")
            nome = input("Nome: ")
            idade = input("Idade: ")
            disciplinas = input("Disciplinas: ")
            serie = input("Série: ")

            aluno = Alunos(id, nome, idade, disciplinas, serie)
            aluno.salvarAluno()

        elif opcao == '2':
            aluno = Alunos('', '', '', '', '')
            aluno.listarAlunos()

        elif opcao == '3':
            id = input("ID: ")
            aluno = Alunos('', '', '', '', '')
            aluno.buscarAluno(id)

        elif opcao == '4':
            id = input("ID: ")
            nome = input("Nome: ")
            idade = input("Idade: ")
            disciplinas = input("Disciplinas: ")
            serie = input("Série: ")

            aluno = Alunos('', '', '', '', '')
            aluno.atualizarAluno(id, nome, idade, disciplinas, serie)

        elif opcao == '5':
            id = input("ID: ")
            aluno = Alunos('', '', '', '', '')
            aluno.deletarAluno(id)
      
        elif opcao == '0':
            break
