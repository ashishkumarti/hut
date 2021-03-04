from django.contrib.auth.models import User
from django.db import models

class Vendor(models.Model):
    name = models.CharField(max_length=255)
    contact = models.CharField(max_length=15, null=True)
    location = models.CharField(max_length=255,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.OneToOneField(User, related_name='vendor', on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name
    
    def get_balance(self):
        #items = self.items.filter(vendor_paid=False, order__vendors__in=[self.id])
        #return sum((item.product.price * item.quantity) for item in items)
        return self.contact
    
    def get_paid_amount(self):
        #items = self.items.filter(vendor_paid=True, order__vendors__in=[self.id])
        #return sum((item.product.price * item.quantity) for item in items)
        return self.location