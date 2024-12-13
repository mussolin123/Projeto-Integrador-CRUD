import requests

# URL do endpoint que receberá a foto (substitua pelo seu domínio ou IP local)
url = 'http://localhost:8000/reconhecer/'  # ou 'http://seu-servidor/reconhecer/'

# Caminho para a foto que será enviada (substitua com o caminho correto da foto)
caminho_foto = 'caminho_para_a_foto.jpg'  # Ex: 'C:/fotos/aluno1.jpg'

# Abra o arquivo de imagem em modo binário
with open(caminho_foto, 'rb') as foto:
    # Prepare os dados para enviar: 'foto' é o campo esperado no Django
    files = {'foto': foto}

    # Envie a requisição POST com a foto
    response = requests.post(url, files=files)

    # Exiba a resposta do servidor
    if response.status_code == 200:
        print("Reconhecimento realizado com sucesso!")
        print(response.json())  # Exibe a resposta JSON do servidor
    else:
        print("Erro no reconhecimento:", response.status_code)
        print(response.json())  # Exibe a resposta de erro, se houver
