import pandas as pd
from datetime import datetime
import os
import psycopg2
import psycopg2.extras
import requests
from io import BytesIO
from psycopg2 import sql
import urllib3

# Suprime os avisos de segurança sobre SSL
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Conexão com o banco de dados PostgreSQL local
db_params = {
    'dbname': 'cripto',
    'user': 'postgres',
    'password': 'senac@123',
    'host': 'localhost',
    'port': '5434'
}

# URL base do GitHub raw
github_base_url = 'https://raw.githubusercontent.com/pevehdev/Analise-Criptomoedas/main/Criptos/'



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
]

# Função para baixar e processar arquivos
def process_file(filename, connection):
    # URL completa do arquivo raw
    file_url = github_base_url + filename
    
    # Baixa o arquivo com verificação de certificado desabilitada
    response = requests.get(file_url, verify=False)
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
        
        with connection.cursor() as cursor:
            try:
                cursor.execute(create_table_query)
                connection.commit()
            except psycopg2.Error as e:
                print(f"Erro ao criar a tabela {table_name}: {e}")
                connection.rollback()
                return
            
            # Insere os dados na tabela
            for _, row in df.iterrows():
                insert_query = sql.SQL("INSERT INTO {} VALUES ({})").format(
                    sql.Identifier(table_name),
                    sql.SQL(', ').join(sql.Placeholder() * len(row))
                )
                try:
                    cursor.execute(insert_query, tuple(row))
                except psycopg2.Error as e:
                    print(f"Erro ao inserir dados na tabela {table_name}: {e}")
                    connection.rollback()
                    break
            else:
                connection.commit()
                print(f'Tabela {table_name} criada e populada com sucesso.')
    else:
        print(f'Falha ao baixar o arquivo {filename} com status code {response.status_code}')

# Conexão com o banco de dados
try:
    with psycopg2.connect(**db_params) as connection:
        for filename in files:
            process_file(filename, connection)
except psycopg2.Error as e:
    print("Erro ao conectar ao banco de dados:", e)

print('Todas as tabelas foram criadas e os dados foram inseridos.')
