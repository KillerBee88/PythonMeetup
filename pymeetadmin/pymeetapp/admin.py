from django.contrib import admin
from .models import Message, Speaker, User

class MessageAdmin(admin.ModelAdmin):
    list_display = ('guest', 'speaker', 'message')

class SpeakerAdmin(admin.ModelAdmin):
    list_display = ('user', 'start_date', 'end_date', 'subject', 'delay')

class UserAdmin(admin.ModelAdmin):
    list_display = ('tg_id', 'name')
    fields = ('tg_id', 'name')  # Добавьте эту строку

admin.site.register(Message, MessageAdmin)
admin.site.register(Speaker, SpeakerAdmin)
admin.site.register(User, UserAdmin)
