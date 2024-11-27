from pymongo import MongoClient

def relatorio_notas_por_disciplina():
    try:
        # Conexão com o MongoDB e a base de dados 'escola'
        client = MongoClient('localhost', 27017)
        db = client['escola']
        
        # Agregação para calcular a soma das notas por disciplina
        pipeline = [
            {
                "$group": {
                    "_id": "$id_disciplina",  # Agrupar por id_disciplina
                    "total_notas": {"$sum": "$nota"}  # Somar as notas
                }
            },
            {
                "$lookup": {
                    "from": "disciplinas",  # Referência à coleção disciplinas
                    "localField": "_id",     # Campo id_disciplina em notas
                    "foreignField": "id",    # Campo id nas disciplinas
                    "as": "disciplina_info"  # Nome do campo onde armazenamos as informações
                }
            },
            {
                "$unwind": "$disciplina_info"  # Desestruturar para obter o nome da disciplina
            },
            {
                "$project": {
                    "disciplina_id": "$_id",
                    "disciplina_nome": "$disciplina_info.nome",  # Nome da disciplina
                    "total_notas": 1  # Mostrar a soma das notas
                }
            }
        ]

        # Executando a agregação
        resultado = db.notas.aggregate(pipeline)
        
        # Exibindo os resultados
        print("\n--- Relatório de Total de Notas por Disciplina ---")
        for item in resultado:
            print(f"Disciplina: {item['disciplina_nome']} (ID: {item['disciplina_id']}) - Total de Notas: {item['total_notas']}")

    except Exception as e:
        print(f"Erro ao gerar o relatório: {e}")

def relatorio_alunos_por_disciplina():
    try:
        # Conexão com o MongoDB e a base de dados 'escola'
        client = MongoClient('localhost', 27017)
        db = client['escola']
        
        # Agregação para agrupar alunos por disciplina
        pipeline = [
            {
                "$lookup": {
                    "from": "notas",       # Referência à coleção de notas
                    "localField": "id",    # Campo id no alunos
                    "foreignField": "id_aluno",  # Campo id_aluno na coleção notas
                    "as": "notas_info"     # Resultado será colocado em 'notas_info'
                }
            },
            {
                "$unwind": "$notas_info"  # Desestrutura o array de notas_info
            },
            {
                "$lookup": {
                    "from": "disciplinas",  # Referência à coleção de disciplinas
                    "localField": "notas_info.id_disciplina",  # Campo id_disciplina de notas
                    "foreignField": "id",   # Campo id na coleção disciplinas
                    "as": "disciplina_info" # Resultado será colocado em 'disciplina_info'
                }
            },
            {
                "$unwind": "$disciplina_info"  # Desestrutura o array de disciplina_info
            },
            {
                "$group": {
                    "_id": "$disciplina_info.nome",  # Agrupa pelos nomes das disciplinas
                    "alunos": {"$push": "$nome"}      # Agrupa os nomes dos alunos
                }
            },
            {
                "$project": {
                    "_id": 0,
                    "disciplina": "$_id",      # Exibe o nome da disciplina
                    "alunos": 1                # Exibe a lista de alunos
                }
            }
        ]

        # Executando a agregação
        resultado = db.alunos.aggregate(pipeline)
        
        # Exibindo os resultados
        print("\n--- Relatório de Alunos por Disciplina ---")
        for item in resultado:
            print(f"Disciplina: {item['disciplina']}")
            print(f"Alunos: {', '.join(item['alunos'])}\n")

    except Exception as e:
        print(f"Erro ao gerar o relatório: {e}")
