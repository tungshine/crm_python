from django.contrib import admin
from crm import models


# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'creator')
    # list_filter = ('source', 'consultant', 'data')
    search_fields = ('first_name',)
    # filter_horizontal = ('tags')
    # list_editable = ('status')
    list_per_page = 5
    pass


admin.site.register(models.User)
admin.site.register(models.Role)
admin.site.register(models.Company)
admin.site.register(models.Customer, CustomerAdmin)
admin.site.register(models.Menu)
