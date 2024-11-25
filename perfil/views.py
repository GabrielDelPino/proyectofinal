from django.shortcuts import render, redirect
from .forms import PerfilForm
from django.contrib.auth.decorators import login_required


@login_required
def editar_perfil(request):
    if request.method == 'POST':
        form = PerfilForm(request.POST, request.FILES, instance=request.user.perfil)
        if form.is_valid():
            form.save()
            return redirect('calendario')  # Redirigir al calendario
    else:
        form = PerfilForm(instance=request.user.perfil)
    return render(request, 'perfil/editar_perfil.html', {'form': form})

@login_required
def detalle_perfil(request):
    return render(request, 'perfil/detalle_perfil.html')  # Cargar la plantilla para mostrar el perfil