from django.contrib import admin
from .models import Registration, Event
from import_export import resources
from import_export.admin import ExportMixin

class RegistrationResource(resources.ModelResource):
    class Meta:
        model = Registration
        fields = (
            'name', 
            'college', 
            'department',  # Add department
            'technical_events', 
            'non_technical_events', 
            'paper_title',  # Add paper title
            'paper_submission_link',  # Add paper submission link
            'phone', 
            'email', 
            'payment_link',  # Add payment submission link
            'transaction_number',  # Add transaction number
            'whatsapp_group_link'  # Add WhatsApp group link
        )

class TechnicalEventFilter(admin.SimpleListFilter):
    title = 'Technical Events'
    parameter_name = 'technical_events'

    def lookups(self, request, model_admin):
        events = Event.objects.filter(event_type='technical')
        return [(event.id, event.name) for event in events]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(technical_events__id=self.value())
        return queryset

class NonTechnicalEventFilter(admin.SimpleListFilter):
    title = 'Non-Technical Events'
    parameter_name = 'non_technical_events'

    def lookups(self, request, model_admin):
        events = Event.objects.filter(event_type='non_technical')
        return [(event.id, event.name) for event in events]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(non_technical_events__id=self.value())
        return queryset

@admin.register(Registration)
class RegistrationAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = RegistrationResource

    # Customize the list display in the admin panel
    list_display = (
        'name', 
        'college', 
        'department',  # Add department
        'get_technical_events', 
        'get_non_technical_events', 
        'phone', 
        'email', 
        'paper_title',  # Add paper title
        'payment_link',  # Add payment link
        'transaction_number',  # Add transaction number
        'whatsapp_group_link'  # Add WhatsApp group link
    )
    
    # Add search capability to the admin panel
    search_fields = ('name', 'college', 'department', 'phone', 'email')

    # Add custom filters for technical and non-technical events
    list_filter = (TechnicalEventFilter, NonTechnicalEventFilter, 'college')

    # Optional: Add ordering
    ordering = ('name',)

    # Optional: Customize the admin form layout
    fieldsets = (
        (None, {
            'fields': (
                'name', 
                'college', 
                'department',  # Add department
                'technical_events', 
                'non_technical_events', 
                'paper_title',  # Add paper title
                'paper_submission_link',  # Add paper submission link
                'phone', 
                'email', 
                'payment_link',  # Add payment link
                'transaction_number',  # Add transaction number
                'whatsapp_group_link'  # Add WhatsApp group link
            )
        }),
    )

    # Custom methods to display events in list_display
    def get_technical_events(self, obj):
        return ", ".join([event.name for event in obj.technical_events.all()])
    get_technical_events.short_description = 'Technical Events'

    def get_non_technical_events(self, obj):
        return ", ".join([event.name for event in obj.non_technical_events.all()])
    get_non_technical_events.short_description = 'Non-Technical Events'
