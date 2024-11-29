from django.db import models


class Servidor(models.Model):
    # ID - Não declarar coluna ID, deixar que o Django cria sozinho
    NU_ANO = models.IntegerField(verbose_name="Ano", validators=[], blank=True)
    NU_MES = models.IntegerField(verbose_name="Mês", validators=[], blank=True)
    CO_COMP_MASSA = models.IntegerField(
        verbose_name="CO_COMP_MASSA", validators=[], blank=True
    )
    NU_CNPJ_ORGAO = models.CharField(
        verbose_name="Cnpj Órgão", validators=[], blank=True, max_length=20
    )
    NO_ORGAO = models.IntegerField(verbose_name="Órgão", validators=[], blank=True)
    CO_PODER = models.IntegerField(verbose_name="Poder", validators=[], blank=True)
    ID_SERVIDOR = models.IntegerField(
        verbose_name="Id.Servidor", validators=[], blank=True
    )
    NO_SERVIDOR = models.CharField(
        verbose_name="Servidor", validators=[], blank=True, max_length=110
    )
    ID_SERVIDOR_MATRICULA = models.IntegerField(
        verbose_name="Matricula", validators=[], blank=True
    )
    ID_SERVIDOR_CPF = models.IntegerField(
        verbose_name="CPF", validators=[], blank=True, max_length=15
    )
    ID_SERVIDOR_PASEP = models.IntegerField(
        verbose_name="PASEP", validators=[], blank=True, max_length=15
    )
    CO_SEXO_SERVIDOR = models.IntegerField(
        verbose_name="Sexo", validators=[], blank=True
    )
    CO_ESTCIVIL_SERVIDOR = models.IntegerField(
        verbose_name="Estado Civil", validators=[], blank=True
    )
    DT_NASC_SERVIDOR = models.DateField(
        verbose_name="Dt.Nascimento", validators=[], blank=True
    )
    CO_SITUACAO_FUNCIONAL = models.IntegerField(
        verbose_name="Situação", validators=[], blank=True
    )
    CO_TIPO_VINCULO = models.IntegerField(
        verbose_name="Vínculo", validators=[], blank=True
    )
    DT_ING_UNIAO = models.DateField(verbose_name="Dt.União", validators=[], blank=True)
    IN_DEFICIENCIA = models.IntegerField(
        verbose_name="Deficiência", validators=[], blank=True
    )
    IN_EXP_NOCIVO = models.IntegerField(
        verbose_name="Exp.Nocivo", validators=[], blank=True
    )
    IN_ABONO_PERMANENCIA = models.IntegerField(
        verbose_name="Abono Permanência", validators=[], blank=True
    )
    DT_INICIO_ABONO = models.DateField(
        verbose_name="Dt.Inicio Abono", validators=[], blank=True
    )
    IN_PREV_COMP = models.IntegerField(
        verbose_name="IN_PREV_COMP", validators=[], blank=True
    )
    DT_ING_CARREIRA = models.DateField(
        verbose_name="DT_ING_CARREIRA", validators=[], blank=True
    )
    NO_CARREIRA = models.IntegerField(
        verbose_name="NO_CARREIRA", validators=[], blank=True
    )
    DT_ING_CARGO = models.DateField(
        verbose_name="DT_ING_CARGO", validators=[], blank=True
    )
    CO_TIPO_CARGO = models.IntegerField(
        verbose_name="CO_TIPO_CARGO", validators=[], blank=True
    )
    NO_CARGO = models.CharField(
        verbose_name="NO_CARGO", validators=[], blank=True, max_length=100
    )
    CO_CARGO = models.IntegerField(verbose_name="CO_CARGO", validators=[], blank=True)
    CO_TIPO_CARGO = models.IntegerField(
        verbose_name="CO_TIPO_CARGO", validators=[], blank=True
    )
    CO_ESCOLARIDADE = models.IntegerField(
        verbose_name="CO_ESCOLARIDADE", validators=[], blank=True
    )
    VL_BASE_CALCULO = models.DecimalField(
        verbose_name="VL_BASE_CALCULO",
        validators=[],
        blank=True,
        max_digits=10,
        decimal_places=2,
    )
    VL_REMUNERACAO = models.DecimalField(
        verbose_name="VL_REMUNERACAO",
        validators=[],
        blank=True,
        max_digits=10,
        decimal_places=2,
    )
    VL_CONTRIBUICAO = models.DecimalField(
        verbose_name="VL_CONTRIBUICAO",
        validators=[],
        blank=True,
        max_digits=10,
        decimal_places=2,
    )
    DT_INICIO_RGPS = models.DateField(
        verbose_name="DT_INICIO_RGPS", validators=[], blank=True
    )
    DT_FIM_RGPS = models.DateField(
        verbose_name="DT_FIM_RGPS", validators=[], blank=True
    )
    NU_TEMPO_RGPS = models.IntegerField(
        verbose_name="NU_TEMPO_RGPS", validators=[], blank=True
    )
    DT_ING_SPUB = models.DateField(
        verbose_name="DT_ING_SPUB", validators=[], blank=True
    )
    DT_FIM_SPUB = models.DateField(
        verbose_name="DT_FIM_SPUB", validators=[], blank=True
    )
    NU_TEMPO_RPPS = models.IntegerField(
        verbose_name="NU_TEMPO_RPPS", validators=[], blank=True
    )
    IN_BENEF_ESPECIAL = models.IntegerField(
        verbose_name="IN_BENEF_ESPECIAL", validators=[], blank=True
    )
    DT_ADESAO_PREV_COMP = models.DateField(
        verbose_name="DT_ADESAO_PREV_COMP", validators=[], blank=True
    )
    NU_TEMPO_CONTRIB_ADESAO = models.IntegerField(
        verbose_name="NU_TEMPO_CONTRIB_ADESAO", validators=[], blank=True
    )
    NU_TEMPO_CONTRIB_TOTAL = models.IntegerField(
        verbose_name="NU_TEMPO_CONTRIB_TOTAL", validators=[], blank=True
    )
    VL_BENEFICIO_ESPECIAL = models.DecimalField(
        verbose_name="VL_BENEFICIO_ESPECIAL",
        validators=[],
        blank=True,
        max_digits=10,
        decimal_places=2,
    )
    VL_REMUNERACAO_1994 = models.DecimalField(
        verbose_name="VL_REMUNERACAO_1994",
        validators=[],
        blank=True,
        max_digits=10,
        decimal_places=2,
    )
    VL_REMUNERACAO_2003 = models.DecimalField(
        verbose_name="VL_REMUNERACAO_2003",
        validators=[],
        blank=True,
        max_digits=10,
        decimal_places=2,
    )
    VL_REMUNERACAO_2014 = models.DecimalField(
        verbose_name="VL_REMUNERACAO_2014",
        validators=[],
        blank=True,
        max_digits=10,
        decimal_places=2,
    )
    VL_REMUNERACAO_2019 = models.DecimalField(
        verbose_name="VL_REMUNERACAO_2019",
        validators=[],
        blank=True,
        max_digits=10,
        decimal_places=2,
    )
    BONUS_BEP = models.DecimalField(
        verbose_name="BONUS_BEP",
        validators=[],
        blank=True,
        max_digits=10,
        decimal_places=2,
    )
    AUXILIO_SAUDE = models.DecimalField(
        verbose_name="AUXILIO_SAUDE",
        validators=[],
        blank=True,
        max_digits=10,
        decimal_places=2,
    )

    def __str__(self):
        return self.id

    class Meta:
        db_table = "servidores"
        verbose_name = "Servidor"
        verbose_name_plural = "Servidores"
        db_table_comment = "Gerenciamento de Servidores"
        indexes = [models.Index(fields=["NO_SERVIDOR"])]
