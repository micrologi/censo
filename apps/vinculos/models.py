from django.db import models


class Vinculo(models.Model):
    # ID - Não declarar coluna ID, deixar que o Django cria sozinho
    vinculo = models.CharField(
        verbose_name="Vinculo",
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
        db_table = "vinculos"
        verbose_name = "Vinculo"
        verbose_name_plural = "Vinculos"
        db_table_comment = "Gerenciamento"
        indexes = [models.Index(fields=["vinculo"])]
