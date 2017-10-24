from django.shortcuts import render
from king_admin import king_admin
import importlib


# Create your views here.
def index(request):
    # king_admin.enabled_admins为自定义admin中的全局字典
    return render(request, 'king_admin/table_index.html', {'table_list': king_admin.enabled_admins})


def display_table_obj(request, app_name, table_name):
    """通过反射获取class的各种属性"""
    # print(app_name, table_name)

    # 通过字符串反射动态导入模块
    # importlib.import_module
    # importlib.import_module('crm')

    admin_class = king_admin.enabled_admins[app_name][table_name]

    # model_module = importlib.import_module('%s.models' % (app_name))
    # model_obj = getattr(model_module, table_name)
    # print(model_obj)

    return render(request, 'king_admin/table_obj.html', {'admin_class': admin_class})
