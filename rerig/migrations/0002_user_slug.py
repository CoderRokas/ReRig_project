# Generated by Django 2.2.26 on 2022-03-10 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rerig', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='slug',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
    ]
