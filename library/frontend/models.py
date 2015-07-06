from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=200)

class Author(models.Model):
    name = models.CharField(db_index=True, max_length=200)
    age = models.IntegerField()
    country = models.ForeignKey(Country)

class Genre(models.Model):
    name = models.CharField(db_index=True, max_length=200)
    popular_coef = models.IntegerField()

class BookType(models.Model):
    name = models.CharField(db_index=True, max_length=200)

class PublishingHouse(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=250)
    speed = models.IntegerField()

class Book(models.Model):
    name = models.CharField(db_index=True, max_length=200)
    genre = models.ForeignKey(Genre)
    type = models.ForeignKey(BookType)
    author = models.ForeignKey(Author)
    pub_house = models.ForeignKey(PublishingHouse)
    size = models.IntegerField()
    price = models.IntegerField()
    pub_date = models.DateTimeField('date published')

class ShopHead(models.Model):
    name = models.CharField(max_length=200)
    phone = models.IntegerField()

class BookShop(models.Model):
    name = models.CharField(db_index=True, max_length=200)
    address = models.CharField(max_length=200)
    metro = models.CharField(max_length=100)
    specialization = models.ForeignKey(Genre)
    head = models.ForeignKey(ShopHead)

class Seller(models.Model):
    name = models.CharField(db_index=True, max_length=200)
    shop = models.ForeignKey(BookShop)
    expected_salary = models.IntegerField()
    real_salary = models.IntegerField()
    phone = models.IntegerField()

class Sale(models.Model):
    book = models.ForeignKey(Book)
    count = models.IntegerField()
    shop = models.ForeignKey(BookShop)
    seller = models.ForeignKey(Seller)
    sale_date = models.DateTimeField(auto_now_add=True)