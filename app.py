import pandas as pd
from dotenv import load_dotenv
from datetime import datetime
import os
import psycopg2 #pip install psycopg2  
import psycopg2.extras


#CONEXÃO DO BANCO DE DADOS
#load_dotenv()
#url = os.getenv("DATABASE_URL")
try:
    db_connection = psycopg2.connect(
    dbname='cripto',
    user='postgres',
    password='senac@123',
    host='localhost',
    port='5434'
    )
    cursor = db_connection.cursor()
    

except psycopg2.Error as e:
    print("Erro ao conectar ao banco de dados:", e)



# URL base do GitHub raw
github_base_url = 'https://raw.githubusercontent.com/pevehdev/Analise-Criptomoedas/main/'

files = [
    'BNB.xlsx',
    'BTC.xlsx',
    'ETH.xlsx',
    'ADA.xlsx',
    'DOGE.xlsx',
    'EOS.xlsx',
    'LTC.xlsx',
    'SOL.xlsx',
    'TRON.xlsx',
    'XRP.xlsx'
    # Adicione mais arquivos conforme necessário
]

for filename in files:
    # URL completa do arquivo raw
    file_url = github_base_url + filename
    
    # Baixa o arquivo
    response = requests.get(file_url)
    if response.status_code == 200:
        # Lê o arquivo .xlsx em um DataFrame
        df = pd.read_excel(BytesIO(response.content), engine='openpyxl')
        
        # Nome da tabela será o nome do arquivo sem a extensão
        table_name = filename.split('.')[0]
        
        # Cria a tabela no PostgreSQL
        columns = ', '.join(f"{col} TEXT" for col in df.columns)
        create_table_query = sql.SQL("CREATE TABLE IF NOT EXISTS {} ({})").format(
            sql.Identifier(table_name),
            sql.SQL(columns)
        )
        try:
            cursor.execute(create_table_query)
        except psycopg2.Error as e:
            print("Erro ao conectar ao banco de dados:", e)
        
        # Insere os dados na tabela
        for _, row in df.iterrows():
            try:
                with psycopg2.connect(url) as db_connection:
                    with db_connection.cursor() as cursor:
                        insert_query = sql.SQL("INSERT INTO {} VALUES ({})").format(
                            sql.Identifier(table_name),
                            sql.SQL(', ').join(sql.Placeholder() * len(row))
                        )
                        cursor.execute(insert_query, tuple(row))
            
        
        print(f'Tabela {table_name} criada e populada com sucesso.')
    else:
        print(f'Falha ao baixar o arquivo {filename}')

# Confirma as mudanças e fecha a conexão
conn.commit()
cursor.close()
conn.close()

print('Todas as tabelas foram criadas e os dados foram inseridos.')

