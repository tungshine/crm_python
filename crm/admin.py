from django.contrib import admin
from crm import models


# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'creator')
    # list_filter = ('source', 'consultant', 'data')
    # search_fields = ('consultant')
    # filter_horizontal = ('tags')
    # list_editable = ('status')
    pass


admin.site.register(models.User)
admin.site.register(models.Role)
admin.site.register(models.Company)
admin.site.register(models.Customer, CustomerAdmin)
admin.site.register(models.Menu)
