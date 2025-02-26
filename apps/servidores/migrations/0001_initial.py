# Generated by Django 5.0.6 on 2024-11-05 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Servidor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NU_ANO', models.IntegerField(verbose_name='NU_ANO')),
                ('NU_MES', models.IntegerField(verbose_name='NU_MES')),
                ('CO_COMP_MASSA', models.IntegerField(verbose_name='CO_COMP_MASSA')),
                ('NU_CNPJ_ORGAO', models.CharField(max_length=20, verbose_name='NU_CNPJ_ORGAO')),
                ('NO_ORGAO', models.IntegerField(verbose_name='NO_ORGAO')),
                ('CO_PODER', models.IntegerField(verbose_name='CO_PODER')),
                ('ID_SERVIDOR', models.IntegerField(verbose_name='ID_SERVIDOR')),
                ('NO_SERVIDOR', models.CharField(max_length=100, verbose_name='NO_SERVIDOR')),
                ('ID_SERVIDOR_MATRICULA', models.IntegerField(verbose_name='ID_SERVIDOR_MATRICULA')),
                ('ID_SERVIDOR_CPF', models.CharField(max_length=15, verbose_name='ID_SERVIDOR_CPF')),
                ('ID_SERVIDOR_PASEP', models.CharField(max_length=15, verbose_name='ID_SERVIDOR_PASEP')),
                ('CO_SEXO_SERVIDOR', models.IntegerField(verbose_name='CO_SEXO_SERVIDOR')),
                ('CO_ESTCIVIL_SERVIDOR', models.IntegerField(verbose_name='CO_ESTCIVIL_SERVIDOR')),
                ('DT_NASC_SERVIDOR', models.DateField(verbose_name='DT_NASC_SERVIDOR')),
                ('CO_SITUACAO_FUNCIONAL', models.IntegerField(verbose_name='CO_SITUACAO_FUNCIONAL')),
                ('CO_TIPO_VINCULO', models.IntegerField(verbose_name='CO_TIPO_VINCULO')),
                ('DT_ING_UNIAO', models.DateField(verbose_name='DT_ING_UNIAO')),
                ('IN_DEFICIENCIA', models.IntegerField(verbose_name='IN_DEFICIENCIA')),
                ('IN_EXP_NOCIVO', models.IntegerField(verbose_name='IN_EXP_NOCIVO')),
                ('IN_ABONO_PERMANENCIA', models.IntegerField(verbose_name='IN_ABONO_PERMANENCIA')),
                ('DT_INICIO_ABONO', models.DateField(verbose_name='DT_INICIO_ABONO')),
                ('IN_PREV_COMP', models.IntegerField(verbose_name='IN_PREV_COMP')),
                ('DT_ING_CARREIRA', models.DateField(verbose_name='DT_ING_CARREIRA')),
                ('NO_CARREIRA', models.IntegerField(verbose_name='NO_CARREIRA')),
                ('DT_ING_CARGO', models.DateField(verbose_name='DT_ING_CARGO')),
                ('NO_CARGO', models.CharField(max_length=100, verbose_name='NO_CARGO')),
                ('CO_CARGO', models.IntegerField(verbose_name='CO_CARGO')),
                ('CO_TIPO_CARGO', models.IntegerField(verbose_name='CO_TIPO_CARGO')),
                ('CO_ESCOLARIDADE', models.IntegerField(verbose_name='CO_ESCOLARIDADE')),
                ('VL_BASE_CALCULO', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='VL_BASE_CALCULO')),
                ('VL_REMUNERACAO', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='VL_REMUNERACAO')),
                ('VL_CONTRIBUICAO', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='VL_CONTRIBUICAO')),
                ('DT_INICIO_RGPS', models.DateField(verbose_name='DT_INICIO_RGPS')),
                ('DT_FIM_RGPS', models.DateField(verbose_name='DT_FIM_RGPS')),
                ('NU_TEMPO_RGPS', models.IntegerField(verbose_name='NU_TEMPO_RGPS')),
                ('DT_ING_SPUB', models.DateField(verbose_name='DT_ING_SPUB')),
                ('DT_FIM_SPUB', models.DateField(verbose_name='DT_FIM_SPUB')),
                ('NU_TEMPO_RPPS', models.IntegerField(verbose_name='NU_TEMPO_RPPS')),
                ('IN_BENEF_ESPECIAL', models.IntegerField(verbose_name='IN_BENEF_ESPECIAL')),
                ('DT_ADESAO_PREV_COMP', models.DateField(verbose_name='DT_ADESAO_PREV_COMP')),
                ('NU_TEMPO_CONTRIB_ADESAO', models.IntegerField(verbose_name='NU_TEMPO_CONTRIB_ADESAO')),
                ('NU_TEMPO_CONTRIB_TOTAL', models.IntegerField(verbose_name='NU_TEMPO_CONTRIB_TOTAL')),
                ('VL_BENEFICIO_ESPECIAL', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='VL_BENEFICIO_ESPECIAL')),
                ('VL_REMUNERACAO_1994', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='VL_REMUNERACAO_1994')),
                ('VL_REMUNERACAO_2003', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='VL_REMUNERACAO_2003')),
                ('VL_REMUNERACAO_2014', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='VL_REMUNERACAO_2014')),
                ('VL_REMUNERACAO_2019', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='VL_REMUNERACAO_2019')),
                ('BONUS_BEP', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='BONUS_BEP')),
                ('AUXILIO_SAUDE', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='AUXILIO_SAUDE')),
            ],
            options={
                'verbose_name': 'Servidor',
                'verbose_name_plural': 'Servidores',
                'db_table': 'servidores',
                'db_table_comment': 'Gerenciamento de Servidores',
                'indexes': [models.Index(fields=['NO_SERVIDOR'], name='servidores_NO_SERV_1976cd_idx')],
            },
        ),
    ]
