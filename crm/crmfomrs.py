# __author: TungShine
# __date: 2017/10/26
# __description:

from django import forms
from django.forms import fields
from django.forms import widgets


class CustomerForm(forms.Form):
    first_name = fields.CharField(widget=widgets.TextInput(attrs={'placeholder': '姓', 'class': 'form-control'}))
    last_name = fields.CharField(widget=widgets.TextInput(attrs={'placeholder': '名', 'class': 'form-control'}))
    address = fields.CharField(
        widget=widgets.Textarea(attrs={'placeholder': '地址', 'class': 'form-control limitTextarea'}))
    head_url = fields.CharField(widget=widgets.TextInput(attrs={'placeholder': '头像地址', 'class': 'form-control'}))
    company = fields.ChoiceField(choices=[(1, '十分联创'), (2, '阿里巴巴'), (3, '腾讯科技'), ],
                                 widget=widgets.Select(attrs={'class': 'form-control'}))

    # create_time = fields.DateTimeField(verbose_name="创建时间", null=True, auto_now_add=True)
    # creator = fields.ForeignKey("User", related_name="creator", verbose_name="创建者", default=1)
    # modify_time = fields.DateTimeField(verbose_name="修改时间", null=True, auto_now=True)
    # modifier = fields.ForeignKey("User", related_name="modifier", verbose_name="修改者", default=1)
    # company = fields.ForeignKey("Company", verbose_name="单位名称", default=1)
