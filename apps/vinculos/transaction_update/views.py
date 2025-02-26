from django.shortcuts import redirect
from django.contrib import messages
from django.views.generic import TemplateView
from web_project import TemplateLayout
from django.contrib.auth.mixins import PermissionRequiredMixin

from apps.vinculos.forms import TransactionForm
from apps.vinculos.models import Vinculo as Transaction


class TransactionUpdateView(PermissionRequiredMixin, TemplateView):
    permission_required = Transaction._meta.db_table + ".update_transaction"

    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        fields = Transaction._meta.get_fields()
        transaction = self.get_transaction(self.kwargs["pk"])

        values = []

        for field in fields:
            values.append(
                [
                    field.name,
                    field.attname,
                    field.verbose_name,
                    field.get_internal_type(),
                    field.choices,
                    field.max_length,
                    transaction.__dict__[field.attname],
                    field.blank,
                ]
            )

        context["transaction"] = transaction
        context["values"] = values

        return context

    def post(self, request, pk):
        transaction = self.get_transaction(pk)
        form = TransactionForm(request.POST, instance=transaction)

        if form.is_valid():

            if not self.transaction_exists(form.cleaned_data, transaction):
                form.save()
                messages.success(request, "Registro atualizado")
                return redirect(Transaction._meta.db_table)
            else:
                messages.error(request, "Um registro semelhante já existe")

        else:
            messages.error(request, form.errors)

        return redirect(Transaction._meta.db_table)

    def get_transaction(self, pk):
        return Transaction.objects.get(pk=pk)

    def transaction_exists(self, cleaned_data, current_transaction):
        return False

        """
        matching_transactions = Transaction.objects.filter(
            Q(customer__iexact=cleaned_data["customer"])
            & Q(transaction_date=cleaned_data["transaction_date"])
            & Q(due_date=cleaned_data["due_date"])
            & Q(total=cleaned_data["total"])
            & Q(status=cleaned_data["status"])
        ).exclude(pk=current_transaction.pk)
        return matching_transactions.exists()
        """
