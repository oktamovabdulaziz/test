from django.contrib import admin
from . import models


admin.site.register(models.Gender)
admin.site.register(models.Location)
admin.site.register(models.Person)
admin.site.register(models.Friendship)

