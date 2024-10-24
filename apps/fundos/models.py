from django.db import models


class Fundo(models.Model):
    # ID - Não declarar coluna ID, deixar que o Django cria sozinho
    fundo = models.CharField(
        verbose_name="Fundo",
        max_length=100,
        db_index=True,
        default="",
        validators=[],
        blank=False,
        unique=True,
    )

    def __str__(self):
        return self.id

    class Meta:
        db_table = "fundos"
        verbose_name = "Fundo"
        verbose_name_plural = "Fundos"
        db_table_comment = "Fundos"
        # indexes = [models.Index(fields=["nomeestado"])]
