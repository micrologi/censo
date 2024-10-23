from django.db import models


class Cidade(models.Model):
    nomecidade = models.CharField(
        verbose_name="Cidade",
        max_length=65,
        db_index=True,
        default="",
        validators=[],
        blank=False,
        unique=True,
    )

    def __str__(self):
        return self.id

    class Meta:
        db_table = "cidades"
        verbose_name = "Cidade"
        verbose_name_plural = "Cidades"
        db_table_comment = "Cidades do brasil"
        indexes = [models.Index(fields=["nomecidade"])]
