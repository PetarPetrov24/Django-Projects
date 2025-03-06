from django.shortcuts import render

from core.util import get_first_profile

# Create your views here.


def home_page(request):
    profile = get_first_profile()
    context = {'profile': profile}

    return render(request, template_name='index.html', context=context)
