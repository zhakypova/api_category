from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Item(models.Model):
    item_id = models.IntegerField()
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    QR = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.name} - {self.QR}'


    def get_QR(self):
        self.QR = f'{self.category.id}C{self.price}P{self.item_id}l'
        return self.QR