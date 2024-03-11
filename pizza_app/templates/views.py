from django.http import HttpResponse
from django.views.generic import CreateView
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .models import *
from .forms import * 
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.utils import timezone
from datetime import datetime, timedelta


def index(request):
    try:
        userCurr = request.user
        userOrders = Order.objects.filter(user=userCurr)
    except:
        return render(request, 'index.html')

    return render(request, 'index.html', {'orders': userOrders})

@login_required
def view_completed(request):
    userCurr = request.user

    try:
        order = Order.objects.filter(user=userCurr).latest('id')
    except:
        return render(request, 'message.html', {'message': f"You need to create a pizza before ordering"})

    return render(request, 'completed.html', {'order': order})

class UserSignupView(CreateView):
    model = User
    form_class = UserSignupForm
    template_name = 'user_signup.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')

class UserLoginView(LoginView):
    template_name='login.html'

@login_required
def logout_user(request):
    logout(request)
    return redirect("/")

@login_required
def create_pizza(request):
    user = request.user
    topping_fields = ['Chicken', 'Pepperoni', 'Mushroom', 
                        'Olives', 'Ham', 'Pineapple', 
                        'Pesto', 'Jalapeno', 'Onion',
                        'Peppers', 'Anchovies', 'Sweetcorn']

    if request.method == 'POST':
        form = PizzaForm(request.POST)
        if form.is_valid():
            # Delete all of a users unordered pizzas before they can go to order page with another
            Pizza.objects.filter(user=user, completed=False).delete()

            pizza = form.save(commit=False)
            pizza.user = user
            pizza.save()
            return redirect('order')
    else:
        form = PizzaForm()

    return render(request, 'create_pizza.html', {'form': form, 'topping_fields': topping_fields})

@login_required
def order_pizza(request):
    userCurr = request.user
    userPizza = Pizza.objects.filter(user=userCurr, completed=False).first()

    if not userPizza or userPizza.completed == True:
        #return redirect('create')
        return render(request, 'message.html', {'message': f"You need to create a pizza before ordering"})

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = userCurr
            order.pizza = userPizza
            userPizza.completed = True
            userPizza.save()
            current_time = datetime.now()
            order.order_time = current_time + timedelta(minutes=30)
            order.save()
            return redirect('completed')
    else:
        form = OrderForm()

    return render(request, 'order_pizza.html', {'form': form})

def about(request):
    return render(request, 'about.html')