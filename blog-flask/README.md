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
<<<<<<< HEAD

Variáveis de ambiente: https://medium.com/@victorromariopazdejesus/python-3-configurando-vari%C3%A1veis-de-ambiente-no-windows-10-63059c7192e6

=======
## Incluir as variáveis de ambiente:
>>>>>>> ec53f2e02f9ab571204afbcc2c7f6e50d21d4231
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
