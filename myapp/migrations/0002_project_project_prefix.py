# Generated by Django 3.0.7 on 2020-06-17 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_prefix',
            field=models.CharField(default='', max_length=10),
            preserve_default=False,
        ),
    ]
