# Generated by Django 3.2 on 2021-04-26 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('queries', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NYTMovieReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('summaryShort', models.TextField()),
                ('author', models.CharField(max_length=50)),
                ('urlLink', models.TextField(default='')),
            ],
        ),
    ]
