# Generated by Django 4.1 on 2022-12-08 03:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("Autor", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Categoria",
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
                ("nombre", models.CharField(max_length=50, verbose_name="Categoria")),
            ],
        ),
        migrations.CreateModel(
            name="Libro",
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
                ("titulo", models.CharField(max_length=50, verbose_name="Titulo")),
                ("fecha", models.DateField(verbose_name="Fecha Publicacion")),
                (
                    "portada",
                    models.ImageField(upload_to="portada", verbose_name="Portada"),
                ),
                ("visitas", models.PositiveIntegerField()),
                ("autores", models.ManyToManyField(to="Autor.autor")),
                (
                    "categoria",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Libro.categoria",
                    ),
                ),
            ],
        ),
    ]