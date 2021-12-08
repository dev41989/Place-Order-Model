"""Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Order import views
from django.conf.urls import url
urlpatterns = [
    path('',views.base_order_function, name = 'ordera'), 
    path('record/',views.record_order_function, name = 'record'),
    path('data_show/',views.show_data_function, name = 'Show_data'),  
    path('admin/', admin.site.urls),
    path('updated/',views.edit_Modify_function, name = 'updated'),

    url(r'^show/(?P<show_id>[0-9]+)/$',views.modify_show_function, name = 'Modifydata'),
    url(r'^delete/(?P<delete_id>[0-9]+)/$',views.delete_data_function, name = 'remain'),
]
