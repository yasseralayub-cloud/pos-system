// ============================================
//  نظام تخزين المنتجات في POS (Storage System)
//  صنع بواسطة: Yasser Alayub
// ============================================

// بيانات المنتجات الافتراضية
let products = [
    { id: 1, name: "قهوة عربي", price: 8 },
    { id: 2, name: "قهوة تركي", price: 10 },
    { id: 3, name: "كابتشينو", price: 12 },
    { id: 4, name: "اسبريسو", price: 7 },
    { id: 5, name: "شاي أحمر", price: 5 },
    { id: 6, name: "شاي أخضر", price: 6 },
];

// تحميل المنتجات من LocalStorage إذا كانت موجودة
if (localStorage.getItem("pos_products")) {
    products = JSON.parse(localStorage.getItem("pos_products"));
}

// حفظ المنتجات في LocalStorage
function saveProducts() {
    localStorage.setItem("pos_products", JSON.stringify(products));
}

// إضافة منتج جديد
function addProduct(name, price) {
    const newProduct = {
        id: Date.now(),
        name: name,
        price: price
    };
    products.push(newProduct);
    saveProducts();
    loadProductButtons();
}

// حذف منتج
function deleteProduct(id) {
    products = products.filter(p => p.id !== id);
    saveProducts();
    loadProductButtons();
}

// إضافة الأزرار إلى الواجهة
function loadProductButtons() {
    const list = document.getElementById("productList");
    list.innerHTML = "";

    products.forEach(product => {
        const btn = document.createElement("div");
        btn.className = "product-btn";
        btn.textContent = `${product.name} - ${product.price} ريال`;
        btn.onclick = () => addItemToInvoice(product);
        list.appendChild(btn);
    });
}

// تشغيل النظام عند فتح الصفحة
document.addEventListener("DOMContentLoaded", () => {
    loadProductButtons();
});
