# Generated by Django 3.2.4 on 2021-06-21 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pw', '0007_alter_event_title'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['-event_date']},
        ),
        migrations.RemoveField(
            model_name='event',
            name='location',
        ),
        migrations.AddField(
            model_name='event',
            name='city',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='state',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='street',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='zip_code',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
