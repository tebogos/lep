from django import forms

from .models import Firm


class FirmModelForm(forms.ModelForm):
    class Meta:
        model = Firm
        fields =[
            'firm_name',
            'firm_no',
            'firm_contact',
            'firm_email',

        ]