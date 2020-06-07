from django.shortcuts import render
from .models import Audio, Mice, Keyboard
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
# Create your views here.


def Search(brend, search_name, Category):

    if search_name:
        search_result = Category.objects.filter(name=search_name, brend=brend)
    else:
        search_result = Category.objects.filter(brend=brend)
    return search_result

def index(request):
    if request.user.is_authenticated:
        name = request.user.username
        print(name)
    return render(request, 'Pages/index.html')

def razer_audio(request):
    search_name = request.GET.get("name")
    context = {'all_info': Search('1', search_name, Audio)}
    return render(request, 'Pages/razer_audio.html', context)
def razer_mice(request):
    search_name = request.GET.get("name")
    context = {'all_info': Search('1', search_name, Mice)}
    return render(request, 'Pages/razer_mice.html', context)
def razer_keyboard(request):
    search_name = request.GET.get("name")
    context = {'all_info': Search('1', search_name, Keyboard)}
    return render(request, 'Pages/razer_keyboard.html', context)

def dead(request):
    return render(request, 'Pages/Basket.html')

def Products(request, product_name):
    categories = {
        Audio: 'Pages/ProductAudio.html',
        Mice: 'Pages/ProductMice.html',
        Keyboard: 'Pages/ProductKeyboard.html',
    }
    for category, template in categories.items():
        product = category.objects.filter(name=product_name).first()
        if product is not None:
            return render(request, template, locals())

def register(request):
    if request.method == 'POST':

        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
    else:
        form = UserCreationForm()
    context = {'form' : form}
    return render(request, 'registration/register.html', context)

