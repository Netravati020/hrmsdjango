from django.contrib import admin
# #
# Register your models here.
from .models import OpdRegistration, OpdSourceofconsultationcharges, OpdPackagemaster, User, Employees
# #
admin.site.register(OpdRegistration)
# class opdAdmin(admin.ModelAdmin):
#     pass
# admin.site.register(User)
admin.site.register(OpdSourceofconsultationcharges)
admin.site.register(OpdPackagemaster)
admin.site.register(User)
admin.site.register(Employees)