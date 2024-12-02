from django import forms #cette line importe forms de django ,qui est utlise pour creer des forms web
from employee.models import Employee 


class EmployeeForm(forms.ModelForm):
    class Meta : 
        model=Employee
        fields = ['eid', 'ename', 'eemail', 'econtact']