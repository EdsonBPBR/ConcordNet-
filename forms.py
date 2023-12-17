from django import forms 
from .models import Usuario
from .models import Instalacao  

class CadastroForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'

class InstalacaoForm(forms.ModelForm):
    class Meta:
        model = Instalacao
        fields = '__all__'

