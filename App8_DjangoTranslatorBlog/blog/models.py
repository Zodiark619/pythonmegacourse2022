from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.db.models.signals import post_save
from django.dispatch import receiver


inventory_movement=((0,'Stock In'),(1,'Stock Out'))
# ,(2,'transfer')
class Division(models.Model):
    name=models.CharField(max_length=500)

    def __str__(self):
        return self.name
class Item(models.Model):
    division=models.ForeignKey(Division,on_delete=models.CASCADE)
    name=models.CharField(max_length=500)
    quantity=models.IntegerField()

    def __str__(self):
        return self.name.title()
class Inventory(models.Model):
    
    name=models.ForeignKey(Item,on_delete=models.CASCADE)

    type=models.IntegerField(choices=inventory_movement)
    quantity=models.IntegerField()
    date_created=models.DateTimeField(auto_now_add=True)
    
    
    def inventory_verbose(self):
        return dict(inventory_movement)[self.type]

    def __str__(self):
        if self.type==0:
            return 'Stock In'+" +"+str(self.quantity)
        elif self.type==1:
            return 'Stock Out'+" -"+str(self.quantity)



@receiver(post_save, sender=Inventory)
def post_save_quantity(sender, instance,created,**kwargs):
    if created:
        target=Item.objects.get(id=instance.name.id)

        
        if instance.type==0:
            target.quantity+=instance.quantity
            target.save()
        elif instance.type==1:
            target.quantity-=instance.quantity
            target.save()
        











