from django.shortcuts import redirect, render
from app.forms import ProdutosForm
from app.models import Produtos

# Create your views here.
def home (request):
    data = {}
    data['bancodados'] = Produtos.objects.all()
    return render(request, 'home.html', data)

def productsform (request):
    data = {}
    data['productsform'] = ProdutosForm()
    return render(request, 'products-form.html', data)

def createproduct(request):
    form = ProdutosForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('products-form')


