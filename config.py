# Conexão com o banco de dados PostgreSQL local
db_params = {
    'dbname': 'cripto',
    'user': 'postgres',
    'password': 'senac@123',
    'host': 'localhost',
    'port': '5434'
}

# URL base do GitHub raw para o diretório correto
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

# Definição dos tipos de dados das colunas para cada arquivo
column_types = {
    'BNB.xlsx': {
        'Data': 'DATE',
        'Abertura': 'FLOAT',
        'Máxima': 'FLOAT',
        'Mínima': 'FLOAT',
        'Fechamento': 'FLOAT',
        'Volume': 'FLOAT',
        'Marketcap': 'FLOAT'
    },
    'BTC.xlsx': {
        'Data': 'DATE',
        'Abertura': 'FLOAT',
        'Máxima': 'FLOAT',
        'Mínima': 'FLOAT',
        'Fechamento': 'FLOAT',
        'Volume': 'FLOAT',
        'Marketcap': 'FLOAT'
    },
    'ETH.xlsx': {
        'Data': 'DATE',
        'Abertura': 'FLOAT',
        'Máxima': 'FLOAT',
        'Mínima': 'FLOAT',
        'Fechamento': 'FLOAT',
        'Volume': 'FLOAT',
        'Marketcap': 'FLOAT'
    },
    # Adicione os tipos de dados para os demais arquivos
    'ADA.xlsx': {
        'Data': 'DATE',
        'Abertura': 'FLOAT',
        'Máxima': 'FLOAT',
        'Mínima': 'FLOAT',
        'Fechamento': 'FLOAT',
        'Volume': 'FLOAT',
        'Marketcap': 'FLOAT'
    },
    'DOGE.xlsx': {
        'Data': 'DATE',
        'Abertura': 'FLOAT',
        'Máxima': 'FLOAT',
        'Mínima': 'FLOAT',
        'Fechamento': 'FLOAT',
        'Volume': 'FLOAT',
        'Marketcap': 'FLOAT'
    },
    'EOS.xlsx': {
        'Data': 'DATE',
        'Abertura': 'FLOAT',
        'Máxima': 'FLOAT',
        'Mínima': 'FLOAT',
        'Fechamento': 'FLOAT',
        'Volume': 'FLOAT',
        'Marketcap': 'FLOAT'
    },
    'LTC.xlsx': {
        'Data': 'DATE',
        'Abertura': 'FLOAT',
        'Máxima': 'FLOAT',
        'Mínima': 'FLOAT',
        'Fechamento': 'FLOAT',
        'Volume': 'FLOAT',
        'Marketcap': 'FLOAT'
    },
    'SOL.xlsx': {
        'Data': 'DATE',
        'Abertura': 'FLOAT',
        'Máxima': 'FLOAT',
        'Mínima': 'FLOAT',
        'Fechamento': 'FLOAT',
        'Volume': 'FLOAT',
        'Marketcap': 'FLOAT'
    },
    'TRON.xlsx': {
        'Data': 'DATE',
        'Abertura': 'FLOAT',
        'Máxima': 'FLOAT',
        'Mínima': 'FLOAT',
        'Fechamento': 'FLOAT',
        'Volume': 'FLOAT',
        'Marketcap': 'FLOAT'
    },
    'XRP.xlsx': {
        'Data': 'DATE',
        'Abertura': 'FLOAT',
        'Máxima': 'FLOAT',
        'Mínima': 'FLOAT',
        'Fechamento': 'FLOAT',
        'Volume': 'FLOAT',
        'Marketcap': 'FLOAT'
    }
}