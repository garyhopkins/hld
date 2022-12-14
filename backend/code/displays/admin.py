# Register your models here.

from django.contrib import admin

# Make the displays app modifiable in the admin
# To do this, we need to tell the admin that Display objects have an admin interface by importing and registering

from .models import Display

admin.site.register(Display)