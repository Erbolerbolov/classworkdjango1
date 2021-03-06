# Generated by Django 4.0.4 on 2022-05-20 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_comment', models.CharField(max_length=100, verbose_name='Комментарий')),
                ('author', models.CharField(max_length=100, verbose_name='Автор')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('description', models.TextField(max_length=500, verbose_name='Описание')),
                ('author', models.CharField(max_length=100, verbose_name='Автор')),
            ],
        ),
    ]
