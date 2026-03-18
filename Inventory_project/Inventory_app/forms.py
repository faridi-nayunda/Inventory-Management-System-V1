from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        #It is important to define the model inside the Meta class when using  Django's ModelForm
        #The models tells the Django which database model the form is based on.
        #Without it, Django wouldn't know which fields to include or validate

        model = Product
        fields = '__all__' # Include all fields from the Product model
        labels = {
            'product_id': 'Product ID',
            'name': 'Name',
            'sku': 'SKU',
            'price': 'Price',
            'quantity': 'Quantity',
            'supplier': 'Supplier',
        }
        widgets = {
            'product_id': forms.NumberInput(attrs={'placeholder':'e.g. 1', 'class':'w-full px-4 text-gray-800 text-md py-2 border rounded-lg focus:ring-green-500'}),
            'name': forms.TextInput(attrs={'placeholder':'e.g. shirt', 'class':'w-full px-4 text-gray-800 text-md py-2 border rounded-lg focus:ring-green-500'}),
            'sku': forms.TextInput(attrs={'placeholder':'e.g. S12345', 'class':'w-full px-4 text-gray-800 text-mdpy-2 border rounded-lg focus:ring-green-500'}),
            'price': forms.NumberInput(attrs={'placeholder':'e.g. 19.99', 'class':'w-full px-4 text-gray-800 text-md py-2 border rounded-lg focus:ring-green-500'}),
            'quantity': forms.NumberInput(attrs={'placeholder':'e.g. 10', 'class':'w-full px-4 text-gray-800 text-md py-2 border rounded-lg focus:ring-green-500'}),
            'supplier': forms.TextInput(attrs={'placeholder':'e.g. ABC Company', 'class': 'w-full px-4 text-gray-800 text-md py-2 border rounded-lg focus:ring-green-500'}),
        }

        error_messages = {
            'name': {
                'required':'Product name is required',
            },

             'price': {
                'required':'Please enter the product price.',
                'invalid': 'Enter a valid price (e.g., 19,99).',
            },
        }