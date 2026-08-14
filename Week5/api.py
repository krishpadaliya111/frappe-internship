import frappe

def set_customer_group_count(doc, method):
    if doc.customer_group:
        count = frappe.db.count("Customer", {"customer_group": doc.customer_group})
        doc.custom_customer_group_count = count + 1

from frappe.utils import nowdate, add_days

def mark_overdue_loans():
    cutoff = add_days(nowdate(), -14)
    loans = frappe.get_all(
        "Book Loan",
        filters={"status": "Issued", "loan_date": ["<", cutoff]},
        pluck="name"
    )
    for loan_name in loans:
        frappe.db.set_value("Book Loan", loan_name, "status", "Overdue")
    if loans:
        frappe.db.commit()

