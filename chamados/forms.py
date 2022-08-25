from django.forms import ModelForm
from .models import *

class ChamadoForm(ModelForm):
    class Meta:
        model = Chamado
        #exclude = ('colaborador',)
        #readonly_fields = ['colaborador']
        fields = '__all__'
        
        #fields = ['categoria','assunto', 'descricao', 'status']

    #def __init__(self, *args, **kwargs):
    #    super(ChamadoForm, self).__init__(*args, **kwargs)
    #    self.fields['colaborador'].disabled = True
    #    #self.fields['categoria'].disabled = True
    #    #self.fields['assunto'].disabled = True
    
    def __init__(self, *args, **kwargs):
        super(ChamadoForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.id:
            self.fields['colaborador'].required = False
            self.fields['colaborador'].widget.attrs['disabled'] = 'disabled'

    def clean_sku(self):
        # As shown in the above answer.
        instance = getattr(self, 'instance', None)
        if instance:
            return instance.sku
        else:
            return self.cleaned_data.get('colaborador', None)
    