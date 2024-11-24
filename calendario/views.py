from django.shortcuts import render
from calendar import monthcalendar
from datetime import datetime
from nuevo_evento.models import Evento
from perfil.models import Perfil

def get_calendar_data(user, year, month):
    # Validar que el mes esté en el rango válido (1 a 12)
    if month < 1:
        month = 12
        year -= 1
    elif month > 12:
        month = 1
        year += 1
    
    # Obtener los días del mes solicitado
    calendar_data = monthcalendar(year, month)
    
    # Nombres de los meses en español
    months = {
        1: 'ENERO', 2: 'FEBRERO', 3: 'MARZO', 4: 'ABRIL',
        5: 'MAYO', 6: 'JUNIO', 7: 'JULIO', 8: 'AGOSTO',
        9: 'SEPTIEMBRE', 10: 'OCTUBRE', 11: 'NOVIEMBRE', 12: 'DICIEMBRE'
    }
    
    # Obtener el perfil del usuario
    perfil = Perfil.objects.get(usuario=user)
    
    return {
        'month_name': months[month],
        'calendar_weeks': calendar_data,
        'empresa_nombre': perfil.nombre_empresa,
        'empresa_logo': perfil.logo,
        'current_month': month,
        'current_year': year,
        'eventos': Evento.objects.filter(asignado=True, fecha__year=year, fecha__month=month),  # Solo eventos asignados
    }

def calendar_view(request):
    # Obtener mes y año de los parámetros GET
    year = int(request.GET.get('year', datetime.now().year))
    month = int(request.GET.get('month', datetime.now().month))
    
    # Obtener los datos del calendario
    calendar_data = get_calendar_data(request.user, year, month)
    
    return render(request, 'calendario/calendar.html', calendar_data)







