# Generated by Django 5.1.1 on 2024-10-06 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='nickname',
        ),
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(blank=True, default='테스트', max_length=4),
        ),
    ]
