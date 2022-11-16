from django.db import models

# Create your models here.
# no cmd execute >> 'python manage.py mekemigrations'
# será criado um arquivo do tipo x_initial.py na pasta migrations, 
# posteriormente execute o comando 'python manage.py migrate' 
# para criar a tabela no banco (por padrão é utilizado o SQLite)
class Person(models.Model):
    primeiro_nome = models.CharField(max_length=100)
    segundo_nome = models.CharField(max_length=100)
    usuario = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)

