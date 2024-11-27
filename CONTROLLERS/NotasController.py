from MODELS.Notas import Notas


def nota():
    while True:
        print('''
        1 - Cadastrar Nota
        2 - Listar Notas
        3 - Buscar Nota
        4 - Atualizar Nota
        5 - Deletar Nota
        0 - Sair
        ''')
        opcao = input('Digite uma opção: ')
        
        if opcao == '1':
            id = input('ID: ')
            id_aluno = input('ID Aluno: ')
            id_disciplina = input('ID Disciplina: ')
            nota = input('Nota: ')
            
            nota = Notas(id, id_aluno, id_disciplina, nota)
            nota.salvarNota()

        elif opcao == '2':
            nota = Notas('', '', '', '')
            nota.listarNotas()
        
        elif opcao == '3':
            id = input('ID: ')
            nota = Notas('', '', '', '')
            nota.buscarNota(id)
        
        elif opcao == '4':
            id = input('ID: ')
            id_aluno = input('ID Aluno: ')
            id_disciplina = input('ID Disciplina: ')
            nota = input('Nota: ')
            
            nota = Notas('', '', '', '')
            nota.atualizarNota(id, id_aluno, id_disciplina, nota)
        
        elif opcao == '5':
            id = input('ID: ')
            nota = Notas('', '', '', '')
            nota.deletarNota(id)
        
        elif opcao == '0':
            break