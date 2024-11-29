from django.shortcuts import redirect
from django.contrib import messages
from django.views.generic import TemplateView
from web_project.template_helpers.theme import TemplateHelper
from web_project import TemplateLayout

from apps.uploads.models import Upload as Transaction


class FormUpload(TemplateView):

    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))

        TemplateHelper.map_context(context)
        return context

    # Post - Processa arquivo enviado

    def post(self, request):
        try:

            if request.method == "POST":
                print("Aqui o arquivo: ")
                print(request)
                print(request.FILES["excel"])

            messages.success(request, "Planilha importada com sucesso!")

        except BaseException as e:
            messages.error(request, "Erro: " + str(e))

        return redirect(Transaction._meta.db_table)

    def get_annotated_transactions(self):
        # Get all transactions and order them by ID
        first_field = Transaction._meta.get_fields(
            include_parents=False, include_hidden=False
        )
        return Transaction.objects.all().order_by(first_field[0].name)
