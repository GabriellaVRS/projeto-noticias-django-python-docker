# Generated by Django 4.2.3 on 2023-08-01 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fotografia',
            name='categoria',
            field=models.CharField(choices=[('NEBULOSA', 'Nebulosa'), ('ESTRELA', 'Estrela'), ('GALAXIA', 'Galaxia'), ('PLANETA', 'Planeta')], default=' ', max_length=100),
        ),
    ]
