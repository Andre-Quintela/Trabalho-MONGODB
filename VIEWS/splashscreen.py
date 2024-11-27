from pymongo import MongoClient

def contarRegistros():
    client = MongoClient('localhost', 27017)
    db = client['disciplinas']
    disciplinas = db.disciplinas
    totalDisciplinas = disciplinas.count_documents({})
    
    db = client['alunos']
    alunos = db.alunos
    totalAlunos = alunos.count_documents({})
    
    db = client['notas']
    notas = db.notas
    totalNotas = notas.count_documents({})
    
    db = client['professores']
    professores = db.professores
    totalProfessores = professores.count_documents({})
    
    return totalAlunos, totalDisciplinas, totalNotas, totalProfessores

registros = contarRegistros()

def splashScreen():
    print(f"""
          ==========================================
              Sistema de Gerenciamento de Escolas
          
          TOTAL DE REGISTROS:
            Alunos: {registros[0]}
            Disciplinas: {registros[1]}
            Notas: {registros[2]}
            Professores: {registros[3]}
        
        Criado por: 
                André Quintela                        
                Cassio Jordan                         
                Entony Jovino                         
                Guilherme Ambrozio                   
                Raphael Simoes                        
                                                          
        Disciplica: Banco de Dados 2024-2                
            Professor: Howard Roatti 

          """)
