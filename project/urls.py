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
from app.views import deletecompany, home
from app.views import productsform, createproduct, editproduct, updateproduct, deleteproduct, companyproducts
from app.views import showallcompany, companyform, createcompany, editcompany, deletecompany, updatecompany
# from app.views import procurar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),

    path('products-form/', productsform, name='products-form'),
    path('createproduct/', createproduct, name='createproduct'),
    path('editproduct/<int:pk>/', editproduct, name='editproduct'),
    path('updateproduct/<int:pk>/', updateproduct, name='updateproduct'),
    path('deleteproduct/<int:pk>/', deleteproduct, name='deleteproduct'),

    path('companyproducts/<int:fk>/', companyproducts, name='companyproducts'),

    path('showallcompany/', showallcompany, name='showallcompany'),
    path('company-form/', companyform, name='company-form'),
    path('createcompany/', createcompany, name='createcompany'),
    path('showallcompany/editcompany/<int:id>/', editcompany, name='editacompany'),
    path('showallcompany/updatecompany/<int:id>/', updatecompany, name='updatecompany'),
    path('showallcompany/deletecompany/<int:id>/', deletecompany, name='deletecompany'),

    # path('procurar/', procurar, name='procurar'),
]
