from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime

def storage_information_view(request):
    non_closed_visits = []
    active_visits = Visit.objects.filter(leaved_at__isnull=True)
    for visit in active_visits:
        formatted_duration = visit.format_duration()
        non_closed_visits.append({
            'who_entered': visit.passcard.owner_name,
            'entered_at': localtime(visit.entered_at).strftime('%d %B %Y г. %H:%M'),
            'duration': formatted_duration,
        })
    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
