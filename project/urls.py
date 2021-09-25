"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import companyform, home, procurar, productsform, createproduct, createcompany, editacompany ,atualizacompany,procurar, showallcompany

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('products-form/', productsform, name='products-form'),
    path('createproduct/', createproduct, name='createproduct'),
    path('company-form/', companyform, name='company-form'),
    path('createcompany/', createcompany, name='createcompany'),
    path('editacompany/<int:id>/', editacompany, name='editacompany'),
    path('atualizacompany/<int:id>/', atualizacompany, name='atualizacompany'),
    path('procurar/', procurar, name='procurar'),
    path('showallcompany/', showallcompany, name='showallcompany'),
]
