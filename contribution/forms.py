from django import forms

from .models import Contribution
from firm.models import Firm
from django_select2.forms import Select2Widget


class ContributionModelForm(forms.ModelForm):
    class Meta:
        model = Contribution
        fields =[
            'id_no',           
            'amount',
        ]
        
    def __init__(self, *args, **kwargs):
        super(ContributionModelForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.id:
            self.fields['id_no'].required = False
            self.fields['id_no'].widget.attrs['disabled'] = 'disabled'

class FirmAutocompleteForm(forms.ModelForm):
    qset=Firm.objects.all()
    choice_field=[]
    for item in qset:
         choice_field.append((item.firm_no,item.firm_name))
    firm_name = forms.ChoiceField(choices=choice_field, widget=Select2Widget)
    month = forms.ChoiceField(choices=[(1,'Jan'),(2,'Feb'),(3,'Mar'),(4,'Apr')], required=False, widget=Select2Widget)
    # first_name = forms.ModelChoiceField(
    #     queryset=Employee.objects.all(),
    #     widget=autocomplete.ModelSelect2(url='employee-autocomplete',
    #      attrs={'data-html': True})
    # )

    class Meta:
        model = Firm
        fields = ('firm_name','month')

       