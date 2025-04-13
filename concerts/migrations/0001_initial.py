# Generated by Django 5.2 on 2025-04-13 08:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
        ('lieux', '0001_initial'),
        ('organisateurs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Concert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('price', models.FloatField()),
                ('DateStart', models.DateTimeField()),
                ('DateEnd', models.DateTimeField()),
                ('categorie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categories.categorie')),
                ('lieu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lieux.lieu')),
                ('organisateur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organisateurs.organisateur')),
            ],
            options={
                'unique_together': {('title', 'DateStart', 'lieu', 'organisateur', 'categorie')},
            },
        ),
    ]
