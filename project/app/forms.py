
## padrão do Django de formularios

from django.forms import ModelForm
from app.models import Person

class PersonForm(ModelForm):
    class Meta:
        model=Person
        fields = ['primeiro_nome','segundo_nome','usuario','endereco']