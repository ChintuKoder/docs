# from django.http import HttpResponse
# from django.shortcuts import render
# from django.views import View
# from .models import FeedBack_Form
# # from customer.models import MenuItem, Category, OrderModel 


# class Index(View):
#     def get(self, request, *args, **kwargs):
#         return render(request,'customer/index.html')


# class About(View):
#     def get(self, request, *args, **kwargs):
#         return render(request,'customer/about.html')


# class Html(View):
#     def get(self, request, *args, **kwargs):
#         return render(request,'customer/html.html')

# class Css(View):
#     def get(self, request, *args, **kwargs):
#         return render(request,'customer/css.html')

# class Js(View):
#     def get(self, request, *args, **kwargs):
#         return render(request,'customer/js.html')

# class Bootstrap(View):
#     def get(self, request, *args, **kwargs):
#         return render(request,'customer/bootstrap.html')


# class Feedback_Form(View):
#     def get(self, request, *args, **kwargs):
#         if request.method=="POST":
#             feedback_form=FeedBack_Form()
#             name=request.POST.get('name')
#             email=request.POST.get('email')
#             subject=request.POST.get('subject')
#             feedback_form.name=name
#             feedback_form.email=email
#             feedback_form.subject=subject
#             feedback_form.save()
#             return HttpResponse("<h1>THANKS FOR YOUR VALUABLE TIME</h1>")
#         return render(request,'customer/feedback_form.html')
        
        




#     # return render(request,'customer/feedback_form.html')


   

       

# # def feedback_form(request):
# #     if request.method=="POST":
# #         feedback_form=FeedBack_Form()
# #         name=request.POST.get('name')
# #         email=request.POST.get('email')
# #         subject=request.POST.get('subject')
# #         feedback_form.name=name
# #         feedback_form.email=email
# #         feedback_form.subject=subject
# #         feedback_form.save()
# #         return HttpResponse("<h1>THANKS FOR YOUR VALUABLE TIME</h1>")

# #     return render(request,'customer/feedback_form.html')
   





# # class Order(View):
# #     def get(self, request, *args, **kwargs):
# #         drinks = MenuItem.objects.filter(category__name__contains='Drinks')
# #         desserts = MenuItem.objects.filter(category__name__contains='Desserts')

# #         context = {
# #             'drinks': drinks,
# #             'desserts': desserts,

# #         }

# #         return render(request, 'customer/order.html', context)

# #     def post(self, request, *args, **kwargs):
# #         order_items = {
# #             'items': []
# #         }

# #         items = request.POST.getlist('items[]')

# #         for item in items:
# #             menu_item = MenuItem.objects.get(pk__contains=int(item))
# #             item_data = {
# #                 'id': menu_item.pk,
# #                 'name': menu_item.name,
# #                 'price': menu_item.price
# #             }

# #             order_items['items'].append(item_data)

# #             price = 0
# #             item_ids = []

# #             for item in order_items['items']:
# #                 price += item['price']
# #                 item_ids.append(item['id'])

# #             order = OrderModel.objects.create(price=price)
# #             order.items.add(*item_ids)

# #             context = {
# #                 'items': order_items['items'],
# #                 'price': price
# #             }

# #             return render(request, 'customer/order_confirmation.html', context)


from django.http import HttpResponse
from django.shortcuts import render
from customer.models import FeedBack_Form
from django.http import HttpResponse


# Create your views here.

def index(request):
    return render(request,'index.html')

def base(request):
    return render(request,'base.html')


def about(request):
    return render(request,'about.html')

def html(request):
    return render(request,'html.html')

def css(request):
    return render(request,'css.html')

def js(request):
    return render(request,'js.html')

def bootstrap(request):
    return render(request,'bootstrap.html')

def navigation(request):
    return render(request,'navigation.html')

def feedback_form(request):
    if request.method=="POST":
        feedback_form=FeedBack_Form()
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        feedback_form.name=name
        feedback_form.email=email
        feedback_form.subject=subject
        feedback_form.save()
        return HttpResponse("<h1>THANKS FOR YOUR VALUABLE TIME</h1>")

    return render(request,'feedback_form.html')

   
       

