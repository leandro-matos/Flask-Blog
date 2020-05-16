# Blog em Flask

Projeto simples feito em Flask

## Rodando o projeto

```
git clone https://github.com/leandro-matos/flask-projects.git
cd flask-projects\blog-flask
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Incluir as variáveis de ambiente:

```
SECRET_KEY = os.environ.get('SECRET_KEY')
SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
MAIL_SERVER = 'smtp.googlemail.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USERNAME = os.environ.get('EMAIL_USER')
MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
```

Rodar o comando:
```
python run.py
```

## **Links Úteis**
https://devcontent.com.br/artigos/windows/o-que-sao-como-alterar-criar-excluir-variaveis-de-ambiente
