from django.core import paginator
from django.shortcuts import redirect, render
from app.forms import ProdutosForm
from app.models import Produtos, Company
from django.core.paginator import Paginator

# Create your views here.
def home (request):
    data = {}
    # data['bancodados'] = Produtos.objects.all()
    todosProdutos = Produtos.objects.all()
    paginator = Paginator(todosProdutos, 8)
    paginas = request.GET.get('pagina')
    data['bancodados'] = paginator.get_page(paginas)
    return render(request, 'home.html', data)

def productsform (request):
    data = {}
    data['productsform'] = ProdutosForm()
    data['bancodadosempresa'] = Company.objects.all()
    return render(request, 'products-form.html', data)

def createproduct(request):
    form = ProdutosForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('products-form')

def editproduct(request, pk):
    data = {}
    data['bancodados'] = Produtos.objects.get(pk=pk)
    data['productsform'] = ProdutosForm(instance=data['bancodados'])
    return render(request, 'products-form.html', data)

def updateproduct(request, pk):
    data = {}
    data['bancodados'] = Produtos.objects.get(pk=pk)
    productsform = ProdutosForm(request.POST or None, instance=data['bancodados'])
    if productsform.is_valid():
        productsform.save()
        return redirect ('home')

def deleteproduct(request, pk):
    db = Produtos.objects.get(pk=pk)
    db.delete()
    return redirect('home')

def companyproducts(request, fk):
    data = {}
    data['bancodados'] = Produtos.objects.all().filter(empresa=fk)
    return render (request, 'company-products.html', data)