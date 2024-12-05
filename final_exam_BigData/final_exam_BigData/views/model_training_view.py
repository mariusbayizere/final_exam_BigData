from django.shortcuts import render, get_object_or_404, redirect
from .models import ModelTraining
from .forms import ModelTrainingForm

def model_training_list(request):
    """List all model training records."""
    records = ModelTraining.objects.all()
    return render(request, 'modeltraining/model_training_list.html', {'records': records})

def model_training_detail(request, pk):
    """Display details of a single model training record."""
    record = get_object_or_404(ModelTraining, pk=pk)
    return render(request, 'modeltraining/model_training_detail.html', {'record': record})

def model_training_create(request):
    """Create a new model training record."""
    if request.method == 'POST':
        form = ModelTrainingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('model_training_list')
    else:
        form = ModelTrainingForm()
    return render(request, 'modeltraining/model_training_form.html', {'form': form})

def model_training_update(request, pk):
    """Update an existing model training record."""
    record = get_object_or_404(ModelTraining, pk=pk)
    if request.method == 'POST':
        form = ModelTrainingForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('model_training_list')
    else:
        form = ModelTrainingForm(instance=record)
    return render(request, 'modeltraining/model_training_form.html', {'form': form})

def model_training_delete(request, pk):
    """Delete a model training record."""
    record = get_object_or_404(ModelTraining, pk=pk)
    if request.method == 'POST':
        record.delete()
        return redirect('model_training_list')
    return render(request, 'modeltraining/model_training_confirm_delete.html', {'record': record})
