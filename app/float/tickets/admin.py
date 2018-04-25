from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from django.conf.urls import url
from django.template.response import TemplateResponse

from .models import Ticket

class TicketAdmin(admin.ModelAdmin):

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            url(
                r'^(?P<ticket_id>.+)/print/$',
                self.admin_site.admin_view(self.process_generate_ticket),
                name='generate-ticket',
            ),
        ]
        return custom_urls + urls

    def generate_ticket_action(self, obj):
        return format_html(
            '<a href="{}" class="action-button" target="_blank">Print</a>&nbsp;',
            reverse('admin:generate-ticket', args=[obj.pk]),
        )
    generate_ticket_action.short_description = 'Ticket'
    generate_ticket_action.allow_tags = True

    def process_generate_ticket(self, request, ticket_id):
        ticket = self.get_object(request, ticket_id)

        context = self.admin_site.each_context(request)
        context['opts'] = self.model._meta
        context['ticket'] = ticket

        return TemplateResponse(
            request,
            'admin/ticket/print.html',
            context,
        )

    list_display = (
        'id',
        'room_type',
        'duration',
        'code',
        'redeemed',
        'validto',
        'created',
        'generate_ticket_action'
    )

    readonly_fields = (
        'id',
        'code',
        'created',
        'redeemed'
    )
    search_fields = ['code']
    list_filter = ('redeemed', 'room_type', 'duration', 'validto')

    # edit / new
    fieldsets = [
        ('Ticket', {'fields': [
            ('room_type', 'duration'),
            ('created', 'code', 'redeemed'),
            ('validto'),
            ('comment')
        ]})
    ]

admin.site.register(Ticket, TicketAdmin)

admin.site.site_header = 'MoonYoga - Float Admin'