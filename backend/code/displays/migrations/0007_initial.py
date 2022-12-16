# Generated by Django 4.1.4 on 2022-12-14 04:43

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('displays', '0006_delete_display'),
    ]

    operations = [
        migrations.CreateModel(
            name='Display',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('address1', models.CharField(max_length=255)),
                ('address2', models.CharField(blank=True, max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('state_province', models.CharField(max_length=255)),
                ('zip', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('location_name', models.CharField(max_length=255)),
                ('display_name', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=255)),
                ('holiday', models.CharField(max_length=255)),
                ('style', models.CharField(max_length=255)),
                ('hide_address', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True)),
                ('deleted', models.BooleanField(default=False)),
                ('free_entrance', models.BooleanField(default=True)),
                ('opening_date', models.DateField()),
                ('closing_data', models.DateField()),
                ('updated_date', models.DateField()),
                ('description', models.TextField()),
                ('viewer_instructions', models.TextField(blank=True)),
                ('hours', models.TextField()),
                ('website_url', models.TextField(blank=True)),
                ('facebook_url', models.TextField(blank=True)),
                ('youtube_url', models.TextField(blank=True)),
                ('remotefalcon_url', models.TextField(blank=True)),
            ],
        ),
    ]