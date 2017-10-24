# __author: TungShine
# __date: 2017/10/23
# __description:

from django import template
from django.apps import apps
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag
def render_app_name(admin_class):
    return admin_class.model._meta.verbose_name


@register.simple_tag
def attr_name(admin_class, attr):
    # print(admin_class.model._meta.object_name)
    # print(admin_class.model._meta.fields)
    model_obj = apps.get_model(admin_class.model._meta.app_label, admin_class.model._meta.object_name)
    # print(model_obj._meta.fields)
    for field in model_obj._meta.fields:
        if attr == field.name:
            return field.verbose_name


@register.simple_tag
def get_query_sets(admin_class):
    return admin_class.model.objects.all()


@register.simple_tag
def build_table_row(obj, admin_class):
    row_ele = ""
    for column in admin_class.list_display:
        column_value = getattr(obj, column)  # 通过反射去对象的值
        row_ele += str(column_value).join(('<td>', '</td>'))
    return mark_safe(row_ele)
