from django.contrib import admin
from .models import concertModel,locationModel,timeModel,ProfileModel,ticketModel

# Register your models here.

admin.site.register(concertModel)
admin.site.register(locationModel)
admin.site.register(timeModel)
admin.site.register(ProfileModel)
admin.site.register(ticketModel)