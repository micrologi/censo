from django.urls import path
from django.contrib.auth.decorators import login_required

from apps.uploads.models import Upload as Transaction
from apps.uploads.formupload.views import FormUpload

urlpatterns = [
    path(
        Transaction._meta.db_table + "/fileupload/",
        login_required(
            FormUpload.as_view(
                template_name=Transaction._meta.db_table + "_fileupload.html"
            )
        ),
        name=Transaction._meta.db_table,
    ),
]
