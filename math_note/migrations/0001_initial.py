# Generated by Django 2.2 on 2021-05-17 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page', models.CharField(max_length=70)),
                ('WR', models.TextField()),
                ('cover', models.ImageField(upload_to='images/')),
            ],
        ),
    ]