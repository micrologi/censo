from django.urls import path
from django.contrib.auth.decorators import login_required

from apps.estados.models import Estado as Transaction
from apps.estados.transaction_list.views import TransactionListView
from apps.estados.transaction_add.views import TransactionAddView
from apps.estados.transaction_update.views import TransactionUpdateView
from apps.estados.transaction_delete.views import TransactionDeleteView

urlpatterns = [
    path(
        Transaction.tableName() + "/list/",
        login_required(
            TransactionListView.as_view(
                template_name=Transaction.tableName() + "_list.html"
            )
        ),
        name=Transaction.tableName(),
    ),
    path(
        Transaction.tableName() + "/add/",
        login_required(
            TransactionAddView.as_view(template_name="transactions_add.html")
        ),
        name=Transaction.tableName() + "-add",
    ),
    path(
        Transaction.tableName() + "/update/<int:pk>",
        login_required(
            TransactionUpdateView.as_view(template_name="transactions_update.html")
        ),
        name=Transaction.tableName() + "-update",
    ),
    path(
        Transaction.tableName() + "/delete/<int:pk>/",
        login_required(TransactionDeleteView.as_view()),
        name=Transaction.tableName() + "-delete",
    ),
]
