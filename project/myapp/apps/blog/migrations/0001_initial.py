# Generated by Django 3.1.5 on 2021-01-18 01:20

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('lastName', models.CharField(max_length=50, verbose_name='Apellido')),
                ('facebook', models.CharField(blank=True, max_length=50, null=True, verbose_name='Facebook')),
                ('twitter', models.CharField(blank=True, max_length=50, null=True, verbose_name='Twitter')),
                ('instagram', models.CharField(blank=True, max_length=50, null=True, verbose_name='Instagram')),
                ('email', models.CharField(blank=True, max_length=50, null=True, verbose_name='Correo')),
                ('state', models.BooleanField(default=True, verbose_name='Autor activo / No activo')),
                ('creationDate', models.DateField(auto_now_add=True, verbose_name='Fecha de creaciÃ³n')),
                ('time', models.TimeField(auto_now_add=True, verbose_name='Hora de publicación')),
            ],
            options={
                'verbose_name': 'Autor',
                'verbose_name_plural': 'Autores',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='Nombre de categoria')),
                ('state', models.BooleanField(default=True, verbose_name='Categoria activada / desactivada')),
                ('creationDate', models.DateField(auto_now_add=True, verbose_name='Fecha de creación')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categrias',
            },
        ),
        migrations.CreateModel(
            name='Contry',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, verbose_name='Pais')),
            ],
        ),
        migrations.CreateModel(
            name='Discipline',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, verbose_name='Nombre de la disciplina')),
                ('state', models.BooleanField(default=True, verbose_name='Disciplina activada / desactivada')),
            ],
            options={
                'verbose_name': 'Disciplina',
                'verbose_name_plural': 'Disciplinas',
            },
        ),
        migrations.CreateModel(
            name='Ligue',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, verbose_name='Nombre de la liga')),
                ('state', models.BooleanField(default=True, verbose_name='Liga activada / desactivada')),
            ],
            options={
                'verbose_name': 'Liga',
                'verbose_name_plural': 'Ligas',
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='Nombre')),
                ('teamLogo', models.ImageField(upload_to='logo/', verbose_name='Logo')),
                ('Contry', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='TeamContry', to='blog.contry')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Categoria', to='blog.category')),
            ],
            options={
                'verbose_name': 'Equipo',
                'verbose_name_plural': 'Equipos',
            },
        ),
        migrations.CreateModel(
            name='Stadium',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='Nombre')),
                ('city', models.CharField(max_length=100, null=True, verbose_name='Ciudad')),
                ('Contry', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='EstadiumContry', to='blog.contry')),
            ],
            options={
                'verbose_name': 'Estadio',
                'verbose_name_plural': 'Estadios',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=80, verbose_name='Título')),
                ('slug', models.CharField(max_length=100, verbose_name='Slug')),
                ('description', models.CharField(max_length=100, verbose_name='Descripción')),
                ('content', ckeditor.fields.RichTextField()),
                ('image', models.URLField(max_length=255, verbose_name='Imagen URL')),
                ('outstandingType1', models.BooleanField(default=False, verbose_name='Destacado tipo 1  SI/ NO')),
                ('outstandingType2', models.BooleanField(default=False, verbose_name='Destacado tipo 2  SI/ NO')),
                ('state', models.BooleanField(default=False, verbose_name='Publicado / No publicado')),
                ('creationDate', models.DateField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('time', models.TimeField(auto_now_add=True, verbose_name='Hora de publicación')),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.autor')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.category')),
                ('contry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.contry')),
            ],
            options={
                'verbose_name': 'Artículo',
                'verbose_name_plural': 'Artículos',
                'ordering': ['-creationDate'],
            },
        ),
        migrations.AddField(
            model_name='category',
            name='Discipline',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.discipline'),
        ),
        migrations.CreateModel(
            name='BlackboardResults',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('runsScoredWinner', models.IntegerField(verbose_name='Carreras')),
                ('runsScoredLoser', models.IntegerField(verbose_name='Carreras')),
                ('date', models.DateField(verbose_name='Fecha de juego')),
                ('state', models.BooleanField(default=False, verbose_name='Publicar SI/NO')),
                ('loserTeam', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Visitante', to='blog.team', verbose_name='Visitante')),
                ('stadium', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.stadium')),
                ('winnerTeam', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Ganador', to='blog.team', verbose_name='Equipo ganador')),
            ],
            options={
                'verbose_name': 'Resultado',
                'verbose_name_plural': 'Resultados',
                'ordering': ['-date'],
            },
        ),
    ]
