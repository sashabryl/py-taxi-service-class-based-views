from django.shortcuts import render
from django.views import generic

from taxi.models import Driver, Car, Manufacturer


def index(request):
    """View function for the home page of the site."""

    context = {
        "num_drivers": Driver.objects.count(),
        "num_cars": Car.objects.count(),
        "num_manufacturers": Manufacturer.objects.count(),
    }

    return render(request, "taxi/index.html", context=context)


class ManufacturerListView(generic.ListView):
    model = Manufacturer
    queryset = Manufacturer.objects.all().order_by("name")
    paginate_by = 5
    context_object_name = "manufacturer_list"


class CarListView(generic.ListView):
    model = Car
    paginate_by = 5
    queryset = Car.objects.\
        select_related("manufacturer").all().order_by("model")


class DriverListView(generic.ListView):
    model = Driver
    queryset = Driver.objects.prefetch_related("cars").all()


class DriverDetailView(generic.DetailView):
    model = Driver
    queryset = Driver.objects.prefetch_related("cars").all()


class CarDetailView(generic.DetailView):
    model = Car
    queryset = Car.objects.select_related("manufacturer")\
        .prefetch_related("drivers").all()
