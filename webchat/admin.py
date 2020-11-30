from django.contrib import admin
from .models import User , Message , Chat


class UserAdmin(admin.ModelAdmin):
    list_display = ('id' , 'login' , '_ban' , 'time_create')

# Register your models here.
admin.site.register(User , UserAdmin)
admin.site.register(Message)
admin.site.register(Chat)
