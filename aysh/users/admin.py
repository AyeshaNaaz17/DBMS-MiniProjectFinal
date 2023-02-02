from django.contrib import admin
from .models import Profile, Conference, Journal, Message
# Register your models here.

admin.site.register(Profile)
admin.site.register(Conference)
admin.site.register(Journal)
admin.site.register(Message)