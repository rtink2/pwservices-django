# Generated by Django 3.2.4 on 2021-07-31 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pw', '0009_event_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['event_date']},
        ),
        migrations.AddField(
            model_name='event',
            name='event_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
