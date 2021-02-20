from django.contrib import admin

from .models import DccDepts, DccUsers, DccProcs, DccCerts

admin.site.register(DccDepts)
admin.site.register(DccUsers)
admin.site.register(DccProcs)
#admin.site.register(Question)
#admin.site.register(Choice)
admin.site.register(DccCerts)