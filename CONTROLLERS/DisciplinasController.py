from MODELS.Disciplinas import Disciplinas


def disciplina():
    while True:
        print('''
        1 - Cadastrar Disciplina
        2 - Listar Disciplinas
        3 - Buscar Disciplina
        4 - Atualizar Disciplina
        5 - Deletar Disciplina
        0 - Sair
        ''')
        opcao = input('Digite uma opção: ')

        if opcao == '1':
            id = input('ID: ')
            nome = input('Nome: ')
            cargaHoraria = input('Carga Horária: ')
            professor = input('Professor: ')

            disciplina = Disciplinas(id, nome, cargaHoraria, professor)
            disciplina.salvarDisciplina()
        
        elif opcao == '2':
            disciplina = Disciplinas('', '', '', '')
            disciplina.listarDisciplinas()

        elif opcao == '3':
            id = input('ID: ')
            disciplina = Disciplinas('', '', '', '')
            disciplina.buscarDisciplina(id)
        
        elif opcao == '4':
            id = input('ID: ')
            nome = input('Nome: ')
            cargaHoraria = input('Carga Horária: ')
            professor = input('Professor: ')

            disciplina = Disciplinas('', '', '', '')
            disciplina.atualizarDisciplina(id, nome, cargaHoraria, professor)

        elif opcao == '5':
            id = input('ID: ')
            disciplina = Disciplinas('', '', '', '')
            disciplina.deletarDisciplina(id)
        
        elif opcao == '0':
            break