# Generated by Django 4.2.16 on 2024-10-25 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0004_videoproduto_label'),
    ]

    operations = [
        migrations.AddField(
            model_name='modelo',
            name='icone',
            field=models.TextField(default='', verbose_name='Ícone HTML'),
        ),
    ]
