from django.db import models


class <<model>>(models.Model):
    # ID - Não declarar coluna ID, deixar que o Django cria sozinho
    sigla = models.CharField(
        verbose_name="Sigla",
        max_length=2,
        db_index=True,
        default="",
        validators=[],
        blank=False,
        unique=True,  # Se esse valor não pode duplicar na database, setar como True
    )
    nomeestado = models.CharField(
        verbose_name="Estado",
        max_length=50,
        db_index=True,
        default="",
        validators=[],
        blank=False,
        unique=True,
    )

    def __str__(self):
        return self.id

    class Meta:
        db_table = "<<crud>>"
        verbose_name = "<<model>>"
        verbose_name_plural = "<<module>>"
        db_table_comment = "Gerenciamento"
        #indexes = [models.Index(fields=["nomeestado"])]
