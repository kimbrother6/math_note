# Generated by Django 2.2 on 2021-05-24 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('english_note', '0002_auto_20210524_0434'),
    ]

    operations = [
        migrations.AddField(
            model_name='sentence',
            name='Classification',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
