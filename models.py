from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal


# جدول المنتجات
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


# جدول الفواتير
class Invoice(models.Model):
    invoice_number = models.CharField(max_length=50, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    payment_type = models.CharField(
        max_length=20,
        choices=[
            ("cash", "Cash"),
            ("mada", "Mada"),
            ("apple", "Apple Pay")
        ],
        default="cash"
    )

    subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    vat = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"فاتورة {self.invoice_number}"


# عناصر الفاتورة
class InvoiceItem(models.Model):
    invoice = models.ForeignKey(Invoice, related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    price = models.DecimalField(max_digits=10, decimal_places=2)
    qty = models.PositiveIntegerField(default=1)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.product.name} × {self.qty}"
