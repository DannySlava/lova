# Generated by Django 5.1.6 on 2025-02-24 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Utilisateur', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='photo_profil',
            field=models.ImageField(blank=True, null=True, upload_to='photos_profil/Client'),
        ),
        migrations.AlterField(
            model_name='professeur',
            name='photo_profil',
            field=models.ImageField(blank=True, null=True, upload_to='photos_profil/Professeur'),
        ),
    ]
