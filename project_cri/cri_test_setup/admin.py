from django.contrib import admin
from cri_test_setup import models as crimodels
from django.db.models.base import ModelBase

# Very hacky!
# for name, var in crimodels.__dict__.items():
#     if type(var) is ModelBase:
#         admin.site.register(var)
# Register your models here.



admin.site.register(crimodels.CriProject, crimodels.CriProjectAdmin)
admin.site.register(crimodels.CriBranch, crimodels.CriBranchAdmin)
admin.site.register(crimodels.CriProjectConfig, crimodels.CriProjectConfigAdmin)
admin.site.register(crimodels.CriBranchConfig, crimodels.CriBranchConfigAdmin)
admin.site.register(crimodels.CriServer, crimodels.CriServerAdmin)
admin.site.register(crimodels.CriRequest,crimodels.crirequest)
