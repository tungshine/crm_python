from django.test import TestCase


# Create your tests here.


class Customer():
    """客户表"""
    first_name = ''
    last_name = ''

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return self.first_name + self.last_name

    class Meta:
        verbose_name = "客户表"
        verbose_name_plural = "客户表"


print(getattr(Customer, 'first_name'))
column_value = '唐'
s = column_value.join(['<td>', '</td>'])
print(s)
