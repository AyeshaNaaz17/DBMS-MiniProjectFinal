from django.contrib import admin
from .models import Submissions, Review, Tag, Events
# Register your models here.

admin.site.register(Submissions)
admin.site.register(Review)
admin.site.register(Tag)
admin.site.register(Events)