from django.db import models
from  firm.models import Firm
from django.urls import reverse
from django.utils.encoding import smart_text
from django.conf import settings

# Create your models here.

class EmployeeModelManager(models.Manager):
    def get_queryset(self):
        return models.query.QuerySet(self.model, using=self._db)

    def get_by_acc(self,acc):
        qs=self.get_queryset()
        return qs.filter(bank__exact=acc)
        



class Employee(models.Model):
        ACTIVE = 'AC'
        RESIGNED = 'RS'
        FIRED = 'FI'
        RETIRED = 'RT'
        RETRENCHED='RC'
        EMPLOYEE_STATUS = (
            (ACTIVE, 'ACTIVE'),
            (RESIGNED, 'RESIGNED'),
            (FIRED, 'FIRED'),
            (RETIRED, 'RETIRED'),
            (RETRENCHED,'RETRENCHED')
        )
        FNB='FNB'
        STANDARD_BANK='STB'
        NEDBANK='NDB'
        ABSA='ABS'
        CAPITEC='CPT'
        BANK_CHOICE=(
           (FNB,'FNB'),
        (STANDARD_BANK,'STANDARD BANK'),
        (NEDBANK,'NEDBANK'),
        (ABSA,'ABSA'),
        (CAPITEC,'CAPITEC')
        )
        id_no = models.CharField(max_length=13,unique=True)
        firm_no=models.ForeignKey(Firm, on_delete=models.CASCADE)
        added_by=models.CharField(max_length=255,null=False,default='NONE')
        last_edited_by=models.TextField(max_length=255,null=False,default='NONE')
        first_name=models.CharField(max_length=255,unique=True)
        last_name=models.CharField(max_length=255)    
        firm_email=models.EmailField(max_length=255)
        account_number=models.CharField(max_length=20)
        bank=models.CharField(
            max_length=10,
            choices=BANK_CHOICE,
            default=FNB,
        )

        status=models.CharField(
            max_length=8,
            choices=EMPLOYEE_STATUS,
            default=ACTIVE,
        )

        def __str__(self):
           return smart_text(self.first_name)   
        @property
        def full_name(self):
            return self.first_name +" "+self.last_name


        def get_absolute_url(self):
           return reverse("employee:employee-detail", kwargs={"id": self.id})

        objects=EmployeeModelManager()
        



