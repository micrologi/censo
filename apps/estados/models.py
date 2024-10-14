from django.db import models


class Estado(models.Model):
    # ID - Não declarar coluna ID, deixar que o Django cria sozinho
    sigla = models.CharField(
        verbose_name="Sigla", max_length=2, db_index=True, default="SP", blank=False
    )
    nome_estado = models.CharField(
        verbose_name="Estado",
        max_length=50,
        db_index=True,
        default="",
        blank=False,
    )

    def moduleName():
        return "Estados"

    def tableName():
        return "estados"

    def __str__(self):
        return self.id
