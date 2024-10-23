from django.db import models


class Cargo(models.Model):
    # ID - Não declarar coluna ID, deixar que o Django cria sozinho
    cargo = models.CharField(
        verbose_name="Cargo",
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
        db_table = "cargos"
        verbose_name = "Cargo"
        verbose_name_plural = "Cargos"
        db_table_comment = "Cargos dos servidores"
        indexes = [models.Index(fields=["cargo"])]
