# Generated by Django 3.2.4 on 2021-06-19 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pw', '0002_rename_events_event'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=150)),
                ('message', models.TextField()),
            ],
        ),
    ]
