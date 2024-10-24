from django.db import models


class EstadoCivil(models.Model):
    # ID - Não declarar coluna ID, deixar que o Django cria sozinho
    estadocivil = models.CharField(
        verbose_name="Estado Civil",
        max_length=30,
        db_index=True,
        default="",
        validators=[],
        blank=False,
        unique=True,  # Se esse valor não pode duplicar na database, setar como True
    )

    def __str__(self):
        return self.id

    class Meta:
        db_table = "estadoscivis"
        verbose_name = "EstadoCivil"
        verbose_name_plural = "EstadosCivis"
        db_table_comment = "Estado Civil das pessoas"
        # indexes = [models.Index(fields=["nomeestado"])]
