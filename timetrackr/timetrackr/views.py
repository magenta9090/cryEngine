from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from timetrackr.models import Work


@require_http_methods(['GET', 'HEAD'])
@login_required()
def index(request):
    context = {
        'works': Work.objects.filter(worker=request.user.id)
    }
    return render(request, 'timetrackr/index.html', context)
