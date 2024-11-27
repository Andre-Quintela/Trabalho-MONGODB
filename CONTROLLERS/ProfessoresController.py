from MODELS.Professores import Professores


def professor():
    while True:
        print('''
        1 - Cadastrar Professor
        2 - Listar Professores
        3 - Buscar Professor
        4 - Atualizar Professor
        5 - Deletar Professor
        0 - Sair
        ''')
        opcao = input('Digite uma opção: ')
        
        if opcao == '1':
            id = input('ID: ')
            nome = input('Nome: ')
            idade = input('Idade: ')
            disciplinas = input('Disciplinas: ')
            
            professor = Professores(id, nome, idade, disciplinas)
            professor.salvarProfessor()

        elif opcao == '2':
            professor = Professores('', '', '', '')
            professor.listarProfessores()
        
        elif opcao == '3':
            id = input('ID: ')
            professor = Professores('', '', '', '')
            professor.buscarProfessor(id)

        elif opcao == '4':
            id = input('ID: ')
            nome = input('Nome: ')
            idade = input('Idade: ')
            disciplinas = input('Disciplinas: ')
            
            professor = Professores('', '', '', '')
            professor.atualizarProfessor(id, nome, idade, disciplinas)
        
        elif opcao == '5':
            id = input('ID: ')
            professor = Professores('', '', '', '')
            professor.deletarProfessor(id)

        elif opcao == '0':
            break