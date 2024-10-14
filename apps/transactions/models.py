from django.db import models
from datetime import date
from django.core.validators import EmailValidator

class Transaction(models.Model):

    empresa = models.CharField(verbose_name="Empresa", max_length=50, db_index=True,default="",blank=False)
    atividades = models.CharField(verbose_name="Atividades", max_length=100, db_index=False,default="",blank=False)
    requisitos = models.CharField(verbose_name="Requisitos", max_length=100, db_index=False,default="",blank=False)

    email_validator = EmailValidator("Informe um endereço de e-mail correto!")
    email = models.EmailField(verbose_name="E-mail", max_length=150, db_index=True,default="",blank=False,validators=[email_validator])

    area = models.IntegerField(verbose_name="Área",
        choices=[
                    (1, "Administração e gestão"),
                    (2, "Alimentos e bebidas"),
                    (3, "Construção civil e design"),
                    (4, "Moda Têxtil, calçados e joalheria"),
                    (5, "Papel, celulose, gráfica, editorial"),
                    (6, "Mecânica industrial"),
                    (7, "Logistica e transporte"),
                    (8, "Automotiva"),
                    (9, "Mecâtronica, automação e energia"),
                    (10, "Meio ambiente, saúde e segurança do trabalho"),
                    (11, "Metalurgia e soldagem"),
                    (12, "Química cerâmica e plásticos"),
                    (13, "Refrigeração e climatização"),
                    (14, "Tecnologia da informação"),
                    (15, "Outras")
                ],default=15
    )
    salario = models.DecimalField(verbose_name="Salário", max_digits=10, decimal_places=2, default=0)
    aprovada = models.BooleanField(verbose_name="Aprovada",default=False)

    def tableName():
        return "transactions"

    def __str__(self):
        return self.id
