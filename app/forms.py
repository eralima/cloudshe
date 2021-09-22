from django.forms import ModelForm
from app.models import Company, Produtos

# Create the form class.
class ProdutosForm(ModelForm):
    class Meta:
        model = Produtos
        fields = ['nome', 'preco', 'quantidade', 'marca']

class CompanyForm(ModelForm):
    class Meta:
        model = Company
        fields = ['nome','email','rua','cep','bairro','cidade', 'fone', 'cnpj']        