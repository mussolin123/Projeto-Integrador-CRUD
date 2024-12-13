# 📸 Reconhecimento Facial para Chamada de Alunos
Este projeto foi desenvolvido para modernizar o sistema de chamada de alunos nas salas de aula utilizando **reconhecimento facial.** Com uma interface web, os professores podem cadastrar e gerenciar imagens, e os alunos têm suas entradas avaliadas por meio de reconhecimento facial via webcam.

## 📋 Funcionalidades

<li> Cadastro de Alunos: Sistema de cadastro de fotos e informações de alunos. </li>
<li> Reconhecimento Facial em Tempo Real: Avaliação de entrada para identificar alunos em tempo real. </li>
<li> API REST: Implementação com Django Rest Framework para operações de CRUD de alunos. </li>

## 🔧 1. Configuração do Ambiente
> [!WARNING]
> Para configurar o ambiente de desenvolvimento, siga as etapas abaixo.

<li> Python 3.11.9 (ou versão compatível) Baixe em: https://www.python.org/downloads/release/python-3119/</li>
<li> Django para backend </li>
<li> OpenCV e face_recognition para reconhecimento facial </li>
<li> Pillow para manipulação de imagens </li>

## 🖥️ 2. Configuração do Ambiente Virtual
> [!IMPORTANT]
> Recomenda-se criar um ambiente virtual para isolar as dependências do projeto (principalmente se estiver executando no Windows).

```
python -m venv ambiente
```
Em seguida, ative o ambiente:
```
ambiente\Scripts\activate
```

## 🛠️ 3 Preparação do Sistema para dlib
Algumas dependências adicionais são necessárias para o funcionamento do dlib:

### 3.1 Visual C++ Build Tools: Instale as ferramentas de compilação C++.

> https://visualstudio.microsoft.com/pt-br/downloads/?q=build+tools  <br>  <br>


### 3.2 Dlib
Após instalar os pré-requisitos, instale o dlib:
```
pip install dlib-19.24.1-cp311-cp311-win_amd64.whl
```

# 📦 4. Instalação das Bibliotecas Necessárias
Use o comando abaixo para instalar todas as bibliotecas requeridas de uma vez (dentro do ambiente virtual):

```
pip install -r requirements.txt
```

## 🐍 5. Executando o Servidor Django

Rode os comandos abaixo para atualizar alterações diretamente ao banco de dados.
```
python manage.py makemigrations
```
```
python manage.py migrate
```

Inicie o servidor de desenvolvimento do Django:
```
python manage.py runserver
```
Acesse o endereço http://127.0.0.1:8000/ para verificar se o sistema está funcionando.

## 5.1 🔑 Criar suário base de dados Django
```
python manage.py createsuperuser
```

# 🔗 Links Úteis
<li> Django Admin: http://127.0.0.1:8000/admin/ </li>
<li> API de Alunos: http://127.0.0.1:8000/api/alunos/ </li>
