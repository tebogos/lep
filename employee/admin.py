from django.contrib import admin
from .models import Employee

# Register your models here.

admin.site.register(Employee)
class EmployeeModelAdmin(admin.ModelAdmin):
    fields =(
            'first_name',
            'last_name',
            'id_no',
            'firm_no',
            'firm_email',
            'account_number',
            'bank',
            'get_full_name',
            
    )
    readonly_fields=('added_by','last_edited_by')
    def get_full_name(self,obj,*arg,**kwarg):
        return str(obj.full_name)

    class Meta:
        model = Employee
        

       

