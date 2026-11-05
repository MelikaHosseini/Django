from django.shortcuts import render
from .models import *
from django.views.generic import ListView
from django.http import HttpResponse
from django.shortcuts import render
def homepage(request):
    flights = Basket.objects.all()
    return render(request, 'homepage/homepage.html', {'baskets':baskets})
class BasketsListView(ListView):
    model = Basket
    template_name = 'homepage/homepage.html'
    context_object_name = 'baskets'
    template_name = "homepage/baskets_details.html"
    context_object_name = "basket"
    success_url = "/"
    def get_success_url(self):
        return reverse('basket_detail', kwargs={'pk': self.object.pk})
def book_ticket(request):
    return render(request, 'homepage/user_form.html')
def add_booking(request):
    counter = 0
    if request.method == "POST":
        form = BookingForm(request.POST) 
        counter = 0
        if(Passenger.objects.count() < 110):
            if(form.is_valid()):                                                                           
                    user_name = form.cleaned_data['user_name']
                    user_surname = form.cleaned_data['user_surname']
                    userID = form.cleaned_data['userID' ]
                    phone_number = form.cleaned_data['phone_number']
                    email = form.cleaned_data['email']
                    user_class_type = form.cleaned_data['user_class_type']
                    basket_Details = Passenger.objects.create( user_name =  user_name, user_surname = user_surname, 
                                                        
                                                                 userID = userID, phone_number = phone_number,  email=  email, user_class_type = user_class_type)
                    Basket.save(basket_Details )
                    return redirect('view_basket', pk=basket_Details.id)
            form = UserBasketForm()
            return render(request, "homepage/checkout.html",{'form':form})
        else:
            return HttpResponse(f"not available ")   
def view_basket(request, pk):
   result = Basket.objects.get(pk=pk)
   return render(request, 'homepage/view_basket.html', context= {'result':result})

