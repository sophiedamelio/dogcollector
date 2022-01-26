from django.shortcuts import render, redirect

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView


from .models import Dog, Treat
from .forms import FeedingForm

# Create your views here.


class DogCreate(CreateView):
    model = Dog
    fields = '__all__'


class DogUpdate(UpdateView):
    model = Dog
    fields = ['breed', 'energyLevel', 'description', 'age']


class DogDelete(DeleteView):
    model = Dog
    success_url = '/dogs/'


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def dogs_index(request):
    dogs = Dog.objects.all()

    return render(request, 'dogs/index.html', {'dogs': dogs})


def dogs_detail(request, dog_id):
    dog = Dog.objects.get(id=dog_id)
    feeding_form = FeedingForm()

    treats_dog_doesnt_have = Treat.objects.exclude(
        id__in=dog.treats.all().values_list('id'))

    return render(request, 'dogs/detail.html', {
        'dog': dog,
        'feeding_form': feeding_form,
        'treats': treats_dog_doesnt_have
    })


def add_feeding(request, dog_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.dog_id = dog_id
        new_feeding.save()
    return redirect('detail', dog_id=dog_id)


def assoc_toy(request, dog_id, treat_id):
    dog = Dog.objects.get(id=dog_id)
    dog.treats.add(treat_id)
    return redirect('detail', dog_id=dog_id)


class TreatList(ListView):
    model = Treat


class TreatDetail(DetailView):
    model = Treat


class TreatCreate(CreateView):
    model = Treat
    fields = '__all__'


class TreatUpdate(UpdateView):
    model = Treat
    fields = ['name', 'description']


class TreatDelete(DeleteView):
    model = Treat
    success_url = '/treats/'
