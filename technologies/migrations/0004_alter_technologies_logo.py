# Generated by Django 3.2.6 on 2021-08-18 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('technologies', '0003_alter_technologies_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='technologies',
            name='logo',
            field=models.ImageField(upload_to='static/technologies/images/'),
        ),
    ]
