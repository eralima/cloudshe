from django.shortcuts import redirect, render
from app.forms import CompanyForm, ProdutosForm
from app.models import Produtos
from django.http import HttpResponse


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
        return redirect('home')

def companyform (request):
    data = {} #dicionario
    data['companyform'] = CompanyForm()
    return render(request, 'company-form.html', data)
