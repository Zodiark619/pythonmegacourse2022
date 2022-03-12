from django.shortcuts import render,get_object_or_404

from django.views import generic
from .models import Division,Item,Inventory
from django.views.generic import DetailView

    




def ItemView(request):
    all_division= Division.objects.all()
    result=Item.objects.all()
    if request.method=='POST':
        meong=request.POST['division_name']
        
        result=Item.objects.filter(division__name=meong)
       
           
            
    context={'all_division': all_division, 
            'all_item':result,
            
            }
    return render(request,'item_detail.html',context)

def InventoryDetail(request,bucin):
    lele=Item.objects.get(id=bucin).id
    
    all_inventory=Inventory.objects.filter(name__id=lele)

    context={'all_inventory':all_inventory}
    return render(request,'index.html',context)

    