from django.contrib import admin
from .models import data



from import_export import resources
from import_export.admin import ImportExportModelAdmin
# Register your models here.





class StudentResource(resources.ModelResource):
   class Meta:
      model = data
class StudentAdmin(ImportExportModelAdmin):
   resource_class = StudentResource

admin.site.register(data,StudentAdmin)