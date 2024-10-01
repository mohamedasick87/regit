from django.db import models

class Event(models.Model):
    EVENT_TYPE_CHOICES = [
        ('technical', 'Technical'),
        ('non_technical', 'Non-Technical'),
    ]
    
    name = models.CharField(max_length=100)
    event_type = models.CharField(max_length=20, choices=EVENT_TYPE_CHOICES)

    def __str__(self):
        return self.name

class Registration(models.Model):
    # Fields for the registration form
    name = models.CharField(max_length=100)
    college = models.CharField(max_length=255)
    department = models.CharField(max_length=100,null=True)

    # Many-to-Many relationship with Event for technical and non-technical events
    technical_events = models.ManyToManyField(Event, related_name='technical_registrations', blank=True)
    non_technical_events = models.ManyToManyField(Event, related_name='non_technical_registrations', blank=True)

    # Paper Submission fields
    paper_title = models.CharField(max_length=255, blank=True, null=True)
    paper_submission_link = models.URLField(blank=True, null=True)

    # Contact information fields
    phone = models.CharField(max_length=15)
    email = models.EmailField()

    # Payment-related fields
    payment_link = models.URLField(blank=True, null=True)
    transaction_number = models.CharField(max_length=100, blank=True, null=True)

    # WhatsApp group link field
    whatsapp_group_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return f'{self.name} ({self.college})'
