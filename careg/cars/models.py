from django.db import models
from directory.models import Mark
from django.contrib.auth import get_user_model

User = get_user_model()

class Car(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cars')
    worker = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='handled_cars')
    mark = models.ForeignKey(Mark, on_delete=models.PROTECT, related_name='cars')
    #Можно записать вот   | тут так - 'direcctory.Nark' вместо того что стоит/Тогда надо убрать import (Это нужно для сокращения кол-ва импортов и чтоб не было путаницы)
    year_issue = models.IntegerField()
    legal_number = models.CharField(max_length=50)

    def __str__(self):
        return self.legal_number

class CarDocument(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='documents')
    file = models.FileField()


