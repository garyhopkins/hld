# Generated by Django 4.1.4 on 2022-12-13 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('displays', '0002_delete_display'),
    ]

    operations = [
        migrations.CreateModel(
            name='Display',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=255)),
                ('style', models.CharField(max_length=255)),
                ('hide_address', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True)),
                ('deleted', models.BooleanField(default=False)),
            ],
        ),
    ]
