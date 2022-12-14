from django.db import models
import uuid

# Create your models here.

# A model is the single, definitive source of information about your data. It contains the essential fields and behaviors of the data you’re storing. 
# Django follows the DRY Principle. The goal is to define your data model in one place and automatically derive things from it.

# This includes the migrations - migrations are entirely derived from your models file, and are essentially a history that Django can roll through to 
# update your database schema to match your current models.


# Models are represented by Python classes

class Display(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  
    address1 = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255)
    state_province = models.CharField(max_length=255)
    zip = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    location_name = models.CharField(max_length=255)
    display_name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    holiday = models.CharField(max_length=255)
    style = models.CharField(max_length=255)
    hide_address = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    deleted = models.BooleanField(default=False)
    free_entrance = models.BooleanField(default=True)
    opening_date = models.DateField()
    closing_date = models.DateField()
    updated_date = models.DateField()
    description = models.TextField()
    viewer_instructions = models.TextField(blank=True)
    hours = models.TextField()
    website_url = models.TextField(blank=True)
    facebook_url = models.TextField(blank=True)
    youtube_url = models.TextField(blank=True)    
    remotefalcon_url = models.TextField(blank=True)

# It’s important to add __str__() methods to your models as a helpful representation, not only for your own convenience when dealing with the interactive prompt, but also because objects’ 
# representations are used throughout Django’s automatically-generated admin.

    def __str__(self):
        return self.display_name