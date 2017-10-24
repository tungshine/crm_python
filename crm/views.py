from django.shortcuts import render
from crm.models import Customer


# Create your views here.
def index(request):
    return render(request, 'index.html', {"msg": 'index'})


def customers(request):
    customer_set = Customer.objects.all()
    return render(request, 'customer/customer-list.html', {"customers": customer_set})


def add_customer(request):
    Customer(request.POST)
    pass


def roles(request):
    return render(request, 'role/role-list.html', )
