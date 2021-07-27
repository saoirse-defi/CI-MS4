from django.shortcuts import render, redirect
from .models import Seller
from .forms import SellerForm


# Create your views here.
def index(request):
    return render(request, 'index/index.html')


def register(request):
    if request.method == 'POST':
        form = SellerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    form = SellerForm()
    context = {'form': form}
    return render(request, 'register/register.html', context)

