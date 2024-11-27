from CONTROLLERS.AlunosController import aluno
from CONTROLLERS.DisciplinasController import disciplina
from CONTROLLERS.NotasController import nota
from CONTROLLERS.ProfessoresController import professor
from VIEWS.relatorios import relatorio_alunos_por_disciplina, relatorio_notas_por_disciplina

def menu():
    while True:
        print("1. Alunos")
        print("2. Professores")
        print("3. Disciplinas")
        print("4. Notas")
        print("5. Relatórios")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            aluno()
        elif opcao == '2':
            professor()
        elif opcao == '3':
            disciplina()
        elif opcao == '4':
            nota()
        elif opcao == '5':
            print("Relatórios")
            print("1. Notas por Disciplina")
            print("2. Alunos por Disciplina")

            opcao_relatorio = input("Escolha uma opção: ")

            if opcao_relatorio == '1':
                relatorio_notas_por_disciplina()

            if opcao_relatorio == '2':
                relatorio_alunos_por_disciplina()                
        elif opcao == '0':
            break