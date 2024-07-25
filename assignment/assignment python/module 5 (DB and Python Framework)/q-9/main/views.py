
# from django.shortcuts import render, redirect
# from.models import product_mst, product_sub_cat
# from django.contrib import messages

# def index(request):
#     if request.method == 'POST':
#         product_name = request.POST["product"]
#         product_price_ = request.POST["price"]
#         product_image_ = request.FILES["img"]
#         product_model_ = request.POST["model"]
#         product_ram_ = request.POST["ram"]

#         # Create a product_mst instance
#         product_mst_instance = product_mst(product_name=product_name)
#         product_mst_instance.save()

#         # Create a product_sub_cat instance
#         new_product = product_sub_cat.objects.create(
#             product=product_mst_instance,  # Assign the product_mst instance to the product field
#             product_price=product_price_,
#             product_image=product_image_,
#             product_model=product_model_,
#             product_ram=product_ram_
#         )

#         new_product.save()
#         messages.success(request, 'Product added successfully!')

#     productsub = product_sub_cat.objects.all()
#     return render(request, 'index.html', {'productsub': productsub})

# def delete_product(request, id):
#     product = product_sub_cat.objects.get(id=id)
#     product.delete()
#     messages.success(request, 'Product deleted successfully!')
#     return redirect('index')

# def edit_product(request, id):
#     product = product_sub_cat.objects.get(id=id)
#     if request.method == 'POST':
#         product.product_price = request.POST["price"]
#         product.product_image = request.FILES["img"]
#         product.product_model = request.POST["model"]
#         product.product_ram = request.POST["ram"]
#         product.save()
#         messages.success(request, 'Product updated successfully!')
#         return redirect('index')
#     return render(request, 'edit_product.html', {'product': product})

# def search_product(request):
#     if request.method == 'GET':
#         search_query = request.GET.get('search')
#         products = product_sub_cat.objects.filter(product__product_name__icontains=search_query)
#         return render(request, 'earch_results.html', {'products': products})\


from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm

def index(request):
    productsub = Product.objects.all()
    return render(request, 'index.html', {'productsub': productsub})

def upload_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProductForm()
    return render(request, 'index.html', {'form': form})

def delete_product(request, pk):
    product = Product.objects.get(pk=pk)
    product.delete()
    return redirect('index')

def edit_product(request, pk):
    product = Product.objects.get(pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('index ')