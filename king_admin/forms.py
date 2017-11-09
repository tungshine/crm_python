# __author: TungShine
# __date: 2017/11/8
# __description:
from django.forms import ModelForm

from crm import models


class CustomerModelForm(ModelForm):
    class Meta:
        model = models.Customer
        fields = "__all__"


def create_model_form(request, admin_class):
    """动态生成MODEL FORM"""

    def __new__(cls, *args, **kwargs):
        for field_name, field_obj in cls.base_fields.items():
            field_obj.widget.attrs['class'] = 'form-control'
        return ModelForm.__new__(cls)

    class Meta:
        model = admin_class.model
        fields = "__all__"

    attrs = {'Meta': Meta}

    _model_form_class = type('%sModelForm' % (admin_class.model._meta.object_name), (ModelForm,), attrs)
    setattr(_model_form_class, '__new__', __new__)

    # print('%sModelForm' % (admin_class.model._meta.object_name))
    # setattr(_model_form_class, 'Meta', Meta)
    # print('model form', _model_form_class.Meta.model)
    return _model_form_class
