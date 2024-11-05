from django.shortcuts import redirect
from django.contrib import messages
from django.views.generic import TemplateView
from web_project.template_helpers.theme import TemplateHelper
from web_project import TemplateLayout
from django.contrib.auth.mixins import PermissionRequiredMixin

from apps.servidores.forms import TransactionForm
from apps.servidores.models import Servidor as Transaction


class TransactionAddView(PermissionRequiredMixin, TemplateView):
    permission_required = Transaction._meta.db_table + ".add_transaction"

    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        fields = Transaction._meta.get_fields()

        # Workaround pois preciso do nome com hifén no template
        for field in fields:
            field.attname = field.attname.replace("_", "-")

        # Update the context
        context.update(
            {
                "fields": fields,
                "transactions_count": Transaction.objects.count(),
            }
        )
        TemplateHelper.map_context(context)

        return context

    # Post - Adiciona os dados
    def post(self, request):
        try:
            form = TransactionForm(request.POST)

            if form.is_valid():
                form.save()
                messages.success(request, "Registro adicionado com sucesso")
            else:
                messages.error(request, form.errors)

        except BaseException as e:
            messages.error(request, "Erro: " + str(e))

        return redirect(Transaction._meta.db_table)

    def exist_record(self, cleaned_data):
        fields = Transaction._meta.get_fields()

        filter_dic = []
        for field in fields:
            if field.attname == "id":
                continue
            filter_dic.append([field.attname, cleaned_data[field.attname]])

        filter_dic = dict(filter_dic)

        return Transaction.objects.filter(**filter_dic).exists()
