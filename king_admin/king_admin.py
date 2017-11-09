# __author: TungShine
# __date: 2017/10/23
# __description:

from crm import models

enabled_admins = {}


class BaseAdmin(object):
    list_display = []
    list_filters = []
    search_fields = []
    list_per_page = 10
    ordering = None


class UserAdmin(BaseAdmin):
    list_display = ['name', 'head_url']


class CustomerAdmin(BaseAdmin):
    list_display = ['id', 'first_name', 'last_name', 'address', 'creator', 'create_time']
    list_filters = ['id', 'first_name', 'last_name', 'address']
    search_fields = ['first_name', 'last_name', 'address', 'creator__name']


def register(model_class, admin_class=None):
    """仿写django自带admin模块，model_class就是我们
    需要管理的Model类，admin_class就是自定义定制显示的类"""

    # 1. 获取app名字, 通过反射获取当前model_class的app名字
    app_name = model_class._meta.app_label
    # 2. 判断全局字典中是否存在该key对应的字典，没有就在全局字典中添加
    if app_name not in enabled_admins:
        enabled_admins[app_name] = {}

    # 3. 获取model_class的model_name
    model_name = model_class._meta.model_name

    # 4. 给admin_class绑定值为model_class对象的model属性
    admin_class.model = model_class
    enabled_admins[app_name][model_name] = admin_class


register(models.User, UserAdmin)
register(models.Customer, CustomerAdmin)
