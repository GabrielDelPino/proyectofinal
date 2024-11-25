from django.shortcuts import render
from calendar import monthcalendar
from datetime import datetime
from nuevo_evento.models import Evento, Nota
from agendar_cita.models import Cita
from perfil.models import Perfil

def get_calendar_data(user, year, month):
    if month < 1:
        month = 12
        year -= 1
    elif month > 12:
        month = 1
        year += 1

    calendar_data = monthcalendar(year, month)

    months = {
        1: 'ENERO', 2: 'FEBRERO', 3: 'MARZO', 4: 'ABRIL',
        5: 'MAYO', 6: 'JUNIO', 7: 'JULIO', 8: 'AGOSTO',
        9: 'SEPTIEMBRE', 10: 'OCTUBRE', 11: 'NOVIEMBRE', 12: 'DICIEMBRE'
    }

    perfil = Perfil.objects.get(usuario=user)

    eventos = Evento.objects.filter(
        usuario=user, asignado=True, fecha__year=year, fecha__month=month
    ).prefetch_related('notas')  # Prefetch para las notas relacionadas
    
    citas = Cita.objects.filter(
        usuario=user, fecha__year=year, fecha__month=month
    )

    return {
        'month_name': months[month],
        'calendar_weeks': calendar_data,
        'empresa_nombre': perfil.nombre_empresa,
        'empresa_logo': perfil.logo,
        'current_month': month,
        'current_year': year,
        'eventos': eventos,
        'citas': citas,
    }

def calendar_view(request):
    year = int(request.GET.get('year', datetime.now().year))
    month = int(request.GET.get('month', datetime.now().month))
    calendar_data = get_calendar_data(request.user, year, month)
    return render(request, 'calendario/calendar.html', calendar_data)










