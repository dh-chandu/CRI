from django.shortcuts import render
from django.utils.safestring import mark_safe
from .models import *
from .decorators import *

# Create your views here.

def home(request):
    return render(request, 'home.html', {})

@query_debugger
def cri_status(request):
    #cri_status = CriStatus.objects.prefetch_related()
    cri_status = CriStatus.objects.select_related()
    cr_dict = {}
    table_bod = ''
    for cr in cri_status:
        #cr_dict[cr.request.id] = cr_dict[cr.request.id].append
        table_bod += "<tr><td>%d</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td><a href=%s>ea_url</a></td><td>%s</td><td>%s</td><td>%s</td><td><a href=%s>jenkins_url</a></td></tr>"\
        % (cr.request.id, cr.request.refinement_type.name, cr.request.project.name, cr.request.branch.name, cr.refinement_iteration, cr.ea_build_url, cr.build_duration, cr.conflicts, cr.refinement_state.name, cr.jenkins_job_url)
        # print('request:%d,refinement_type:%s' % (cr.request.id,cr.request.refinement_type.name))

    table_body = mark_safe(table_bod)
    return render(request, 'cri_status.html', {'table_body' : table_body})

def cri_request():
    cri_req = CriRequest.objects.prefetch_related()
