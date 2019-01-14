from django.db import models
from employee.models import Employee
from firm.models import Firm
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Contribution(models.Model):
    id_no=models.ForeignKey(Employee, on_delete=models.CASCADE)
    firm_no=models.ForeignKey(Firm, on_delete=models.CASCADE)
    date_created=models.DateTimeField(auto_now=True)
    month=models.SmallIntegerField(validators=[MaxValueValidator(12), MinValueValidator(1)])
    amount=models.DecimalField(max_digits=65,decimal_places=2)

    def __str__(self):
        return str(self.id_no)
    

