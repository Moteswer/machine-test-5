from multiprocessing import AuthenticationError
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.
# flywithme/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Flight
from .forms import CustomAuthenticationForm, FlightForm

def flight_list(request):
    flight_id_to_display = request.GET.get('flight_id')
    
    if flight_id_to_display:
        # If a flight ID is provided, retrieve the specific flight details
        flight = Flight.objects.filter(FlightId=flight_id_to_display).first()
        return render(request, 'flight_list.html', {'flights': Flight.objects.all(), 'flight_id_to_display': flight_id_to_display, 'flight': flight})
    else:
        # Display all flights if no specific flight ID is provided
        return render(request, 'flight_list.html', {'flights': Flight.objects.all(), 'flight_id_to_display': None})

def flight_detail(request, flight_id):
    flight = get_object_or_404(Flight, pk=flight_id)
    return render(request, 'flight_detail.html', {'flight': flight})

def flight_add(request):
    if request.method == 'POST':
        form = FlightForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('flight_list')
    else:
        form = FlightForm()
    return render(request, 'flight_form.html', {'form': form})

def flight_edit(request, flight_id):
    flight = get_object_or_404(Flight, pk=flight_id)
    if request.method == 'POST':
        form = FlightForm(request.POST, instance=flight)
        if form.is_valid():
            form.save()
            return redirect('flight_list')
    else:
        form = FlightForm(instance=flight)
    return render(request, 'flight_form.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('flight_list')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')