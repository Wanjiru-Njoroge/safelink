from django.contrib import admin
from django import forms
from .models import Report
from .models import Resource
from .models import Location

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('incident_type', 'location', 'report_date', 'contact_info')
    list_filter = ('incident_type', 'report_date')
    search_fields = ('description', 'location')

class ResourceAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploaded_at')
    search_fields = ('title', 'description')
admin.site.register(Resource)

class LocationForm(forms.ModelForm):
    latitude = forms.DecimalField(widget=forms.NumberInput(attrs={'step': '0.000001'}))
    longitude = forms.DecimalField(widget=forms.NumberInput(attrs={'step': '0.000001'}))
    class Meta:
        model = Location
        fields = '__all__'

    def clean_latitude(self):
        latitude = self.cleaned_data['latitude']
        if latitude < -90 or latitude > 90:
            raise forms.ValidationError("Latitude must be between -90 and 90.")
        return latitude

    def clean_longitude(self):
        longitude = self.cleaned_data['longitude']
        if longitude < -180 or longitude > 180:
            raise forms.ValidationError("Longitude must be between -180 and 180.")
        return longitude

# Admin interface for Location
class LocationAdmin(admin.ModelAdmin):
    form = LocationForm  # Use the custom form for better control
    list_display = ('name', 'latitude', 'longitude')  # Fields to display in the admin list view
    search_fields = ('name',)  # Add a search box for the name field
    ordering = ('name',)  # Default ordering by name
    fields = ('name', 'latitude', 'longitude')  # Fields to display in the admin form

# Register the model and admin
admin.site.register(Location, LocationAdmin)





