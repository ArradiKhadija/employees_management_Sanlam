from django.contrib import admin
from .models import *
# Register your models here.
#here we attach models to admin

class EmployeeAdmin(admin.ModelAdmin):
    list_display= ['id','nomComplet','email','contact','adresse','poste']
admin.site.register(Employee,EmployeeAdmin)

class VacationAdmin(admin.ModelAdmin):
    list_display= ['id_vac', 'id_emp_vac','type_vac','start_vac','end_vac','duration_vac','reason_vac','approbateur_vac']
admin.site.register(Vacation,VacationAdmin)

class TribeAdmin(admin.ModelAdmin):
    list_display= ['id_trb', 'intitule_trb', 'resp_trb']
admin.site.register(Tribe,TribeAdmin)