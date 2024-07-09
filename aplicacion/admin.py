from django.contrib import admin

# Register your models here.

from .models import Cliente,Ciudad

# Register your models here.
admin.site.register(Ciudad)
admin.site.register(Cliente)
