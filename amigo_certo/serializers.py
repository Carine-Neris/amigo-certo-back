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



# class PerfilSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.Perfil
#         fields = '__all__'
        
        
class NecessidadesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Necessidades
        fields = '__all__'
    


# class AcompanhanteSerializer(serializers.ModelSerializer):
#     acompanhante = UserSerializer(required=True)
    
#     class Meta:
#         model = models.Acompanhante
#         fields = '__all__'


#     def create(self, validated_data):
#         import ipdb ; ipdb.set_trace()
#         print(validated_data)
#         user_data = validated_data.pop('acompanhante')
#         perfil = validated_data.pop('perfil')
#         user = UserSerializer.create(validated_data=user_data)
        
#     #     telefone=validated_data.pop('telefone')
#     #     cpf=validated_data.pop('cpf')
#     #     data_nascimento=validated_data.pop('data_nascimento')
#     #     endereco=validated_data.pop('endereco')
#     #     acompanante = AcompanhanteSerializer.objects.create(user=user,
#     #                         telefone=telefone,
#     #                         cpf=cpf,
#     #                         data_nascimento=data_nascimento,
#     #                         endereco=endereco
#     #                         )
#     #     acompanante.save()
#     #     return acompanante


# class ClienteSerializer(serializers.ModelSerializer):
#     cliente = UserSerializer(required=True)
    
#     class Meta:
#         model = models.Cliente
#         fields = '__all__'


#     def create(self, validated_data):

#         user_data = validated_data.pop('acompanhante')
#         user = UserSerializer.create(UserSerializer(), validated_data=user_data)
#         telefone=validated_data.pop('telefone')
#         cpf=validated_data.pop('cpf')
#         data_nascimento=validated_data.pop('data_nascimento')
#         endereco=validated_data.pop('endereco')
#         acompanante = AcompanhanteSerializer.objects.create(user=user,
#                             telefone=telefone,
#                             cpf=cpf,
#                             data_nascimento=data_nascimento,
#                             endereco=endereco
#                             )
#         acompanante.save()
#         return acompanante