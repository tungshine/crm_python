from django.shortcuts import render
from crm.models import Customer
from django.core.paginator import Paginator
from django.db.models import Q


# Create your views here.
def index(request):
    return render(request, 'index.html', {"msg": 'index'})


def customers(request):
    customer_set = Customer.objects.all()
    # page = Paginator()
    # search_value = request.GET.get('_q', "")
    # q = Q()
    # q.connector = 'OR'
    return render(request, 'customer/customer-list.html', {"customers": customer_set})


def add_customer(request):
    from crm import crmforms
    customer = crmforms.CustomerForm()
    return render(request, 'customer/customer-add.html', {'customer': customer})


def roles(request):
    return render(request, 'role/role-list.html', )
