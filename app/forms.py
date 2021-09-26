from django.forms import ModelForm
from app.models import Company, Produtos

# Create the form class.
class CompanyForm(ModelForm):
    class Meta:
        model = Company
        fields = ['nome', 'razao_social','email','rua','cep','bairro','cidade', 'telefone', 'cnpj']  

class ProdutosForm(ModelForm):
    class Meta:
        model = Produtos
        fields = ['nome', 'preco', 'quantidade', 'marca', 'imagem_link', 'empresa']