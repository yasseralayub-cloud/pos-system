let cart = [];

// إضافة منتج للفاتورة
function addToInvoice(id, name, price) {
    let existing = cart.find(item => item.id === id);

    if (existing) {
        existing.qty += 1;
    } else {
        cart.push({
            id: id,
            name: name,
            price: price,
            qty: 1
        });
    }

    renderInvoice();
}

// زر زيادة الكمية
function increaseQty(id) {
    let item = cart.find(x => x.id === id);
    item.qty += 1;
    renderInvoice();
}

// زر نقصان الكمية
function decreaseQty(id) {
    let item = cart.find(x => x.id === id);

    if (item.qty > 1) {
        item.qty -= 1;
    } else {
        cart = cart.filter(x => x.id !== id);
    }

    renderInvoice();
}

// زر حذف منتج بالكامل
function deleteItem(id) {
    cart = cart.filter(item => item.id !== id);
    renderInvoice();
}

// 🔍 دالة البحث عن منتج
function searchProduct(text) {
    text = text.toLowerCase();
    const elements = document.querySelectorAll(".product-btn");

    elements.forEach(el => {
        let name = el.textContent.toLowerCase();
        if (name.includes(text)) {
            el.style.display = "block";
        } else {
            el.style.display = "none";
        }
    });
}

// عرض الفاتورة على الشاشة
function renderInvoice() {
    const box = document.getElementById("invoice-box");
    box.innerHTML = "";

    let total = 0;

    cart.forEach(item => {
        const lineTotal = item.price * item.qty;
        total += lineTotal;

        box.innerHTML += `
            <div class="mb-2 p-2 border rounded">
                <b>${item.name}</b>
                <br>
                السعر: ${item.price} — الكمية: ${item.qty}
                <br>
                الإجمالي: ${lineTotal} ريال
                <br>

                <button class="btn btn-sm btn-success" onclick="increaseQty(${item.id})">+</button>
                <button class="btn btn-sm btn-warning" onclick="decreaseQty(${item.id})">-</button>
                <button class="btn btn-sm btn-danger" onclick="deleteItem(${item.id})">حذف</button>
            </div>
        `;
    });

    // الضريبة 15%
    let vat = total * 0.15;
    let totalVAT = total + vat;

    box.innerHTML += `
        <hr>
        <h4>الإجمالي قبل الضريبة: ${total} ريال</h4>
        <h4>الضريبة (15%): ${vat.toFixed(2)} ريال</h4>
        <h3>الإجمالي مع الضريبة: ${totalVAT.toFixed(2)} ريال</h3>
    `;
}

// حفظ الفاتورة
function saveInvoice() {
    if (cart.length === 0) {
        alert("لا توجد عناصر لحفظ الفاتورة");
        return;
    }

    fetch("/pos/save_invoice/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": getCSRFToken(),
        },
        body: JSON.stringify({ cart: cart }),
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === "success") {
            alert("تم حفظ الفاتورة بنجاح");
            cart = [];
            renderInvoice();
        } else {
            alert("حدث خطأ أثناء حفظ الفاتورة");
        }
    });
}

// جلب CSRF Token من المتصفح
function getCSRFToken() {
    let name = "csrftoken";
    let value = null;
    document.cookie.split(";").forEach(cookie => {
        cookie = cookie.trim();
        if (cookie.startsWith(name + "=")) {
            value = cookie.substring(name.length + 1);
        }
    });
    return value;
}
