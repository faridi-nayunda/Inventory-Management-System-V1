from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Product

# Create your views here.

#CRUD = Create, Read, Update, and Delete

#Home view
def home_view(request):
    return render(request, 'inventories/home.html')


#Create view
def create_product_view(request):
    form = ProductForm()  # Always initialize form
    if request.method == 'POST':
        form = ProductForm(request.POST) #Binds data from the request
        if form.is_valid(): #cheks validation rules
            form.save()
            return redirect('product_list') #Redirect to the list view
     
    return render(request, 'inventories/product_form.html', {'form':form})
           


#Read view (List all products)
def product_list_view(request):
    products = Product.objects.all()
    return render(request, 'inventories/product_list.html', {'products':products})


#Update view
#The instance parameter in Django forms is used to bind a form to an existing model instance, 
# which allow the form to pre-fill data and update existing records instead of creating new ones

def update_product_view(request, product_id):
    product = Product.objects.get(product_id=product_id) #Get existing data
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product) #binds form to instance
        if form.is_valid():
            form.save() #Update the product instead of creating a new one
            return redirect('product_list')
    else:
        form = ProductForm(instance=product) #pre-fill form with existing data
        return render(request, 'inventories/product_form.html', {'form':form})


#Delete view
def delete_product_view(request, product_id):
    product = Product.objects.get(product_id=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'inventories/product_confirm_delete.html', {'product':product})
