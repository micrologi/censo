# Generated by Django 5.0.6 on 2024-10-23 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sexo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sexo', models.CharField(db_index=True, default='', max_length=15, unique=True, verbose_name='Sexo')),
            ],
            options={
                'verbose_name': 'Sexo',
                'verbose_name_plural': 'Sexos',
                'db_table': 'sexos',
                'db_table_comment': 'Sexo das pessoas',
            },
        ),
    ]
