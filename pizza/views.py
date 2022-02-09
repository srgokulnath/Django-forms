from django.shortcuts import render
from .forms import PizzaForm

def home(request):
    return render(request, 'pizza/home.html')
def order(request):
    if request.method == 'post':
        filled_form = PizzaForm(request.post, request.FILES)
        if filled_form.is_valid:
            topping1 = filled_form.cleaned_data['topping1']
            topping2 = filled_form.cleaned_data['topping2']
            size = filled_form.cleaned_data['size']
            note = 'this is ur order %s %s and %s' %(topping1, topping2, size)
            
            new_form = PizzaForm()
            return render(request, 'pizza/order.html', {'pizzaform': new_form, 
            'note': note
            }, context_instance=RequestContext(request))

    else:    
        form = PizzaForm()
        return render(request, 'pizza/order.html', {'pizzaform':form})

# Create your views here.
