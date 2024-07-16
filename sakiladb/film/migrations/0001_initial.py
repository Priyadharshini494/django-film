# Generated by Django 5.0.6 on 2024-07-05 09:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('actor', '0002_alter_category_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('release_year', models.IntegerField()),
                ('rental_duration', models.IntegerField()),
                ('rental_rate', models.DecimalField(decimal_places=2, max_digits=5)),
                ('length', models.IntegerField()),
                ('replacement_cost', models.DecimalField(decimal_places=2, max_digits=5)),
                ('rating', models.CharField(choices=[('G', 'G'), ('PG', 'PG'), ('PG-13', 'PG-13'), ('R', 'R'), ('NC-17', 'NC-17')], default='G', max_length=5)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FilmActor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('actor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='actor.actor')),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='film.film')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='film',
            name='actor',
            field=models.ManyToManyField(through='film.FilmActor', to='actor.actor'),
        ),
        migrations.CreateModel(
            name='FilmCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='actor.category')),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='film.film')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FilmText',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='film.film')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]