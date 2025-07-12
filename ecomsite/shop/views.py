from django.shortcuts import render
from .models import Products
from  django.core.paginator import Paginator
# Create your views here.

def index(request):
    product_objects = Products.objects.all()

    # search
    item_name = request.GET.get('item_name')
    if item_name != '' and item_name is not None:
        product_objects = Products.objects.filter(title__icontains=item_name)

    #paginator
    paginator = Paginator(product_objects,4)
    page = request.GET.get('page')
    product_objects = paginator.get_page(page)

    return render(request, 'shop/index.html', {'product_objects': product_objects})


# detail page
def detail(request, id):
    product= Products.objects.get(id=id)
    return render(request,'shop/detail.html',{'product':product})