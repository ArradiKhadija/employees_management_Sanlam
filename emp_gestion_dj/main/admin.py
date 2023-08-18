from django.contrib import admin
from .models import Employee
# Register your models here.
#here we attach models to admin

class EmployeeAdmin(admin.ModelAdmin):
    list_display= ['id','nomComplet','email','contact','adresse']
admin.site.register(Employee,EmployeeAdmin)
