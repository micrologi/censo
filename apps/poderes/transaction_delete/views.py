from django.shortcuts import redirect, get_object_or_404
from django.views.generic import DeleteView
from django.contrib import messages
from django.contrib.auth.mixins import PermissionRequiredMixin

from apps.poderes.models import Poder as Transaction


class TransactionDeleteView(PermissionRequiredMixin, DeleteView):

    permission_required = Transaction._meta.db_table + ".delete_transaction"

    def get(self, request, pk):
        transaction = get_object_or_404(Transaction, id=pk)
        transaction.delete()
        messages.success(request, "Registro deletado")
        return redirect(Transaction._meta.db_table)
