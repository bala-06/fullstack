# mous/admin.py
from django.contrib import admin
from .models import Department, Organization, Outcome, MOU, Activity

admin.site.register(Department)
admin.site.register(Organization)
admin.site.register(Outcome)
admin.site.register(MOU)
admin.site.register(Activity)
