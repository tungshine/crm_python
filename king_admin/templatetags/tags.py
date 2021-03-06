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
    # django通过app模块获取object
    model_obj = apps.get_model(admin_class.model._meta.app_label, admin_class.model._meta.object_name)
    # print(model_obj._meta.fields)
    for field in model_obj._meta.fields:
        if attr == field.name:
            return field.verbose_name


@register.simple_tag
def get_query_sets(admin_class):
    return admin_class.model.objects.all()


@register.simple_tag
def build_table_row(request, obj, admin_class):
    row_ele = ""
    for index, column in enumerate(admin_class.list_display):
        # field_obj = obj._meta.get_field(column)  # 获取obj(Customer)对象中属性的对象

        column_value = getattr(obj, column)  # 通过反射去对象的值

        if type(column_value).__name__ == 'datetime':  # 判断字段类型
            column_value = column_value.strftime('%Y-%m-%d %H:%M:%S')

        if index == 0:
            column_value = '<a href="{path}/{obj_id}/change">{column_value}</a>'.format(path=request.path,
                                                                                        obj_id=obj.id,
                                                                                        column_value=column_value)
        row_ele += str(column_value).join(('<td>', '</td>'))
    return mark_safe(row_ele)


@register.simple_tag()
def render_page_ele(loop_counter, query_sets):
    current_page = query_sets.number
    total_page = query_sets.paginator.num_pages
    # print(current_page, loop_counter)
    if loop_counter < 3 or loop_counter > total_page - 2:  # 前2页or最后2页
        ele_class = ''
        if query_sets.number == loop_counter:
            ele_class = 'active'
        ele = '''<li class="%s"><a href="?page=%s">%s</a></li>''' % (ele_class, loop_counter, loop_counter)
        return mark_safe(ele)
    if abs(current_page - loop_counter) <= 1:
        ele_class = ""
        if current_page == loop_counter:
            ele_class = "active"
        ele = '''<li class="%s"><a href="?page=%s">%s</a></li>''' % (ele_class, loop_counter, loop_counter)
        return mark_safe(ele)
    else:
        return mark_safe('<li>...</li>')
    return ''


@register.simple_tag
def build_paginators(query_sets, search_value):
    """返回整个分页元素"""
    page_btns = ''
    added_dot_ele = False
    for page_num in query_sets.paginator.page_range:
        if page_num < 3 or page_num > query_sets.paginator.num_pages - 2 \
                or abs(query_sets.number - page_num) <= 2:  # 代表最前2页或最后2页 #abs判断前后1页
            ele_class = ""
            if query_sets.number == page_num:
                added_dot_ele = False
                ele_class = "active"
            page_btns += '''<li class="%s"><a href="?page=%s&_q=%s">%s</a></li>''' % (
                ele_class, page_num, search_value, page_num)
        # elif abs(query_sets.number - page_num) <= 1: #判断前后1页
        #     ele_class = ""
        #     if query_sets.number == page_num:
        #         added_dot_ele = False
        #         ele_class = "active"
        #     page_btns += '''<li class="%s"><a href="?page=%s%s">%s</a></li>''' % (
        #     ele_class, page_num, filters, page_num)
        else:  # 显示...
            if added_dot_ele == False:  # 现在还没加...
                page_btns += '<li><a>...</a></li>'
                added_dot_ele = True

    return mark_safe(page_btns)


@register.simple_tag
def create_field(field, form_obj):
    pass
    # form_obj._meta.model
    # print(field)


@register.simple_tag
def get_model_name(admin_class):
    model_name = admin_class.model._meta.verbose_name
    return model_name


@register.simple_tag
def build_operate_column(request, obj):
    column_ele = '<td><a href="{path}/{id}/change"><li class="fa-edit"></li></a>' \
                 '<a href="{path}/{id}/delete"><li class="fa-trash"></li></a></td>'.format(path=request.path,
                                                                                           id=obj.id)
    return mark_safe(column_ele)
