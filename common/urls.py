from django.urls import path

from common.views import home_page

urlpatterns = [
    path('', home_page, name='home')
]
