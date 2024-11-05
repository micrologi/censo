from django.db import models


class Servidor(models.Model):
    # ID - Não declarar coluna ID, deixar que o Django cria sozinho
    NU_ANO = models.IntegerField(verbose_name="NU_ANO", validators=[], blank=False)
    NU_MES = models.IntegerField(verbose_name="NU_MES", validators=[], blank=False)
    CO_COMP_MASSA = models.IntegerField(
        verbose_name="CO_COMP_MASSA", validators=[], blank=False
    )
    NU_CNPJ_ORGAO = models.CharField(
        verbose_name="NU_CNPJ_ORGAO", validators=[], blank=False, max_length=20
    )
    NO_ORGAO = models.IntegerField(verbose_name="NO_ORGAO", validators=[], blank=False)
    CO_PODER = models.IntegerField(verbose_name="CO_PODER", validators=[], blank=False)
    ID_SERVIDOR = models.IntegerField(
        verbose_name="ID_SERVIDOR", validators=[], blank=False
    )
    NO_SERVIDOR = models.CharField(
        verbose_name="NO_SERVIDOR", validators=[], blank=False, max_length=100
    )
    ID_SERVIDOR_MATRICULA = models.IntegerField(
        verbose_name="ID_SERVIDOR_MATRICULA", validators=[], blank=False
    )
    ID_SERVIDOR_CPF = models.CharField(
        verbose_name="ID_SERVIDOR_CPF", validators=[], blank=False, max_length=15
    )
    ID_SERVIDOR_PASEP = models.CharField(
        verbose_name="ID_SERVIDOR_PASEP", validators=[], blank=False, max_length=15
    )
    CO_SEXO_SERVIDOR = models.IntegerField(
        verbose_name="CO_SEXO_SERVIDOR", validators=[], blank=False
    )
    CO_ESTCIVIL_SERVIDOR = models.IntegerField(
        verbose_name="CO_ESTCIVIL_SERVIDOR", validators=[], blank=False
    )
    DT_NASC_SERVIDOR = models.DateField(
        verbose_name="DT_NASC_SERVIDOR", validators=[], blank=False
    )
    CO_SITUACAO_FUNCIONAL = models.IntegerField(
        verbose_name="CO_SITUACAO_FUNCIONAL", validators=[], blank=False
    )
    CO_TIPO_VINCULO = models.IntegerField(
        verbose_name="CO_TIPO_VINCULO", validators=[], blank=False
    )
    DT_ING_UNIAO = models.DateField(
        verbose_name="DT_ING_UNIAO", validators=[], blank=False
    )
    IN_DEFICIENCIA = models.IntegerField(
        verbose_name="IN_DEFICIENCIA", validators=[], blank=False
    )
    IN_EXP_NOCIVO = models.IntegerField(
        verbose_name="IN_EXP_NOCIVO", validators=[], blank=False
    )
    IN_ABONO_PERMANENCIA = models.IntegerField(
        verbose_name="IN_ABONO_PERMANENCIA", validators=[], blank=False
    )
    DT_INICIO_ABONO = models.DateField(
        verbose_name="DT_INICIO_ABONO", validators=[], blank=False
    )
    IN_PREV_COMP = models.IntegerField(
        verbose_name="IN_PREV_COMP", validators=[], blank=False
    )
    DT_ING_CARREIRA = models.DateField(
        verbose_name="DT_ING_CARREIRA", validators=[], blank=False
    )
    NO_CARREIRA = models.IntegerField(
        verbose_name="NO_CARREIRA", validators=[], blank=False
    )
    DT_ING_CARGO = models.DateField(
        verbose_name="DT_ING_CARGO", validators=[], blank=False
    )
    CO_TIPO_CARGO = models.IntegerField(
        verbose_name="CO_TIPO_CARGO", validators=[], blank=False
    )
    NO_CARGO = models.CharField(
        verbose_name="NO_CARGO", validators=[], blank=False, max_length=100
    )
    CO_CARGO = models.IntegerField(verbose_name="CO_CARGO", validators=[], blank=False)
    CO_TIPO_CARGO = models.IntegerField(
        verbose_name="CO_TIPO_CARGO", validators=[], blank=False
    )
    CO_ESCOLARIDADE = models.IntegerField(
        verbose_name="CO_ESCOLARIDADE", validators=[], blank=False
    )
    VL_BASE_CALCULO = models.DecimalField(
        verbose_name="VL_BASE_CALCULO",
        validators=[],
        blank=False,
        max_digits=10,
        decimal_places=2,
    )
    VL_REMUNERACAO = models.DecimalField(
        verbose_name="VL_REMUNERACAO",
        validators=[],
        blank=False,
        max_digits=10,
        decimal_places=2,
    )
    VL_CONTRIBUICAO = models.DecimalField(
        verbose_name="VL_CONTRIBUICAO",
        validators=[],
        blank=False,
        max_digits=10,
        decimal_places=2,
    )
    DT_INICIO_RGPS = models.DateField(
        verbose_name="DT_INICIO_RGPS", validators=[], blank=False
    )
    DT_FIM_RGPS = models.DateField(
        verbose_name="DT_FIM_RGPS", validators=[], blank=False
    )
    NU_TEMPO_RGPS = models.IntegerField(
        verbose_name="NU_TEMPO_RGPS", validators=[], blank=False
    )
    DT_ING_SPUB = models.DateField(
        verbose_name="DT_ING_SPUB", validators=[], blank=False
    )
    DT_FIM_SPUB = models.DateField(
        verbose_name="DT_FIM_SPUB", validators=[], blank=False
    )
    NU_TEMPO_RPPS = models.IntegerField(
        verbose_name="NU_TEMPO_RPPS", validators=[], blank=False
    )
    IN_BENEF_ESPECIAL = models.IntegerField(
        verbose_name="IN_BENEF_ESPECIAL", validators=[], blank=False
    )
    DT_ADESAO_PREV_COMP = models.DateField(
        verbose_name="DT_ADESAO_PREV_COMP", validators=[], blank=False
    )
    NU_TEMPO_CONTRIB_ADESAO = models.IntegerField(
        verbose_name="NU_TEMPO_CONTRIB_ADESAO", validators=[], blank=False
    )
    NU_TEMPO_CONTRIB_TOTAL = models.IntegerField(
        verbose_name="NU_TEMPO_CONTRIB_TOTAL", validators=[], blank=False
    )
    VL_BENEFICIO_ESPECIAL = models.DecimalField(
        verbose_name="VL_BENEFICIO_ESPECIAL",
        validators=[],
        blank=False,
        max_digits=10,
        decimal_places=2,
    )
    VL_REMUNERACAO_1994 = models.DecimalField(
        verbose_name="VL_REMUNERACAO_1994",
        validators=[],
        blank=False,
        max_digits=10,
        decimal_places=2,
    )
    VL_REMUNERACAO_2003 = models.DecimalField(
        verbose_name="VL_REMUNERACAO_2003",
        validators=[],
        blank=False,
        max_digits=10,
        decimal_places=2,
    )
    VL_REMUNERACAO_2014 = models.DecimalField(
        verbose_name="VL_REMUNERACAO_2014",
        validators=[],
        blank=False,
        max_digits=10,
        decimal_places=2,
    )
    VL_REMUNERACAO_2019 = models.DecimalField(
        verbose_name="VL_REMUNERACAO_2019",
        validators=[],
        blank=False,
        max_digits=10,
        decimal_places=2,
    )
    BONUS_BEP = models.DecimalField(
        verbose_name="BONUS_BEP",
        validators=[],
        blank=False,
        max_digits=10,
        decimal_places=2,
    )
    AUXILIO_SAUDE = models.DecimalField(
        verbose_name="AUXILIO_SAUDE",
        validators=[],
        blank=False,
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
