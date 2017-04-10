from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.urls import reverse_lazy

from orders.models import Order
from .models import OrderItems
from .forms import OrderForm
from store.models import SC_produce, SM_produce


#def orders(request):
#    return render(request, 'orders/orders.html')

def orders(request):
    form = OrderForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        print(instance.order_id)
        request.session['order_id'] = instance.order_id

        itemid1 = 1
        itemid2 = 2
        itemid3 = 3
        quan1 = 4
        quan2 = 1
        quan3 = 2

        OrderItem1 = OrderItems.objects.create(order_id=instance.order_id, item_id=itemid1, quantity=quan1)
        OrderItem2 = OrderItems.objects.create(order_id=instance.order_id, item_id=itemid2, quantity=quan2)
        OrderItem = OrderItems.objects.create(order_id=instance.order_id, item_id=itemid3, quantity=quan3)
        print(OrderItem1.quantity)


        return HttpResponseRedirect(reverse('payment:process'))

    #if request.method == "POST":
    #    print(request.POST.get("first_name"))
    context = {
        "form": form,
    }







    return render(request, "orders/orders.html", {'myform': form})