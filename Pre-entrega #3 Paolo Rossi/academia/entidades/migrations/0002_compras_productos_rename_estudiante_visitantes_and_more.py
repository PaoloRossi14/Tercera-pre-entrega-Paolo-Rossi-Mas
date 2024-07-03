# Generated by Django 5.0.6 on 2024-07-03 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entidades', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('domicilio', models.CharField(max_length=50)),
                ('edad', models.IntegerField()),
                ('correo', models.CharField(max_length=50)),
                ('telefono', models.IntegerField()),
                ('nombredeempresa', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('precio', models.EmailField(max_length=254)),
                ('stock', models.EmailField(max_length=254)),
            ],
        ),
        migrations.RenameModel(
            old_name='Estudiante',
            new_name='Visitantes',
        ),
        migrations.DeleteModel(
            name='Curso',
        ),
        migrations.DeleteModel(
            name='Entregable',
        ),
        migrations.DeleteModel(
            name='Profesor',
        ),
    ]
