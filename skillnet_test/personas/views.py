from django.shortcuts import render, redirect
from .forms import PersonForm
from .models import Person

def person_form_view(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el formulario si es válido
            return redirect('person_form')  # Redirige al formulario vacío
    else:
        form = PersonForm()  # Muestra el formulario vacío
    
    # Obtener todas las personas para mostrarlas en la tabla
    persons = Person.objects.all()
    return render(request, 'personas/person_form.html', {'form': form, 'persons': persons})