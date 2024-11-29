from django.contrib import admin

from .models import Upload as Transaction


# Register your models here.
class TransactionAdmin(admin.ModelAdmin):

    list_display = []
    list_filter = []
    search_fields = []
    ordering = []
    for field in Transaction._meta.get_fields():
        list_display.append(field.name)
        list_filter.append(field.name)
        search_fields.append(field.name)
        ordering.append(field.name)

    list_per_page = 10


admin.site.register(Transaction, TransactionAdmin)
