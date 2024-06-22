from django.forms import ModelForm, DateInput, Textarea

from .models import Exercise


class ExerciseForm(ModelForm):
  class Meta:
    model = Exercise
    fields = '__all__'
    labels = {
      'name': 'Nombre',
      'description': 'Descripción',
      'input_description': 'Entrada esperada',
      'output_description': 'Salida esperada',
      'start_date': 'Fecha de inicio',
      'end_date': 'Fecha de cierre',
      'cases': 'Casos',
      'num_cases': 'Número de casos'
    }
    widgets = { 
    'start_date': DateInput(
      format=('%Y-%m-%d'),
      attrs={
            'type': 'date'
          }),
    'end_date': DateInput(
      format=('%Y-%m-%d'),
      attrs={
            'type': 'date'
          }),
    'description': Textarea(attrs={'rows': 5})
}
