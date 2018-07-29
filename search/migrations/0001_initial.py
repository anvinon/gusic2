# Generated by Django 2.0.3 on 2018-07-28 05:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('genre1', models.CharField(blank=True, max_length=255, null=True)),
                ('genre2', models.CharField(blank=True, max_length=255, null=True)),
                ('genre3', models.CharField(blank=True, max_length=255, null=True)),
                ('genre4', models.CharField(blank=True, max_length=255, null=True)),
                ('genre5', models.CharField(blank=True, max_length=255, null=True)),
                ('genre6', models.CharField(blank=True, max_length=255, null=True)),
                ('genre7', models.CharField(blank=True, max_length=255, null=True)),
                ('genre8', models.CharField(blank=True, max_length=255, null=True)),
                ('genre9', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ArtistAndGenre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='search.Artist')),
            ],
        ),
        migrations.CreateModel(
            name='ArtistAndSongs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='search.Artist')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='SearchHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Songs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('free_download', models.BooleanField(default=False)),
                ('url', models.URLField(blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='artistandsongs',
            name='song',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='search.Songs'),
        ),
        migrations.AddField(
            model_name='artistandgenre',
            name='genre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='search.Genre'),
        ),
    ]
