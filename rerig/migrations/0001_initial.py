# Generated by Django 2.2.26 on 2022-03-09 18:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True)),
                ('description', models.CharField(max_length=200)),
                ('averageRating', models.IntegerField(default=0)),
                ('category', models.CharField(max_length=50)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30, unique=True)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField()),
                ('comment', models.CharField(max_length=200)),
                ('date', models.DateField()),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rerig.Post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rerig.User')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rerig.User'),
        ),
    ]
