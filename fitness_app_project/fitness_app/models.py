from django.db import models
from django.contrib.auth.models import User


class User(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    age = models.CharField(max_length=10)
    weight = models.CharField(max_length=10)
    height = models.CharField(max_length=10)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Custom_Meal(models.Model):
    ingredients = models.TextField()
    instructions = models.TextField()
    portions = models.TextField()
    macros = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='meals')

    def __str__(self):
        return self.name

class Custom_Circuit(models.Model):
    workouts = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='circuits')

    def __str__(self):
        return self.name
# class Workout(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='workouts')


class Food(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='foods')
    label = models.CharField(max_length=100)
    kcal = models.CharField(max_length=100)
    protein = models.CharField(max_length=100)
    fat = models.CharField(max_length=100)
    carbs = models.CharField(max_length=100)

    def __str__(self):
        return self.name
