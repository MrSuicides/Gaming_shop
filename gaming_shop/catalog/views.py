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
    Length_check = [len(Audio.objects.filter(name=product_name)),
                    len(Keyboard.objects.filter(name=product_name)),
                    len(Mice.objects.filter(name=product_name))]

    if max(Length_check) == len(Mice.objects.filter(name=product_name)):
        product = Mice.objects.get(name=product_name)
        a = "Mice"
    elif max(Length_check) == len(Audio.objects.filter(name=product_name)):
        product = Audio.objects.get(name=product_name)
        a = "Audio"
    else:
        product = Keyboard.objects.get(name=product_name)
        a = "Keyboard"
    return render(request, 'Pages/Product'+a+'.html', locals())

def test(request):
    product = Audio.objects.filter(name="rare").first()
    product = Audio.objects.filter(name="rare").first()
    product = Audio.objects.filter(name="rare").first()
    return product
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

