# from django.contrib import admin
# from django.urls import path
# from django.conf import settings
# # from django.conf.urls.static import static
# from customer.views import Index, About, Html, Js, Css, Bootstrap, Feedback_Form

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', Index.as_view(), name='index'),
#     path('about/', About.as_view(), name='about'),
#     path('html/', Html.as_view(), name='html'),
#     path('css/', Css.as_view(), name='css'),
#     path('js/', Js.as_view(), name='js'),
#     path('bootstrap/', Bootstrap.as_view(), name='bootstrap'),
#     path('feedback_form/', Feedback_Form.as_view(), name='feedback_form'),
    
# ] 


from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path,include
from customer import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('base/',views.base,name='base'),
    path('html/',views.html,name='html'),
    path('css/',views.css,name='css'),
    path('js/',views.js,name='js'),
    path('bootstrap/',views.bootstrap,name='bootstrap'),
    path('navigation/',views.navigation,name='navigation'),
    path('feedback_form/',views.feedback_form,name='feedback_form'),
]
