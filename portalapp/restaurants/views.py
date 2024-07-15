from django.shortcuts import render, get_object_or_404, redirect
from .models import Restaurant
from .forms import RestaurantForm

def restaurant_list(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'restaurants/restaurant_list.html', {'restaurants': restaurants})

def restaurant_detail(request, pk):
    restaurant = get_object_or_404(Restaurant, pk=pk)
    return render(request, 'restaurants/restaurant_detail.html', {'restaurant': restaurant})

def restaurant_create(request):
    if request.method == "POST":
        form = RestaurantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('restaurant_list')
    else:
        form = RestaurantForm()
    return render(request, 'restaurants/restaurant_form.html', {'form': form})

def restaurant_delete(request, pk):
    restaurant = get_object_or_404(Restaurant, pk=pk)
    if request.method == "POST":
        restaurant.delete()
        return redirect('restaurant_list')
    return render(request, 'restaurants/restaurant_confirm_delete.html', {'restaurant': restaurant})

def restaurant_update(request, pk):
    restaurant = get_object_or_404(Restaurant, pk=pk)
    if request.method == 'POST':
        form = RestaurantForm(request.POST, instance=restaurant)
        if form.is_valid():
            form.save()
            return redirect('restaurant_list')
    else:
        form = RestaurantForm(instance=restaurant)
    return render(request, 'restaurants/restaurant_form.html', {'form': form, 'title': 'Update Restaurant'})
