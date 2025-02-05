# Generated by Django 5.1.5 on 2025-02-04 15:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ProjetoDjango",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "titulo_filme",
                    models.CharField(max_length=50, verbose_name="Título do Filme"),
                ),
                ("genero", models.CharField(max_length=50, verbose_name="Gênero")),
                (
                    "avaliacao_IMDb",
                    models.DecimalField(
                        decimal_places=2, max_digits=100, verbose_name="Avaliação IMDb"
                    ),
                ),
                (
                    "data",
                    models.DateTimeField(
                        default=datetime.datetime(2025, 2, 4, 12, 31, 38, 539301),
                        verbose_name="Data Lançamento",
                    ),
                ),
            ],
        ),
    ]
