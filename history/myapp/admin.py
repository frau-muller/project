from django.contrib import admin
from .models import Questions
# Register your models here.



class QuestionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')

admin.site.register(Questions, QuestionsAdmin)