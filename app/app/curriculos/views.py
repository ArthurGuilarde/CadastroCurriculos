from django.shortcuts import render, redirect
from .forms import CurriculoCreateForm

# Create your views here.
def add(request):
  template_name = 'addCurriculo.html'
  
  if request.method == 'POST':
    form = CurriculoCreateForm(request.POST, request.FILES)
    
    if form.is_valid():
      form.save(user=request.user)
      return redirect('core:home')
  else:
    form = CurriculoCreateForm()

  context = {
    'form': form
  }
  return render(request, template_name, context)