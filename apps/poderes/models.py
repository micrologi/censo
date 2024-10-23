from django.db import models


class Poder(models.Model):
    poder = models.CharField(
        verbose_name="Poder",
        max_length=30,
        db_index=True,
        default="",
        validators=[],
        blank=False,
        unique=True,
    )

    def __str__(self):
        return self.id

    class Meta:
        db_table = "poderes"
        verbose_name = "Poder"
        verbose_name_plural = "Poderes"
        db_table_comment = "Poderes"
        indexes = [models.Index(fields=["poder"])]
