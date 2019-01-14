from django.shortcuts import render,redirect
import json
from django.utils import timezone
import datetime
from django.forms import formset_factory, modelformset_factory
from .forms import ContributionModelForm,FirmAutocompleteForm
from .models import Contribution
from employee.models import Employee
from firm.models import Firm
from firm.forms import FirmModelForm
from django.http import JsonResponse
from django.views.generic import( CreateView,
ListView,
DetailView,
UpdateView
)
from django.http import HttpResponse,HttpResponseRedirect


class FirmAutocomplete(CreateView):
   model = Firm
   form_class=FirmAutocompleteForm
#    template_name_suffix = '_select_firm_form'  
   template_name = "contribution/select_firm_form.html"
#    success_url = "contribution/foreset_firm_form.html"
   def form_valid(self, form):
        obj=form.save(commit=False)
        month = form.cleaned_data['month']
        print('firm_name --->>>>>',month)
        return HttpResponseRedirect('/contribution/formset/?firm_name={firm_name}&month={month}'.format(firm_name=obj.firm_name,month=month))

def firm_choice(request):
    print(dir(request))
    print(request.get_full_path())

    return render(request,'contribution/select_firm_form.html',{})


   
    
   


def formset_view(request):
        
        form_init=[]
       
        req_firm_no= request.GET.get('firm_name', None)
        req_month=request.GET.get('month', None)
        print('req_firm_no --->>',req_firm_no)
        for emp in Employee.objects.filter(firm_no__firm_no__exact=req_firm_no):
            print('emp---> ',getattr(emp,'id_no'))
            form_init.append({
                'id_no':emp,
                'month':req_month,
                'firm_no':req_firm_no         

            })
            serial_form_init=[]
            for itm in form_init:
                serial_form_init.append({
                    'id_no':getattr(itm['id_no'],'id_no'),
                    'month':itm['month'],
                    'firm_no':itm['firm_no'] 

                })
                
            request.session['serial_form_init'] = serial_form_init
        ContricutionFormSet =  modelformset_factory(Contribution,form=ContributionModelForm, extra=Employee.objects.filter(firm_no__firm_no__exact=req_firm_no).count())
        print('form_init <<<--- ',form_init)

        formset = ContricutionFormSet(request.POST or None,queryset=Contribution.objects.filter(month__exact=req_month),initial=form_init)
        i=0
        if formset.is_valid():
            serial_form_init =request.session.get('serial_form_init')
            print('serial_form_init --->>>*** ',serial_form_init)
            for itm in serial_form_init:
                print('Loop firm_no ----00000---> ',itm['firm_no'])
                form_init.append({
                    'id_no':Employee.objects.filter(id_no__exact=itm['id_no']),
                    'month':itm['month'],
                    'firm_no':Firm.objects.filter(firm_no__exact=itm['firm_no'] )

                })
            print('form_init --->>>#### ',form_init)
            for form in formset:
                print('form_init--->',form_init[i]['firm_no'].first())
                obj=form.save(commit=False)
                obj.firm_no=form_init[i]['firm_no'].first()
                obj.id_no=form_init[i]['id_no'].first()
                obj.month=form_init[i]['month']
                obj.save()
                i=i+1
                print(form.cleaned_data)
            return redirect('/contribution/create')
        context ={
            'formset':formset,
            # 'firm':firm_set
            }

        return render(request,'contribution/foreset_view.html',context)
        # Create your views here.

def validate_firm(request):
    firm_name = request.GET.get('firm_name', None)
    global_firm_no=firm_name
    print("firm_name---> ",firm_name)
    data = {
        'is_taken': Firm.objects.filter(firm_no__iexact=firm_name).exists()
    }
    return JsonResponse(data)


def autocompleteModel(request):
    if request.is_ajax():
        q = request.GET.get('term', '').capitalize()
        search_qs = Employee.objects.filter(name__startswith=q)
        results = []
        print(q)
        for r in search_qs:
            results.append(r.FIELD)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return JsonResponse(data, mimetype)
# def formset_view(request):
#         ContricutionFormSet =  formset_factory(ContributionModelForm, extra=2)

#         form_init=[
#             {
#                 'month':11,
#                 'amount':20
#                 },
#                  {
#                 'month':10,
#                 'amount':12
#                 }
#         ]

#         formset = ContricutionFormSet(request.POST or None)
#         if formset.is_valid():
#             for form in formset:
#                 print(form.cleaned_data)
#         context ={
#             'formset':formset
#             }

#         return render(request,'contribution/foreset_view.html',context)
#         # Create your views here.
