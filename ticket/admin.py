from django.contrib import admin

from .models import Ticket, TicketComment


class TicketAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'updated', 'file')
    search_fields = ('tilte', 'body')
    ordering = ['title']


class TicketCommentAdmin(admin.ModelAdmin):
    class Meta:
        model = TicketComment

admin.site.register(TicketComment, TicketCommentAdmin)
admin.site.register(Ticket, TicketAdmin)
