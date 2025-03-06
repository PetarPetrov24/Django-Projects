from django.shortcuts import render, redirect, get_object_or_404

from car_type.forms import CarForm, DeleteCarForm
from car_type.models import CarType
from core.util import get_first_profile


# Create your views here.
def catalogue_page(request):
    cars = CarType.objects.all()
    context = {
        'profile': get_first_profile(),
        'cars': cars
    }

    return render(request, template_name='catalogue.html', context=context)


def create_car_page(request):
    form = CarForm(request.POST or None)
    profile = get_first_profile()
    if form.is_valid():
        form.instance.owner_id = profile.pk
        form.save()

        return redirect('catalogue')

    context = {
        'profile': profile,
        'form': form
    }

    return render(request, template_name='car-create.html', context=context)


def car_details_page(request, pk):
    car = get_object_or_404(CarType, pk=pk)
    context = {
        'profile': get_first_profile(),
        'car': car
    }

    return render(request, template_name='car-details.html', context=context)


def edit_car_page(request, pk):
    car = get_object_or_404(CarType, pk=pk)
    form = CarForm(instance=car)

    if request.method == 'POST':
        form = CarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'car': car,
        'form': form,
        'profile': get_first_profile(),
    }
    return render(request, 'car-edit.html', context)


def delete_car_page(request, pk):
    car = get_object_or_404(CarType, pk=pk)

    if request.method == 'POST':
        car.delete()
        return redirect('catalogue')

    form = DeleteCarForm(instance=car)
    context = {
        'profile': get_first_profile(),
        'form': form,
        'car': car
    }

    return render(request, 'car-delete.html', context)