from django.db import models


class Upload(models.Model):
    excel_file = models.FileField()
    excel_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id

    class Meta:
        db_table = "uploads"
        verbose_name = "Upload"
        verbose_name_plural = "Uploads"
        db_table_comment = "Envio de Arquivos"
        # indexes = [models.Index(fields=["nomeestado"])]
