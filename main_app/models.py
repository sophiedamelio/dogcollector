from django.db import models
from django.urls import reverse
from datetime import date


# Create your models here.


MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)


class Treat(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('treat_detail', kwargs={'pk': self.id})


class Dog(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    energyLevel = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    treats = models.ManyToManyField(Treat)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'dog_id': self.id})


class Feeding(models.Model):
    date = models.DateField('feeding date')
    meal = models.CharField(
        max_length=1,
        choices=MEALS,
        default=MEALS[0][0]
    )

    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_meal_display()} on {self.date}"

    # change the default sort
    class Meta:
        ordering = ['-date']
