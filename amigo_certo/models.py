from django.db import models
from django.contrib.auth.models import User, AbstractUser
from datetime import date



class User(AbstractUser):
    USER_TYPE_CHOICES = (
      (1, 'Cliente'),
      (2, 'Voluntário')
    )
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=8)
    email = models.EmailField(max_length=254, unique=True, error_messages={'unique': "O email cadastrado já existe."})
    name = models.CharField(max_length=300)
    telefone = models.CharField(max_length=11, null=False, blank=False)
    cpf = models.CharField(max_length=11, null=False, blank=False)
    data_nascimento = models.DateField(null=False, blank=False)
    endereco = models.CharField(max_length=1000, null=False, blank=False)
    is_staff = models.BooleanField(default=True)
    perfil = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES)
    
    
    def __str__(self):
        return self.name



class Necessidades(models.Model):
    ATIVIDADES = [
        ('bate-papo', 'Bate-papo'),
        ('cinema', 'Cinema'),
        ('shopping', 'Shopping'),
        ('passear', 'Passear')
    ]
    motivo = models.CharField(max_length=200,null=False, blank=False)
    data = models.DateField()
    periodo = models.DateTimeField('Data de solicitação', auto_now_add=True)
    local = models.CharField(max_length=200,null=False, blank=False)
    atividades = models.CharField(
        max_length=20, choices=ATIVIDADES, blank=False, null=False)
    cliente = models.ForeignKey(User,on_delete = models.CASCADE)
    
    def __str__(self):
        return self.motivo