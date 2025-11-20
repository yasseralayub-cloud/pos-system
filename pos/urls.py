from django.urls import path
from . import views

urlpatterns = [
    # صفحة الكاشير POS
    path('pos/', views.pos_page, name='pos'),

    # صفحة المنتجات
    path('products/', views.products_page, name='products'),

    # صفحة الفواتير
    path('invoices/', views.invoices_page, name='invoices'),

    # حفظ الفاتورة
    path('pos/save_invoice/', views.save_invoice, name='save_invoice'),

    # صفحة تفاصيل الفاتورة
    path('invoice/<int:invoice_id>/', views.invoice_details, name='invoice_details'),
]
