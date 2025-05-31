from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from UsuariosApp.models import InfoExtra

# 1. Define una clase inline para InfoExtra
class InfoExtraInline(admin.StackedInline):
    model = InfoExtra
    can_delete = False
    verbose_name_plural = 'Información Extra'
    fields = ('avatar', 'fechaNacimiento') 

# 2. Extiende UserAdmin para incluir InfoExtra
class CustomUserAdmin(UserAdmin):
    inlines = (InfoExtraInline,) 
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'get_fecha_nacimiento')
    list_select_related = ('infoextra',)

    def get_fecha_nacimiento(self, instance):
        return instance.infoextra.fechaNacimiento if hasattr(instance, 'infoextra') else None
    get_fecha_nacimiento.short_description = 'Fecha Nacimiento'

# 3. Re-registra UserAdmin con la personalización
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)