"""
    -Customizing Django admin panel
"""
from django.contrib import admin
from app.models import UserOTP,Category,Brand,Product,Order
# Register your models here.


class UserOTPModelAdminView(admin.ModelAdmin):
    """
        - Customizing User Otp Model
    """
    list_display = ['id','user', 'otp', 'invalid_attempt', 'is_expired']

class CategoryModelAdminView(admin.ModelAdmin):
    """
        - Customizing Category Model
    """
    list_display = ['id','name']


class BrandModelAdminView(admin.ModelAdmin):
    """
        - Customizing Brand Model
    """
    list_display = ['id','name']


class ProductModelAdminView(admin.ModelAdmin):
    """
        - Customizing Product Model
    """
    list_display = ["id","name","category","brand","price","qty"]


class OrdersModelAdminView(admin.ModelAdmin):
    """
        - Customizing Order Model
    """
    list_display = ["id","placed","total_price","total_qty","timestamp"]

    def get_form(self, request, obj=None, **kwargs):
        """
            - remove qty and price filed form order form
            this is depend on product price and qty
        """
        self.exclude = ('total_qty','total_price')
        form = super().get_form(request, obj, **kwargs)
        return form

admin.site.register(UserOTP, UserOTPModelAdminView)
admin.site.register(Category, CategoryModelAdminView)
admin.site.register(Brand, BrandModelAdminView)
admin.site.register(Product, ProductModelAdminView)
admin.site.register(Order, OrdersModelAdminView)
