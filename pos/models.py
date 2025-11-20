from django.db import models
from django.contrib.auth.models import User


# جدول المنتجات
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


# جدول الفواتير
class Invoice(models.Model):
    PAYMENT_CHOICES = (
        ("cash", "كاش"),
        ("mada", "مدى"),
        ("apple", "Apple Pay"),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    total = models.DecimalField(max_digits=10, decimal_places=2)

    payment_type = models.CharField(
        max_length=20,
        choices=PAYMENT_CHOICES,
        default="cash"
    )

    invoice_number = models.CharField(
        max_length=100,
        unique=True,
        blank=True,
        null=True
    )

    def __str__(self):
        return f"Invoice #{self.id} - {self.invoice_number}"


# جدول عناصر الفاتورة
class InvoiceItem(models.Model):
    invoice = models.ForeignKey(
        Invoice,
        on_delete=models.CASCADE,
        related_name="items"
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    qty = models.IntegerField(default=1)
    line_total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.product.name} x {self.qty}"
