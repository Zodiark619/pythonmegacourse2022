from django.shortcuts import render,get_object_or_404
# from .models import Post
# Create your views here.
from django.views import generic
from .models import Division,Item,Inventory

class ItemView(generic.DetailView):
    model=Item

    # def book_detail_view(request, pk):
    #     target_item = get_object_or_404(Item, pk=pk)
    #     return render(request, 'item_detail.html', context={'item': target_item})



# class AboutView(generic.TemplateView):
#     template_name='about.html'

class InventoryList(generic.ListView):
    queryset=Inventory.objects.all().order_by('-date_created')
    template_name='index.html'