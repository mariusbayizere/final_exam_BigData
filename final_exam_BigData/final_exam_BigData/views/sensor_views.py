from django.shortcuts import render, get_object_or_404, redirect
from .models import Sensor
from .forms import SensorForm

def sensor_list(request):
    """List all sensors."""
    sensors = Sensor.objects.all()
    return render(request, 'sensors/sensor_list.html', {'sensors': sensors})

def sensor_detail(request, pk):
    """Display details of a single sensor."""
    sensor = get_object_or_404(Sensor, pk=pk)
    return render(request, 'sensors/sensor_detail.html', {'sensor': sensor})

def sensor_create(request):
    """Create a new sensor."""
    if request.method == 'POST':
        form = SensorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sensor_list')
    else:
        form = SensorForm()
    return render(request, 'sensors/sensor_form.html', {'form': form})

def sensor_update(request, pk):
    """Update an existing sensor."""
    sensor = get_object_or_404(Sensor, pk=pk)
    if request.method == 'POST':
        form = SensorForm(request.POST, instance=sensor)
        if form.is_valid():
            form.save()
            return redirect('sensor_list')
    else:
        form = SensorForm(instance=sensor)
    return render(request, 'sensors/sensor_form.html', {'form': form})

def sensor_delete(request, pk):
    """Delete a sensor."""
    sensor = get_object_or_404(Sensor, pk=pk)
    if request.method == 'POST':
        sensor.delete()
        return redirect('sensor_list')
    return render(request, 'sensors/sensor_confirm_delete.html', {'sensor': sensor})
