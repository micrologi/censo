from django.db import models


class Sexo(models.Model):
    # ID - Não declarar coluna ID, deixar que o Django cria sozinho
    sexo = models.CharField(
        verbose_name="Sexo",
        max_length=15,
        db_index=True,
        default="",
        validators=[],
        blank=False,
        unique=True,
    )

    def __str__(self):
        return self.id

    class Meta:
        db_table = "sexos"
        verbose_name = "Sexo"
        verbose_name_plural = "Sexos"
        db_table_comment = "Sexo das pessoas"
        # indexes = [models.Index(fields=["nomeestado"])]
