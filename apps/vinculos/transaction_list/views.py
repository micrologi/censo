from django.views.generic import TemplateView
from web_project.template_helpers.theme import TemplateHelper
from web_project import TemplateLayout

from apps.vinculos.models import Vinculo as Transaction


class TransactionListView(TemplateView):

    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        transactions = self.get_annotated_transactions()
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

    def get_annotated_transactions(self):
        # Get all transactions and order them by ID
        first_field = Transaction._meta.get_fields(
            include_parents=False, include_hidden=False
        )
        return Transaction.objects.all().order_by(first_field[0].name)
