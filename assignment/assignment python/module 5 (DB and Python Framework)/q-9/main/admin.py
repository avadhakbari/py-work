from django.contrib import admin
from .models import product_mst,product_sub_cat

# Register your models here.

class product_mstAdmin(admin.ModelAdmin):
    list_display=['product_id', 'product_name']
    search_fields = ['product_id', 'product_name']


class product_sub_catAdmin(admin.ModelAdmin):
    list_display = ['product', 'product_price', 'product_image','product_model','product_ram']
    search_fields = ['product_sub_cat_id', 'product','product_model']

admin.site.register(product_mst,product_mstAdmin)
admin.site.register(product_sub_cat,product_sub_catAdmin)