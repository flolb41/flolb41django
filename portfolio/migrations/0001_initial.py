# Generated by Django 3.2.6 on 2021-08-18 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
                ('logo', models.ImageField(upload_to='static/portfolio/images/')),
                ('description', models.TextField(blank=True)),
            ],
        ),
    ]
