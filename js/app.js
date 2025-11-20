// =====================================================
//  نظام تشغيل POS (الفاتورة، الحساب، الطباعة)
//  صنع بواسطة: Yasser Alayub
// =====================================================

let cart = []; // سلة المشتريات

// إضافة منتج إلى الفاتورة
function addItemToInvoice(product) {
    const existing = cart.find(item => item.id === product.id);

    if (existing) {
        existing.qty += 1;
    } else {
        cart.push({
            id: product.id,
            name: product.name,
            price: product.price,
            qty: 1
        });
    }

    previewInvoice();
}

// إنشاء معاينة الفاتورة
function previewInvoice() {
    const container = document.getElementById("invoice-content");
    container.innerHTML = "";

    let subtotal = 0;

    cart.forEach(item => {
        const total = item.price * item.qty;
        subtotal += total;

        const div = document.createElement("div");
        div.className = "invoice-item";

        div.innerHTML = `
            <span><b>${item.name}</b></span>
            <span>الكمية: ${item.qty}</span>
            <span>السعر: ${item.price} ريال</span>
            <span>الإجمالي: ${total} ريال</span>
        `;

        container.appendChild(div);
    });

    const taxRate = Number(document.getElementById("taxValue").value) || 0;
    const tax = (subtotal * taxRate) / 100;
    const totalWithTax = subtotal + tax;

    const summary = document.createElement("div");
    summary.innerHTML = `
        <hr>
        <p><b>المجموع قبل الضريبة:</b> ${subtotal.toFixed(2)} ريال</p>
        <p><b>الضريبة (${taxRate}%):</b> ${tax.toFixed(2)} ريال</p>
        <p><b>الإجمالي:</b> ${totalWithTax.toFixed(2)} ريال</p>
        <hr>
    `;

    container.appendChild(summary);
}

// طباعة الفاتورة
function printInvoice() {
    if (cart.length === 0) {
        alert("لا توجد عناصر في الفاتورة");
        return;
    }

    let invoiceWindow = window.open("", "_blank");

    invoiceWindow.document.write(`
        <html>
        <head>
            <title>طباعة الفاتورة</title>
            <style>
                body { font-family: 'Tajawal'; direction: rtl; padding: 20px; }
                .item { margin-bottom: 10px; }
            </style>
        </head>
        <body>
            <h2>فاتورة المبيعات</h2>
    `);

    cart.forEach(item => {
        invoiceWindow.document.write(`
            <div class="item">
                <p><b>${item.name}</b></p>
                <p>الكمية: ${item.qty}</p>
                <p>السعر: ${item.price} ريال</p>
                <p>الإجمالي: ${item.price * item.qty} ريال</p>
                <hr>
            </div>
        `);
    });

    let subtotal = cart.reduce((sum, item) => sum + item.price * item.qty, 0);
    let taxRate = Number(document.getElementById("taxValue").value);
    let tax = (subtotal * taxRate) / 100;
    let total = subtotal + tax;

    invoiceWindow.document.write(`
        <p><b>المجموع قبل الضريبة:</b> ${subtotal.toFixed(2)} ريال</p>
        <p><b>الضريبة (${taxRate}%):</b> ${tax.toFixed(2)} ريال</p>
        <p><b>الإجمالي:</b> ${total.toFixed(2)} ريال</p>

        <script>
            window.onload = () => { window.print(); };
        </script>
        </body>
        </html>
    `);

    invoiceWindow.document.close();
}

// مسح الفاتورة
function clearInvoice() {
    cart = [];
    previewInvoice();
}
