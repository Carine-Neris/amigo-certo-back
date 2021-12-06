from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from amigo_certo.models import Usuario

admin.site.register(Usuario, UserAdmin)
