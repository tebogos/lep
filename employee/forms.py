from django import forms

from .models import Employee
from firm.models import Firm
# from dal import autocomplete
from django_select2.forms import Select2MultipleWidget


class EmployeeModelForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields =[
            'first_name',
            'last_name',
            'id_no',
            'firm_no',
            'firm_email',
            'account_number',
            'bank',
            # 'get_full_name'
        ]

        # def get_full_name(self,obj,*arg,**kwarg):
        #     return str(obj.first_name+''+obj.last_name)
        
class EmployeeAutocompleteForm(forms.ModelForm):
    first_name = forms.ModelMultipleChoiceField(queryset=Employee.objects.all(), widget=Select2MultipleWidget)
    # first_name = forms.ModelChoiceField(
    #     queryset=Employee.objects.all(),
    #     widget=autocomplete.ModelSelect2(url='employee-autocomplete',
    #      attrs={'data-html': True})
    # )

    class Meta:
        model = Employee
        fields = ('__all__')

