from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path,include
from customer import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('customer.urls')),
    path('base/',include('customer.urls')),
    path('about/',include('customer.urls')),
    path('html/',include('customer.urls')),
    path('css/',include('customer.urls')),
    path('js/',include('customer.urls')),
    path('bootstrap/',include('customer.urls')),
    path('navigation/',include('customer.urls')),
    path('feedback_form/',include('customer.urls'))
]
