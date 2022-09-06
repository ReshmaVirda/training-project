# Generated by Django 4.0 on 2022-01-05 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('pass1', models.CharField(max_length=200)),
                ('pass2', models.CharField(max_length=200)),
            ],
        ),
    ]