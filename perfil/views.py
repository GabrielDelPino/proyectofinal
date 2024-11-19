from django.shortcuts import render, redirect
from .forms import PerfilForm
from django.contrib.auth.decorators import login_required


@login_required
def editar_perfil(request):
    perfil = request.user.perfil  # Suponiendo que ya tienes un perfil relacionado con el usuario
    if request.method == 'POST':
        form = PerfilForm(request.POST, request.FILES, instance=perfil)
        if form.is_valid():
            form.save()
            return redirect('perfil:perfil_detalle')  # Redirige a los detalles del perfil después de editar
    else:
        form = PerfilForm(instance=perfil)
    return render(request, 'perfil/editar_perfil.html', {'form': form})

@login_required
def detalle_perfil(request):
    return render(request, 'perfil/detalle_perfil.html')  # Cargar la plantilla para mostrar el perfil