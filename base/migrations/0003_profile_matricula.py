# Generated by Django 4.0.5 on 2022-10-25 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_profile_telefone_alter_profile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='matricula',
            field=models.CharField(blank=True, max_length=14, verbose_name='Matricula'),
        ),
    ]
