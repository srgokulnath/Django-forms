from cProfile import label
from django import forms
from .models import Pizza,Size

# class PizzaForm(forms.Form):
#     # topping1 = forms.CharField(label='Topping 1', max_length=100, widget=forms.PasswordInput)
#     # toppings = forms.MultipleChoiceField(
#     #     choices=[('pep', 'Pepperoni'), ('che', 'cheese'), ('oli', 'olives')], widget=forms.CheckboxSelectMultiple)

#     topping1 = forms.CharField(label='Topping 1', max_length=100)
#     topping2 = forms.CharField(label='Topping 2', max_length=100)    
#     size = forms.ChoiceField(label='Size', choices=[('small', 'samll'),('medium', 'medium'), ('large','large')])

class PizzaForm(forms.ModelForm):

    # size = forms.ModelChoiceField(queryset=Size.objects, empty_label = None, widget=forms.RadioSelect)
    image = forms.ImageField()

    class Meta:
        model = Pizza
        fields = ['topping1', 'topping2','size']
        labels = {'topping1':'Topping 1','topping2':'Topping 2'}
