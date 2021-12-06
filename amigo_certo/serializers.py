from rest_framework import serializers
from . import models


class UsuarioSerializer(serializers.ModelSerializer):
    
    password = serializers.CharField(
        style={'input_type': 'password'},
        write_only=True,
        label="Senha"
    )

    password_confirm = serializers.CharField(
        style={'input_type': 'password'},
        write_only=True,
        label="Confirme a senha"
    )


    class Meta:
        model = models.Usuario
        fields = ('name','username','email', 'password', 'password_confirm','is_acompanhante','is_cliente')
        extra_kwargs = {'password': {'write_only': True}}

    def save(self):
        conta = models.Usuario(
            name=self.validated_data['name'], 
            email=self.validated_data['email'], 
            username=self.validated_data['username'],
            is_acompanhante=self.validated_data['is_acompanhante'],
            is_cliente=self.validated_data['is_cliente']
        )
        password = self.validated_data['password']
        password_confirm = self.validated_data['password_confirm']

        if password != password_confirm:
            raise serializers.ValidationError({'password': 'As senhas não são iguais.'})
        conta.set_password(password)
        conta.save()
        return conta
        



class AcompanhanteSerializer(serializers.ModelSerializer):
    acompanhante = serializers.RelatedField(many=True,read_only=True)
    
    class Meta:
        model = models.Acompanhante
        fields = ['acompanhante', 'telefone', 'cpf', 'data_nascimento', 'servicos', 'Endereco']

