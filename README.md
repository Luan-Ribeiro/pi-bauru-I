Para rodar o projeto local siga os passos...

## Execução


Execute na pasta do projeto o comando:
```shell
python -m venv env
pip install -r requirements.txt
```

Entre na paste venv e rode o comando:
```shell
source /bin/activate
```

Retorne a pasta principal do projeto e rode os comandos:
```shell
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

Pronto agora é só acessar o http://127.0.0.1:8000/inicio


