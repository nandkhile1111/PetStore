from django.contrib import admin
from Petstoreapp.models import Product,Category

# Register your models here.id
class ProductName(admin.ModelAdmin):
    list_display = ['id','name','price','detail','category','image']

class CategoryName(admin.ModelAdmin):
    list_display = ['cid','name']

    


admin.site.register(Product,ProductName)
admin.site.register(Category,CategoryName)