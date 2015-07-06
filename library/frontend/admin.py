from django.contrib import admin

from .models import *

class CountryAdmin(admin.ModelAdmin):
        fieldsets = [
        ('Name',               {'fields': ['name']}),
    ]

class AuthorAdmin(admin.ModelAdmin):
        fieldsets = [
        ('Name',               {'fields': ['name']}),
        ('Age',                {'fields': ['age']}),
        ('Country',            {'fields': ['country']}),
    ]

class GenreAdmin(admin.ModelAdmin):
        fieldsets = [
        ('Name',               {'fields': ['name']}),
        ('Age',                {'fields': ['age']}),
        ('Popular coef',       {'fields': ['popular_coef']}),
    ]

class BookTypeAdmin(admin.ModelAdmin):
        fieldsets = [
        ('Name',               {'fields': ['name']}),
    ]

class PublishingHouseAdmin(admin.ModelAdmin):
        fieldsets = [
        ('Name',               {'fields': ['name']}),
        ('Address',            {'fields': ['address']}),
        ('speed',              {'fields': ['speed']}),
    ]

class BookAdmin(admin.ModelAdmin):
        fieldsets = [
        ('Name',               {'fields': ['name']}),
        ('Date information',   {'fields': ['pub_date']}),
        ('Genre',              {'fields': ['genre']}),
        ('Author',             {'fields': ['author']}),
        ('Type',               {'fields': ['type']}),
        ('Size',               {'fields': ['size']}),
        ('Price',              {'fields': ['price']}),
        ('Publishing House',   {'fields': ['pub_house']}),
    ]

admin.site.register(Country, CountryAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(BookType, BookTypeAdmin)
admin.site.register(PublishingHouse, PublishingHouseAdmin)
admin.site.register(Book, BookAdmin)