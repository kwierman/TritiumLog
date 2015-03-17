from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def index(request):
    menu_items = [["home",""],["about",""],["Help",""] ]
    context = {'SITENAME': "TritiumLog", 'MENUITEMS' : menu_items}
    return render(request, 'home/index.html', context)
