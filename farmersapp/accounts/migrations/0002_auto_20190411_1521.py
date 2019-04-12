# Generated by Django 2.2 on 2019-04-11 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='officer',
            name='login_id',
            field=models.EmailField(help_text='Unique ID for every officer', max_length=255, unique=True),
        ),
    ]
