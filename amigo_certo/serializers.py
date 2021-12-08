from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.fields import ReadOnlyField
from . import models


class UserSerializer(serializers.ModelSerializer):
    
    password = serializers.CharField(
        style={'input_type': 'password'},
        write_only=True,
        label="Senha"
    )

    class Meta:
        model = models.User
        fields = ['email','username','password', 'name', 'telefone', 'cpf', 'data_nascimento',
                  'endereco','perfil']
        extra_kwargs = {'password': {'write_only': True}}

    def save(self):
        conta = models.User( 
            email=self.validated_data['email'], 
            username=self.validated_data['username'],
            name=self.validated_data['name'],
            telefone=self.validated_data['telefone'],
            cpf=self.validated_data['cpf'],
            data_nascimento=self.validated_data['data_nascimento'],
            endereco=self.validated_data['endereco'],
            perfil = self.validated_data['perfil'],
        )
        password = self.validated_data['password']
        conta.set_password(password)
        conta.save()
        return conta


        
        
class NecessidadesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Necessidades
        fields = '__all__'
    

    def create(self, validated_data):
        
        user = validated_data.pop('user')
        necessidade = models.Necessidades.objects.create(user=user,
                            motivo=self.validated_data['motivo'],
                            periodo_inicial=self.validated_data['periodo_inicial'],
                            periodo_final=self.validated_data['periodo_final'],
                            local=self.validated_data['local'],
                            atividades=self.validated_data['atividades']
                            )
        return necessidade

