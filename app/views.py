from django.shortcuts import redirect, render
from app.forms import CompanyForm, ProdutosForm
from app.models import Company, Produtos
from django.http import HttpResponse
from django.contrib import messages


# Create your views here.
# def home (request):
#     data = {}
#     data['bancodados'] = Produtos.objects.all()
#     return render(request, 'home.html', data)


def home(request):
  data = {}
  data['bancodados'] = Produtos.objects.all()
  return render(request, 'home.html', data)

def procurar(request):
  data = {}
  search = request.GET.get('search')
  print("o nome q eu digitei:",search)

  #colocar em uma variavel o q eu pesquisei
  if search:
    print("NOME COMPANY")
    data['bancodados'] = Company.objects.filter(nome__icontains = search)
  if search:
    print("NOME PROD")
    data['bancodados'] = Produtos.objects.filter(nome__icontains = search) 
  if search:
    print("NOME CNPJ")
    data['bancodados'] = Company.objects.filter(cnpj__icontains = search)  
  if search:
    print("MARCA")
    data['bancodados'] = Produtos.objects.filter(marca__icontains = search)
  else:
    print("entrou aqui!2")
    messages.success(request,"Nada encontrado")

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
    print("passou here")
    data = {} #dicionario
    data['companyform'] = CompanyForm()
    return render(request, 'company-form.html', data)

def createcompany(request):
    form = CompanyForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

def editacompany(request, id):
  data = {}
  data['db'] = Company.objects.get(id = id)
  data['form'] = CompanyForm(instance = data['db'])
  return render(request, 'company-form.html', data)#mandar pro form

def atualizacompany(request, id):
  return 0

def showallcompany (request):
  data = {}
  data['bancodados'] = Company.objects.all()
  return render(request, 'all-company.html', data)

# def update(request, pk):
#   data = {}
#   data['db'] = Carros.objects.get(pk = pk)
#   form = CarrosForm(request.POST or None, instance = data['db'])
#   if form.is_valid():
#     form.save()
#     return HttpResponseRedirect("/")  