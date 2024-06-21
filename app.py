import pandas as pd
import os
import psycopg2
import psycopg2.extras
import requests
from io import BytesIO
from psycopg2 import sql
import urllib3
from config import files, column_types, db_params, github_base_url
from dotenv import load_dotenv

DELETE_ADA_TABLE = ('DROP TABLE IF EXISTS public."ADA"')
DELETE_BNB_TABLE = ('DROP TABLE IF EXISTS public."BNB"')
DELETE_BTC_TABLE = ('DROP TABLE IF EXISTS public."BTC"')
DELETE_DOGE_TABLE = ('DROP TABLE IF EXISTS public."DOGE"')
DELETE_EOS_TABLE = ('DROP TABLE IF EXISTS public."EOS"')
DELETE_ETH_TABLE = ('DROP TABLE IF EXISTS public."ETH"')
DELETE_LTC_TABLE = ('DROP TABLE IF EXISTS public."LTC"')
DELETE_SOL_TABLE = ('DROP TABLE IF EXISTS public."SOL"')
DELETE_TRON_TABLE = ('DROP TABLE IF EXISTS public."TRON"')
DELETE_XRP_TABLE = ('DROP TABLE IF EXISTS public."XRP"')

# load_dotenv()
# url = os.getenv("DATABASE_URL")

# Suprime os avisos de segurança sobre SSL
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def deletarDados(connection):
    with connection.cursor() as cursor:
        try:
            cursor.execute(DELETE_ADA_TABLE)
            cursor.execute(DELETE_BNB_TABLE)
            cursor.execute(DELETE_BTC_TABLE)
            cursor.execute(DELETE_DOGE_TABLE)
            cursor.execute(DELETE_EOS_TABLE)
            cursor.execute(DELETE_ETH_TABLE)
            cursor.execute(DELETE_LTC_TABLE)
            cursor.execute(DELETE_SOL_TABLE)
            cursor.execute(DELETE_TRON_TABLE)
            cursor.execute(DELETE_XRP_TABLE)
            connection.commit()
            print("Tabelas deletadas com sucesso.")
        except psycopg2.Error as e:
            print("Erro ao deletar as tabelas:", e)
            connection.rollback()

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
        print(table_name)
        
        # Obtém os tipos de dados das colunas
        column_type_mapping = column_types.get(filename, {})
        columns = ', '.join(f"{col} {column_type_mapping.get(col, 'TEXT')}" for col in df.columns)
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
        deletarDados(connection)
        for filename in files:
            process_file(filename, connection)
except psycopg2.Error as e:
    print("Erro ao conectar ao banco de dados:", e)


print('Todas as tabelas foram criadas e os dados foram inseridos.')

