// ================================
//  نظام اللغات (عربي / إنجليزي)
//  صنع بواسطة: Yasser Alayub POS
// ================================

// اللغة الافتراضية
let currentLang = localStorage.getItem("pos_lang") || "ar";

// جميع النصوص
const translations = {
    ar: {
        invoicePreview: "معاينة الفاتورة",
        posTitle: "نقطة البيع (POS)",
        customerName: "اسم العميل",
        customerPlaceholder: "اكتب اسم العميل",
        employeeName: "الموظف",
        employeePlaceholder: "اسم الموظف",
        posNumber: "رقم نقطة البيع",
        taxValue: "نسبة الضريبة (%)",
        previewBtn: "معاينة الفاتورة",
        printBtn: "طباعة",
        productsTitle: "المنتجات",
        langBtn: "English"
    },

    en: {
        invoicePreview: "Invoice Preview",
        posTitle: "Point of Sale (POS)",
        customerName: "Customer Name",
        customerPlaceholder: "Enter customer name",
        employeeName: "Employee",
        employeePlaceholder: "Employee name",
        posNumber: "POS Number",
        taxValue: "Tax (%)",
        previewBtn: "Preview Invoice",
        printBtn: "Print",
        productsTitle: "Products",
        langBtn: "العربية"
    }
};

// تغيير اللغة
function setLanguage(lang) {
    currentLang = lang;
    localStorage.setItem("pos_lang", lang);
    applyTranslation();
}

// تطبيق الترجمة على الصفحة
function applyTranslation() {
    const t = translations[currentLang];

    document.querySelector("h2").textContent = t.invoicePreview;
    document.querySelector("#pos-panel h2").textContent = t.posTitle;

    document.querySelector("label[for='customerName']").textContent = t.customerName;
    document.getElementById("customerName").placeholder = t.customerPlaceholder;

    document.querySelector("label[for='employeeName']").textContent = t.employeeName;
    document.getElementById("employeeName").placeholder = t.employeePlaceholder;

    document.querySelector("label[for='posNumber']").textContent = t.posNumber;
    document.querySelector("label[for='taxValue']").textContent = t.taxValue;

    document.querySelector("#previewBtn").textContent = t.previewBtn;
    document.querySelector("#printBtn").textContent = t.printBtn;

    document.querySelector("#productsTitle").textContent = t.productsTitle;

    document.querySelector("#langBtn").textContent = t.langBtn;
}

// تفعيل اللغة عند بداية التشغيل
document.addEventListener("DOMContentLoaded", () => {
    applyTranslation();
});
