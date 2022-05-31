from django import forms

class PersonaForm(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=100)
    apellido = forms.CharField(label="Apellido", max_length=100)
    email = forms.EmailField(label="Email")
    fecha_nacimiento = forms.DateField(label="fecha_nacimiento", input_formats=["%d/%m/%Y"],
    widget=forms.TextInput(attrs={'placeholder': '30/12/1995'}))
    altura = forms.FloatField(widget=forms.NumberInput(attrs={'placeholder': "1.75 m"}))

class BuscarPersonasForm(forms.Form):
    palabra_a_buscar = forms.CharField(label="Buscar")

class MascotaForm(forms.Form):
    animal = forms.CharField(label="Animal", max_length=100)
    edad =  forms.IntegerField(label="Edad")

class VehiculoForm(forms.Form):
    marca = forms.CharField(label="Marca", max_length=100)
    dueño = forms.CharField(label="Dueño", max_length=100)




