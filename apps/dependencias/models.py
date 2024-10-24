from django.db import models


class Dependencia(models.Model):
    # ID - Não declarar coluna ID, deixar que o Django cria sozinho
    dependencia = models.CharField(
        verbose_name="Dependência",
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
        db_table = "dependencias"
        verbose_name = "Dependencia"
        verbose_name_plural = "Dependecias"
        db_table_comment = "Tipos de Dependências"
        # indexes = [models.Index(fields=["nomeestado"])]
