# Generated by Django 4.2.2 on 2023-06-14 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('key_master', '0003_alter_aluguel_data_aluguel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluguel',
            name='data_aluguel',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
