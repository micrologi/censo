# Generated by Django 5.0.6 on 2024-10-23 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cargo', models.CharField(db_index=True, default='', max_length=60, unique=True, verbose_name='Cargo')),
            ],
            options={
                'verbose_name': 'Cargo',
                'verbose_name_plural': 'Cargos',
                'db_table': 'cargos',
                'db_table_comment': 'Cargos dos servidores',
                'indexes': [models.Index(fields=['cargo'], name='cargos_cargo_afad19_idx')],
            },
        ),
    ]
