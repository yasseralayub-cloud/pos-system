from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Product, Invoice, InvoiceItem
from accounts.models import UserProfile
from django.contrib import messages

@login_required
def pos_page(request):
    products = Product.objects.all()
    return render(request, 'pos.html', {'products': products})


@login_required
def products_page(request):
    profile = UserProfile.objects.get(user=request.user)

    if profile.role != 'admin':
        messages.error(request, "هذه الصفحة خاصة بالمدير فقط")
        return redirect('pos')

    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})


@login_required
def invoices_page(request):
    profile = UserProfile.objects.get(user=request.user)

    if profile.role not in ['admin', 'manager']:
        messages.error(request, "ليس لديك صلاحية للوصول للفواتير")
        return redirect('pos')

    invoices = Invoice.objects.all().order_by('-id')
    return render(request, 'invoices.html', {'invoices': invoices})


from django.http import JsonResponse
import json
from decimal import Decimal

@login_required
def from django.http import JsonResponse
import json
from decimal import Decimal
from django.contrib.auth.decorators import login_required
from .models import Product, Invoice, InvoiceItem

@login_required
def save_invoice(request):
@login_required
def invoice_details(request, invoice_id):
    try:
        invoice = Invoice.objects.get(id=invoice_id)
    except Invoice.DoesNotExist:
        messages.error(request, "الفاتورة غير موجودة")
        return redirect('/invoices/')

    return render(request, 'invoice_details.html', {
        'invoice': invoice
    })

    if request.method == "POST":
        data = json.loads(request.body)

        cart = data.get("cart", [])
        payment_type = data.get("paymentType", "cash")
        invoice_number = data.get("invoiceNumber", "")

        # حساب الإجمالي قبل الضريبة
        total = sum([Decimal(str(item["price"])) * item["qty"] for item in cart])

        # حساب الضريبة 15%
        vat = total * Decimal("0.15")

        # الإجمالي النهائي بعد الضريبة
        total_with_vat = total + vat

        # إنشاء الفاتورة داخل قاعدة البيانات
        invoice = Invoice.objects.create(
            user=request.user,
            total=total_with_vat,
            payment_type=payment_type,
            invoice_number=invoice_number
        )

        # إضافة عناصر الفاتورة Invoice Items
        for item in cart:
            product = Product.objects.get(id=item["id"])
            InvoiceItem.objects.create(
                invoice=invoice,
                product=product,
                qty=item["qty"],
                line_total=Decimal(str(item["price"])) * item["qty"]
            )

        return JsonResponse({
            "status": "success",
            "invoice_id": invoice.id,
            "message": "Invoice saved successfully"
        })

    return JsonResponse({"status": "error", "message": "Invalid request"}, status=400)


        # إجمالي الفاتورة
        total = sum([Decimal(str(item["price"])) * item["qty"] for item in cart])

        # إنشاء الفاتورة
        invoice = Invoice.objects.create(
            user=request.user,
            total=total
        )

        # عناصر الفاتورة
        for item in cart:
            product = Product.objects.get(id=item["id"])
            InvoiceItem.objects.create(
                invoice=invoice,
                product=product,
                qty=item["qty"],
                line_total=Decimal(str(item["price"])) * item["qty"]
            )

        return JsonResponse({"status": "success", "invoice_id": invoice.id})

    return JsonResponse({"status": "error"}, status=400)
