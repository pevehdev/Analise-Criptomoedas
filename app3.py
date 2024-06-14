import requests

github_token = 'seu_token_de_acesso_pessoal_aqui'  # Substitua pelo seu token de acesso pessoal

headers = {
    'Authorization': f'token {github_token}'
}

# Exemplo de solicitação GET com autenticação
response = requests.get('https://github.com/pevehdev/Analise-Criptomoedas/raw/main/Bitcoin/BTC.xlsx', headers=headers, verify=False)

print(response.status_code)
print(response.content)
