from django.contrib import admin
from .models import Report
from .models import Resource

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('incident_type', 'location', 'report_date', 'contact_info')
    list_filter = ('incident_type', 'report_date')
    search_fields = ('description', 'location')

class ResourceAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploaded_at')
    search_fields = ('title', 'description')






admin.site.register(Resource)
