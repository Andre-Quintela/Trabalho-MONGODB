from pymongo import MongoClient

def contarRegistros():
    # Conectando ao banco de dados 'escola'
    client = MongoClient('localhost', 27017)
    db = client['escola']
    
    # Contando os registros nas diferentes collections dentro da database 'escola'
    totalDisciplinas = db.disciplinas.count_documents({})
    totalAlunos = db.alunos.count_documents({})
    totalNotas = db.notas.count_documents({})
    totalProfessores = db.professores.count_documents({})
    
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
