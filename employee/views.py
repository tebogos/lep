from django.shortcuts import render,get_object_or_404
from .models import Employee
from .forms import EmployeeModelForm , EmployeeAutocompleteForm
from django.views.generic import( CreateView,
ListView,
DetailView,
UpdateView
)
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.html import format_html
# Create your views here.

class EmployeeCreateView(CreateView):
    model = Employee
    form_class=EmployeeModelForm
    template_name = 'employee/create_employee_form.html'
    success_url = '/employee'
    # success_message="%(first_name) has been created"
    def form_valid(self,form):
        form.instance.added_by=self.request.user
       
        # form.instance.last_edited_by=self.request.user
        valid_form=super(EmployeeCreateView,self).form_valid(form)
        messages.success(self.request, 'Employee added successfully.')
        return valid_form

class EmployeeListView(ListView):
    model = Employee
    queryset = Employee.objects.all()
    template_name = 'employee/list_employee_view.html'



class EmployeeDetailView(DetailView):
    template_name = 'employee/employee_detail.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Employee, id=id_)

class EmployeeUpdateView(UpdateView):
    model = Employee
    form_class=EmployeeModelForm
    template_name_suffix = '_update_form'
    # template_name = 'employee/employee_update_form.html'


    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Employee, id=id_)
   
class EmployeeAutocomplete(CreateView):
   model = Employee
   form_class=EmployeeAutocompleteForm
   template_name_suffix = '_autocomplete_form'
    # form_class=EmployeeAutocompleteForm
    # def get_queryset(self):
    #     # Don't forget to filter out results depending on the visitor !
    #     # if not self.request.user.is_authenticated():
    #     #     return Employee.objects.none()

    #     qs = Employee.objects.all()

    #     if self.q:
    #         qs = qs.filter(first_name__istartswith=self.q)

    #     return qs

    # def get_result_label(self, item):
    #     return format_html('<li>{}</li>', item.first_name)
    
    # def get_selected_result_label(self, item):
    #     return item.first_name

