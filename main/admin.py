from django.contrib import admin
from .models import Product, Review


class ReviewInLine(admin.TabularInline):
    model = Review


class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ReviewInLine,
    ]
    list_display = ('title', 'owner')


admin.site.register(Product, ProductAdmin)
