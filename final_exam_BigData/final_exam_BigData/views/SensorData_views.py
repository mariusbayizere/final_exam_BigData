from django.shortcuts import render, get_object_or_404, redirect
from .models import Sensor, SensorData
from .forms import SensorDataForm

def sensor_data_list(request):
    """List all sensor data."""
    data = SensorData.objects.select_related('sensor').all()
    return render(request, 'sensordata/sensor_data_list.html', {'data': data})

def sensor_data_detail(request, pk):
    """Display details of a single sensor data entry."""
    entry = get_object_or_404(SensorData, pk=pk)
    return render(request, 'sensordata/sensor_data_detail.html', {'entry': entry})

def sensor_data_create(request):
    """Create a new sensor data entry."""
    if request.method == 'POST':
        form = SensorDataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sensor_data_list')
    else:
        form = SensorDataForm()
    return render(request, 'sensordata/sensor_data_form.html', {'form': form})

def sensor_data_update(request, pk):
    """Update an existing sensor data entry."""
    entry = get_object_or_404(SensorData, pk=pk)
    if request.method == 'POST':
        form = SensorDataForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            return redirect('sensor_data_list')
    else:
        form = SensorDataForm(instance=entry)
    return render(request, 'sensordata/sensor_data_form.html', {'form': form})

def sensor_data_delete(request, pk):
    """Delete a sensor data entry."""
    entry = get_object_or_404(SensorData, pk=pk)
    if request.method == 'POST':
        entry.delete()
        return redirect('sensor_data_list')
    return render(request, 'sensordata/sensor_data_confirm_delete.html', {'entry': entry})
