from django import forms
from cars.models import Car


class CarModelForm(forms.ModelForm):
    
    class Meta:
        model = Car
        fields = '__all__'
    
    def clean_value(self):
        campo = 'value'

        value = self.cleaned_data.get(campo)

        if (value <= 0):
            self.add_error(campo, "Valor inválido")
        return value