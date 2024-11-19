from django.shortcuts import render
from calendar import monthcalendar
from datetime import datetime

def get_calendar_data(month, year):
    # Generar el calendario para el mes y año proporcionados
    calendar_data = monthcalendar(year, month)

    # Nombres de los meses en español
    months = {
        1: 'ENERO', 2: 'FEBRERO', 3: 'MARZO', 4: 'ABRIL',
        5: 'MAYO', 6: 'JUNIO', 7: 'JULIO', 8: 'AGOSTO',
        9: 'SEPTIEMBRE', 10: 'OCTUBRE', 11: 'NOVIEMBRE', 12: 'DICIEMBRE'
    }

    # Calcular mes y año anteriores
    if month == 1:
        previous_month = 12
        previous_year = year - 1
    else:
        previous_month = month - 1
        previous_year = year

    # Calcular mes y año siguientes
    if month == 12:
        next_month = 1
        next_year = year + 1
    else:
        next_month = month + 1
        next_year = year

    return {
        'month_name': months[month],
        'calendar_weeks': calendar_data,
        'month': month,
        'year': year,
        'previous_month': previous_month,
        'previous_year': previous_year,
        'next_month': next_month,
        'next_year': next_year,
    }

def calendar_view(request):
    # Obtener mes y año desde la solicitud, o usar el actual
    month = int(request.GET.get('month', datetime.now().month))
    year = int(request.GET.get('year', datetime.now().year))

    # Generar datos del calendario
    calendar_data = get_calendar_data(month, year)
    return render(request, 'calendario/calendar.html', calendar_data)


