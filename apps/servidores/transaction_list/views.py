from django.views.generic import TemplateView
from apps.servidores.models import Servidor as Transaction
from django.core import serializers
from web_project.template_helpers.theme import TemplateHelper
from web_project import TemplateLayout


class TransactionListView(TemplateView):

    def get_data():
        queryset = Transaction.objects.all()
        columns = ["id", "NU_ANO", "NU_MES", "NO_ORGAO"]

        print(serializers.serialize("json", queryset))

        return serializers.serialize("json", queryset)

    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))

        transactions = self.get_annotated_transactions(5)
        fields = Transaction._meta.get_fields()

        # Monta a lista de informações dinamicamente
        records = []
        iCont = 0
        for transaction in transactions:
            records.append([iCont, [[], []]])
            for field in fields:

                attname = field.attname
                records[iCont][1][0].append(transaction.__dict__[attname])
                records[iCont][1][1].append(field.get_internal_type())
            iCont += 1

        # Zipa as 2 listas para poder manipular no template
        for iCont in range(len(records)):
            records[iCont][0] = records[iCont][1][0][
                0
            ]  # Capturo o ID para acessar facilmente no template
            records[iCont][1] = zip(records[iCont][1][0], records[iCont][1][1])

        # Update the context
        context.update(
            {
                "records": records,
                "fields": fields,
                "transactions_count": Transaction.objects.count(),
                "verbose_name_plural": Transaction._meta.verbose_name_plural,
                "db_table": Transaction._meta.db_table,
            }
        )
        TemplateHelper.map_context(context)
        return context

    def get_annotated_transactions(self, num_records):

        # sql_result = Transaction.objects.all().order_by("-id")[0:num_records]
        sql_result = Transaction.objects.all().order_by("-id")

        return sql_result
