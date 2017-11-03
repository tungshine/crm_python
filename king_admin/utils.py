# __author: TungShine
# __date: 2017/11/3
# __description:
from django.db.models import Q


def table_filter(request, admin_class):
    """进行条件过滤并返回过滤后的数据"""
    filter_conditions = {}
    keywords = ['page', 'o', '_q']
    for k, v in request.GET.items():
        if k in keywords:  # 保留的分页关键字 and 排序关键字
            continue
        if v:
            filter_conditions[k] = v
    print("filter coditions", filter_conditions)

    return admin_class.model.objects.filter(**filter_conditions).order_by(
        "-%s" % admin_class.ordering if admin_class.ordering else   "-id"), filter_conditions


def table_search(request, admin_class, object_list):
    """页面搜索框"""
    search_value = request.GET.get("_q", "")
    q_obj = Q()
    q_obj.connector = "OR"
    for column in admin_class.search_fields:
        query_column = '%s__contains' % column
        q_obj.children.append((query_column, search_value))
    res = object_list.filter(q_obj)
    return res
