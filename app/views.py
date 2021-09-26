from django.core import paginator
from django.shortcuts import redirect, render
from app.forms import CompanyForm, ProdutosForm
from app.models import Produtos, Company
from django.core.paginator import Paginator
from django.contrib import messages

# Create your views here.
def home (request):
    data = {}
    search = request.GET.get('search')
    if search:
        data['bancodados'] = Produtos.objects.filter(nome__icontains=search)
        produtosNome = Produtos.objects.filter(nome__icontains=search)
        paginator = Paginator(produtosNome, 8)
        paginas = request.GET.get('pagina')
        data['bancodados'] = paginator.get_page(paginas)
    
    else:
        data['bancodados'] = Produtos.objects.all()
        todosProdutos = Produtos.objects.all()
        paginator = Paginator(todosProdutos, 8)
        paginas = request.GET.get('pagina')
        data['bancodados'] = paginator.get_page(paginas)

    return render(request, 'home.html', data)

#CRUD de empresa
def showallcompany (request):
  data = {}
  search = request.GET.get('search')
  if search:
      data['bancodados'] = Company.objects.filter(nome__icontains=search)
      empresasNome = Company.objects.filter(nome__icontains=search)
      paginator = Paginator(empresasNome, 8)
      paginas = request.GET.get('pagina')
      data['bancodados'] = paginator.get_page(paginas)
  else:
      data['bancodados'] = Company.objects.all()
      todasEmpresas = Company.objects.all()
      paginator = Paginator(todasEmpresas, 8)
      paginas = request.GET.get('pagina')
      data['bancodados'] = paginator.get_page(paginas)
  return render(request, 'all-company.html', data)

def companyform (request):
    data = {} #dicionario
    data['companyform'] = CompanyForm()
    return render(request, 'company-form.html', data)

def createcompany(request):
    form = CompanyForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('showallcompany')

def editcompany(request, id):
  data = {}
  data['db'] = Company.objects.get(id = id)
  print(data['db'])
  data['companyform'] = CompanyForm(instance = data['db'])
  return render(request, 'company-form.html', data)#mandar pro form

def updatecompany(request, id):
    data = {}
    data['db'] = Company.objects.get(pk=id)
    companyform = CompanyForm(request.POST or None, instance=data['db'])
    if companyform.is_valid():
        companyform.save()
        return redirect ('showallcompany') 

def deletecompany (request, id):
    db = Company.objects.get(pk=id)
    db.delete()
    return redirect('showallcompany')

#CRUD de produtos
def productsform (request):
    data = {}
    data['productsform'] = ProdutosForm()
    data['bancodadosempresa'] = Company.objects.all() #todas as empresas cadastradas para o select
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
        return redirect('products-form')

def deleteproduct(request, pk):
    db = Produtos.objects.get(pk=pk)
    db.delete()
    return redirect('home')

#exibir todos os produtos de uma determinada empresa
def companyproducts(request, fk):
    data = {}
    data['bancodados'] = Produtos.objects.all().filter(empresa=fk)
    return render (request, 'company-products.html', data)

# def procurar(request):
#   data = {}
#   search = request.GET.get('search')
#   print("o nome q eu digitei:",search)

#   #colocar em uma variavel o q eu pesquisei
#   if search:
#     print("NOME COMPANY")
#     data['bancodados'] = Company.objects.filter(nome__icontains = search)
#   if search:
#     print("NOME PROD")
#     data['bancodados'] = Produtos.objects.filter(nome__icontains = search) 
#   if search:
#     print("NOME CNPJ")
#     data['bancodados'] = Company.objects.filter(cnpj__icontains = search)  
#   if search:
#     print("MARCA")
#     data['bancodados'] = Produtos.objects.filter(marca__icontains = search)
#   else:
#     print("entrou aqui!2")
#     messages.success(request,"Nada encontrado")

#   return render(request, 'home.html', data) 
