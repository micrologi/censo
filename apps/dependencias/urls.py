from django.urls import path
from django.contrib.auth.decorators import login_required

from apps.dependencias.models import Dependencia as Transaction
from apps.dependencias.transaction_list.views import TransactionListView
from apps.dependencias.transaction_add.views import TransactionAddView
from apps.dependencias.transaction_update.views import TransactionUpdateView
from apps.dependencias.transaction_delete.views import TransactionDeleteView

urlpatterns = [
    path(
        Transaction._meta.db_table + "/list/",
        login_required(
            TransactionListView.as_view(
                template_name=Transaction._meta.db_table + "_list.html"
            )
        ),
        name=Transaction._meta.db_table,
    ),
    path(
        Transaction._meta.db_table + "/add/",
        login_required(
            TransactionAddView.as_view(
                template_name=Transaction._meta.db_table + "_add.html"
            )
        ),
        name=Transaction._meta.db_table + "-add",
    ),
    path(
        Transaction._meta.db_table + "/update/<int:pk>",
        login_required(
            TransactionUpdateView.as_view(
                template_name=Transaction._meta.db_table + "_update.html"
            )
        ),
        name=Transaction._meta.db_table + "-update",
    ),
    path(
        Transaction._meta.db_table + "/delete/<int:pk>/",
        login_required(TransactionDeleteView.as_view()),
        name=Transaction._meta.db_table + "-delete",
    ),
]
