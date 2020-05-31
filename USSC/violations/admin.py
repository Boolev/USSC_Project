from django.contrib import admin
from .models import *

admin.site.register(Violation)
admin.site.register(ViolationType)
admin.site.register(Profession)
admin.site.register(Object)