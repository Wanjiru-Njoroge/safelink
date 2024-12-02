from django.db import models

class Report(models.Model):
    INCIDENT_TYPES = [
        ('physical', 'Physical Abuse'),
        ('emotional', 'Emotional Abuse'),
        ('financial', 'Financial Abuse'),
        ('other', 'Other'),
    ]

    incident_type = models.CharField(max_length=20, choices=INCIDENT_TYPES)
    location = models.TextField()
    description = models.TextField()
    contact_info = models.CharField(max_length=255, null=True, blank=True)
    report_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Report ({self.incident_type}) - {self.report_date}"



class Resource(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    file_url = models.URLField(blank=True, null=True)  # Link to the resource
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

