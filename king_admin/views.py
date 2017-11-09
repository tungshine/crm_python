from django.shortcuts import render, redirect
from king_admin import king_admin
# import importlib
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from king_admin.utils import table_search, table_filter
from king_admin.forms import create_model_form


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

    # object_list = admin_class.model.objects.all()
    object_list, filter_conditions = table_filter(request, admin_class)
    object_list = table_search(request, admin_class, object_list)
    paginator = Paginator(object_list, admin_class.list_per_page)

    page = request.GET.get('page')
    try:
        query_sets = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        query_sets = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        query_sets = paginator.page(paginator.num_pages)
    return render(request, 'king_admin/table_obj.html',
                  {'admin_class': admin_class, 'query_sets': query_sets, 'search_value': request.GET.get('_q', '')})


def table_obj_change(request, app_name, table_name, obj_id):
    admin_class = king_admin.enabled_admins[app_name][table_name]
    model_form_class = create_model_form(request, admin_class)

    obj = admin_class.model.objects.get(id=obj_id)
    if request.method == "POST":
        form_obj = model_form_class(request.POST, instance=obj)  # 更新
        if form_obj.is_valid():
            form_obj.save()
        redirect_path = request.path.replace('/%s/change' % obj_id, '')
        return redirect(redirect_path)
    else:
        form_obj = model_form_class(instance=obj)
        return render(request, "king_admin/table_obj_change.html", {"form_obj": form_obj})


def table_obj_add(request, app_name, table_name):
    admin_class = king_admin.enabled_admins[app_name][table_name]
    model_form_class = create_model_form(request, admin_class)

    if request.method == "POST":
        form_obj = model_form_class(request.POST)  # 新增
        if form_obj.is_valid():
            form_obj.save()
        redirect_path = request.path.replace('/add', '')
        return redirect(redirect_path)
    else:
        form_obj = model_form_class()
        return render(request, "king_admin/table_obj_add.html", {"form_obj": form_obj})
