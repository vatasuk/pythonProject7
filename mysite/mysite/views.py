from django.http import HttpResponse
from django.shortcuts import render
from .forms import UserForm
def index(request):
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        bf = request.POST.get("bf")
        nbf = request.POST.get("nbf")
        output = ("<h2>Пользователь</h2> <h3> Имя - {0},Возраст - {1}, Согласие - {2},"
                  " Точное согласие - {3}</h3>").format(name,age,bf,nbf)
        return HttpResponse(output)
    else:
        userform = UserForm
        return render(request, "index.html", {"form": userform})
def about(request):
    return HttpResponse("<h2> О сайте </h2>")
def contact(request):
    return HttpResponse("<h2> Контакт </h2>")
def products(request,productid = 1):
    output = "<h2>Продукт №{0} </h2>".format(productid)
    return HttpResponse(output)
def users(request,id,name):
    output = "<h2>Пользователь</h2> <h3> id: {0} Имя:{0} </h3>".format(id,name)
    return HttpResponse(output)